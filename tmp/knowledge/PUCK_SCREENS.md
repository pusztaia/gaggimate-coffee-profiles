# Puck Screens

Quick reference for puck screens (metal disc placed on top of the puck, between coffee bed and shower screen) and their effect on extraction.

> *For deep physics — heat-buffer numerics, hydraulic resistance data, temperature-compensation table — see [`reference/PUCK_SCREENS_REFERENCE.md`](reference/PUCK_SCREENS_REFERENCE.md).*

---

## Screen Classification

Two axes drive recommendations: **thickness** and **hole type**. Each downstream section labels its applicability with the canonical tokens below.

### Thickness axis

| Token | Range | Examples |
|-------|-------|----------|
| **thin (≤ 1mm)** | 0.2 mm to 1.0 mm | Normcore 0.8mm, IMS 0.5mm mesh |
| **thick (> 1mm)** | greater than 1.0 mm | BPlus 1.7mm, Pesado 1.7mm |

Thickness drives heat behavior. **thin (≤ 1mm)** screens carry little thermal mass and lose ≤ 1°C at the surface when preheated; **thick (> 1mm)** screens can pull 2–3°C from cold and call for boiler compensation.

### Hole-type axis

| Token | Description | Examples |
|-------|-------------|----------|
| **round-hole** | Discrete drilled holes (typically 7–19 holes, 0.18–0.4 mm) | Normcore round-hole, MHW-3BOMBER round-hole |
| **mesh** | Woven or laser-sintered fine mesh (~150–250 µm) | IMS mesh, Pesado mesh, Sworks mesh |

Hole type drives dispersion, oil retention, and cleaning cadence. **round-hole** is easier to clean and retains fewer oils but disperses water less evenly. **mesh** disperses best but retains more oils and demands more maintenance.

The Equipment table in `user-setup.md` records both axes (e.g. `Normcore 58.5mm round-hole, 0.8mm` → **thin round-hole**).

---

## When to Use

A puck screen is a passive distribution aid. It supplements puck prep; it does not replace it.

- **Channeling from the shower screen jets** (water arriving in concentrated streams onto the puck surface) — applies to **thin** and **thick**, **round-hole** and **mesh**. The screen evens out water arrival.
- **Surface erosion / "screen kiss"** — applies to all screens. The disc protects the top of the puck from imprint and abrasion.
- **Light roasts** — community-reported benefit: dense, slow-wetting light-roast pucks may show more uniform initial saturation with a screen. This claim is **anecdotal** and **not controlled** — no controlled A/B testing has been located, so the effect size is unverified. Do not treat this as a reason to change starting grind, temp, or ratio in `/new-coffee`; treat it as a tiebreaker only.
- **Already-excellent shower screens** — diminishing returns. Modern Gaggimate-equipped machines have good distribution; the marginal benefit from adding a screen is small.

---

## Effects on Extraction

### Channeling reduction

Applies to **thin** and **thick**, **round-hole** and **mesh**. Puck screens reduce **shower-screen-driven** channeling by spreading concentrated water jets across the puck surface. They do **NOT** reduce **puck-prep-driven** channeling (clumps, uneven distribution, tilted tamp). For puck-prep-driven channeling, fix puck prep — see `EXTRACTION_SCIENCE.md`.

### Heat behavior

A puck screen is metal and acts as a heat buffer. **thin (≤ 1mm)** screens lose negligible heat when preheated (locked into the portafilter during the flush). **thick (> 1mm)** screens carry more thermal mass and may warrant boiler-temperature compensation. For numeric compensation values by thickness class, see `reference/PUCK_SCREENS_REFERENCE.md`.

### Pre-infusion behavior

Qualitative: a puck screen evens initial wetting, which can let pre-infusion saturate the puck more uniformly before pressure ramps. For dense **light roast** pucks specifically, a slightly longer pre-infusion may benefit; this is a profile-tuning hint, not a required change.

### Flow / pressure

Modest. The screen redistributes flow rather than restricting it. No grind shift is warranted for **thin (≤ 1mm) round-hole** screens.

---

## Common Pitfalls

- **Cold screen → sour shot.** A non-preheated screen pulls heat from the puck surface, dropping extraction temperature on the first shot. **Preheat the screen by locking it into the portafilter during the flush.** This is the most common puck-screen misdiagnosis trap (see Diagnostic Guardrails below).
- **Over-dosing → choke or bent screen.** Adding a screen reduces headroom between the puck and shower screen. If the user is already borderline-overdosing, the screen will hydraulic-lock ("sneeze") or bend. Keep dose = basket size; do not increase dose to compensate for the screen's thickness.
- **Upside-down screen orientation.** Most screens have a smooth side and a textured/perforated side. Installing an upside-down screen reduces dispersion effectiveness; some designs bend or fit poorly when flipped. Always verify orientation per manufacturer instructions.
- **Wrong size.** A 58.5mm screen in a 54mm basket (or vice versa) creates pressure spikes, bypass channeling, or won't seat. Match the screen size to the basket.
- **Bent screen.** A previously over-dosed or mis-stacked screen may be permanently deformed. A bent screen seats unevenly and channels along its warped edge. Replace bent screens.
- **Oil retention on mesh.** **mesh** screens trap oils far more than **round-hole** screens. Without regular cleaning, oils go rancid and contribute bitter/stale notes to subsequent shots.
- **Diminishing returns.** On machines with already-excellent shower screens, the marginal benefit is small. Do not chase a screen as a fix for an extraction problem that lives elsewhere (grind, dose, prep).
- **Protects puck from shower screen imprint** — a screen prevents the surface erosion and "screen kiss" that overdosed pucks otherwise show; this means the BASKETS.md headroom-by-imprint check is masked when a puck screen is installed (rely on flow behavior and measured headroom instead).

---

## Cleaning & Maintenance

| Cadence | Action | Notes |
|---------|--------|-------|
| Daily | Rinse with hot water | Both **round-hole** and **mesh** |
| Weekly | Cafiza (puly caff) soak | **mesh screens require this more strictly** — oils embed faster in fine mesh than in discrete drilled holes |
| As needed | Inspect for bend, deformation, fouling | Replace if bent; deep-clean if mesh dispersion drops |

**round-hole** screens (e.g. Normcore 0.18mm × 19 holes) are easier to maintain — fewer trapped oils, faster rinse.
**mesh** screens (e.g. IMS, Pesado, Sworks) need stricter weekly degreasing; expect 2–3× the cleaning effort of round-hole.

316 stainless steel is corrosion-resistant but not immune to staining or salt damage; avoid leaving any screen in standing water.

---

## Diagnostic Guardrails

This section is the **Single Source of Truth** for skill-side puck-screen guardrails. Skills (`/diagnose`, `/shot-feedback`) reference this section by name; they do NOT carry their own copy of the wording.

### Cold-Screen Sour Guardrail

**When**: a shot tastes sour AND the user has a puck screen installed (Equipment row value ≠ `None`).

**Action**: ASK about preheat discipline before recommending a grind-finer adjustment. Specifically: was the screen locked into the portafilter during the flush, or was it added after?

**Why**: cold metal pulls heat from the puck surface on the first shot, dropping effective extraction temperature and producing a sour, under-extracted result. **Preheat fixes the cause; grinding finer makes it worse** (a finer grind compounds under-extraction's astringency and slows flow into the still-cold screen).

**Resolution path**: if preheat was missed, rerun the shot with proper preheat before any grind change. If preheat was correct and sourness persists, fall back to the standard sour-shot adjustment ladder (temp up, then grind finer).

### Channeling-Nuance Note

**When**: diagnosing a sour-AND-bitter shot (the classic channeling signature) AND a puck screen is installed.

**Interpretation**: remaining channeling is **likely** (NOT "almost certainly") puck-prep-driven, **because** shower-screen-driven channeling is already mitigated by the screen. The probability mass shifts toward WDT / distribution / tamp issues.

**EXCEPT**: when the screen itself could be the source — verify orientation/fit first:
- Is the screen right-side-up (smooth side vs textured side per manufacturer)?
- Is it the correct size for the basket (58.5mm screen → 58mm basket)?
- Is it bent or warped from prior over-dosing?

If orientation, size, and condition all check out, the diagnosis defaults to puck-prep-driven channeling.

**Recommendation**: per CLAUDE.md Core Rule, the fix remains **fix puck prep, NOT grind**. The screen presence does not change the recommendation; it changes the confidence level and adds the orientation pre-check. Grinding finer makes channeling worse regardless of screen presence.

---

## Safety: never propose a screen as a diagnostic fix

The agent will **never propose** installing a puck screen as the answer to a diagnostic problem. Puck screens are a passive modifier on diagnostic expectations when the user already has one installed; they are not a recommended remedy for channeling, sourness, bitterness, body, or any other extraction issue. If a user asks "would a puck screen help my channeling?", the honest answer is: fix puck prep first; a screen is at best a marginal supplementary aid and at worst a distraction from the real cause.

---

## Edge Cases (parsing & handling)

The Equipment table in `user-setup.md` may present the Puck Screen field in several states. Handle each as follows:

- **missing row** — the Equipment table has no Puck Screen row at all (older user-setup.md predating this feature). Treat as `None`; do not load this knowledge file; do not branch.
- **blank value** — the row exists but the value cell is empty. Treat as `None`; same handling as missing row.
- **non-canonical value** — the value cell contains free text that doesn't cleanly map to thin/thick or round-hole/mesh (e.g. just a brand name with no spec). Best-effort: load this knowledge file, ask the user to clarify if a downstream recommendation depends on the classification.
- **mesh screen** — value indicates a mesh design. Apply mesh-specific guidance (stricter cleaning cadence, better dispersion, more oil retention).
- **thick screen** — value indicates thickness > 1mm. Apply thick-screen guidance (boiler-temperature compensation candidate; see reference file for numbers).
- **upside-down screen** — diagnostic possibility surfaced by the Channeling-Nuance Note. Not a setup-table value; a hypothesis to verify when channeling persists despite a screen being present.

For canonical tokens and full parsing contract, see `CLAUDE.md`.

---

*See reference for deep physics: [`reference/PUCK_SCREENS_REFERENCE.md`](reference/PUCK_SCREENS_REFERENCE.md).*
