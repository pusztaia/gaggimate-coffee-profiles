# Espresso Pressure Guide

A reference for how extraction pressure affects flavor, and how to match pressure to roast level, processing method, and shot style.

> *For deep explanations — matrix rationale, flavor compound effects, variable interactions, misconceptions — see [`reference/PRESSURE_REFERENCE.md`](reference/PRESSURE_REFERENCE.md).*

---

## Why Pressure Matters

Pressure defines espresso. At ~9 bar, water extracts lipids, emulsified oils, and dissolved solids that remain insoluble in gravity-driven brewing. But 9 bar is not always optimal.

### The Physics

- **Primary puck compression** occurs at ~4 bar. Pre-infusion should stay below this.
- **Flow rate peaks at ~9 bar.** Above this, secondary compression makes the puck denser, *reducing* flow. This is why 9 bar became the standard.
- **Above ~10 bar**, secondary compression causes channeling and harsh over-extraction.
- **As a shot progresses**, the puck erodes. Fixed 9-bar forces increasing flow through weakening channels — this is why pressure decline is beneficial.

> *For channeling physics, fines migration, and prevention strategies, see `EXTRACTION_SCIENCE.md`*

### What Pressure Controls

| Higher Pressure (8-9+ bar) | Lower Pressure (5-7 bar) |
|----------------------------|--------------------------|
| More body, viscosity | More clarity, transparency |
| More crema | Less crema |
| More oils extracted | Cleaner, tea-like character |
| Risk of channeling as puck degrades | More forgiving puck prep |
| Better for dense, hard-to-extract beans | Better for soluble, easy-to-extract beans |

---

## The Comprehensive Pressure Matrix

### By Roast Level + Processing Method

This table gives **main extraction pressure** (the sustained pressure during the brew phase, after pre-infusion). Pre-infusion should always be 2-4 bar regardless of target extraction pressure.

| | **Light Roast** | **Medium Roast** | **Dark Roast** |
|---|---|---|---|
| **Washed** | 8-9 bar | 9 bar | 7-8 bar |
| **Natural** | 7-8 bar | 8-9 bar | 6-7 bar |
| **Honey (Yellow)** | 8-9 bar | 9 bar | 7-8 bar |
| **Honey (Red/Black)** | 7-8 bar | 8-9 bar | 7-8 bar |
| **Anaerobic** | 6-8 bar | 7-8 bar | 6-7 bar |
| **Carbonic Maceration** | 6-8 bar | 7-8 bar | 6-7 bar |

---

## Pressure by Shot Style

Different shot styles use pressure differently. The target extraction pressure, profile shape, and timing all interact.

### Traditional Espresso (Fixed Pressure)

| Parameter | Value |
|-----------|-------|
| Pre-infusion | 2-4 bar, 4-8 seconds |
| Main extraction | Fixed at target (see matrix above) |
| Decline | None (or gentle taper in last 5s) |
| Ratio | 1:2 |
| Time | 25-32 seconds |

Best for: Medium roasts, washed coffees, everyday espresso. For coffees that need lower pressure (naturals, anaerobics), simply set the target pressure lower.

### Blooming Espresso

| Parameter | Value |
|-----------|-------|
| Gentle fill | Flow 2 ml/s, 5-8 seconds |
| Bloom (pump off) | 0 bar, 8-15 seconds |
| Ramp to extraction | Ease-in, 3-5 seconds |
| Main extraction | 7-9 bar (per matrix), with optional decline |
| Ratio | 1:2 to 1:2.5 |
| Time | 30-40 seconds total |

Best for: Light roasts, naturals, anaerobics — any coffee where you want maximum sweetness and even saturation.

**Pressure note:** With a bloom, you can sometimes use slightly higher extraction pressure than the matrix suggests, because the bloom ensures even extraction.

### Turbo Shot

| Parameter | Value |
|-----------|-------|
| Pre-wet | 5-6 bar, 2-3 seconds |
| Extraction | 5-6 bar constant flow |
| Ratio | 1:2.5 to 1:3 |
| Time | 12-20 seconds |
| Grind | Much coarser than traditional |

Best for: Light to medium roasts where you want maximum clarity and sweetness. Coarser grind + lower pressure = more uniform water distribution, less channeling, and surprisingly high extraction yields (19-22%).

**Pressure note:** Hendon et al. showed that 6-bar shots consistently achieved *higher* extraction yields than 9-bar shots at the same grind — because 9 bar causes more channeling.

### Allongé

| Parameter | Value |
|-----------|-------|
| Pre-infusion | 2-3 bar, 5-8 seconds |
| Ramp | To 6 bar peak |
| Main extraction | Constant flow (~2-3 ml/s), pressure naturally rises then declines |
| Ratio | 1:4 to 1:5 |
| Time | 25-40 seconds |
| Grind | Slightly coarser than traditional |

Best for: Light roasts, showcasing origin character. Extraction yields up to 27% through even, gradual extraction.

**Pressure note:** Uses flow control rather than pressure control. Pressure naturally peaks mid-shot and declines — mimicking a lever machine.

### Lever Decline

| Parameter | Value |
|-----------|-------|
| Pre-infusion | 2-4 bar, 5-8 seconds |
| Peak | 8-9 bar, 3-5 seconds |
| Decline | Linear from peak to 3-5 bar over 20-30 seconds |
| Ratio | 1:2 |
| Time | 28-35 seconds |

Best for: Medium roasts, natural and honey coffees — syrupy body with a clean finish. Declining pressure compensates for puck degradation, preventing late-shot channeling.

---

## Decision Framework: How to Pick Pressure

### Step 1: Start with the Matrix

Look up your coffee's roast level + processing method in the matrix above. This gives your target extraction pressure range.

### Step 2: Adjust for Shot Style

- **Traditional** → Use the matrix pressure directly
- **Blooming** → Can go 0.5-1 bar higher than matrix (bloom compensates)
- **Turbo** → 5-6 bar regardless of matrix (style overrides)
- **Allongé** → 6 bar peak, flow-controlled (style overrides)
- **Lever decline** → Start at matrix pressure, decline to matrix minus 4-5 bar

### Step 3: Adjust Based on Taste

| If the shot is... | Adjust pressure... | Why |
|--------------------|--------------------|-----|
| Sour/thin despite correct time | Up by 0.5-1 bar | More extraction force |
| Bitter/harsh/astringent | Down by 0.5-1 bar | Less aggressive extraction |
| Muddy/overly fermented (naturals) | Down by 1 bar | Less fermentation compound extraction |
| Flat/lacking character | Up by 0.5 bar, or try decline profile | More initial extraction, cleaner finish |
| Good balance but thin body | Up by 0.5 bar | More oils and dissolved solids |
| Good balance but too heavy | Down by 0.5 bar | Less body, more clarity |

---

*Pressure is one lever among many. The best shot comes from matching pressure to your specific coffee — its roast, its processing, its age — not from defaulting to a number that worked for someone else's beans. For the deep reference — matrix explanations, flavor compounds, variable interactions, misconceptions — see [`reference/PRESSURE_REFERENCE.md`](reference/PRESSURE_REFERENCE.md).*
