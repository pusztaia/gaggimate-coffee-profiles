# Pressure Guide — Deep Reference

> *Quick reference: For the pressure matrix, shot style parameters, and decision framework, see [`../PRESSURE_GUIDE.md`](../PRESSURE_GUIDE.md).*

---

## Why Each Cell in the Pressure Matrix Makes Sense

**Roast level drives solubility:**
- Light roasts are denser, harder to extract. They can tolerate (and sometimes need) higher pressure to reach adequate extraction yield.
- Dark roasts are porous, highly soluble. They extract readily even at low pressure. Higher pressure risks pulling excessive bitter compounds (CGA lactones, phenylindanes).
- Medium roasts sit at the sweet spot where 9 bar was historically optimized.

**Processing method drives intensity and solubility:**
- **Washed** coffees have the lowest solubility — the bean must provide all flavor on its own, with no residual fruit compounds. They handle full pressure well because there's less risk of over-extracting intense fermentation flavors.
- **Natural** coffees absorbed fruit compounds during drying, making them more soluble and flavor-intense. Higher pressure extracts more of these fermentation-derived compounds, which can push the flavor from "blueberry jam" into "overripe fruit wine." Lower pressure keeps the fruit character clean and sweet.
- **Honey** coffees scale with how much mucilage was left on. Yellow honey (less mucilage) behaves closer to washed. Red/black honey (more mucilage, longer fermentation) behaves closer to natural.
- **Anaerobic/Experimental** coffees have the highest concentration of fermentation-derived compounds. These flavors are intense by design — high pressure amplifies the funk and ferment beyond pleasant levels. Lower pressure (6-8 bar) keeps the interesting flavors controlled.

---

## Pressure's Effect on Specific Flavor Compounds

| Pressure Level | Acids | Sugars | Bitter Compounds | Oils/Body |
|----------------|-------|--------|------------------|-----------|
| **5-6 bar** | Moderate extraction | Good — long contact time compensates | Minimal — low force avoids harsh compounds | Light body, less crema |
| **7-8 bar** | Well extracted | Excellent — sweet spot for balance | Moderate — controlled | Good body, moderate crema |
| **9 bar** | Fully extracted (can be sharp on light roasts) | Good | Higher — especially late in shot as puck degrades | Full body, rich crema |
| **10+ bar** | Over-extracted acids become astringent | Masked by bitterness | Excessive — secondary puck compression forces channeling | Heavy, muddy body |

**Key insight from research:** Higher initial pressure disproportionately extracts acids early in the shot (before the puck saturates evenly). This is why washed light roasts at 9 bar can taste sharp/sour even when total extraction yield is adequate — the acids came out first and dominated the cup.

---

## Interaction With Other Variables

### Pressure + Temperature

Temperature and pressure compound each other's effects on extraction:

| Scenario | Effect | When to Use |
|----------|--------|-------------|
| High temp + high pressure | Maximum extraction — risk of harshness | Only for very dense, hard-to-extract light washed coffees |
| High temp + low pressure | Good extraction, gentler approach | Light roast anaerobics — need the temp for extraction but lower pressure to control intensity |
| Low temp + high pressure | Concentrated body, controlled extraction | Medium-dark washed coffees for milk drinks |
| Low temp + low pressure | Minimum extraction | Dark roasts — prevents bitterness on already-soluble beans |

### Pressure + Grind Size

Pressure and grind are deeply interlinked — they're two sides of the same equation:

- **Finer grind + lower pressure** = similar flow rate to coarser grind + higher pressure, but different flavor (more even extraction with finer grind at lower pressure)
- **Coarser grind + lower pressure** = turbo shot territory (fast, clear, sweet)
- **Finer grind + higher pressure** = traditional espresso (slow, rich, full body)
- **Coarser grind + higher pressure** = inconsistent (puck resistance insufficient for the pressure, leading to fast channeling)

### Pressure + Pre-Infusion Length

Research from the Decent Espresso community and Scott Rao shows:

- Longer pre-infusion (10-30 seconds) allows lower main extraction pressure to achieve equivalent or better results than short pre-infusion + high pressure.
- With a 20-second pre-infusion, extraction pressure of 6-7 bar can match or exceed the extraction yield of a 5-second pre-infusion + 9 bar.
- The bloom (pump off after fill) is the extreme version of this — maximum saturation, then moderate extraction pressure.

---

## Common Misconceptions

### "Higher pressure = stronger coffee"
Wrong. Extraction strength (TDS) has more to do with contact time and ratio than pressure. A 6-bar turbo shot at 1:3 can achieve higher *extraction yield* than a 9-bar shot at 1:2.

### "Light roasts need higher pressure because they're harder to extract"
Partially true, partially misleading. Light roasts need more *total extraction* but not necessarily more *pressure*. Longer pre-infusion, bloom phases, or longer ratios can achieve this at lower pressure with better results.

### "9 bar is always correct for traditional espresso"
9 bar was optimized for medium-roast Italian blends. The specialty coffee world works with a much wider range of roasts and processing methods. 9 bar is the starting point, not the destination.

### "More pressure = more crema = better shot"
Crema is CO2 + oils emulsified by pressure. More crema doesn't mean better extraction — it just means more gas and oil in suspension. Some of the best-tasting shots (turbo, allongé) have minimal crema.

---

## Sources & Further Reading

- **Scott Rao** — Blooming espresso profiles, allongé extraction, and high-extraction-yield research (scottrao.com)
- **James Hoffmann** — "Understanding Espresso" series: pressure physics, channeling, and why puck degradation matters
- **Lance Hedrick** — Flow profiling over pressure profiling, turbo shots, and the case against fixed 9-bar extraction
- **Jonathan Gagné** — "The Physics of Filter Coffee" and espresso viscosity research (coffeeadastra.com)
- **Decent Espresso Community** — Empirical pressure profiling data across hundreds of coffees and profiles
- **Hendon et al.** — Research showing 6-bar shots achieve higher extraction yields than 9-bar at equivalent grind settings
- **Seven Miles Coffee** — Controlled experiments at 6, 9, and 12 bar showing flow rate peaks at 9 bar

---

*For the actionable pressure matrix, shot style parameters, and decision framework, see [`../PRESSURE_GUIDE.md`](../PRESSURE_GUIDE.md). For profile creation, see [`../GAGGIMATE_PROFILE_CREATION_GUIDE.md`](../GAGGIMATE_PROFILE_CREATION_GUIDE.md).*
