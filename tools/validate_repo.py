#!/usr/bin/env python3
"""Release-hardening validator for the GaggiMate Coffee Profiles site.

Runs the checks described in the Phase 15 ("release hardening") step of
dev/gaggimate-web-development-prompts.md:

- every profiles/**/*.json GaggiMate profile only uses keys the firmware
  schema (schema/profile.json) actually defines, derived at runtime so this
  never drifts out of sync with the schema itself
- every profile has non-empty label/type/phases (mirrors the stricter
  parseProfile() validation added in firmware v1.9.0)
- profiles/catalog.json passes tools/build_catalog.py --check (duplicate
  ids, duplicate variant ids, exactly one default variant, variant files
  exist) and additionally: every variant's PNG/recipe.md/changelog.md
  resolves (hard failure here, not just a warning)
- every file referenced from the static site shell actually exists on disk:
  index.html's DOCS/KNOWLEDGE arrays, each top-level page's <script src="...">
  tags, manifest.json icons, sw.js's SHELL_ASSETS precache list

Exit code is non-zero if any check fails, so this is safe to wire into a
pre-commit hook or a GitHub Actions job (see .github/workflows/validate.yml).

Usage:
    python3 tools/validate_repo.py
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILES_ROOT = ROOT / "profiles"
SCHEMA_PATH = ROOT / "schema" / "profile.json"


def load_schema_key_sets() -> dict[str, set[str]]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    definitions = schema.get("definitions", {})
    return {
        "root": set(schema.get("properties", {}).keys()),
        "phase": set(definitions.get("phase", {}).get("properties", {}).keys()),
        "pump": set(definitions.get("pumpAdvanced", {}).get("properties", {}).keys()),
        "transition": set(definitions.get("transition", {}).get("properties", {}).keys()),
        "target": set(definitions.get("target", {}).get("properties", {}).keys()),
    }


def check_profile_json_files(issues: list[str]) -> None:
    keys = load_schema_key_sets()
    skip_names = {"catalog.json", "catalog.meta.json"}
    for path in sorted(PROFILES_ROOT.glob("**/*.json")):
        if path.name in skip_names:
            continue
        rel = path.relative_to(ROOT)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append(f"{rel}: invalid JSON ({exc})")
            continue
        if not isinstance(data, dict):
            issues.append(f"{rel}: root must be a JSON object")
            continue

        extra_root = {k for k in data if not k.startswith("_")} - keys["root"]
        if extra_root:
            issues.append(f"{rel}: unknown root keys: {sorted(extra_root)}")

        if not isinstance(data.get("label"), str) or not data["label"].strip():
            issues.append(f"{rel}: 'label' must be a non-empty string")
        if not isinstance(data.get("type"), str) or not data["type"].strip():
            issues.append(f"{rel}: 'type' must be a non-empty string")

        phases = data.get("phases")
        if not isinstance(phases, list) or not phases:
            issues.append(f"{rel}: 'phases' must be a non-empty array")
            continue

        for i, phase in enumerate(phases):
            if not isinstance(phase, dict):
                issues.append(f"{rel}: phase[{i}] is not an object")
                continue
            extra_phase = {k for k in phase if not k.startswith("_")} - keys["phase"]
            if extra_phase:
                issues.append(f"{rel}: phase[{i}] ({phase.get('name', '?')}): unknown keys: {sorted(extra_phase)}")
            pump = phase.get("pump")
            if isinstance(pump, dict):
                extra_pump = {k for k in pump if not k.startswith("_")} - keys["pump"]
                if extra_pump:
                    issues.append(f"{rel}: phase[{i}] pump: unknown keys: {sorted(extra_pump)}")
            transition = phase.get("transition")
            if isinstance(transition, dict):
                extra_tr = {k for k in transition if not k.startswith("_")} - keys["transition"]
                if extra_tr:
                    issues.append(f"{rel}: phase[{i}] transition: unknown keys: {sorted(extra_tr)}")
            for j, target in enumerate(phase.get("targets") or []):
                if not isinstance(target, dict):
                    issues.append(f"{rel}: phase[{i}] targets[{j}] is not an object")
                    continue
                extra_tgt = {k for k in target if not k.startswith("_")} - keys["target"]
                if extra_tgt:
                    issues.append(f"{rel}: phase[{i}] targets[{j}]: unknown keys: {sorted(extra_tgt)}")
                operator = target.get("operator")
                if operator is not None and operator not in ("gte", "lte"):
                    issues.append(
                        f"{rel}: phase[{i}] targets[{j}]: operator {operator!r} is not 'gte'/'lte' — "
                        "firmware silently falls back to 'lte' for anything else"
                    )


def run_build_catalog_check(issues: list[str]) -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "build_catalog.py"), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        issues.append("tools/build_catalog.py --check failed:\n" + (result.stdout + result.stderr).strip())


def check_catalog_companions(issues: list[str]) -> None:
    catalog_path = PROFILES_ROOT / "catalog.json"
    if not catalog_path.is_file():
        issues.append("profiles/catalog.json is missing")
        return
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    seen_ids: set[str] = set()
    for entry in catalog.get("profiles", []):
        entry_id = entry.get("id")
        folder = PROFILES_ROOT / str(entry.get("folder", ""))
        if entry_id in seen_ids:
            issues.append(f"catalog.json: duplicate coffee id '{entry_id}'")
        seen_ids.add(entry_id)

        variants = entry.get("variants", [])
        variant_ids: set[str] = set()
        defaults = 0
        for variant in variants:
            vid = variant.get("id")
            if vid in variant_ids:
                issues.append(f"catalog.json [{entry_id}]: duplicate variant id '{vid}'")
            variant_ids.add(vid)
            if variant.get("default"):
                defaults += 1

            json_file = folder / str(variant.get("file", ""))
            if not json_file.is_file():
                issues.append(f"catalog.json [{entry_id}/{vid}]: missing profile JSON {json_file.relative_to(ROOT)}")
                continue
            png_file = json_file.with_name(json_file.stem + "-profile.png")
            if not png_file.is_file():
                issues.append(f"catalog.json [{entry_id}/{vid}]: missing chart PNG {png_file.relative_to(ROOT)}")

        if defaults != 1:
            issues.append(f"catalog.json [{entry_id}]: expected exactly one default/current variant, found {defaults}")

        recipe = folder / f"{entry.get('folder')}-recipe.md"
        changelog = folder / f"{entry.get('folder')}-changelog.md"
        if not recipe.is_file():
            issues.append(f"catalog.json [{entry_id}]: missing recipe {recipe.relative_to(ROOT)}")
        if not changelog.is_file():
            issues.append(f"catalog.json [{entry_id}]: missing changelog {changelog.relative_to(ROOT)}")

        for numeric_field in ("dose",):
            value = entry.get(numeric_field)
            if value is not None and (not isinstance(value, (int, float)) or value <= 0):
                issues.append(f"catalog.json [{entry_id}]: '{numeric_field}' must be a positive number, got {value!r}")


def extract_quoted_paths(text: str, *keys: str) -> list[str]:
    # Negative lookbehind for a quote character excludes false matches like
    # `location.protocol==="file:"` (a string literal, not a `file: "..."` key).
    pattern = r'(?<!")\b(?:' + "|".join(re.escape(k) for k in keys) + r')\s*:\s*"([^"]+)"'
    return re.findall(pattern, text)


def check_referenced_files(issues: list[str]) -> None:
    index_html = (ROOT / "index.html").read_text(encoding="utf-8")
    for rel_path in extract_quoted_paths(index_html, "file"):
        if rel_path.startswith(("http:", "https:", "#")):
            continue
        if not (ROOT / rel_path).is_file():
            issues.append(f"index.html: referenced doc/knowledge file not found: {rel_path}")

    for html_name in ("index.html", "profile.html", "brew.html", "compare.html", "finder.html"):
        html_path = ROOT / html_name
        if not html_path.is_file():
            continue
        html = html_path.read_text(encoding="utf-8")
        for src in re.findall(r'<script[^>]+src="([^"]+)"', html):
            if src.startswith(("http:", "https:")):
                continue
            if not (ROOT / src).is_file():
                issues.append(f"{html_name}: <script src> not found: {src}")
        for href in re.findall(r'rel="(?:manifest|apple-touch-icon|icon)"[^>]*href="([^"]+)"', html):
            if not (ROOT / href).is_file():
                issues.append(f"{html_name}: linked asset not found: {href}")

    manifest_path = ROOT / "manifest.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for icon in manifest.get("icons", []):
            src = icon.get("src", "")
            if not (ROOT / src).is_file():
                issues.append(f"manifest.json: icon not found: {src}")

    sw_path = ROOT / "sw.js"
    if sw_path.is_file():
        sw = sw_path.read_text(encoding="utf-8")
        match = re.search(r"SHELL_ASSETS\s*=\s*\[(.*?)\]", sw, re.S)
        if match:
            for rel_path in re.findall(r'"([^"]+)"', match.group(1)):
                if rel_path in ("./",):
                    continue
                if not (ROOT / rel_path).is_file():
                    issues.append(f"sw.js: SHELL_ASSETS entry not found: {rel_path}")


def main() -> int:
    issues: list[str] = []
    check_profile_json_files(issues)
    run_build_catalog_check(issues)
    check_catalog_companions(issues)
    check_referenced_files(issues)

    if issues:
        print(f"FAILED — {len(issues)} issue(s) found:\n")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("OK — all release-hardening checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
