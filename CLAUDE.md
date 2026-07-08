# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not** a software application — it's a documentation/data repository of espresso brew profiles for a **GaggiMate Pro** controller (Gaggia Classic Pro 2025 + DF64V Gen 2 grinder + BOOKOO Themis Ultra Bluetooth scale). The "code" is JSON profile files consumed by GaggiMate firmware, a Python chart-rendering script, and a static HTML gallery viewer. Most prose in the repo is in Hungarian.

## Commands

Regenerate profile charts from JSON (requires `matplotlib`):

```bash
python3 tools/render_profiles.py                                   # all profiles under profiles/**/*.json
python3 tools/render_profiles.py profiles/wangera/wangera-stable-38s-945c.json  # single profile
```

Output is always written next to the source JSON as `{json-stem}-profile.png` (overwrites existing).

Quick JSON syntax check on a new profile:

```bash
python3 -c "import json; json.load(open('profiles/<coffee>/<file>.json'))" && echo OK
```

Full structural validation against the schema's allowed keys (root + phase level) across every profile — see `PROFILE_CREATION_GUIDE.md` for the full script; run it after adding/editing any profile JSON to catch stray/typo'd keys, since the firmware rejects unknown root fields (`additionalProperties: false`).

View the gallery (`index.html`) locally — it `fetch()`es recipe/changelog `.md` files client-side, so it must be served over HTTP, not opened via `file://`:

```bash
python3 -m http.server 8000   # then open http://localhost:8000/
```

There is no build step, package manager, linter, or test suite in this repo (the `.kilo/` directory is an unrelated local agent-tool cache, not part of the project).

## Repository structure

- `profiles/{coffee-slug}/` — one directory per coffee. Each contains the GaggiMate JSON profile(s), a matching auto-generated `-profile.png` chart, a human-readable `{dir}-recipe.md`, and a `{dir}-changelog.md`.
- `profile.json` (repo root) — **this is the JSON Schema for the profile format**, not a sample profile. It's the canonical documentation of every field GaggiMate firmware accepts, cross-referenced to firmware source lines (`src/display/models/profile.h`, `src/display/core/process/BrewProcess.h`, etc.). When in doubt about what a field does or what values are valid, read the `description` text in this file rather than inferring from an example profile — per its own `$comment`, if the schema and the real firmware parser ever disagree, the parser wins.
- `tools/render_profiles.py` — renders each JSON profile's pressure/flow/temperature-over-time into the accompanying PNG chart.
- `index.html` — single-file static gallery: hardcoded cards linking to each profile's JSON/PNG, plus a tab section that `fetch()`s each coffee's recipe/changelog Markdown at runtime and renders it client-side (see the `file:` entries and the `fetch(entry.file, ...)` call near the end of the file). Adding a new profile means updating both the profile's own directory *and* the corresponding card/entry in `index.html`.
- `templates/` — starter Markdown templates (`recipe-template.md`, `changelog-template.md`, `shot-log-template.md`) for documenting a new coffee.
- `README.md`, `SUMMARY.md`, `PROFILE_GALLERY.md`, `FILE_NAMING.md`, `PROFILE_CREATION_GUIDE.md`, `BREW_GUIDELINES.md`, `BLUETOOTH_SCALE_WORKFLOW.md`, `CHANGELOG.md` — all human documentation; several are effectively views over the same profile data (index, gallery, naming rules, dial-in guidance, scale workflow) and must be kept in sync manually when profiles change.

## Profile format essentials (from `profile.json`)

A profile is `{ label, type, description, temperature, utility, phases[] }`. Root object has `additionalProperties: false` — do not add ad-hoc fields; use an underscore-prefixed key (e.g. `_notes`) if you need to stash metadata, since the schema reserves `^_` patterns as firmware-ignored. Never set `id` in hand-authored profiles — it's firmware/UI-managed and generated on import.

- **`type: "pro"`** (every real profile in this repo) — `duration` on each phase is always a **hard cap**; a `targets[]` stop condition can only end a phase *early*, never extend it past `duration`. (`type: "standard"` behaves oppositely — a volumetric target blocks the duration timeout — but this repo doesn't use standard profiles.)
- **Phases** run in order; each has `pump` (pressure- or flow-controlled, with the non-selected field acting as a soft limit — `0` means "no limit", `-1` means "hold whatever was measured at phase entry"), an optional `transition` (ramp easing from the previous setpoint), and optional `targets[]`.
- **`targets[]`** are OR-combined and evaluated every 100 ms; the first one to fire ends the phase. `operator` must be lowercase `"gte"` or `"lte"` — any other string (including `"gt"` or `"GTE"`) silently falls back to `lte` in the firmware parser, a common source of profiles that behave backwards. For `type: "volumetric"`, `value: 0` means "no target, run full duration."
- **V3 vs V4 naming convention** used throughout this repo (not a firmware concept): "V3" profiles are pure time-based (no `targets`, yield is only checked by weighing the cup separately). "V4" / `-scale-v4.json` profiles add a `volumetric` target (BOOKOO Themis Ultra beverage-weight stop) to the extraction phase, with a longer `duration` acting as a safety-timeout fallback if the Bluetooth scale disconnects or isn't in brew-by-weight mode.

## File naming convention (see `FILE_NAMING.md` for full detail)

```
profiles/{coffee-slug}/{coffee-slug}-{time}[{temp}].json        # V3 (e.g. burundi-mubuga-38s.json)
profiles/{coffee-slug}/{v3-json-stem}-scale-v4.json              # V4 (e.g. burundi-mubuga-38s-scale-v4.json)
profiles/{coffee-slug}/{json-stem}-profile.png                   # auto-generated chart
profiles/{coffee-slug}/{coffee-slug}-recipe.md
profiles/{coffee-slug}/{coffee-slug}-changelog.md
```

All names: lowercase, hyphen-separated, no accents/spaces/punctuation (except the file extension). `945c` in a filename means 94.5°C (decimal point dropped for filename safety). The old V3 profile is always kept alongside a new V4 version — never delete/replace it.

## Adding a new coffee profile

Follow the step-by-step process in `PROFILE_CREATION_GUIDE.md` (setup reference, JSON templates for V3 and V4, recipe/changelog content requirements). In short: pick the closest existing profile as a starting point based on processing method (washed/natural/honey/anaerobic — see the guide's mapping table), create the profile directory, JSON, recipe, and changelog following the naming convention above, regenerate the PNG with `render_profiles.py`, and add corresponding entries to `README.md` and `index.html`.
