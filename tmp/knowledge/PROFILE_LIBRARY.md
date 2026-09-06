# Profile Library

Ready-to-use extraction profiles for Gaggimate Pro. These are **generic templates** — coffee-specific profiles created during dialing are saved in `coffees/{roaster}-{coffee-name}/`.

> **Deep dive:** Full profile definitions with JSON, parameters, and flavor expectations in [`reference/PROFILE_LIBRARY_REFERENCE.md`](reference/PROFILE_LIBRARY_REFERENCE.md).

> **Note:** All profiles are sized for a **22g dose**. Volumetric targets reflect the stated ratio at 22g in. If your basket size changes, recalculate: `target = dose × ratio`.

---

## Quick Reference

| Profile | Roast | Temp | Ratio | Time | Best For |
|---------|-------|------|-------|------|----------|
| [Classic 9-Bar](#classic-9-bar) | Medium | 93°C | 1:2 | 25-32s | Everyday espresso |
| [Light Roast Bloom](#light-roast-bloom) | Light | 95°C | 1:2.5 | 28-35s | Fruity, floral coffees |
| [Dark Roast Gentle](#dark-roast-gentle) | Dark | 89°C | 1:1.5-2 | 22-28s | Italian roasts, milk drinks |
| [Natural Process Bloom](#natural-process-bloom) | Light-Med | 94°C | 1:2-2.5 | 30-38s | Natural/dry processed beans |
| [Turbo Shot](#turbo-shot) | Any | 96°C | 1:2.5-3 | 15-20s | Clarity, brightness |
| [Allongé](#allongé) | Light-Med | 94°C | 1:4-5 | 40-50s | Long, sweet, tea-like |
| [Lever Decline](#lever-decline) | Medium | 91°C | 1:2 | 28-35s | Syrupy body, complex |
| [Milk Drink Base](#milk-drink-base) | Med-Dark | 92°C | 1:1.5 | 22-26s | Concentrated, intense body |

---

## Profile Summaries

### Classic 9-Bar
The reliable workhorse — pre-infusion → ramp → hold for most medium roasts.
`93°C | 1:2 | 25-32s | Standard grind | Balanced, chocolate, mild sweetness`

### Light Roast Bloom
Bloom phase enhances sweetness in Nordic-style light roasts.
`95°C | 1:2.5 | 28-35s | Finer than medium | Bright acidity, floral, stone fruit`

### Dark Roast Gentle
Lower temp and pressure to avoid bitterness; shorter ratio for body.
`89°C | 1:1.5-2 | 22-28s | Coarser than medium | Chocolate, caramel, full body`

### Natural Process Bloom
Extended bloom tames natural process intensity, preserves fruit.
`94°C | 1:2-2.5 | 30-38s | Medium-fine | Blueberry, strawberry, juicy body`

### Turbo Shot
Coarse grind, high flow, fast extraction for clarity. Ratio must be 1:2.5-3 — a 1:2 turbo will be sour.
`96°C | 1:2.5-3 | 15-20s | Significantly coarser | Bright, clean, tea-like`

### Allongé
Long, sweet extraction at extended ratios — not a lungo, a true extended extraction.
`94°C | 1:4-5 | 40-50s | Slightly coarser | Sweet, tea-like, delicate acidity`

### Lever Decline
Mimics spring lever with declining pressure for syrupy body and complex sweetness.
`91°C | 1:2 | 28-35s | Slightly finer than classic | Syrupy, caramel, reduced acidity`

### Milk Drink Base
Punchy, concentrated ristretto-style shot with maximum intensity.
`92°C | 1:1.5 | 22-26s | Standard to slightly finer | Intense, chocolate/caramel, full body`

---

## Firmware Built-In Profiles

### Automatic Pro (vIT3)

The **Automatic Pro** is a firmware built-in profile maintained by the Gaggimate developer — not an agent-created profile. It ships pre-installed on Gaggimate Pro devices in multiple dose variants (16g, 18g, 20g, 22g).

It uses flow-based variable pressure with declining flow extraction. Select the correct dose variant on your machine's display, then adjust temperature and target weight/time.

> **Full documentation**: [`automatic-pro/AUTOMATIC_PRO_GUIDE.md`](automatic-pro/AUTOMATIC_PRO_GUIDE.md) — 5-phase architecture, dose scaling, and Second Blooming effect.

---

## Profile Selection Guide

### By Taste Goal

| Want More... | Try This Profile | Key Change |
|--------------|------------------|------------|
| Brightness/acidity | Light Roast Bloom | Higher temp, longer ratio |
| Sweetness | Lever Decline or Natural Process Bloom | Bloom phase, declining pressure |
| Body | Dark Roast Gentle | Lower temp, shorter ratio |
| Clarity | Turbo Shot | Coarse grind, high flow |
| Balance | Classic 9-Bar | Standard parameters |

### By Problem

| Issue | Profile Suggestion | Why |
|-------|-------------------|-----|
| Shots too sour | Light Roast Bloom | Higher temp, bloom for better extraction |
| Shots too bitter | Dark Roast Gentle | Lower temp/pressure, taper at end |
| Want more intensity | Milk Drink Base | Shorter ratio concentrates flavor |
| Inconsistent | Automatic Pro (firmware) | Self-regulating flow control |
| Channeling | Natural Process Bloom | Extended pre-infusion, gentle fill |

---

*All profiles marked [AI] were created by your barista assistant and can be safely deleted via the MCP tools.*
