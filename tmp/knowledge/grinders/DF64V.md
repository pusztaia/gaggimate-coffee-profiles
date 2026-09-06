# DF64V Grinder Reference

A quick reference for grind settings and adjustments on the **DF64V Gen-3 variable-speed single-dose grinder** with factory-fitted **SSP Cast Lab Sweet V3 Red Speed espresso burrs** (64 mm flat, pre-installed). For your personal grind settings that have worked well, see `grind-map.md` in the project root. Log all settings using the format in [`_NOTATION.md`](_NOTATION.md).

> **Deep dive:** Seasoning schedule, RDT/bellows workflow, commissioning, stall troubleshooting, and burr notes in [`../reference/DF64V_REFERENCE.md`](../reference/DF64V_REFERENCE.md).

---

## Adjustment System

The DF64V uses a **stepless collar** — there are no fixed macro or micro steps. Grind size is set by rotating the upper burr carrier collar; finer is clockwise (inward), coarser is counter-clockwise.

### Finding Your Zero (Chirp Point)

The DF64V is zeroed by motor-assisted chirp dialing:

1. Start the motor at your working RPM.
2. Slowly rotate the collar finer until the burrs make first contact — a faint, brief chirp or scratch.
3. Back off 1–2 marks immediately. This is your **zero reference**.
4. Log this zero date in `grind-map.md` as `zero set: YYYY-MM-DD` (see [`_NOTATION.md`](_NOTATION.md)).

Re-zero after any burr removal, reinstallation, or alignment adjustment. Prior-epoch rows in your grind map do not carry forward — see [`_NOTATION.md`](_NOTATION.md) for the superseding convention.

### Logging Your Setting

Record your grind as a **bare integer** equal to the number of marks the collar is open from your current chirp zero (e.g. `11`). The grind-log table declares **"Grind = marks open from chirp zero (DF64V)"** once in its header/footnote, so the bare number is unambiguous; without that header declaration a bare number is meaningless. The recorded number is still the chirp-relative operator coordinate — the header supplies the "from chirp" anchor; it is **not** the absolute printed-dial position. This is an operator coordinate, not a micron or particle-size claim. No microns-per-mark figure exists for the DF64V's stepless collar; do not treat mark counts as absolute gap measurements. See [`_NOTATION.md`](_NOTATION.md).

### Espresso Start Window

For espresso, begin dialing around **10–20 (marks from chirp)** from zero. This is a starting window only — your actual setting will depend on bean, dose, roast, and freshness. Dial from this range; do not assume it is a working shot.

---

## Motor Speed (RPM)

The DF64V Gen-3 is variable-speed. For espresso, the recommended operating range is approximately **1000–1200 RPM**:

- **~1000–1200 RPM** is the standard espresso window converged on by independent testers.
- **~1400 RPM** is a retailer preference reported to shift toward more body (vendor-framed; see Burr Character note below); it is not a floor or default.
- **Below ~700–800 RPM** risks a low-RPM stall with dense, light-roast beans fed all at once — this is an edge case, not a motor-torque flaw (see Deep Dive for context).

Start at **~1000–1100 RPM**. RPM changes shift the grind distribution and may require a grind-setting re-dial; treat RPM as a coarse lever, not a fine-tuning tool. Before reaching for RPM as a tuning move, read the **RPM as a dial-in lever** note below — the link between RPM and cup body is contested, not a settled dial.

---

## RPM as a dial-in lever

**When to reach for it.** RPM is the last lever, not the first. Dial grind, ratio, temperature, and puck prep first — they do far more, far more predictably. Only reach for RPM once those are settled and you want to run a *deliberate, logged* body/clarity experiment. RPM is **never** the opening move, and it is **never** a channeling fix (sour *and* bitter is a puck-prep problem — see the Quick Adjustment Guide).

**The one uncontested fact — anchor on your shot timer.** Changing RPM shifts the grind distribution, so after any RPM change you must **re-dial grind to restore your target shot time**. Let your shot timer tell you which way to move the grind — do not assume a direction. (No printed "raise RPM → go finer" rule lives here on purpose; the timer decides.)

**Why "more RPM → more body" is contested.** The popular framing that higher RPM adds body is **contested**, not established:

- One rigorous independent measurement (McKeon Aloe) found higher RPM shifted the distribution *coarser* with fewer fines — the opposite of the vendor "more body" story.
- Hoffmann's blind tasting found no clean correlation here at all (null result).
- The vendor-framed "RPM is a body lever" claim is unproven; treat it as plausible-at-best, not a calibrated dial.

So do not dial against RPM as if "RPM = body" were confirmed. **Your own logged RPM↔outcome data is the real signal** — record RPM with each shot and let your own cup tell you whether a given RPM change did anything for *this* coffee on *your* machine.

> **Deep dive:** the McKeon/Hoffmann evidence and the re-dial mechanics are covered in [`../reference/DF64V_REFERENCE.md`](../reference/DF64V_REFERENCE.md) → "RPM as a Body/Clarity Lever".

---

## Espresso Range

For espresso with the SSP Cast V3 Red Speed, typical starting windows by roast level:

Values in the **Typical Start Window** column are marks open from chirp zero.

| Roast Level | Typical Start Window (marks from chirp) | Notes |
|-------------|----------------------|-------|
| Light       | 10–15  | Fine end; slow target time likely needed |
| Medium      | 13–18  | Standard espresso range |
| Dark        | 16–22  | Coarser to avoid over-extraction |

**These are starting points only.** Actual settings depend on bean freshness (fresher = slightly coarser), dose, target ratio/time, and your current zero epoch. The DF64V with SSP Cast burrs has a reputation for a narrower-than-average dial-in window — expect to work the range methodically.

---

## Quick Adjustment Guide

Starting from a working shot, adjust grind setting by small steps:

| Problem | Adjustment | Magnitude |
|---------|------------|-----------|
| Shot too fast, tastes sour | Go finer | 1–3 marks |
| Shot too slow, tastes bitter | Go coarser | 1–3 marks |
| Large correction needed | Move several marks, then fine-tune | 5+ marks |
| Both sour and bitter | Do not adjust grind — fix puck prep (channeling) | — |

**Rule of thumb:** Adjust in small increments — 1–3 marks per change. Taste, then adjust again if needed. The stepless collar is sensitive; large sweeps overshoot easily.

---

## Burr Character Note

> **This is a tendency/vendor-framed characterisation, not a measured guarantee. Dial against your actual cup.**

The SSP Cast Lab Sweet V3 Red Speed is a **64 mm flat espresso burr**. Flat burrs tend toward clarity (distinct, separated flavours) relative to conical burrs — but this is a contested tendency, not a deterministic law (Hoffmann's blind tasting found no clean burr-shape → body/clarity correlation).

Within the SSP flat range, the **Cast** line produces **higher fines than typical low-fines flats** (such as the SSP Multipurpose). This means the "flat = clarity, less body" characterisation applies with less force here than on lower-fines flat burrs.

The **Red Speed** TiAlCN coating is vendor-described as adding body relative to the Silver Knight (DLC) variant; the vendor itself notes this is "secondary and grinder-dependent." Treat as plausible, not established.

**Practical implication:** Since the burr is fixed, the levers you actually have for body are **dose and ratio** (predictable) — and, with caveats, **RPM**. RPM is *not* a settled body dial: the "more RPM → more body" link is contested (see the **RPM as a dial-in lever** note above for the McKeon-coarser / Hoffmann-null evidence and the own-data hedge). Reach for dose and ratio first; only run RPM as a deliberate, logged experiment. The cup-character details defer to your specific extraction and taste rather than the burr specification.

---

*For your personal successful settings, see `grind-map.md` in the project root. For the logging format and epoch conventions, see [`_NOTATION.md`](_NOTATION.md).*
