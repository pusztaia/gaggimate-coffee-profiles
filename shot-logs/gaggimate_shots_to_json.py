#!/usr/bin/env python3
"""Download all GaggiMate shot logs and convert current GaggiMate v5 .slog files to JSON.

Based on the current GaggiMate binary shot log layout documented in:
  src/display/models/shot_log_format.h

Network endpoints used:
  GET /api/history/index.bin
  GET /api/history/000123.slog
  GET /api/history/000123.json   (optional shot notes)

Default GaggiMate address: 192.168.50.68
No third-party Python packages are required.
"""

from __future__ import annotations

import argparse
import json
import socket
import struct
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen


# ---------------------------------------------------------------------------
# GaggiMate format constants (current v5)
# ---------------------------------------------------------------------------

SHOT_LOG_MAGIC = 0x544F4853  # bytes: SHOT
SHOT_LOG_VERSION = 5
SHOT_LOG_HEADER_SIZE = 512
SHOT_LOG_SAMPLE_SIZE = 26
SHOT_LOG_SAMPLE_INTERVAL_MS = 250

SHOT_INDEX_MAGIC = 0x58444953  # bytes: SIDX
SHOT_INDEX_VERSION = 1
SHOT_INDEX_HEADER_SIZE = 32
SHOT_INDEX_ENTRY_SIZE = 128

SHOT_FLAG_COMPLETED = 0x01
SHOT_FLAG_DELETED = 0x02
SHOT_FLAG_HAS_NOTES = 0x04

SYSTEM_INFO_SHOT_STARTED_VOLUMETRIC = 0x0001
SYSTEM_INFO_CURRENTLY_VOLUMETRIC = 0x0002
SYSTEM_INFO_BLUETOOTH_SCALE_CONNECTED = 0x0004
SYSTEM_INFO_VOLUMETRIC_AVAILABLE = 0x0008
SYSTEM_INFO_EXTENDED_RECORDING = 0x0010

PHASE_EXIT_REASON_NAMES = {
    0: "none",
    1: "target_volumetric",
    2: "target_pressure",
    3: "target_flow",
    4: "target_pumped",
    5: "duration",
    6: "safety",
    7: "aborted",
}

# Header up to finalWeight, exactly 110 bytes.
SHOT_HEADER_BASE = struct.Struct("<IBBHHHIIII32s48sH")
PHASE_TRANSITION = struct.Struct("<HBB25s")  # 29 bytes
SHOT_SAMPLE_V5 = struct.Struct("<HHHHHhhhhHHHH")  # 26 bytes

INDEX_HEADER = struct.Struct("<IHHII16s")  # 32 bytes
INDEX_ENTRY = struct.Struct("<IIIHBB32s48sHHH26s")  # 128 bytes


class GaggiMateError(RuntimeError):
    pass


class UnsupportedSlogVersion(GaggiMateError):
    pass


@dataclass
class ShotIndexEntry:
    shot_id: int
    timestamp: int
    duration_ms: int
    final_weight_g: float
    rating: int
    flags: int
    profile_id: str
    profile_name: str
    avg_temp_c: Optional[float] = None
    max_pressure_bar: Optional[float] = None
    avg_flow_ml_s: Optional[float] = None

    @property
    def completed(self) -> bool:
        return bool(self.flags & SHOT_FLAG_COMPLETED)

    @property
    def deleted(self) -> bool:
        return bool(self.flags & SHOT_FLAG_DELETED)

    @property
    def has_notes(self) -> bool:
        return bool(self.flags & SHOT_FLAG_HAS_NOTES)

    def as_json(self) -> dict[str, Any]:
        return {
            "id": self.shot_id,
            "timestamp": self.timestamp,
            "timestamp_iso_utc": epoch_to_iso(self.timestamp),
            "duration_ms": self.duration_ms,
            "duration_s": round(self.duration_ms / 1000.0, 3),
            "final_weight_g": round(self.final_weight_g, 1),
            "rating": self.rating,
            "flags": self.flags,
            "completed": self.completed,
            "deleted": self.deleted,
            "has_notes": self.has_notes,
            "profile_id": self.profile_id,
            "profile_name": self.profile_name,
            "avg_temp_c": self.avg_temp_c,
            "max_pressure_bar": self.max_pressure_bar,
            "avg_flow_ml_s": self.avg_flow_ml_s,
        }


def decode_c_string(raw: bytes) -> str:
    return raw.split(b"\x00", 1)[0].decode("utf-8", errors="replace")


def epoch_to_iso(epoch: int) -> Optional[str]:
    if not epoch:
        return None
    try:
        return datetime.fromtimestamp(epoch, tz=timezone.utc).isoformat().replace("+00:00", "Z")
    except (OverflowError, OSError, ValueError):
        return None


def normalize_base_url(host: str) -> str:
    host = host.strip().rstrip("/")
    if not host.startswith(("http://", "https://")):
        host = "http://" + host
    return host + "/"


def http_get(
    url: str,
    *,
    timeout: float,
    retries: int,
    allow_404: bool = False,
) -> Optional[bytes]:
    headers = {
        "User-Agent": "gaggimate-shots-to-json/1.0",
        "Accept": "*/*",
        "Cache-Control": "no-cache",
    }

    last_error: Optional[BaseException] = None

    for attempt in range(1, retries + 1):
        try:
            request = Request(url, headers=headers, method="GET")
            with urlopen(request, timeout=timeout) as response:
                return response.read()

        except HTTPError as exc:
            if exc.code == 404 and allow_404:
                return None
            last_error = exc
            # Retrying most 4xx errors will not help.
            if 400 <= exc.code < 500:
                break

        except (URLError, TimeoutError, socket.timeout, ConnectionError) as exc:
            last_error = exc

        if attempt < retries:
            time.sleep(min(0.5 * attempt, 2.0))

    raise GaggiMateError(f"HTTP download failed: {url} ({last_error})")


def parse_index(data: bytes) -> tuple[dict[str, Any], list[ShotIndexEntry]]:
    if len(data) < SHOT_INDEX_HEADER_SIZE:
        raise GaggiMateError(f"index.bin is too short: {len(data)} bytes")

    magic, version, entry_size, entry_count, next_id, _reserved = INDEX_HEADER.unpack_from(data, 0)

    if magic != SHOT_INDEX_MAGIC:
        prefix = data[:32]
        raise GaggiMateError(
            "Invalid index.bin magic. The server may have returned a web page instead of "
            f"the binary index. First bytes: {prefix!r}"
        )

    if version != SHOT_INDEX_VERSION:
        raise GaggiMateError(
            f"Unsupported shot index version: {version} (expected {SHOT_INDEX_VERSION})"
        )

    if entry_size != SHOT_INDEX_ENTRY_SIZE:
        raise GaggiMateError(
            f"Unsupported shot index entry size: {entry_size} (expected {SHOT_INDEX_ENTRY_SIZE})"
        )

    expected = SHOT_INDEX_HEADER_SIZE + entry_count * entry_size
    if len(data) < expected:
        raise GaggiMateError(
            f"Truncated index.bin: {len(data)} bytes, expected at least {expected}"
        )

    entries: list[ShotIndexEntry] = []
    offset = SHOT_INDEX_HEADER_SIZE

    for _ in range(entry_count):
        raw = data[offset : offset + entry_size]
        (
            shot_id,
            timestamp,
            duration_ms,
            volume_x10,
            rating,
            flags,
            profile_id_raw,
            profile_name_raw,
            avg_temp_x10,
            max_pressure_x10,
            avg_flow_x100,
            _reserved_entry,
        ) = INDEX_ENTRY.unpack(raw)

        entries.append(
            ShotIndexEntry(
                shot_id=shot_id,
                timestamp=timestamp,
                duration_ms=duration_ms,
                final_weight_g=volume_x10 / 10.0,
                rating=rating,
                flags=flags,
                profile_id=decode_c_string(profile_id_raw),
                profile_name=decode_c_string(profile_name_raw),
                avg_temp_c=(round(avg_temp_x10 / 10.0, 1) if avg_temp_x10 else None),
                max_pressure_bar=(round(max_pressure_x10 / 10.0, 1) if max_pressure_x10 else None),
                avg_flow_ml_s=(round(avg_flow_x100 / 100.0, 2) if avg_flow_x100 else None),
            )
        )
        offset += entry_size

    header = {
        "magic": "SIDX",
        "version": version,
        "entry_size": entry_size,
        "entry_count": entry_count,
        "next_id": next_id,
    }
    return header, entries


def parse_phase_transitions(data: bytes, count: int) -> list[dict[str, Any]]:
    transitions: list[dict[str, Any]] = []
    offset = SHOT_HEADER_BASE.size

    for i in range(12):
        sample_index, phase_number, transition_reason, phase_name_raw = PHASE_TRANSITION.unpack_from(data, offset)
        offset += PHASE_TRANSITION.size

        if i < count:
            transitions.append(
                {
                    "sample_index": sample_index,
                    "phase_number": phase_number,
                    "phase_name": decode_c_string(phase_name_raw),
                    "transition_reason": transition_reason,
                    "transition_reason_name": PHASE_EXIT_REASON_NAMES.get(transition_reason, f"unknown_{transition_reason}"),
                }
            )

    return transitions


def system_info_to_json(value: int) -> dict[str, Any]:
    return {
        "raw": value,
        "shot_started_volumetric": bool(value & SYSTEM_INFO_SHOT_STARTED_VOLUMETRIC),
        "currently_volumetric": bool(value & SYSTEM_INFO_CURRENTLY_VOLUMETRIC),
        "bluetooth_scale_connected": bool(value & SYSTEM_INFO_BLUETOOTH_SCALE_CONNECTED),
        "volumetric_available": bool(value & SYSTEM_INFO_VOLUMETRIC_AVAILABLE),
        "extended_recording": bool(value & SYSTEM_INFO_EXTENDED_RECORDING),
    }


def parse_slog_v5(data: bytes, shot_id: int) -> dict[str, Any]:
    if len(data) < SHOT_HEADER_BASE.size:
        raise GaggiMateError(f"Shot {shot_id}: .slog file too short: {len(data)} bytes")

    (
        magic,
        version,
        sample_size_diag,
        header_size,
        sample_interval_ms,
        _reserved1,
        fields_mask,
        sample_count,
        duration_ms,
        start_epoch,
        profile_id_raw,
        profile_name_raw,
        final_weight_x10,
    ) = SHOT_HEADER_BASE.unpack_from(data, 0)

    if magic != SHOT_LOG_MAGIC:
        raise GaggiMateError(
            f"Shot {shot_id}: invalid SHOT magic (0x{magic:08X})"
        )

    if version != SHOT_LOG_VERSION:
        raise UnsupportedSlogVersion(
            f"Shot {shot_id}: unsupported .slog version {version}; this script currently "
            f"decodes the current GaggiMate v{SHOT_LOG_VERSION} format."
        )

    if header_size != SHOT_LOG_HEADER_SIZE:
        raise GaggiMateError(
            f"Shot {shot_id}: unexpected v5 header size {header_size}; expected {SHOT_LOG_HEADER_SIZE}"
        )

    sample_size = sample_size_diag or SHOT_LOG_SAMPLE_SIZE
    if sample_size != SHOT_LOG_SAMPLE_SIZE:
        raise GaggiMateError(
            f"Shot {shot_id}: unexpected v5 sample size {sample_size}; expected {SHOT_LOG_SAMPLE_SIZE}"
        )

    if len(data) < header_size:
        raise GaggiMateError(
            f"Shot {shot_id}: truncated header: {len(data)} bytes total, header says {header_size}"
        )

    phase_count_offset = SHOT_HEADER_BASE.size + (12 * PHASE_TRANSITION.size)
    phase_transition_count = data[phase_count_offset]
    final_exit_reason = data[phase_count_offset + 1]
    brew_delay_ms = struct.unpack_from("<H", data, phase_count_offset + 2)[0]
    if phase_transition_count > 12:
        raise GaggiMateError(
            f"Shot {shot_id}: invalid phase transition count {phase_transition_count}"
        )

    transitions = parse_phase_transitions(data, phase_transition_count)
    transitions.sort(key=lambda item: item["sample_index"])

    for transition in transitions:
        transition["time_ms"] = transition["sample_index"] * sample_interval_ms
        transition["time_s"] = round(transition["time_ms"] / 1000.0, 3)

    available_sample_bytes = len(data) - header_size
    physically_available_samples = available_sample_bytes // sample_size
    trailing_bytes = available_sample_bytes % sample_size

    # In a clean file, header sampleCount and physical count match. In an interrupted
    # recording the header can be incomplete, so parse whatever complete samples exist.
    parse_count = min(sample_count, physically_available_samples) if sample_count else physically_available_samples

    samples: list[dict[str, Any]] = []
    phase_cursor = -1
    current_phase_number: Optional[int] = None
    current_phase_name: Optional[str] = None

    offset = header_size
    for sample_index in range(parse_count):
        while (
            phase_cursor + 1 < len(transitions)
            and transitions[phase_cursor + 1]["sample_index"] <= sample_index
        ):
            phase_cursor += 1
            current_phase_number = transitions[phase_cursor]["phase_number"]
            current_phase_name = transitions[phase_cursor]["phase_name"]

        (
            tick,
            target_temp_x10,
            current_temp_x10,
            target_pressure_x10,
            current_pressure_x10,
            pump_flow_x100,
            target_flow_x100,
            puck_flow_x100,
            bluetooth_flow_x100,
            bluetooth_weight_x10,
            estimated_weight_x10,
            puck_resistance_x100,
            system_info,
        ) = SHOT_SAMPLE_V5.unpack_from(data, offset)
        offset += sample_size

        time_ms = tick * sample_interval_ms
        samples.append(
            {
                "sample_index": sample_index,
                "tick": tick,
                "time_ms": time_ms,
                "time_s": round(time_ms / 1000.0, 3),
                "target_temperature_c": round(target_temp_x10 / 10.0, 1),
                "temperature_c": round(current_temp_x10 / 10.0, 1),
                "target_pressure_bar": round(target_pressure_x10 / 10.0, 1),
                "pressure_bar": round(current_pressure_x10 / 10.0, 1),
                "pump_flow_ml_s": round(pump_flow_x100 / 100.0, 2),
                "target_flow_ml_s": round(target_flow_x100 / 100.0, 2),
                "puck_flow_ml_s": round(puck_flow_x100 / 100.0, 2),
                "scale_flow_ml_s": round(bluetooth_flow_x100 / 100.0, 2),
                "scale_weight_g": round(bluetooth_weight_x10 / 10.0, 1),
                "estimated_weight_g": round(estimated_weight_x10 / 10.0, 1),
                "puck_resistance": round(puck_resistance_x100 / 100.0, 2),
                "phase_number": current_phase_number,
                "phase_name": current_phase_name,
                "system_info": system_info_to_json(system_info),
            }
        )

    return {
        "format": {
            "magic": "SHOT",
            "version": version,
            "header_size": header_size,
            "sample_size": sample_size,
            "sample_interval_ms": sample_interval_ms,
            "fields_mask": fields_mask,
        },
        "shot": {
            "id": shot_id,
            "timestamp": start_epoch,
            "timestamp_iso_utc": epoch_to_iso(start_epoch),
            "profile_id": decode_c_string(profile_id_raw),
            "profile_name": decode_c_string(profile_name_raw),
            "duration_ms": duration_ms,
            "duration_s": round(duration_ms / 1000.0, 3),
            "final_weight_g": round(final_weight_x10 / 10.0, 1),
            "sample_count_header": sample_count,
            "sample_count_parsed": parse_count,
            "incomplete_header": sample_count == 0,
            "physical_sample_count": physically_available_samples,
            "trailing_bytes": trailing_bytes,
            "final_exit_reason": final_exit_reason,
            "final_exit_reason_name": PHASE_EXIT_REASON_NAMES.get(final_exit_reason, f"unknown_{final_exit_reason}"),
            "brew_delay_ms": brew_delay_ms,
        },
        "phase_transitions": transitions,
        "samples": samples,
    }


def fetch_notes(
    base_url: str,
    shot_id: int,
    *,
    timeout: float,
    retries: int,
) -> Optional[Any]:
    padded = f"{shot_id:06d}"
    candidates = [
        urljoin(base_url, f"api/history/{padded}.json"),
        urljoin(base_url, f"api/history/{shot_id}.json"),
    ]

    for url in candidates:
        raw = http_get(url, timeout=timeout, retries=retries, allow_404=True)
        if raw is None:
            continue
        try:
            return json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return {
                "_parse_error": "Notes file was not valid UTF-8 JSON",
                "_raw_text": raw.decode("utf-8", errors="replace"),
            }
    return None


def write_json(path: Path, obj: Any, indent: int) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.write("\n")
    tmp.replace(path)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Download all GaggiMate shot logs from /api/history and convert current "
            "v5 .slog files into one JSON file per shot."
        )
    )
    parser.add_argument(
        "host",
        nargs="?",
        default="192.168.50.68",
        help="GaggiMate IP/hostname (default: 192.168.50.68)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="gaggimate-shots",
        help="Output directory (default: gaggimate-shots)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing shot-<id>.json files",
    )
    parser.add_argument(
        "--keep-slog",
        action="store_true",
        help="Also save the original .slog files under <output>/raw/",
    )
    parser.add_argument(
        "--keep-index-bin",
        action="store_true",
        help="Also save the original index.bin under <output>/raw/",
    )
    parser.add_argument(
        "--no-notes",
        action="store_true",
        help="Do not try to download the optional per-shot notes JSON",
    )
    parser.add_argument(
        "--start-id",
        type=int,
        default=None,
        help="Only process shot IDs >= this value",
    )
    parser.add_argument(
        "--end-id",
        type=int,
        default=None,
        help="Only process shot IDs <= this value",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=15.0,
        help="HTTP timeout in seconds (default: 15)",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="HTTP attempts per file (default: 3)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.05,
        help="Delay between shot downloads in seconds (default: 0.05)",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="JSON indentation (default: 2)",
    )
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()

    if args.retries < 1:
        print("--retries must be at least 1", file=sys.stderr)
        return 2
    if args.timeout <= 0:
        print("--timeout must be > 0", file=sys.stderr)
        return 2
    if args.delay < 0:
        print("--delay must be >= 0", file=sys.stderr)
        return 2

    base_url = normalize_base_url(args.host)
    output_dir = Path(args.output).expanduser().resolve()
    raw_dir = output_dir / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)
    if args.keep_slog or args.keep_index_bin:
        raw_dir.mkdir(parents=True, exist_ok=True)

    index_url = urljoin(base_url, "api/history/index.bin")
    print(f"GaggiMate: {base_url.rstrip('/')}")
    print(f"Index:     {index_url}")
    print(f"Output:    {output_dir}")
    print()

    try:
        index_bytes = http_get(
            index_url,
            timeout=args.timeout,
            retries=args.retries,
        )
        assert index_bytes is not None
        index_header, all_entries = parse_index(index_bytes)
    except Exception as exc:
        print(f"ERROR: could not download/parse index.bin: {exc}", file=sys.stderr)
        return 1

    if args.keep_index_bin:
        (raw_dir / "index.bin").write_bytes(index_bytes)

    # Keep the last index record for each ID, then ignore records marked deleted.
    # This is robust even if an older firmware/index rebuild left duplicate IDs.
    latest_by_id: dict[int, ShotIndexEntry] = {}
    for entry in all_entries:
        latest_by_id[entry.shot_id] = entry
    active_entries = [entry for entry in latest_by_id.values() if not entry.deleted]
    active_entries.sort(key=lambda entry: entry.shot_id)

    if args.start_id is not None:
        active_entries = [entry for entry in active_entries if entry.shot_id >= args.start_id]
    if args.end_id is not None:
        active_entries = [entry for entry in active_entries if entry.shot_id <= args.end_id]

    index_json = {
        "source": {
            "gaggimate": base_url.rstrip("/"),
            "endpoint": "/api/history/index.bin",
            "downloaded_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        },
        "index": index_header,
        "entries": [entry.as_json() for entry in all_entries],
    }
    write_json(output_dir / "index.json", index_json, args.indent)

    print(
        f"Index entries: {len(all_entries)} total, "
        f"{sum(1 for e in all_entries if e.deleted)} deleted, "
        f"{len(active_entries)} selected"
    )
    print()

    downloaded = 0
    skipped = 0
    failed = 0
    unsupported = 0

    for position, entry in enumerate(active_entries, start=1):
        shot_id = entry.shot_id
        padded = f"{shot_id:06d}"
        json_path = output_dir / f"shot-{padded}.json"

        prefix = f"[{position:>4}/{len(active_entries):<4}] shot {shot_id}"

        if json_path.exists() and not args.force:
            print(f"{prefix}: already exists -> {json_path.name}")
            skipped += 1
            continue

        slog_url = urljoin(base_url, f"api/history/{padded}.slog")
        slog_bytes: Optional[bytes] = None

        try:
            slog_bytes = http_get(
                slog_url,
                timeout=args.timeout,
                retries=args.retries,
            )
            assert slog_bytes is not None

            if args.keep_slog:
                (raw_dir / f"{padded}.slog").write_bytes(slog_bytes)

            parsed = parse_slog_v5(slog_bytes, shot_id)

            notes = None
            if not args.no_notes:
                notes = fetch_notes(
                    base_url,
                    shot_id,
                    timeout=args.timeout,
                    retries=args.retries,
                )

            parsed["source"] = {
                "gaggimate": base_url.rstrip("/"),
                "slog_endpoint": f"/api/history/{padded}.slog",
                "notes_endpoint": f"/api/history/{padded}.json",
                "downloaded_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            }
            parsed["index_entry"] = entry.as_json()
            parsed["notes"] = notes

            write_json(json_path, parsed, args.indent)
            downloaded += 1
            print(
                f"{prefix}: OK -> {json_path.name} "
                f"({parsed['shot']['sample_count_parsed']} samples, "
                f"{parsed['shot']['duration_s']:.3f}s)"
            )

        except UnsupportedSlogVersion as exc:
            unsupported += 1
            failed += 1
            # Preserve unknown/old logs for later decoding, even without --keep-slog.
            raw_dir.mkdir(parents=True, exist_ok=True)
            try:
                if slog_bytes is not None:
                    fallback = raw_dir / f"{padded}.slog"
                    fallback.write_bytes(slog_bytes)
                    print(f"{prefix}: UNSUPPORTED -> saved raw {fallback}", file=sys.stderr)
                else:
                    print(f"{prefix}: UNSUPPORTED: {exc}", file=sys.stderr)
            except OSError:
                print(f"{prefix}: UNSUPPORTED: {exc}", file=sys.stderr)

        except Exception as exc:
            failed += 1
            print(f"{prefix}: ERROR: {exc}", file=sys.stderr)

        if args.delay:
            time.sleep(args.delay)

    print()
    print("Done.")
    print(f"  JSON created: {downloaded}")
    print(f"  Skipped:      {skipped}")
    print(f"  Failed:       {failed}")
    if unsupported:
        print(f"  Unsupported:  {unsupported} (raw .slog saved under {raw_dir})")
    print(f"  Directory:    {output_dir}")

    return 0 if failed == 0 else 3


if __name__ == "__main__":
    raise SystemExit(main())
