#!/usr/bin/env python3
"""Build ``profiles/catalog.json`` from the repository profile folders.

The script scans every immediate subdirectory of ``profiles/`` and treats every
GaggiMate JSON file in that folder as a profile variant. It derives data from:

1. the GaggiMate JSON profile;
2. ``{folder}-recipe.md`` (when present);
3. the previous ``profiles/catalog.json`` (to preserve curated UI metadata);
4. an optional per-folder ``catalog.meta.json`` override.

This makes new profiles discoverable without editing ``index.html``. Fields that
cannot be inferred reliably (for example marketing subtitle, flavour notes,
accent colours or featured status) can be kept in the existing catalog or in a
small ``catalog.meta.json`` file.

Typical usage:

    python tools/build_catalog.py
    python tools/build_catalog.py --check
    python tools/build_catalog.py --dry-run
    python tools/build_catalog.py --no-preserve

Per-folder override example (``profiles/example/catalog.meta.json``):

    {
      "title": "Ethiopia Yirgacheffe",
      "subtitle": "Floral Citrus",
      "origin": "Roaster · Ethiopia",
      "process": "washed",
      "notes": ["jasmine", "lemon", "black tea"],
      "grind": "9–10",
      "featured": true,
      "accent": "#7d1d2f",
      "accent2": "#b94a31",
      "variants": {
        "ethiopia-yirgacheffe-scale.json": {
          "label": "Scale V2",
          "default": true
        }
      }
    }
"""
from __future__ import annotations

import argparse
import copy
import difflib
import hashlib
import json
import math
import re
import sys
import unicodedata
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable, Mapping, MutableMapping, Sequence

JSONDict = dict[str, Any]

PROFILE_ROOT_KEYS = {
    "id",
    "label",
    "type",
    "description",
    "temperature",
    "favorite",
    "selected",
    "utility",
    "phases",
}

DEFAULTS: JSONDict = {
    "dose": 18.5,
    "rpm": 1200,
    "machine": "Gaggia Classic Pro 2025 + GaggiMate Pro",
    "grinder": "DF64V Gen 2 · SSP Sweet Lab Espresso V3",
    "basket": "IMS B682TH24.5M",
    "scale": "BOOKOO Themis Ultra",
}

PALETTES: tuple[tuple[str, str], ...] = (
    ("#7d1d2f", "#b94a31"),
    ("#8c294b", "#bc5271"),
    ("#4b2458", "#70406f"),
    ("#6f2b55", "#bd6a4f"),
    ("#365d65", "#73a0a3"),
    ("#6b3a2a", "#bd7851"),
    ("#485c35", "#879b61"),
    ("#7a4d20", "#c28a43"),
)


@dataclass(frozen=True)
class VariantSource:
    path: Path
    data: JSONDict
    kind: str
    version: int | None


class CatalogError(RuntimeError):
    """Raised for a catalog generation error that should stop the build."""


def detect_root(script_path: Path) -> Path:
    """Find the repository root while supporting the standard ``tools/`` layout."""
    resolved = script_path.resolve()
    if resolved.parent.name == "tools" and (resolved.parent.parent / "profiles").is_dir():
        return resolved.parent.parent

    for candidate in (resolved.parent, *resolved.parents):
        if (candidate / "profiles").is_dir():
            return candidate
    return resolved.parent


DEFAULT_ROOT = detect_root(Path(__file__))


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help=f"Repository root (default: {DEFAULT_ROOT}).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("profiles/catalog.json"),
        help="Output path, relative to --root unless absolute.",
    )
    parser.add_argument(
        "--metadata-name",
        default="catalog.meta.json",
        help="Optional per-profile metadata filename (default: catalog.meta.json).",
    )
    parser.add_argument(
        "--no-preserve",
        action="store_true",
        help="Do not preserve curated fields from an existing catalog.json.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail when companion recipe/changelog/PNG files are missing.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write; exit 1 when catalog.json would change.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the generated catalog to stdout instead of writing it.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print discovered folders and warnings.",
    )
    return parser.parse_args(argv)


def resolve_output(root: Path, output: Path) -> Path:
    return output.resolve() if output.is_absolute() else (root / output).resolve()


def read_json(path: Path, *, required: bool = True) -> JSONDict:
    try:
        raw = path.read_text(encoding="utf-8-sig")
    except FileNotFoundError:
        if required:
            raise CatalogError(f"Missing JSON file: {path}")
        return {}
    except OSError as exc:
        raise CatalogError(f"Cannot read {path}: {exc}") from exc

    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CatalogError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CatalogError(f"JSON root must be an object: {path}")
    return value


def clean_markdown(value: str) -> str:
    value = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
    value = value.replace("**", "").replace("__", "").replace("`", "")
    value = re.sub(r"<[^>]+>", "", value)
    return re.sub(r"\s+", " ", value).strip()


def ascii_key(value: str) -> str:
    value = clean_markdown(value).lower().replace("–", "-").replace("—", "-")
    value = "".join(
        char for char in unicodedata.normalize("NFKD", value) if not unicodedata.combining(char)
    )
    return re.sub(r"[^a-z0-9]+", " ", value).strip()


def markdown_rows(text: str) -> dict[str, str]:
    rows: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not (line.startswith("|") and line.endswith("|")):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 2:
            continue
        key, value = cells
        if not key or re.fullmatch(r"[-: ]+", key) or re.fullmatch(r"[-: ]+", value):
            continue
        rows.setdefault(ascii_key(key), clean_markdown(value))
    return rows


def first_row(rows: Mapping[str, str], keys: Iterable[str]) -> str:
    for key in keys:
        value = rows.get(ascii_key(key), "").strip()
        if value:
            return value
    return ""


def parse_decimal(value: Any) -> float | None:
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, float)):
        number = float(value)
        return number if math.isfinite(number) else None
    match = re.search(r"-?\d+(?:[.,]\d+)?", str(value))
    if not match:
        return None
    try:
        number = float(match.group(0).replace(",", "."))
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def fmt_number(value: float, digits: int = 1) -> str:
    rounded = round(value, digits)
    if math.isclose(rounded, round(rounded), abs_tol=10 ** (-(digits + 1))):
        return str(int(round(rounded)))
    return f"{rounded:.{digits}f}".rstrip("0").rstrip(".").replace(".", ",")


def phase_total(profile: Mapping[str, Any]) -> float:
    phases = profile.get("phases")
    if not isinstance(phases, list):
        return 0.0
    total = 0.0
    for phase in phases:
        if isinstance(phase, dict):
            duration = parse_decimal(phase.get("duration")) or 0.0
            total += max(0.0, duration)
    return total


def last_weight_target(profile: Mapping[str, Any]) -> float | None:
    result: float | None = None
    phases = profile.get("phases")
    if not isinstance(phases, list):
        return None
    for phase in phases:
        if not isinstance(phase, dict):
            continue
        targets = phase.get("targets")
        if not isinstance(targets, list):
            continue
        for target in targets:
            if not isinstance(target, dict) or target.get("type") != "volumetric":
                continue
            value = parse_decimal(target.get("value"))
            if value is not None and value > 0:
                result = value
    return result


def detect_kind(stem: str) -> str:
    lowered = stem.lower()
    if re.search(r"(?:^|-)scale(?:-|$)", lowered):
        return "scale"
    if re.search(r"(?:^|-)manual(?:-|$)", lowered):
        return "manual"
    return "general"


def detect_version(stem: str) -> int | None:
    match = re.search(r"-v(\d+)$", stem.lower())
    return int(match.group(1)) if match else None


def variant_id(source: VariantSource) -> str:
    stem = source.path.stem.lower()
    if source.kind == "general":
        stem = re.sub(r"^profile-", "", stem)
        return stem or "general"
    marker = f"-{source.kind}"
    index = stem.find(marker)
    if index >= 0:
        result = stem[index + 1 :]
    elif stem.startswith(source.kind):
        result = stem
    else:
        result = source.kind
    return result


def concise_label(source: VariantSource, same_kind_count: int) -> str:
    temperature = parse_decimal(source.data.get("temperature"))
    total = phase_total(source.data)

    if source.kind == "general":
        return str(source.data.get("label") or source.path.stem)

    base = "Scale" if source.kind == "scale" else "Manual"
    if source.version is not None:
        base += f" V{source.version}"
    elif source.kind == "scale":
        base += " V2"
    elif total > 0:
        base += f" {fmt_number(total, 0)} s"

    if same_kind_count > 1 and temperature is not None:
        base += f" · {fmt_number(temperature)} °C"
    return base


def split_notes(value: str) -> list[str]:
    if not value:
        return []
    parts = re.split(r"\s*(?:·|;|\||,| / )\s*", clean_markdown(value))
    return [part for part in (item.strip(" .") for item in parts) if part][:6]


def strip_technical_label(label: str) -> str:
    value = clean_markdown(label)
    value = re.sub(r"\s+[–-]\s+Scale\s+V\d+.*$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"\s+[–-]\s+\d+(?:[.,]\d+)?\s*g.*$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"\s+\d+(?:[.,]\d+)?-\d+.*$", "", value)
    return value.strip(" –-")


def deterministic_palette(folder_name: str) -> tuple[str, str]:
    digest = hashlib.sha256(folder_name.encode("utf-8")).digest()
    return PALETTES[int.from_bytes(digest[:2], "big") % len(PALETTES)]


def find_companion(folder: Path, suffix: str) -> Path | None:
    preferred = folder / f"{folder.name}-{suffix}"
    if preferred.is_file():
        return preferred
    candidates = sorted(folder.glob(f"*-{suffix}"))
    return candidates[0] if candidates else None


def detect_page(folder: Path) -> str | None:
    preferred = folder / f"{folder.name}.html"
    if preferred.is_file():
        return preferred.name
    candidates = sorted(folder.glob("*.html"))
    return candidates[0].name if len(candidates) == 1 else None


def read_recipe(folder: Path) -> tuple[Path | None, dict[str, str]]:
    recipe = find_companion(folder, "recipe.md")
    if recipe is None:
        return None, {}
    try:
        return recipe, markdown_rows(recipe.read_text(encoding="utf-8-sig"))
    except OSError as exc:
        raise CatalogError(f"Cannot read recipe {recipe}: {exc}") from exc


def infer_process(rows: Mapping[str, str], profiles: Sequence[VariantSource]) -> str:
    direct = first_row(rows, ("Feldolgozás", "Processing", "Process"))
    if direct:
        return direct
    text = " ".join(
        str(source.data.get(field, ""))
        for source in profiles
        for field in ("label", "description")
    ).lower()
    patterns = (
        ("anaerob", "anaerobic"),
        ("natural", "natural"),
        ("washed", "washed"),
        ("honey", "honey"),
        ("lever", "lever"),
        ("adaptive", "univerzális"),
    )
    for token, result in patterns:
        if token in text:
            return result
    return "profil"


def derive_entry(folder: Path, sources: Sequence[VariantSource], defaults: Mapping[str, Any]) -> JSONDict:
    recipe_path, rows = read_recipe(folder)
    primary = choose_default_source(sources)
    profile = primary.data

    brand = first_row(rows, ("Márka", "Roaster", "Pörkölő"))
    coffee = first_row(rows, ("Kávé", "Coffee"))
    label = str(profile.get("label") or folder.name.replace("-", " ").title())
    title = f"{brand} {coffee}".strip() if coffee else strip_technical_label(label)
    title = title or folder.name.replace("-", " ").title()

    process = infer_process(rows, sources)
    notes = split_notes(first_row(rows, ("Ízjegyek", "Ízprofil", "Tasting notes", "Notes")))
    subtitle = " · ".join(notes[:2]) if notes else str(profile.get("description") or "GaggiMate Pro espresso profil")

    origin_bits = [
        first_row(rows, ("Márka", "Roaster", "Pörkölő")),
        first_row(rows, ("Eredet", "Origin", "Régió / farm", "Régió", "Farm", "Termőhely")),
    ]
    origin = " · ".join(bit for bit in origin_bits if bit)
    if not origin:
        origin = "Általános espresso profil" if process in {"profil", "lever", "univerzális"} else title

    grind = first_row(
        rows,
        ("Őrlés tartomány", "Őrlés indulás", "Őrlés", "Grind range", "Grind"),
    ) or "recept szerint"

    dose_value = first_row(rows, ("Dózis", "Dose"))
    dose = parse_decimal(dose_value)
    if dose is None:
        dose = parse_decimal(defaults.get("dose")) or 18.5

    yield_value = first_row(rows, ("Ideális hozam", "Cél hozam", "Célhozam", "Target Yield"))
    target = last_weight_target(profile)
    output_yield = yield_value or (f"{fmt_number(target)} g" if target is not None else "—")

    expected_time = first_row(rows, ("Cél idő", "Teljes profilidő", "Profilidő", "Target time"))
    if not expected_time:
        expected_time = f"{fmt_number(phase_total(profile), 0)} s"

    accent, accent2 = deterministic_palette(folder.name)
    return {
        "id": folder.name,
        "folder": folder.name,
        "title": title,
        "subtitle": subtitle,
        "origin": origin,
        "process": process,
        "notes": notes,
        "grind": grind,
        "dose": dose,
        "yield": output_yield,
        "expectedTime": expected_time,
        "page": detect_page(folder),
        "accent": accent,
        "accent2": accent2,
        "featured": False,
        "variants": build_variants(sources),
        "_recipe": recipe_path.name if recipe_path else None,
    }


def choose_default_source(sources: Sequence[VariantSource]) -> VariantSource:
    def key(source: VariantSource) -> tuple[int, int, str]:
        kind_priority = {"scale": 3, "manual": 2, "general": 1}[source.kind]
        return kind_priority, source.version or 0, source.path.name.lower()

    return max(sources, key=key)


def build_variants(sources: Sequence[VariantSource]) -> list[JSONDict]:
    counts: dict[str, int] = {}
    for source in sources:
        counts[source.kind] = counts.get(source.kind, 0) + 1

    default_source = choose_default_source(sources)
    result: list[JSONDict] = []
    used_ids: set[str] = set()
    kind_order = {"scale": 0, "manual": 1, "general": 2}
    for source in sorted(
        sources,
        key=lambda item: (kind_order[item.kind], -(item.version or 0), item.path.name.lower()),
    ):
        item_id = variant_id(source)
        base_id = item_id
        suffix = 2
        while item_id in used_ids:
            item_id = f"{base_id}-{suffix}"
            suffix += 1
        used_ids.add(item_id)

        item: JSONDict = {
            "id": item_id,
            "label": concise_label(source, counts[source.kind]),
            "kind": source.kind,
            "file": source.path.name,
        }
        if source.path == default_source.path:
            item["default"] = True
        result.append(item)
    return result


def load_sources(folder: Path, metadata_name: str) -> list[VariantSource]:
    sources: list[VariantSource] = []
    excluded = {"catalog.json", "catalog.defaults.json", metadata_name}
    for path in sorted(folder.glob("*.json")):
        if path.name in excluded or path.name.startswith("catalog."):
            continue
        data = read_json(path)
        # Do not accidentally treat arbitrary JSON files as a GaggiMate profile.
        if not isinstance(data.get("phases"), list) or not data.get("phases"):
            continue
        unknown = {key for key in data if not key.startswith("_")} - PROFILE_ROOT_KEYS
        if unknown:
            raise CatalogError(f"Unknown GaggiMate root keys in {path}: {sorted(unknown)}")
        sources.append(
            VariantSource(
                path=path,
                data=data,
                kind=detect_kind(path.stem),
                version=detect_version(path.stem),
            )
        )
    return sources


def merge_dict(base: JSONDict, overlay: Mapping[str, Any], *, skip: set[str] | None = None) -> JSONDict:
    result = copy.deepcopy(base)
    blocked = skip or set()
    for key, value in overlay.items():
        if key in blocked or key.startswith("_"):
            continue
        result[key] = copy.deepcopy(value)
    return result


def variant_overrides(value: Any) -> dict[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(item, dict):
                result[str(key)] = item
    elif isinstance(value, list):
        for item in value:
            if not isinstance(item, dict):
                continue
            key = item.get("file") or item.get("id")
            if key:
                result[str(key)] = item
    return result


def merge_variants(
    derived: Sequence[JSONDict],
    existing: Any,
    metadata: Any,
) -> list[JSONDict]:
    existing_map = variant_overrides(existing)
    metadata_map = variant_overrides(metadata)
    result: list[JSONDict] = []

    for source in derived:
        item = copy.deepcopy(source)
        keys = (str(item.get("file", "")), str(item.get("id", "")))
        for mapping in (existing_map, metadata_map):
            for key in keys:
                if key and key in mapping:
                    item = merge_dict(item, mapping[key], skip={"file"})
        result.append(item)

    # Exactly one default must exist. Metadata wins, then existing, then derived.
    default_indexes = [index for index, item in enumerate(result) if item.get("default")]
    if not default_indexes:
        result[0]["default"] = True
    elif len(default_indexes) > 1:
        keep = default_indexes[0]
        for index, item in enumerate(result):
            if index != keep:
                item.pop("default", None)
    return result


def clean_entry(entry: JSONDict) -> JSONDict:
    entry.pop("_recipe", None)
    # Stable, index-friendly key order.
    order = (
        "id",
        "folder",
        "title",
        "subtitle",
        "origin",
        "process",
        "notes",
        "grind",
        "dose",
        "yield",
        "expectedTime",
        "page",
        "accent",
        "accent2",
        "featured",
        "variants",
    )
    return {key: entry[key] for key in order if key in entry}


def build_entry(
    folder: Path,
    sources: Sequence[VariantSource],
    defaults: Mapping[str, Any],
    existing: Mapping[str, Any] | None,
    metadata_name: str,
) -> JSONDict:
    derived = derive_entry(folder, sources, defaults)
    metadata_path = folder / metadata_name
    metadata = read_json(metadata_path, required=False)

    entry = derived
    if existing:
        # File-derived fields such as ``page`` must follow the actual directory
        # contents. Curated descriptive/UI fields are preserved.
        entry = merge_dict(entry, existing, skip={"id", "folder", "page", "variants"})
    if metadata:
        entry = merge_dict(entry, metadata, skip={"id", "folder", "variants"})

    entry["id"] = folder.name
    entry["folder"] = folder.name
    entry["variants"] = merge_variants(
        derived["variants"],
        existing.get("variants") if existing else None,
        metadata.get("variants") if metadata else None,
    )
    return clean_entry(entry)


def warn(message: str, warnings: list[str], verbose: bool) -> None:
    warnings.append(message)
    if verbose:
        print(f"warning: {message}", file=sys.stderr)


def validate_companions(entry: Mapping[str, Any], folder: Path, warnings: list[str], verbose: bool) -> None:
    recipe = folder / f"{folder.name}-recipe.md"
    changelog = folder / f"{folder.name}-changelog.md"
    if not recipe.is_file():
        warn(f"missing recipe: {recipe}", warnings, verbose)
    if not changelog.is_file():
        warn(f"missing changelog: {changelog}", warnings, verbose)

    page = entry.get("page")
    if page and not (folder / str(page)).is_file():
        warn(f"missing HTML page: {folder / str(page)}", warnings, verbose)

    for variant in entry.get("variants", []):
        if not isinstance(variant, dict):
            continue
        file_name = str(variant.get("file", ""))
        if not file_name or not (folder / file_name).is_file():
            raise CatalogError(f"Catalog variant file is missing: {folder / file_name}")
        png = folder / re.sub(r"\.json$", "-profile.png", file_name, flags=re.IGNORECASE)
        if not png.is_file():
            warn(f"missing generated PNG: {png}", warnings, verbose)


def validate_catalog(catalog: Mapping[str, Any]) -> None:
    profiles = catalog.get("profiles")
    if not isinstance(profiles, list):
        raise CatalogError("catalog profiles must be an array")

    ids: set[str] = set()
    for entry in profiles:
        if not isinstance(entry, dict):
            raise CatalogError("every catalog profile must be an object")
        entry_id = str(entry.get("id", ""))
        if not entry_id:
            raise CatalogError("catalog profile has no id")
        if entry_id in ids:
            raise CatalogError(f"duplicate profile id: {entry_id}")
        ids.add(entry_id)

        variants = entry.get("variants")
        if not isinstance(variants, list) or not variants:
            raise CatalogError(f"profile {entry_id} has no variants")
        variant_ids: set[str] = set()
        default_count = 0
        for variant in variants:
            if not isinstance(variant, dict):
                raise CatalogError(f"invalid variant in {entry_id}")
            variant_id_value = str(variant.get("id", ""))
            if not variant_id_value or variant_id_value in variant_ids:
                raise CatalogError(f"missing or duplicate variant id in {entry_id}: {variant_id_value}")
            variant_ids.add(variant_id_value)
            if variant.get("default"):
                default_count += 1
        if default_count != 1:
            raise CatalogError(f"profile {entry_id} must have exactly one default variant")


def catalog_without_updated(catalog: Mapping[str, Any]) -> JSONDict:
    result = copy.deepcopy(dict(catalog))
    result.pop("updated", None)
    return result


def generate_catalog(options: argparse.Namespace) -> tuple[JSONDict, list[str]]:
    root = options.root.resolve()
    profiles_root = root / "profiles"
    if not profiles_root.is_dir():
        raise CatalogError(f"profiles directory not found: {profiles_root}")

    output = resolve_output(root, options.output)
    existing_catalog = {} if options.no_preserve else read_json(output, required=False)
    existing_entries = {
        str(item.get("folder") or item.get("id")): item
        for item in existing_catalog.get("profiles", [])
        if isinstance(item, dict)
    }

    defaults = copy.deepcopy(DEFAULTS)
    if isinstance(existing_catalog.get("defaults"), dict) and not options.no_preserve:
        defaults.update(existing_catalog["defaults"])
    defaults_file = profiles_root / "catalog.defaults.json"
    if defaults_file.is_file():
        defaults.update(read_json(defaults_file))

    warnings: list[str] = []
    entries: list[JSONDict] = []
    for folder in sorted((item for item in profiles_root.iterdir() if item.is_dir()), key=lambda p: p.name):
        sources = load_sources(folder, options.metadata_name)
        if not sources:
            continue
        if options.verbose:
            print(f"profile: {folder.name} ({len(sources)} variant(s))", file=sys.stderr)
        existing = existing_entries.get(folder.name)
        entry = build_entry(folder, sources, defaults, existing, options.metadata_name)
        validate_companions(entry, folder, warnings, options.verbose)
        entries.append(entry)

    if not entries:
        raise CatalogError(f"no GaggiMate profile JSON files found under {profiles_root}")

    version = existing_catalog.get("version", 1) if not options.no_preserve else 1
    candidate: JSONDict = {
        "version": version,
        "updated": str(existing_catalog.get("updated") or date.today().isoformat()),
        "defaults": defaults,
        "profiles": entries,
    }

    # Keep the date stable unless the generated content actually changes.
    if catalog_without_updated(candidate) != catalog_without_updated(existing_catalog):
        candidate["updated"] = date.today().isoformat()

    validate_catalog(candidate)
    if options.strict and warnings:
        raise CatalogError("strict mode failed:\n- " + "\n- ".join(warnings))
    return candidate, warnings


def json_text(value: Mapping[str, Any]) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def write_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(text, encoding="utf-8", newline="\n")
    temp.replace(path)


def main(argv: Sequence[str] | None = None) -> int:
    options = parse_args(sys.argv[1:] if argv is None else argv)
    root = options.root.resolve()
    output = resolve_output(root, options.output)

    try:
        catalog, warnings = generate_catalog(options)
    except CatalogError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    generated = json_text(catalog)
    current = output.read_text(encoding="utf-8-sig") if output.is_file() else ""

    if options.dry_run:
        sys.stdout.write(generated)
        return 0

    if options.check:
        if current == generated:
            print(f"up to date: {output}")
            return 0
        print(f"catalog would change: {output}", file=sys.stderr)
        diff = difflib.unified_diff(
            current.splitlines(),
            generated.splitlines(),
            fromfile=str(output),
            tofile=f"{output} (generated)",
            lineterm="",
        )
        for line in diff:
            print(line, file=sys.stderr)
        return 1

    if current == generated:
        print(f"unchanged: {output}")
    else:
        write_atomic(output, generated)
        print(f"written: {output}")
    print(f"profiles: {len(catalog['profiles'])}")
    print(f"variants: {sum(len(entry['variants']) for entry in catalog['profiles'])}")
    if warnings and not options.verbose:
        print(f"warnings: {len(warnings)} (run with --verbose for details)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
