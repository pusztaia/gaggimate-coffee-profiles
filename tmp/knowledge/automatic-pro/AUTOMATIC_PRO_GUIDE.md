# Automatic Pro Profile Guide

> **Source**: GaggiMate firmware built-in profile by modsmthng (GM#0031, GaggiMate Owner)
> **Version**: vIT3_0_8 (current) — 5-phase, declining flow, pressure-targeted ramp
> **Profile files**: `profile_files/Automatic Pro vIT3_0_8 {dose}g.json` (16g, 18g, 20g, 22g)

## Overview

The Automatic Pro is a **firmware built-in** profile that ships with Gaggimate. It uses flow-based variable pressure to create self-regulating extraction that adapts to puck resistance automatically. Unlike agent-created profiles in the Profile Library, Auto Pro is maintained by the Gaggimate developer and updated with firmware releases.

**Key behaviors:**
- Flow targeting with pressure ceilings — pressure adapts to grind automatically
- 9 bar extraction ceiling prevents over-extraction bitterness
- Declining flow during main extraction for sweetness and balance
- "Second Blooming" effect with fine grinds (see below)

---

## Quick Settings (via display)

| Mode | Formula | Example (18g, 1:2) |
|------|---------|---------------------|
| **Weight** | `Dose × Ratio` | 2 × 18g = **36g** |
| **Time** | `(Dose × Ratio) / Flow + 16s` | (36) / 1.8 + 16 = **36s** |

---

## Brewing Recommendations

For temperature, ratio, and roast-level guidance, see [Espresso Brewing Basics](../ESPRESSO_BREWING_BASICS.md). The default profile temperature is 91°C; adjust via the machine display based on roast level.

---

## 5-Phase Architecture (vIT3_0_8)

The actual firmware profile has **5 phases**, not the 4 described in older v2 documentation:

### Phase 1: Initialization
- **Goal**: Detect portafilter state, prepare for fill
- **Pump**: Minimal flow (0.1 g/s) at 1 bar ceiling
- **Duration**: 3s max
- **Stop**: Exits when pressure drops to ≤0.7 bar (confirms system is depressurized and ready)
- **Note**: This phase is new in vIT3 — v2 skipped straight to filling

### Phase 2: Fill Headspace
- **Goal**: Rapidly fill the space above the puck without building extraction pressure
- **Pump**: High flow (10 g/s) at 1 bar ceiling — fast fill, no extraction
- **Transition**: Ease-out over 10s (ramps up from previous phase's low flow, decelerates as headspace fills)
- **Duration**: 20s max
- **Stop**: Exits when pressure reaches ≥0.8 bar (headspace is full, water has contacted puck)
- **Key change from v2**: Pressure ceiling lowered from 2 bar to 1 bar; uses pressure-based stop instead of pumped volume stop

### Phase 3: Saturate Puck
- **Goal**: Fully wet the coffee bed at low pressure, allow CO2 to escape
- **Pump**: Moderate flow (2 g/s) at 2 bar ceiling
- **Duration**: 30s max
- **Stop**: Exits on EITHER `volumetric ≥ 1g` (first drip in cup) OR `pumped ≥ X ml` (dose-dependent, see scaling table)
- **Key change from v2**: Combines the old "Bloom" concept with saturation; uses constant 2 g/s across all doses instead of dose-scaled flow

### Phase 4: Extraction Start
- **Goal**: Build pressure through puck resistance to begin extraction
- **Pump**: **Pressure-targeted** at 12 bar with dose-scaled flow limit
- **Transition**: Instant, `adaptive: false` (starts from target, not current value)
- **Duration**: 6s max
- **Stop**: Exits when `volumetric ≥ 10g` (extraction underway)
- **Key change from v2**: Switched from flow-targeting to **pressure-targeting** — the pump drives to 12 bar while flow acts as a limiter. This is fundamentally different from v2's flow-based ramp.

### Phase 5: Main Extraction
- **Goal**: Extract at declining flow with 9 bar pressure ceiling
- **Pump**: Flow-targeted, declining from Phase 4 flow → 1.2 g/s over 40 seconds
- **Transition**: Linear over 40s, adaptive (starts from actual current flow)
- **Duration**: 90s max
- **Stop**: Exits when target weight reached (dose × ratio)
- **Key change from v2**: v2 used constant flow; vIT3 uses a **40-second declining flow** from the Phase 4 flow rate down to 1.2 g/s, similar to lever machine behavior

---

## Dose Scaling

Only **3 parameters** change between dose variants. Everything else is identical:

| Dose | Saturate Puck: pumped stop (ml) | Extraction Start: flow limit (g/s) | Main Extraction: volumetric stop (g) at 1:2 |
|------|------|------|------|
| **16g** | 8 | 1.6 | 32 |
| **18g** | 10 | 1.8 | 36 |
| **20g** | 12 | 2.0 | 40 |
| **22g** | 14 | 2.2 | 44 |

### Scaling Formulas

```
Saturate pumped stop  = (Dose - 10) / 1           → rounds to nearest even
Extraction Start flow = Dose × 2 / 20s            → same formula as v2
Volumetric stop       = Dose × Ratio              → adjust via display
```

**Constants across all doses:**
- Temperature: 91°C
- Phase durations: 3s, 20s, 30s, 6s, 90s
- Pressure ceilings: 1 → 1 → 2 → 12 → 9 bar
- Main Extraction decline: 40s linear to 1.2 g/s
- Initialization and Fill Headspace are identical for all doses
- Saturate Puck flow is always 2 g/s (v2 scaled this; vIT3 does not)

---

## The "Second Blooming" Effect

When ground very fine, the transition from the 12 bar Extraction Start (Phase 4) to the 9 bar Main Extraction ceiling (Phase 5) causes flow to briefly pause as the system regulates pressure downward. This is **not an error** — it creates a secondary saturation moment that often produces rich, chocolatey profiles.

**Best for**: Chocolatey/nutty roasts at a 1:1.5 ratio with a fine grind.
**Not occurring?** Grind finer — this effect only happens with high puck resistance.

---

## v2 vs vIT3 Comparison

The original documentation (and many online guides) describe the v2 architecture. The actual firmware profiles are vIT3_0_8:

| Aspect | v2 (documented, outdated) | vIT3_0_8 (actual firmware) |
|--------|---------------------------|----------------------------|
| **Phases** | 4 (Pre-Infusion → Bloom → Ramp → Brew) | 5 (Initialization → Fill Headspace → Saturate Puck → Extraction Start → Main Extraction) |
| **Pre-infusion pressure** | 2 bar | 1 bar (gentler) |
| **Pre-infusion fill** | 20 g/s flow target | 10 g/s with ease-out transition |
| **Pre-infusion stop** | Pumped volume + volumetric | Pressure-based (≥0.8 bar) |
| **Saturation flow** | Dose-scaled (e.g., 1.8 g/s for 18g) | Constant 2 g/s for all doses |
| **Ramp/Extraction Start** | Flow-targeted, 12 bar ceiling | **Pressure-targeted**, 12 bar with flow limit |
| **Main extraction** | Constant flow | **Declining flow** (40s linear to 1.2 g/s) |
| **Initialization phase** | None | Yes — 3s system check |

**Why the change**: vIT3 addresses several v2 limitations:
- Gentler 1 bar pre-infusion reduces puck disturbance
- Pressure-based headspace detection is more reliable than fixed volume calculation
- Constant 2 g/s saturation simplifies dose scaling
- Pressure-targeted ramp provides more consistent extraction start
- Declining flow improves sweetness and reduces late-extraction harshness

---

## Troubleshooting

For diagnosing extraction issues (sour, bitter, channeling, stalls), see the [Diagnostic Decision Tree](../ESPRESSO_BREWING_BASICS.md) in Espresso Brewing Basics.

---

## For Custom Flow-Variable Profiles

The Automatic Pro's flow-variable-pressure technique can be applied to custom agent-created profiles. For profile JSON structure, pump modes, transitions, and stop conditions, see:

- **[Profile Creation Guide](../GAGGIMATE_PROFILE_CREATION_GUIDE.md)** — Full JSON schema reference
- **[Profile Library](../PROFILE_LIBRARY.md)** — Ready-to-use agent-created profiles

The core technique (flow targeting with pressure ceiling) is documented in the Profile Creation Guide. The Auto Pro's specific innovation is combining this with declining flow and pressure-targeted ramp — patterns you can incorporate into custom profiles.
