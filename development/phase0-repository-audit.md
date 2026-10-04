# Phase 0 – Repository audit (2026-10-04)

Audit performed per `dev/gaggimate-web-development-prompts.md` Phase 0 prompt, ahead of
implementing the `Coffee → Recipe → Profile → Brew → Taste → Adjust` roadmap.

## 1. Repository structure

- `profiles/{slug}/` × 14 coffee folders. Each contains the GaggiMate JSON(s), an
  auto-generated `-profile.png`, `{slug}-recipe.md`, `{slug}-changelog.md` — **and a
  standalone `{slug}.html` detail page** (e.g. `kirinyaga.html`, 1119 lines). Across all
  14 coffees these detail pages total **~10,900 lines**.
- `profiles/catalog.json` — the single source `index.html` fetches to build every card,
  variant selector, mini chart and phase list (per `MODULAR_INDEX_README.md`).
- `index.html` (620 lines) — single inline `<script>`, no `js/`/`css/` directory yet.
- `index_old.html` (1390 lines) — superseded version; nothing links to it.
- `development/gaggimate-index-redesign-developer-spec.md` — an **existing, partially
  implemented** redesign spec for `index.html` (dated 2026-08-09). Its "not yet
  implemented" list overlaps directly with Phase 1–4/14 of
  `dev/gaggimate-web-development-prompts.md` (segmented Scale/Manual control, CTA
  hierarchy, lazy-rendered chart, `catalog.json` schema extension, URL state, dedicated
  profile routes, JS module split, accessibility/Lighthouse pass). Future phase work
  must reconcile with this document instead of re-deriving the same plan.
- `gaggimate-1.8.1/` and `gaggimate-1.9.0/` — full firmware source checkouts, used as the
  reference for `schema/profile.json`.
- `knowledge/`, `equipment/`, `info/`, `websocket/` — documentation directories that
  exist but are **not** listed in `CLAUDE.md`'s repository-structure section (mildly
  stale documentation).

## 2. Current data flow

- Coffee name/origin/notes/accent color → `profiles/catalog.json` (curated fields +
  `tools/build_catalog.py` derivation from each folder, optionally overridden via
  `catalog.meta.json`).
- Recipe/changelog text → Markdown files, fetched client-side into a modal by
  `index.html`.
- Profile chart exists **twice**: (a) the static PNG from
  `tools/render_gaggimate_profiles.py`, and (b) a dynamic inline SVG mini-chart that
  `index.html` already renders per card directly from the profile JSON
  (`renderMiniChart()`), independently of the PNG.
- The 14 per-coffee `{slug}.html` pages are **self-contained**: own `<style>` block,
  own recipe/chart rendering, not driven by `catalog.json` or any shared JS.

## 3. Duplication (ranked)

1. **Critical** — the 14 `{slug}.html` files are ~95% identical CSS/HTML scaffolding
   (`:root` color tokens, `.nav`, `.icon-button`, etc.), hand-copied per coffee with
   only title/colors/content swapped. Any UI fix needs to be applied in up to 14 places.
   This is the single largest piece of technical debt in the repo.
2. Recipe metadata duplicated between `catalog.json` fields (title/subtitle/notes/
   grind/dose/yield) and the `{slug}-recipe.md` table.
3. `index_old.html` is dead weight — unreferenced anywhere.
4. `equipment/setup.md` is linked from `README.md`, `SUMMARY.md`, `CHANGELOG.md`, but
   **not from `index.html`** — a real, fixable documentation-surfacing gap.
5. `CLAUDE.md`'s repository-structure section omits `development/`, `equipment/`,
   `info/`, `knowledge/`, `websocket/`, `gaggimate-1.8.x/`.

## 4. Target architecture

Keep the existing `catalog.json`-driven model — extend it, and stop hand-authoring the
14 per-coffee HTML pages:

```
profiles/
  {slug}/
    {slug}-manual.json / -scale.json   (unchanged — firmware source of truth)
    {slug}-profile.png                 (unchanged)
    {slug}-recipe.md / -changelog.md   (unchanged)
    catalog.meta.json                  (already exists, extensible)
  catalog.json                         (extended schema, see §5)
assets/
  css/site.css          <- extracted from index.html + the 14 {slug}.html common styles
  js/catalog.js          <- fetch+render logic, extracted from the inline <script>
  js/profile-parser.js   <- single place for JSON→chart/phase logic (reused by compare/
                             version-history phases later)
index.html               (homepage — unchanged entry point)
profiles/{slug}/index.html   (generated from a template, not hand-edited)
```

Key decision: the 14 hand-written `{slug}.html` files should become **generated**
output (e.g. a `tools/build_profile_pages.py` driven by `catalog.json` + a template),
matching Phase 3 of the roadmap.

## 5. Proposed extended coffee metadata fields

`catalog.json` entries already cover most of the Phase 0 prompt's proposed schema.
Missing fields (add only where real data exists, don't pad every entry):

```json
{
  "roaster": "",
  "region": "",
  "producer": "",
  "variety": [],
  "roast": "",
  "status": "dialed-in|experimental|archived"
}
```

## 6. Migration plan

1. No breaking changes: `index.html`, `catalog.json`, and JSON downloads stay stable
   throughout.
2. Extract shared CSS/JS into `assets/`; convert **one** coffee (`kirinyaga`) to the
   templated detail page as a pilot, with a visual diff check.
3. Convert the remaining 13 pages once the pilot is validated; delete the hand-written
   HTML once superseded.
4. Delete `index_old.html` (unreferenced).
5. Update `CLAUDE.md`'s repository-structure section to list the currently-undocumented
   top-level directories.

## 7. Files touched by Phase 1

- `index.html` — add the missing `equipment/setup.md` documentation entry (confirmed
  gap, see §3.4); begin CSS/JS extraction is deferred to a dedicated refactor step to
  keep Phase 1 changes small and reviewable.
- `profiles/catalog.json` — no changes required yet (existing fields already satisfy
  Phase 1's card requirements).
- `CLAUDE.md` — repository-structure section update (separate, non-UI change).
