# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not** a software application — it's a documentation/data repository of espresso brew profiles for a **GaggiMate Pro** controller (Gaggia Classic Pro 2025 + DF64V Gen 2 grinder + IMS B682TH24.5M basket + IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 holes, DS58.5) + BOOKOO Themis Ultra Bluetooth scale). The "code" is JSON profile files consumed by GaggiMate firmware, a Python chart-rendering script, and a static HTML gallery viewer. Most prose in the repo is in Hungarian.

## Commands

Regenerate profile charts from JSON (requires `matplotlib`):

```bash
python3 tools/render_gaggimate_profiles.py                                   # all profiles under profiles/**/*.json
python3 tools/render_gaggimate_profiles.py profiles/wangera/wangera-manual-v2.json  # single profile
```

Output is always written next to the source JSON as `{json-stem}-profile.png` (overwrites existing).

Regenerate `profiles/catalog.json` (the data file `index.html` fetches — this is what makes the gallery reflect new/changed profile folders automatically, no `index.html` edits needed):

```bash
python3 tools/build_catalog.py            # scan profiles/*, write profiles/catalog.json
python3 tools/build_catalog.py --check    # exit 1 if catalog.json is stale, without writing
python3 tools/build_catalog.py --dry-run  # print the generated catalog instead of writing
```

It derives variants (manual/scale/general JSON files, PNG, recipe, changelog) straight from each `profiles/{coffee-slug}/` folder's contents, and preserves curated fields (title, subtitle, notes, accent colors, featured, variant labels) from the existing `catalog.json`, optionally overridden per-folder via `profiles/{coffee-slug}/catalog.meta.json` (see the script's module docstring for the schema).

This runs automatically on commit via a git pre-commit hook (not tracked by git itself — reinstall after a fresh clone with `cp tools/git-hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit`), which regenerates and re-stages `catalog.json` whenever it's out of sync. Run `build_catalog.py` manually only to preview the result before committing.

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

- `profiles/{coffee-slug}/` — one directory per coffee. Each contains the GaggiMate JSON profile(s), a matching auto-generated `-profile.png` chart, a human-readable `{dir}-recipe.md`, and a `{dir}-changelog.md`. Even when a coffee has both a V1 and a V2 profile, there is still only **one** `{dir}-recipe.md` and **one** `{dir}-changelog.md` per coffee — V2-specific content goes in a `## V2 – Bluetooth Scale Edition` section within the same file, not a separate file. A coffee doesn't strictly need a V1 profile (e.g. a coffee can ship with only a `-scale.json`), but if a V1 baseline already exists it is never deleted when a V2 version is added.
- `schema/profile.json` — **this is the JSON Schema for the profile format**, not a sample profile. It's the canonical documentation of every field GaggiMate firmware accepts, cross-referenced to firmware source lines (`src/display/models/profile.h`, `src/display/core/process/BrewProcess.h`, etc.). When in doubt about what a field does or what values are valid, read the `description` text in this file rather than inferring from an example profile — per its own `$comment`, if the schema and the real firmware parser ever disagree, the parser wins.
- `tools/render_gaggimate_profiles.py` — renders each JSON profile's pressure/flow/temperature-over-time into the accompanying PNG chart.
- `tools/build_catalog.py` — regenerates `profiles/catalog.json` from the `profiles/*` directory tree; this is what `index.html` actually renders (see below).
- `index.html` — single-file static gallery. It has **no hardcoded profile cards** — at load time it `fetch()`es `profiles/catalog.json` and builds every card, variant selector, mini chart, and phase list from that plus the referenced GaggiMate JSON files, and `fetch()`es each coffee's recipe/changelog Markdown on demand for the modal viewer. Adding a new profile means only adding files under `profiles/{coffee-slug}/` — `catalog.json` (and therefore `index.html`) updates itself via `tools/build_catalog.py` (see Commands), which runs automatically on commit through the pre-commit hook.
- `templates/` — starter Markdown templates (`recipe-template.md`, `changelog-template.md`, `shot-log-template.md`) for documenting a new coffee.
- `README.md`, `SUMMARY.md`, `PROFILE_GALLERY.md`, `FILE_NAMING.md`, `PROFILE_CREATION_GUIDE.md`, `BREW_GUIDELINES.md`, `BLUETOOTH_SCALE_WORKFLOW.md`, `CHANGELOG.md` — all human documentation; several are effectively views over the same profile data (index, gallery, naming rules, dial-in guidance, scale workflow) and must be kept in sync manually when profiles change.

## Profile format essentials (from `schema/profile.json`)

A profile is `{ label, type, description, temperature, utility, phases[] }`. Root object has `additionalProperties: false` — do not add ad-hoc fields; use an underscore-prefixed key (e.g. `_notes`) if you need to stash metadata, since the schema reserves `^_` patterns as firmware-ignored. Never set `id` in hand-authored profiles — it's firmware/UI-managed and generated on import.

- **`type: "pro"`** (every real profile in this repo) — `duration` on each phase is always a **hard cap**; a `targets[]` stop condition can only end a phase *early*, never extend it past `duration`. (`type: "standard"` behaves oppositely — a volumetric target blocks the duration timeout — but this repo doesn't use standard profiles.)
- **Phases** run in order; each has `pump` (pressure- or flow-controlled, with the non-selected field acting as a soft limit — `0` means "no limit", `-1` means "hold whatever was measured at phase entry"), an optional `transition` (ramp easing from the previous setpoint), and optional `targets[]`.
- **`targets[]`** are OR-combined and evaluated every 100 ms; the first one to fire ends the phase. `operator` must be lowercase `"gte"` or `"lte"` — any other string (including `"gt"` or `"GTE"`) silently falls back to `lte` in the firmware parser, a common source of profiles that behave backwards. For `type: "volumetric"`, `value: 0` means "no target, run full duration."
- **V1 vs V2 naming convention** used throughout this repo (not a firmware concept): "V1" profiles are pure time-based (no `targets`, yield is only checked by weighing the cup separately). "V2" / `-scale.json` profiles add a `volumetric` target (BOOKOO Themis Ultra beverage-weight stop) to the extraction phase, with a longer `duration` acting as a safety-timeout fallback if the Bluetooth scale disconnects or isn't in brew-by-weight mode.

## File naming convention (see `FILE_NAMING.md` for full detail)

```
profiles/{coffee-slug}/{coffee-slug}-manual.json   # V1, time-based (e.g. kirinyaga-manual.json)
profiles/{coffee-slug}/{coffee-slug}-scale.json    # V2, BOOKOO scale-based (e.g. kirinyaga-scale.json)
profiles/{coffee-slug}/{json-stem}-profile.png     # auto-generated chart
profiles/{coffee-slug}/{coffee-slug}-recipe.md
profiles/{coffee-slug}/{coffee-slug}-changelog.md
```

`profiles/kirinyaga/` is the reference example: exactly one `-manual.json` and one `-scale.json`. If a coffee has multiple variants of the same type (e.g. two temperature options), append `-v1`, `-v2`, ... to both the manual and scale filenames, keeping the same number for the same variant (see `profiles/wangera/`: `wangera-manual-v1.json`/`wangera-scale-v1.json` are the 94.0°C pair, `-v2` is the 94.5°C pair). A coffee doesn't need both types — e.g. `honduras-las-calaveras-scale.json` has no manual counterpart.

All names: lowercase, hyphen-separated, no accents/spaces/punctuation (except the file extension). An existing manual profile is never deleted when a scale version is added — the one documented exception is `kirinyaga/`, where an old separately-kept baseline pair was explicitly removed at the user's request.

## Recipe.md content conventions

- The header metadata block (Kávé, Feldolgozás, Ízjegyek, Setup, etc.) must be a markdown table (`| Mező | Érték |`), not a run of `**Label:** value` lines. `index.html`'s hand-rolled `renderMarkdown()`/`inlineMarkdown()` joins consecutive non-blank lines into a single paragraph with a plain space (no `<br>` support, trailing double-space line breaks are ignored) — a table is the only block type it renders row-by-row.
- Don't embed the profile chart image (`![...](...-profile.png)`) anywhere in a recipe.md body. The chart is already shown on the coffee's card in `index.html`; an embedded copy just duplicates it (often broken, since the image path is relative to the modal's fetch location, not the recipe's own directory) when the recipe is opened in the "Recept" modal.

## Adding a new coffee profile

Follow the step-by-step process in `PROFILE_CREATION_GUIDE.md` (setup reference, JSON templates for V1 and V2, recipe/changelog content requirements). In short: pick the closest existing profile as a starting point based on processing method (washed/natural/honey/anaerobic — see the guide's mapping table), create the profile directory, JSON, recipe, and changelog following the naming convention above, regenerate the PNG with `render_gaggimate_profiles.py`, and add a corresponding entry to `README.md`. `index.html`/`catalog.json` need no manual edit — the pre-commit hook (or a manual `tools/build_catalog.py` run) picks up the new folder automatically; use a `catalog.meta.json` in the new folder if you need to curate title/notes/accent/featured beyond what's inferred from the recipe.
