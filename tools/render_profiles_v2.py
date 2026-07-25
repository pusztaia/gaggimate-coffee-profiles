#!/usr/bin/env python3
"""Render GaggiMate JSON profiles to PNG charts.

The renderer follows the GaggiMate profile schema:

- ``phase.temperature == 0`` inherits the profile-level temperature.
- only the pump field selected by ``pump.target`` is an active setpoint;
  the other field is a soft limit, and a zero limit means "disabled".
- ``-1`` is a dynamic hold sentinel, so the exact value cannot be known from
  the JSON alone and is labelled as HOLD instead of being plotted as -1.
- phase durations are maximum durations. A phase target may end a phase early.
- pressure/flow transitions are rendered as schematic setpoint ramps.
  Adaptive ramps start from a measured value at runtime, so their exact start
  cannot be reconstructed from a static profile file.

Usage:
  python tools/render_profiles.py
  python tools/render_profiles.py profiles/wangera/wangera-scale-v2.json
  python tools/render_profiles.py --root /path/to/repository
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Tuple

import matplotlib.pyplot as plt

JSONDict = Dict[str, Any]


@dataclass(frozen=True)
class ProfileMetadata:
    coffee: str = ""
    dose: str = ""
    target_yield: str = ""
    grind: str = ""


@dataclass(frozen=True)
class HoldAnnotation:
    variable: str
    x: float
    phase_name: str


def detect_root(script_path: Path) -> Path:
    """Find the repository root while preserving the original tools/ layout."""
    resolved = script_path.resolve()
    if resolved.parent.name == "tools":
        return resolved.parent.parent

    for parent in (resolved.parent, *resolved.parents):
        if (parent / "profiles").is_dir():
            return parent

    # Useful when testing the standalone file outside the repository.
    return resolved.parent


DEFAULT_ROOT = detect_root(Path(__file__))


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "profiles",
        nargs="*",
        help="Profile JSON paths. Relative paths are resolved from --root.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help=f"Repository root (default: {DEFAULT_ROOT}).",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=160,
        help="PNG resolution in dots per inch (default: 160).",
    )
    return parser.parse_args(argv)


def find_profiles(root: Path, args: Sequence[str]) -> List[Path]:
    if args:
        paths: List[Path] = []
        for value in args:
            candidate = Path(value)
            paths.append(candidate.resolve() if candidate.is_absolute() else (root / candidate).resolve())
        return paths
    return sorted((root / "profiles").glob("**/*.json"))


def read_json(path: Path) -> JSONDict:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read JSON profile {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"profile root must be a JSON object: {path}")
    return value


def as_float(value: Any, default: float = 0.0) -> float:
    if value is None or isinstance(value, bool):
        return default
    try:
        number = float(value)
    except (TypeError, ValueError):
        return default
    return number if math.isfinite(number) else default


def clean_markdown(value: str) -> str:
    value = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
    value = value.replace("**", "").replace("__", "").replace("`", "")
    value = re.sub(r"<[^>]+>", "", value)
    return re.sub(r"\s+", " ", value).strip()


def normalize_key(value: str) -> str:
    value = clean_markdown(value).lower().replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", value).strip()


def markdown_rows(text: str) -> Dict[str, str]:
    rows: Dict[str, str] = {}
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
        norm = normalize_key(key)
        rows.setdefault(norm, clean_markdown(value))
    return rows


def section_text(text: str, heading: str) -> str:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)",
        re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group(1) if match else ""


def first_value(rows: Mapping[str, str], keys: Iterable[str]) -> str:
    for key in keys:
        value = rows.get(normalize_key(key), "")
        if value:
            return value
    return ""


def find_companion_recipe(profile_path: Path) -> Path | None:
    candidates = sorted(profile_path.parent.glob("*-recipe.md"))
    if not candidates:
        return None

    expected = profile_path.parent / f"{profile_path.parent.name}-recipe.md"
    if expected in candidates:
        return expected

    # Stable fallback for folders whose profile JSON names do not match the recipe prefix.
    return min(candidates, key=lambda item: (len(item.name), item.name.lower()))


def load_metadata(profile_path: Path) -> ProfileMetadata:
    recipe_path = find_companion_recipe(profile_path)
    if recipe_path is None:
        return ProfileMetadata()

    try:
        text = recipe_path.read_text(encoding="utf-8-sig")
    except OSError:
        return ProfileMetadata()

    all_rows = markdown_rows(text)
    base_rows = markdown_rows(section_text(text, "Alap recept"))

    coffee = first_value(all_rows, ("Kávé", "Coffee"))
    dose = first_value(base_rows, ("Dózis", "Dose")) or first_value(all_rows, ("Dózis", "Dose"))
    target_yield = first_value(
        base_rows,
        ("Ideális hozam", "Cél hozam", "Célhozam", "Target Yield"),
    ) or first_value(
        all_rows,
        ("Ideális hozam", "Cél hozam", "Célhozam", "Target Yield"),
    )
    grind = first_value(
        base_rows,
        ("Őrlés indulás", "Őrlés tartomány", "Őrlés", "Grind"),
    ) or first_value(
        all_rows,
        ("Őrlés indulás", "Őrlés tartomány", "Őrlés", "Grind"),
    )

    return ProfileMetadata(coffee=coffee, dose=dose, target_yield=target_yield, grind=grind)


def resolve_temperature(phase: Mapping[str, Any], profile_temperature: float) -> float:
    phase_temperature = as_float(phase.get("temperature"), 0.0)
    return profile_temperature if phase_temperature == 0 else phase_temperature


def easing(kind: str, progress: float) -> float:
    p = min(1.0, max(0.0, progress))
    if kind == "linear":
        return p
    if kind == "ease-in":
        return p * p
    if kind == "ease-out":
        return 1.0 - (1.0 - p) * (1.0 - p)
    if kind == "ease-in-out":
        return 0.5 * (1.0 - math.cos(math.pi * p))
    return 1.0


def pump_object(phase: Mapping[str, Any]) -> Mapping[str, Any] | None:
    pump = phase.get("pump")
    return pump if isinstance(pump, dict) else None


def previous_numeric_value(phases: Sequence[Mapping[str, Any]], index: int, variable: str) -> float:
    for previous in reversed(phases[:index]):
        pump = pump_object(previous)
        if pump is None:
            continue
        value = as_float(pump.get(variable), 0.0)
        if value >= 0:
            return value
    return 0.0


def append_point(xs: List[float], ys: List[float], x: float, y: float) -> None:
    if xs and math.isclose(xs[-1], x, abs_tol=1e-9) and math.isclose(ys[-1], y, abs_tol=1e-9):
        return
    xs.append(x)
    ys.append(y)


def build_setpoint_series(
    phases: Sequence[Mapping[str, Any]], variable: str
) -> Tuple[List[float], List[float], List[HoldAnnotation], bool]:
    """Build the active pressure or flow setpoint curve."""
    xs: List[float] = []
    ys: List[float] = []
    holds: List[HoldAnnotation] = []
    adaptive_ramp_seen = False
    t = 0.0

    for index, phase in enumerate(phases):
        duration = max(0.0, as_float(phase.get("duration"), 0.0))
        t_end = t + duration
        pump = pump_object(phase)
        if pump is None or pump.get("target") != variable:
            # NaN creates a visual gap while preserving the timeline.
            append_point(xs, ys, t, math.nan)
            append_point(xs, ys, t_end, math.nan)
            t = t_end
            continue

        value = as_float(pump.get(variable), 0.0)
        if value == -1:
            holds.append(HoldAnnotation(variable, t + duration / 2.0, str(phase.get("name", ""))))
            append_point(xs, ys, t, math.nan)
            append_point(xs, ys, t_end, math.nan)
            t = t_end
            continue

        transition = phase.get("transition") if isinstance(phase.get("transition"), dict) else {}
        transition_type = str(transition.get("type", "instant"))
        ramp_duration = min(duration, max(0.0, as_float(transition.get("duration"), 0.0)))
        adaptive = bool(transition.get("adaptive", False))
        is_ramp = transition_type != "instant" and ramp_duration > 0

        if is_ramp:
            adaptive_ramp_seen = adaptive_ramp_seen or adaptive
            start_value = previous_numeric_value(phases, index, variable)
            samples = max(12, int(ramp_duration * 8))
            for sample in range(samples + 1):
                fraction = sample / samples
                x = t + ramp_duration * fraction
                y = start_value + (value - start_value) * easing(transition_type, fraction)
                append_point(xs, ys, x, y)
            append_point(xs, ys, t_end, value)
        else:
            # Duplicate x values render a vertical step at phase entry.
            if xs and not math.isnan(ys[-1]):
                append_point(xs, ys, t, ys[-1])
            append_point(xs, ys, t, value)
            append_point(xs, ys, t_end, value)

        t = t_end

    return xs, ys, holds, adaptive_ramp_seen


def build_limit_series(phases: Sequence[Mapping[str, Any]], variable: str) -> Tuple[List[float], List[float], List[HoldAnnotation]]:
    """Build the inactive pressure/flow soft-limit curve."""
    xs: List[float] = []
    ys: List[float] = []
    holds: List[HoldAnnotation] = []
    t = 0.0

    for phase in phases:
        duration = max(0.0, as_float(phase.get("duration"), 0.0))
        t_end = t + duration
        pump = pump_object(phase)
        if pump is None or pump.get("target") == variable:
            append_point(xs, ys, t, math.nan)
            append_point(xs, ys, t_end, math.nan)
            t = t_end
            continue

        value = as_float(pump.get(variable), 0.0)
        if value == 0:
            # Schema sentinel: zero on the non-target side disables the limit.
            append_point(xs, ys, t, math.nan)
            append_point(xs, ys, t_end, math.nan)
        elif value == -1:
            holds.append(HoldAnnotation(variable, t + duration / 2.0, str(phase.get("name", ""))))
            append_point(xs, ys, t, math.nan)
            append_point(xs, ys, t_end, math.nan)
        else:
            if xs and not math.isnan(ys[-1]):
                append_point(xs, ys, t, ys[-1])
            append_point(xs, ys, t, value)
            append_point(xs, ys, t_end, value)
        t = t_end

    return xs, ys, holds


def build_temperature_series(
    phases: Sequence[Mapping[str, Any]], profile_temperature: float
) -> Tuple[List[float], List[float]]:
    xs: List[float] = []
    ys: List[float] = []
    t = 0.0
    previous: float | None = None

    for phase in phases:
        duration = max(0.0, as_float(phase.get("duration"), 0.0))
        value = resolve_temperature(phase, profile_temperature)
        if previous is not None:
            append_point(xs, ys, t, previous)
        append_point(xs, ys, t, value)
        append_point(xs, ys, t + duration, value)
        previous = value
        t += duration

    return xs, ys


def phase_target_text(phase: Mapping[str, Any]) -> str:
    targets = phase.get("targets")
    if not isinstance(targets, list):
        return ""

    units = {"volumetric": "g", "pressure": "bar", "flow": "ml/s", "pumped": "ml"}
    symbols = {"gte": "≥", "lte": "≤"}
    parts: List[str] = []
    for target in targets:
        if not isinstance(target, dict):
            continue
        kind = str(target.get("type", ""))
        if kind not in units:
            continue
        operator = symbols.get(str(target.get("operator", "gte")), "≥")
        value = as_float(target.get("value"), 0.0)
        parts.append(f"{kind} {operator} {value:g}{units[kind]}")
    return " / ".join(parts)


def last_volumetric_target(phases: Sequence[Mapping[str, Any]]) -> str:
    result = ""
    for phase in phases:
        targets = phase.get("targets")
        if not isinstance(targets, list):
            continue
        for target in targets:
            if isinstance(target, dict) and target.get("type") == "volumetric":
                result = f"{as_float(target.get('value'), 0.0):g} g"
    return result


def has_phase_targets(phases: Sequence[Mapping[str, Any]]) -> bool:
    return any(isinstance(phase.get("targets"), list) and phase.get("targets") for phase in phases)


def finite_values(*series: Sequence[float]) -> List[float]:
    return [value for values in series for value in values if math.isfinite(value)]


def subtitle_for(
    metadata: ProfileMetadata,
    phases: Sequence[Mapping[str, Any]],
    total: float,
) -> str:
    parts: List[str] = []
    if metadata.coffee:
        parts.append(metadata.coffee)
    if metadata.dose:
        parts.append(f"{metadata.dose} in")
    if metadata.target_yield:
        parts.append(f"target {metadata.target_yield}")
    else:
        auto_stop = last_volumetric_target(phases)
        if auto_stop:
            parts.append(f"weight stop {auto_stop}")
    if metadata.grind:
        parts.append(f"grind {metadata.grind}")
    parts.append(f"{'max' if has_phase_targets(phases) else 'total'} {total:g} s")
    return " · ".join(parts)


def render(path: Path, dpi: int = 160) -> Path:
    data = read_json(path)
    phases_raw = data.get("phases")
    if not isinstance(phases_raw, list) or not phases_raw:
        raise ValueError(f"profile has no phases: {path}")
    phases: List[Mapping[str, Any]] = [phase for phase in phases_raw if isinstance(phase, dict)]
    if not phases:
        raise ValueError(f"profile has no valid phase objects: {path}")

    label = str(data.get("label") or path.stem)
    profile_temperature = as_float(data.get("temperature"), 0.0)
    metadata = load_metadata(path)
    total = sum(max(0.0, as_float(phase.get("duration"), 0.0)) for phase in phases)

    pressure_x, pressure_y, pressure_holds, pressure_adaptive = build_setpoint_series(phases, "pressure")
    flow_x, flow_y, flow_holds, flow_adaptive = build_setpoint_series(phases, "flow")
    pressure_limit_x, pressure_limit_y, pressure_limit_holds = build_limit_series(phases, "pressure")
    flow_limit_x, flow_limit_y, flow_limit_holds = build_limit_series(phases, "flow")
    temperature_x, temperature_y = build_temperature_series(phases, profile_temperature)

    fig, ax = plt.subplots(figsize=(12, 6.5))
    colors = plt.rcParams["axes.prop_cycle"].by_key().get("color", ["C0", "C1", "C2"])
    pressure_color = colors[0]
    flow_color = colors[1] if len(colors) > 1 else colors[0]
    temperature_color = colors[0]

    # Phase background bands and labels use maximum durations from the profile.
    t = 0.0
    for index, phase in enumerate(phases, start=1):
        duration = max(0.0, as_float(phase.get("duration"), 0.0))
        if index % 2 == 0:
            ax.axvspan(t, t + duration, alpha=0.07)
        ax.axvline(t, linewidth=0.6, alpha=0.5)

        target_text = phase_target_text(phase)
        label_text = f"{index}. {phase.get('name', '')}"
        if target_text:
            label_text += f"\n{target_text}"
        ax.text(
            t + duration / 2,
            0.98,
            label_text,
            rotation=90,
            transform=ax.get_xaxis_transform(),
            va="top",
            ha="center",
            fontsize=7.6,
        )
        t += duration
    ax.axvline(total, linewidth=0.6, alpha=0.5)

    if finite_values(pressure_y):
        ax.plot(pressure_x, pressure_y, linewidth=2.2, color=pressure_color, label="Pressure setpoint / bar")
    if finite_values(pressure_limit_y):
        ax.plot(
            pressure_limit_x,
            pressure_limit_y,
            linewidth=1.5,
            linestyle=":",
            color=pressure_color,
            alpha=0.8,
            label="Pressure soft limit / bar",
        )
    if finite_values(flow_y):
        ax.plot(flow_x, flow_y, linewidth=2.2, color=flow_color, label="Flow setpoint / ml/s")
    if finite_values(flow_limit_y):
        ax.plot(
            flow_limit_x,
            flow_limit_y,
            linewidth=1.5,
            linestyle=":",
            color=flow_color,
            alpha=0.8,
            label="Flow soft limit / ml/s",
        )

    ax.set_xlabel("Time / s")
    ax.set_ylabel("Pressure / bar and flow / ml/s")
    ax.set_xlim(0, max(total, 1.0))
    left_values = finite_values(pressure_y, pressure_limit_y, flow_y, flow_limit_y)
    ymax = max([10.0, *left_values])
    ax.set_ylim(0, ymax + 1.0)
    ax.grid(True, linewidth=0.4, alpha=0.4)

    ax2 = ax.twinx()
    ax2.plot(
        temperature_x,
        temperature_y,
        linestyle="--",
        linewidth=1.8,
        color=temperature_color,
        label="Temperature / °C",
    )
    temperatures = finite_values(temperature_y)
    if temperatures:
        low = min(temperatures)
        high = max(temperatures)
        padding = 1.0 if math.isclose(low, high) else max(0.75, (high - low) * 0.2)
        ax2.set_ylim(low - padding, high + padding)
    ax2.set_ylabel("Temperature / °C")

    # Dynamic -1 sentinels are intentionally not plotted as a numeric value.
    hold_annotations = pressure_holds + flow_holds + pressure_limit_holds + flow_limit_holds
    for hold in hold_annotations:
        ax.text(
            hold.x,
            0.06,
            f"{hold.variable.upper()} HOLD",
            transform=ax.get_xaxis_transform(),
            ha="center",
            va="bottom",
            fontsize=7.2,
            fontweight="bold",
        )

    fig.suptitle(label, fontsize=14, fontweight="bold")
    ax.set_title(subtitle_for(metadata, phases, total), fontsize=10)

    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines + lines2, labels + labels2, loc="lower right", fontsize=8.6)

    notes: List[str] = []
    if has_phase_targets(phases):
        notes.append("Phase widths are maximum durations; a target can end a phase earlier.")
    if pressure_adaptive or flow_adaptive:
        notes.append("Adaptive ramp starts are schematic because runtime starts from the measured entry value.")
    if hold_annotations:
        notes.append("HOLD marks a -1 sentinel; its exact runtime value is not knowable from JSON alone.")
    if notes:
        fig.text(
            0.5,
            0.008,
            "\n".join(notes),
            ha="center",
            va="bottom",
            fontsize=7.2,
            linespacing=1.25,
        )

    out = path.with_name(path.stem + "-profile.png")
    bottom_margin = min(0.12, 0.025 + 0.022 * len(notes)) if notes else 0.02
    fig.tight_layout(rect=[0, bottom_margin, 1, 0.92])
    fig.savefig(out, dpi=dpi)
    plt.close(fig)
    return out


def display_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def main(argv: Sequence[str] | None = None) -> int:
    options = parse_args(sys.argv[1:] if argv is None else argv)
    root = options.root.resolve()
    profiles = find_profiles(root, options.profiles)
    if not profiles:
        print(f"no profile JSON files found under {root / 'profiles'}", file=sys.stderr)
        return 1

    outputs: List[Path] = []
    for profile in profiles:
        if not profile.exists():
            print(f"missing: {profile}", file=sys.stderr)
            return 1
        try:
            outputs.append(render(profile, dpi=options.dpi))
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1

    for output in outputs:
        print(display_path(output, root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
