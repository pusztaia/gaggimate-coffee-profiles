# [Grinder Name] Grinder Reference

<!-- TEMPLATE INSTRUCTIONS
  This file is the quick-ref for a single grinder. Replace all [bracketed placeholders] with
  grinder-specific content. Delete comment blocks before publishing.

  OPERATE-VS-MAINTAIN SEAM — keep this split consistent across all grinder docs:

    QUICK-REF (this file) — operational, session-to-session use:
      ✓ Adjustment system / dial mechanics
      ✓ Espresso starting window and range table
      ✓ Quick symptom → adjustment table
      ✓ Short hedged burr-character note (tendency only, flagged as vendor-framed)
      ✗ NOT: seasoning schedule, commissioning steps, step-by-step workflow, troubleshooting detail

    REFERENCE COMPANION ([GRINDER_ID]_REFERENCE.md) — deep background, setup once:
      ✓ Seasoning schedule (kg before trusting settings, full settling span)
      ✓ Single-dose / retention / workflow specifics (RDT, bellows, purge, etc.)
      ✓ Commissioning and alignment check (factory-installed vs self-install burr)
      ✓ Troubleshooting (speed/stall, "can't grind fine enough", burr wear)
      ✗ NOT: session-to-session adjustment guidance (that lives in this quick-ref)

  The reference companion is optional — a grinder with no complex setup story can omit it.
  If created, name it `knowledge/reference/[GRINDER_ID]_REFERENCE.md` and open it with a
  `> **Quick lookup:**` blockquote linking back to this file.

  Log format: see _NOTATION.md — do not restate the notation contract in this file.
-->

A quick reference for grind settings and adjustments. For your personal grind settings, see `grind-map.md` in the project root.

> **Deep dive:** [Seasoning schedule, single-dose workflow, commissioning, and troubleshooting] in [`../reference/[GRINDER_ID]_REFERENCE.md`](../reference/[GRINDER_ID]_REFERENCE.md).

---

## Adjustment System

<!-- PLACEMENT: Describe the mechanical adjustment system of this specific grinder.
  Stepless collar → describe chirp/zero dialing procedure and what "a mark" means on this unit.
                    A chirp-zeroed grinder records a BARE INTEGER = marks opened from chirp zero;
                    the "from chirp" anchor is declared once in the grind-log header per _NOTATION.md,
                    so individual settings drop the repetitive "chirp + ... marks" wording.
  Stepped collar  → describe step count and any macro/micro split.
  Speed control   → document RPM range and the operating point for espresso (if applicable).

  Do NOT prescribe a microns-per-mark figure.
  For the logging format (bare marks-from-chirp notation, epoch anchors, superseding rows),
  link to _NOTATION.md — do not duplicate the contract here. -->

### [Adjustment Type — e.g. "Stepless Collar" or "Macro + Micro Dial"]

- [Describe the physical mechanism and how to move it]
- [How to establish the zero / chirp point]
- [How to read or record a setting]
- For the logging format, see [`_NOTATION.md`](_NOTATION.md).

---

## Espresso Operating Point

<!-- PLACEMENT: Grinder-specific operating characteristics for espresso.
  Include: starting window (rough mark range from zero), any speed/RPM-control notes,
  and any grinder-specific caveats (stall risk, minimum grind size floor, etc.).
  Absolute micron/particle-size claims → do NOT include.
  Burr character tendency → include a short, hedged note (see Burr Character section below).
  Variable-speed gating: a grinder is treated as variable-speed (RPM behavior enabled across the skills) when its file includes a `## Motor Speed (RPM)` section; fixed-speed grinders omit it. -->

### Starting Window

[Describe the typical starting window for espresso. On a chirp-zeroed/stepless grinder this is a bare range, e.g. "~[N–M]" (marks from chirp, per the grind-log header); on an absolute-scale grinder use that grinder's own dial codes.]

### Burr Character (tendency only)

<!-- A short, explicitly-hedged note on this burr set's tendency. Must be flagged as a
  tendency/vendor-framed claim, not a measured or guaranteed outcome. Examples:
  "tends toward [X], but judge by cup" or "vendor-reported to [Y] — actual results vary by
  roast, dose, and ratio." Do not state cup-character tendencies as fact. -->

[Short hedged burr-character note — flagged as a tendency, not a guarantee.]

### Espresso Range

<!-- Roast-level starting points. For a chirp-zeroed/stepless grinder, write bare ranges
  (e.g. "[N–M]") — the "marks from chirp" anchor is declared once in the grind-log header per
  _NOTATION.md, not repeated per row. For an absolute-scale grinder, use that grinder's own dial
  codes. Label clearly as starting points only. -->

| Roast Level | Typical Starting Point | Notes |
|-------------|------------------------|-------|
| Light       | [N–M]                  |       |
| Medium      | [N–M]                  |       |
| Dark        | [N–M]                  |       |

**Important:** These are starting points. Actual settings depend on bean freshness, humidity, dose size, target ratio and time. All values are operator coordinates — see [`_NOTATION.md`](_NOTATION.md).

---

## Quick Adjustment Guide

<!-- PLACEMENT: Symptom → action table using grinder-relative vocabulary.
  Use "finer / coarser" language and relative magnitudes (small step, larger step).
  Do NOT use "macro step" or "micro step" (Sette-era vocabulary).
  "Sour AND bitter simultaneously → fix puck prep, NOT grind" — do not suggest a grind
  adjustment for channeling symptoms. -->

Starting from a working shot:

| Problem | Adjustment | Magnitude |
|---------|------------|-----------|
| Shot too fast, sour | Go finer | Small step |
| Shot too slow, bitter | Go coarser | Small step |
| Large correction needed | [Finer or coarser] | Larger step — [grinder-specific guidance] |

---

*For your personal successful settings, see `grind-map.md` in the project root. For the grind-logging format, see [`_NOTATION.md`](_NOTATION.md).*
