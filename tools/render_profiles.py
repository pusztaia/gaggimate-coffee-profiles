#!/usr/bin/env python3
"""Render GaggiMate JSON profiles to PNG charts.

Usage:
  python tools/render_profiles.py
  python tools/render_profiles.py profiles/wangera/wangera-stable-38s-945c.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def find_profiles(args: List[str]) -> List[Path]:
    if args:
        return [Path(a).resolve() if Path(a).is_absolute() else (ROOT / a).resolve() for a in args]
    return sorted(ROOT.glob("profiles/**/*.json"))


def phase_value(phase: Dict[str, Any]) -> Tuple[float | None, float | None]:
    pump = phase.get("pump", {}) or {}
    target = pump.get("target")
    if target == "pressure":
        return float(pump.get("pressure", 0)), pump.get("flow")
    if target == "flow":
        return pump.get("pressure"), float(pump.get("flow", 0))
    return pump.get("pressure"), pump.get("flow")


def build_steps(phases: List[Dict[str, Any]], key: str) -> Tuple[List[float], List[float]]:
    xs: List[float] = [0]
    ys: List[float] = []
    t = 0.0
    last = 0.0
    for ph in phases:
        dur = float(ph.get("duration", 0))
        pump = ph.get("pump", {}) or {}
        if key == "pressure":
            val = float(pump.get("pressure", 0) or 0)
        elif key == "flow":
            val = float(pump.get("flow", 0) or 0)
        elif key == "temperature":
            val = float(ph.get("temperature", 0) or 0)
        else:
            val = 0.0
        ys.extend([last, val, val]) if not ys else ys.extend([val, val])
        if len(xs) == 1:
            xs.extend([t, t + dur])
        else:
            xs.extend([t, t + dur])
        last = val
        t += dur
    if len(ys) > len(xs):
        ys = ys[-len(xs):]
    if len(ys) < len(xs):
        ys = [0.0] + ys
    return xs, ys


def render(path: Path) -> Path:
    data = json.loads(path.read_text(encoding="utf-8"))
    phases = data.get("phases", [])
    label = data.get("label", path.stem)
    recipe = data.get("recipe", {})
    coffee = recipe.get("coffee", "")
    dose = recipe.get("dose_g", "")
    target_yield = recipe.get("target_yield_g", {})
    ideal_yield = target_yield.get("ideal", "") if isinstance(target_yield, dict) else ""
    grind = recipe.get("grind", {})
    grind_start = grind.get("start", "") if isinstance(grind, dict) else ""
    total = sum(float(p.get("duration", 0)) for p in phases)

    fig, ax = plt.subplots(figsize=(12, 6.5))

    # Phase background bands and labels
    t = 0.0
    for i, ph in enumerate(phases, start=1):
        dur = float(ph.get("duration", 0))
        if i % 2 == 0:
            ax.axvspan(t, t + dur, alpha=0.07)
        ax.axvline(t, linewidth=0.6, alpha=0.5)
        ax.text(t + dur / 2, 0.98, f"{i}. {ph.get('name','')}", rotation=90,
                transform=ax.get_xaxis_transform(), va="top", ha="center", fontsize=8)
        t += dur
    ax.axvline(total, linewidth=0.6, alpha=0.5)

    x_p, y_p = build_steps(phases, "pressure")
    x_f, y_f = build_steps(phases, "flow")
    x_t, y_t = build_steps(phases, "temperature")

    ax.step(x_p, y_p, where="post", linewidth=2.2, label="Pressure target / bar")
    ax.step(x_f, y_f, where="post", linewidth=2.2, label="Flow target / ml/s")
    ax.set_xlabel("Time / s")
    ax.set_ylabel("Pressure / bar and flow / ml/s")
    ax.set_xlim(0, max(total, 1))
    ymax = max([0] + y_p + y_f + [10])
    ax.set_ylim(0, ymax + 1)
    ax.grid(True, linewidth=0.4, alpha=0.4)

    ax2 = ax.twinx()
    ax2.step(x_t, y_t, where="post", linestyle="--", linewidth=1.8, label="Temperature / °C")
    temps = [v for v in y_t if v]
    if temps:
        ax2.set_ylim(min(temps) - 1.0, max(temps) + 1.0)
    ax2.set_ylabel("Temperature / °C")

    title = label
    subtitle = f"{coffee} · {dose} g in · target {ideal_yield} g · grind {grind_start} · total {total:g} s"
    fig.suptitle(title, fontsize=14, fontweight="bold")
    ax.set_title(subtitle, fontsize=10)

    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines + lines2, labels + labels2, loc="lower right", fontsize=9)

    out = path.with_name(path.stem + "-profile.png")
    fig.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(out, dpi=160)
    plt.close(fig)
    return out


def main() -> int:
    outputs = []
    for profile in find_profiles(sys.argv[1:]):
        if not profile.exists():
            print(f"missing: {profile}", file=sys.stderr)
            return 1
        outputs.append(render(profile))
    for out in outputs:
        print(out.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
