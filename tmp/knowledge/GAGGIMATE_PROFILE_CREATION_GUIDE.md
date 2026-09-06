# Gaggimate Profile Creation Guide

## Overview

Quick-reference card for Gaggimate profile JSON structure. For full profile creation workflow, use `/gaggimate-profiles`. For complete examples, transition details, and advanced techniques, see [`reference/PROFILE_CREATION_REFERENCE.md`](reference/PROFILE_CREATION_REFERENCE.md).

> **Looking for ready-to-use profiles?** See `PROFILE_LIBRARY.md` for a curated collection organized by roast level, processing method, and shot style.

## Profile Versions

- **Gaggimate Standard**: Basic temperature control, volumetric dosing, timed phases
- **Gaggimate Pro**: Advanced pressure/flow profiling, real-time pressure monitoring, complex transitions, multiple stop conditions

---

## JSON Profile Structure

### Top-Level Properties

```json
{
  "label": "Profile Name",
  "type": "pro",
  "description": "Optional description of the profile",
  "temperature": 93,
  "phases": [...]
}
```

| Field | Type | Required | Description | Valid Values |
|-------|------|----------|-------------|--------------|
| `label` | string | Yes | Display name shown on machine | Any string |
| `type` | string | Yes | Profile complexity level | `"simple"` or `"pro"` |
| `description` | string | No | Optional notes about the profile | Any string |
| `temperature` | number | Yes | Global target temperature in °C | 70-100 (typical: 88-96) |
| `phases` | array | Yes | Ordered list of extraction phases | Array of phase objects |

---

## Phase Structure

### Phase Fields Reference

| Field | Type | Required | Description | Valid Values |
|-------|------|----------|-------------|--------------|
| `name` | string | Yes | Display name shown during brew | Any string (e.g., "Pre-infusion", "Ramp", "Hold") |
| `phase` | string | Yes | Phase category for display | `"preinfusion"`, `"brew"`, `"decline"` |
| `valve` | number | Yes | Three-way valve position | `0` = closed, `1` = open |
| `duration` | number | Yes | Maximum phase duration in seconds | 1-60 (typical: 3-30) |
| `temperature` | number | No | Override global temp (0 = use global) | 0 or 70-100 |
| `transition` | object | Yes (Pro) | How to transition to target values | See Transition section |
| `pump` | object | Yes | Pump control configuration | See Pump section |
| `targets` | array | No | Stop conditions (exits phase early) | See Targets section |

### Phase Type Guidelines

- **`preinfusion`**: Low-flow wetting phase (typically 2-5 seconds)
- **`brew`**: Main extraction phase (pressure/flow control)
- **`decline`**: Pressure taper/finish phase (optional)

---

## Pump Configuration

### Pump Fields

| Field | Type | Required | Description | Valid Values |
|-------|------|----------|-------------|--------------|
| `target` | string | Yes | Control mode | `"pressure"`, `"flow"`, `"power"`, `"off"` |
| `pressure` | number | Yes | Target/limit pressure in bars | 0-12 (typical: 6-9) |
| `flow` | number | Yes | Target/limit flow in ml/s | 0-10 (typical: 2-5), `-1` = adaptive |

### Pump Target Modes

- **Pressure** (`"pressure"`) — Maintain specific pressure. `flow` acts as optional limit.
- **Flow** (`"flow"`) — Maintain specific flow rate. `pressure` acts as ceiling. Use `flow: -1` for adaptive flow (auto-adjusts to puck resistance).
- **Power** (`"power"`) — Fixed pump percentage (Standard only). Use `pressure: 0, flow: 0` for **bloom (pump off)**.

> **Flow limit vs ease-in for a gentle build (channeling prevention).** In `pressure` mode the
> `flow` value is an *optional limit*, but on a **permeable puck** a low limit (e.g. `flow: 4`)
> can become the *binding constraint* and pin pressure **below target** — the pump sits pegged
> at the limit while pressure stalls, giving a thin, sour, under-extracted shot. If you want a
> gentle build that **still reaches full pressure**, lengthen the **ease-in transition** (slows
> the pressure *ramp*) rather than capping flow (caps the pressure *ceiling*). Set `flow: 0`
> (no limit) on the ramp/hold and let a longer ease-in do the gentling. Reserve a low flow
> limit for when you deliberately want a flow-ceilinged shot. (See the matching telemetry
> signature "Capped below target" in `diagnose/references/TELEMETRY_PATTERNS.md`.)

---

## Transition Configuration

### Transition Fields

| Field | Type | Required | Description | Valid Values |
|-------|------|----------|-------------|--------------|
| `type` | string | Yes | Ramp curve shape | `"instant"`, `"linear"`, `"ease-in"`, `"ease-out"`, `"ease-in-out"` |
| `duration` | number | Yes | Ramp duration in seconds | 0-10 (0 = instant) |
| `adaptive` | boolean | Yes | Start from current or previous target | `true` = current, `false` = previous target |

### Transition Types

- **Instant** — Immediate jump. Use for phase starts.
- **Linear** — Constant rate. Use for standard pressure ramps.
- **Ease-in** — Slow start, fast finish. Use for pre-infusion → extraction.
- **Ease-out** — Fast start, slow finish. Use for tapering/decline.
- **Ease-in-out** — Slow start and finish. Use for complex pressure changes.

---

## Stop Conditions (Targets)

### Target Fields

| Field | Type | Required | Description | Valid Values |
|-------|------|----------|-------------|--------------|
| `type` | string | Yes | Measurement type | `"volumetric"`, `"pumped"`, `"pressure"`, `"flow"` |
| `operator` | string | Yes | Comparison operator | `"gte"` (>=), `"lte"` (<=), `"gt"` (>), `"lt"` (<) |
| `value` | number | Yes | Threshold value | Depends on type |

### Target Types

- **Volumetric** — Exit at scale weight (requires BT scale). Most common for final shot weight.
- **Pumped** — Exit after X ml pumped. Scale-independent. (The token is `"pumped"` — firmware profiles and `phase_exits` telemetry both use it; an earlier revision of this guide said `"water_pumped"`, which is wrong.)
- **Pressure** — Exit when pressure crosses threshold (above or below).
- **Flow** — Exit when flow crosses threshold.

Multiple targets per phase use **OR logic** — phase exits when ANY condition is met.

> **Always pair long volumetric phases with a `pumped` backstop.** If the BT scale drops mid-shot (a documented Bookoo/Gaggimate failure mode), a volumetric target can never fire and the phase runs to its full duration timeout — potentially 3× the intended beverage. Add `{"type": "pumped", "operator": "gte", "value": N}` where N clears a normal shot's total pumped volume with ~15–20% margin (observed normal totals for a 22g/55g shot: ~90–115 ml → backstop 130). Confirmed live on-device Jul 2026.

### Firmware behaviors observed on-device (Jul 2026, fw 1.8.0)

- **`phase: "decline"` is normalized to `"brew"` on upload** — the device rewrites it. The enum is display-only anyway; author repo JSONs with `"brew"` for decline phases so repo and device stay byte-identical.
- **`transition.duration` above the documented 10s max executes correctly** — 38–40s linear declines run as authored (telemetry-verified). The 0–10s range in the transition table is stale documentation for ramp-style transitions, not a firmware limit.
- **A pump-off phase encodes as `{"target": "flow", "pressure": 0, "flow": 0}`** — this is how the working on-device bloom/soak phases are written; `"power"`/0/0 also appears in older examples but flow/0/0 is the pattern the current firmware profiles use.

---

## Flow-Based Variable Pressure Technique

Pioneered by modsmthng_57901 on Gaggimate Discord. This technique creates **self-regulating pressure** — target a flow rate with a pressure ceiling, and the machine adapts to puck resistance automatically.

```json
"pump": {
  "target": "flow",      // Primary: maintain this flow rate
  "pressure": 9,         // Secondary: never exceed this pressure
  "flow": 1.8            // Target flow in g/s
}
```

**How it works**: High puck resistance (fine grind) → pressure builds to the ceiling, flow may drop below target. Low resistance (coarse grind) → pressure stays low, flow is maintained. The profile adapts without manual adjustment.

**Advantages**: Grind tolerance, channeling prevention (lower initial pressure), flavor balance (pressure ceiling prevents bitterness), consistency across different coffees.

**Scaling flow to dose**: `Flow = Dose × 2 / 20s` (e.g., 16g → 1.6 g/s, 18g → 1.8 g/s, 22g → 2.2 g/s)

> **Gaggimate's built-in Automatic Pro profile** implements this technique with a 5-phase architecture including declining flow extraction. See [`automatic-pro/AUTOMATIC_PRO_GUIDE.md`](automatic-pro/AUTOMATIC_PRO_GUIDE.md).

---

## Best Practice Tables

For temperature, ratio, and adjustment strategies, see `ESPRESSO_BREWING_BASICS.md`.
For pressure selection by roast and processing method, see `PRESSURE_GUIDE.md`.
For ready-to-use profile patterns, see `PROFILE_LIBRARY.md`.

### Phase Duration Guidelines

| Phase Type | Typical Duration | Purpose |
|------------|------------------|---------|
| Fast fill | 2-3 seconds | Quick wetting at low pressure |
| Slow pre-infusion | 4-8 seconds | Even saturation, de-gas |
| Bloom/soak | 5-10 seconds | Enhance sweetness |
| Pressure ramp | 3-5 seconds | Build to extraction pressure |
| Hold phase | 15-30 seconds | Main extraction |
| Decline/taper | 3-6 seconds | Smooth finish |

> **Duration vs volumetric stop:** On phases with a volumetric stop, the volumetric target is the real exit condition — it controls the cup weight. Duration is a safeguard timeout. Set it generously (at least 1.5× expected extraction time) so it never cuts the shot short under normal conditions.

### Flow Rate Guidelines

| Flow Rate | Use Case | Pressure |
|-----------|----------|----------|
| 1.5-2.5 ml/s | Very gentle pre-infusion | <3 bar |
| 2.5-4 ml/s | Standard pre-infusion | 3-6 bar |
| 4-5 ml/s | Main extraction (with flow limit) | 8-9 bar |
| Adaptive (-1) | Final phase, adjusts to resistance | Variable |

---

*For complete profile examples, transition details, taste-driven profile tuning, advanced techniques, troubleshooting, lever simulation, and volumetric estimation — see [`reference/PROFILE_CREATION_REFERENCE.md`](reference/PROFILE_CREATION_REFERENCE.md). For full profile creation workflow — use `/gaggimate-profiles`.*
