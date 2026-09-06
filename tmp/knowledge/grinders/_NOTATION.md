# Grind-Logging Notation Contract

> **Applies to all grinders.** This file defines the grinder-neutral notation for logging grind settings. For per-grinder operating details, see the grinder's quick-ref under `knowledge/grinders/`. For your personal logged settings, see `grind-map.md` in the project root.

---

## Core Principle: Chirp-Relative Coordinates

Log grind settings **relative to your grinder's current zero (chirp) point**, not as absolute dial positions.

**Format:** `chirp + N marks`

- `chirp` is the moment your burrs just touch at minimum resistance — your grinder's personal, current zero reference.
- `N marks` is the number of graduation marks (steps, clicks, or collar turns) you've opened from that zero.
- **This value is an operator coordinate — explicitly NOT a micron gap or particle-size claim.** The same `chirp + 15 marks` on two different grinders, or on the same grinder before and after a re-zero, does not represent the same physical particle distribution.

Do not log absolute printed-dial numbers as the canonical record. `chirp + N marks` is the record; the dial number at that chirp is incidental and meaningless after any re-zero or burr reinstallation.

### Chirp-zeroed shorthand: the bare integer

On a **chirp-zeroed / stepless grinder** (e.g. the DF64V), record the grind as a **bare integer** equal to the number of marks the collar is opened from the chirp zero — for example, `11`. This is shorthand only: it is meaningful **only** because the grind-log table carries a **mandatory** one-time header (or footnote) declaration:

```
Grind = marks open from chirp zero (<GRINDER>)
```

That header supplies the "from chirp" anchor once, so the repetitive `chirp + … marks` wording can be factored out of every row. The bare integer is canonical **only** because of this declaration; a bare number without the header is meaningless.

- **The bare integer is STILL the chirp-relative operator coordinate.** The header supplies the "from chirp" anchor — we are only factoring the repeated `chirp + …` wording out of each row, not changing what the number *means*. It is **NOT** the absolute printed dial position. The existing prohibition above still holds: do **not** bless the absolute printed-dial number as the canonical record. (A user who has zeroed their grinder *at* the chirp point will read the same number off the dial, but the record's meaning is "marks from chirp", not "dial position".)
- The same operator-coordinate caveat applies unchanged: `11` is an operator coordinate, not a micron gap or particle-size claim.

---

## Motor Speed (RPM) — A Separate, Non-Chirp Coordinate

For variable-speed grinders, motor RPM is logged as a **plain integer** (e.g. `850`) — never as `chirp + N marks`. RPM is **additive to** the chirp/epoch contract above, not a redefinition of it: it is a second, independent column, never folded into the `chirp + N marks` value.

- **RPM is a grinder configuration value, NOT a chirp coordinate.** It describes how fast the burrs turn, not how far the dial is opened from zero.
- **RPM is NOT bound to the zero-set epoch.** A re-zero, burr swap, or burr reinstallation does not invalidate a logged RPM — the integer carries forward across epochs unchanged.
- **Blank for fixed-speed grinders.** If the grinder has no motor-speed control, leave the RPM column empty. Do not record a value where none exists.
- **Never infer an unobserved RPM.** Log only the RPM the user actually set or reported. Do not back-calculate, estimate, or guess a motor speed.
- **Logged as an independent column**, parallel to `chirp + N marks` — never substituted for it or merged into it.

---

## Epoch Binding: Zero-Set Anchor

A `chirp + N marks` value is only meaningful relative to the zero it was dialed from. **Every grind-log table must open with a zero-set anchor line identifying the epoch:**

```
zero set: YYYY-MM-DD
```

This anchor is the epoch for every row beneath it. If you re-zero or swap burrs and establish a new zero, rows logged under the old epoch do not carry forward to the new one — see the superseding convention below.

On a chirp-zeroed grinder using the bare-integer shorthand, the marks-from-chirp header declaration (`Grind = marks open from chirp zero (<GRINDER>)`) sits **alongside** this zero-set anchor — the zero-set anchor establishes *which* chirp epoch the integers count from, and the header declares that the bare integers *are* marks-from-chirp counts. Both are required.

### Worked example

```
zero set: 2026-05-01   ← anchors all rows below to this burr-seating / zero date

| Date       | Coffee             | Grind          | Notes          |
|------------|--------------------|----------------|----------------|
| 2026-05-03 | Honduras Finca Mil | chirp + 18 mk  | 28 s, 1:2.2    |
| 2026-05-10 | Ethiopia Guji      | chirp + 14 mk  | 26 s, 1:2      |
```

Without the `zero set: 2026-05-01` header, the row `chirp + 18 mk` is ambiguous — you cannot tell which zero it was measured from. The epoch anchor makes every logged value unambiguous.

---

## Superseding Convention: Re-Zero and Burr-Swap Epochs

When you establish a new zero (re-zero after alignment drift, burr swap, or burr reinstallation), the prior epoch's rows become **dead coordinates** — they do not transfer to the new zero and must not be silently reused as a starting point.

**Convention:** Insert a `--- pre-rezero (zero set: YYYY-MM-DD) ---` divider immediately before the new `zero set:` anchor. This visually sections the old epoch and labels it superseded.

### Worked example

```
| 2026-05-10 | Ethiopia Guji      | chirp + 14 mk  | 26 s, 1:2      |

--- pre-rezero (zero set: 2026-05-01) ---

zero set: 2026-06-15   ← new epoch after burr swap; rows above belong to the old epoch

| Date       | Coffee             | Grind          | Notes          |
|------------|--------------------|----------------|----------------|
| 2026-06-16 | Honduras Finca Mil | chirp + 20 mk  | 27 s, 1:2.1    |
```

The `chirp + 14 mk` from the old epoch is a historical record, not a carry-forward. Re-dial from scratch on the new zero rather than transplanting old values.

---

## Seasoning-State Caveat

The chirp point **drifts coarser** as new burrs break in and seat against each other. This means early `chirp + N marks` values quietly re-mean themselves over time: the same logged coordinate becomes effectively finer as the zero shifts coarser beneath it.

- Treat rows logged during the break-in period as **provisional references only** — they will not reproduce exactly once burr seating completes.
- Do not over-trust week-1 or week-2 settings; the zero is still moving.
- Once the chirp point stabilises (it stops noticeably drifting between sessions), logged values become reliable long-term references.
- Consult your grinder's reference companion for the specific seasoning span before trusting any logged setting.

---

## Prior-Grinder Values Are Dead-Coordinate Data

Values logged in a prior grinder's native units — for example, a Baratza Sette 270 code such as `13D` — **do not translate** to chirp-relative notation and are not carry-forward data.

- A Sette macro+micro code encodes a position on that grinder's stepped dial; it has no physical equivalent on any other grinder (or on the same grinder after a re-zero).
- Do not attempt to convert a prior-grinder value to `chirp + N marks`. Re-dial from scratch on the new grinder.
- Prior-grinder log rows should be archived or clearly labelled as grinder-specific historical data to avoid confusion during a migration.
- **The bare-integer shorthand applies ONLY to chirp-zeroed / stepless grinders.** An absolute-scale grinder (e.g. the Baratza Sette 270, with macro+micro codes like `9D`) keeps its own native code as the record — the bare-marks-from-chirp rule does **not** apply to it.

---

## Summary

| Concept | Rule |
|---------|------|
| Log format | Chirp-zeroed / stepless grinder → bare integer (marks open from chirp zero), valid only under a header declaring `Grind = marks open from chirp zero (<GRINDER>)`; absolute-scale grinder → its own native code (e.g. Sette `9D`). Either way it is an operator coordinate, not a micron or particle-size claim |
| Epoch anchor | Every table begins with `zero set: YYYY-MM-DD` |
| Re-zero / burr-swap | Insert `--- pre-rezero (zero set: ...) ---` divider; old rows are dead coordinates, do not carry forward |
| Seasoning drift | Early values are provisional; the chirp zero drifts coarser through break-in |
| Prior-grinder codes | Dead-coordinate data — do not translate or carry forward |
| Motor speed (RPM) | Plain integer in an independent column; a grinder config value, not a chirp coordinate; not epoch-bound (survives re-zero/burr-swap); blank for fixed-speed grinders; never inferred |
