# Extraction Science — Deep Reference

> *Quick reference: For actionable tables (grinder-profile mapping, channeling prevention, pre-infusion mechanics, freshness guidance, visual diagnosis), see [`../EXTRACTION_SCIENCE.md`](../EXTRACTION_SCIENCE.md).*

---

## TDS & Extraction Yield

Two numbers that describe every coffee beverage: how strong it is, and how much of the coffee was dissolved.

### Total Dissolved Solids (TDS)

TDS measures **concentration** — what percentage of your beverage is dissolved coffee solids vs. water.

| Brew Method | Typical TDS Range |
|-------------|-------------------|
| Filter/pour-over | 1.15–1.45% |
| Espresso | 7–14% |

Espresso is roughly 10x more concentrated than filter coffee. This is why a 36g espresso shot has as much "coffee" in it as a 200g pour-over.

### Extraction Yield (EY)

Extraction yield measures **completeness** — what percentage of your dry coffee grounds ended up dissolved in the beverage.

**The formula:**

```
Extraction Yield % = (Beverage Weight × TDS%) ÷ Dose Weight
```

**Example:** 18g dose → 36g shot at 10% TDS = (36 × 0.10) ÷ 18 = **20% EY**

### Target Ranges by Shot Style

| Style | Extraction Yield | TDS | Notes |
|-------|------------------|-----|-------|
| Traditional espresso | 18–22% | 8–12% | Classic balance |
| Turbo shot | 19–24% | 6–9% | Higher EY, lower concentration |
| Allongé | 22–27% | 5–8% | Filter-like clarity, high EY |
| Filter coffee | 18–22% | 1.15–1.45% | Reference point |

Scott Rao's perspective: "You've probably never had an overextracted espresso." True overextraction (26%+ EY) is difficult to achieve accidentally — most "bitter" shots are actually channeled, not overextracted.

### Concentration vs. Extraction: The Key Distinction

The same extraction yield can produce very different TDS values depending on your brew ratio:

| Dose | Yield | Ratio | TDS | Extraction Yield |
|------|-------|-------|-----|------------------|
| 18g | 36g | 1:2 | 10% | 20% |
| 18g | 54g | 1:3 | 6.7% | 20% |
| 18g | 72g | 1:4 | 5% | 20% |

All three shots extract the same percentage of the coffee — but they taste completely different because concentration affects perceived intensity, body, and balance.

**Practical implication:** If your shot tastes weak but not sour (adequate extraction, low concentration), shorten your ratio. If it tastes sour AND weak (low extraction, low concentration), grind finer and possibly shorten your ratio.

### Which Variables Move Extraction Yield Most

Ranked by impact (most → least):

1. **Grind size** — The biggest lever. Finer = more surface area = more extraction
2. **Contact time** — Longer extraction = more dissolved
3. **Temperature** — Higher temp = faster extraction kinetics
4. **Pressure** — Affects flow dynamics more than extraction directly; lower pressure with longer time can match higher pressure extraction

### The Brewing Control Chart

Developed by Ernest Earl Lockhart at the Coffee Brewing Institute (MIT, 1957), the original Brewing Control Chart plots TDS (vertical) against extraction yield (horizontal), with diagonal lines showing brew ratio.

The chart divides into quadrants:
- **Upper left:** Strong but under-extracted (sour, intense)
- **Upper right:** Strong and well-extracted (ideal zone for espresso)
- **Lower left:** Weak and under-extracted (sour, thin)
- **Lower right:** Weak but well-extracted (filter-like)

The SCA "ideal zone" for filter coffee (1.15–1.35% TDS, 18–22% EY) doesn't directly apply to espresso — espresso operates in a completely different region of the chart with much higher TDS.

### Refractometers: When Useful, When Overkill

A refractometer measures TDS by shining light through a coffee sample and measuring how much it bends (refractive index).

**Common options:**
- **VST Coffee Lab III** (~$700) — Industry standard, extremely accurate
- **DiFluid R2 Extract** (~$200) — Comparable accuracy, much more affordable, no lid needed
- **Atago** (~$300–500) — Good accuracy, common in cafes

**When a refractometer is useful:**
- Diagnosing whether "bad" shots are under-extracted vs. channeled vs. under-concentrated
- Comparing extraction efficiency between different profiles or grinders
- Tracking extraction yield when dialing in a new coffee
- Research and experimentation

**When it's overkill:**
- Daily home brewing once you're dialed in
- If you trust your palate and shot times are consistent
- If you're not interested in the numbers — taste is what matters

**Measurement protocol (simplified):**
1. Calibrate with distilled water at room temperature
2. Let espresso cool for 1 minute, stir gently
3. Filter the sample (reduces error from suspended particles)
4. Apply small amount to refractometer, wait for stable reading
5. Take the stable number — don't average multiple readings

---

## Grind Science

Your grinder determines your espresso potential more than any other piece of equipment except the beans themselves.

### Particle Size Distribution

When coffee is ground, it doesn't produce uniform particles. Every grinder produces a distribution of sizes — some fine particles (fines), some large particles (boulders), and various sizes in between.

**Key terms:**
- **Unimodal distribution:** Single peak — most particles are similar size
- **Bimodal distribution:** Two peaks — distinct populations of fines and larger particles
- **Uniformity:** How tight the distribution is around the peaks

At espresso settings, both flat and conical burrs produce bimodal distributions — the question is how pronounced the two peaks are and how much overlap exists between them.

### Conical vs. Flat Burrs

Burr shape is commonly used as a proxy for fines content — conical burrs tend to produce more fines; flat burrs tend to produce fewer. This is a tendency, not a deterministic rule: geometry varies significantly within each category.

| Burr Type | Particle Distribution | Cup Character (tendency — contested; burr set matters) | Forgiveness |
|-----------|----------------------|-------------------------------------------------------|-------------|
| **Conical (high-fines)** | More bimodal, more fines | Fuller body, texture, sweetness | More forgiving of prep |
| **Flat (lower-fines)** | More unimodal, fewer fines | More clarity, uniformity, brightness | Rewards precise prep |

**Why this matters for profiles:**
- High-fines grinders (many conical designs, and some flat designs) produce more fines → may benefit from slightly lower extraction pressure to avoid over-compacting fines
- Low-fines / unimodal grinders can handle higher pressure more consistently because the particle bed is more uniform

Jonathan Gagné's research found that "more unimodal grinders require a much finer average grind size when pulling a shot of espresso" — the lack of fines means you need more total surface area to achieve adequate extraction.

> *For your grinder's specific settings and burr character, see the active grinder's reference (per the Grinder field in `user-setup.md`).*

### The Role of Fines

Fines (particles below ~50–100 microns) play a dual role in espresso:

**The good:**
- Provide essential extraction surface area — espresso extraction time is too short for large particles to extract via diffusion
- Fill gaps between larger particles, creating consistent flow resistance
- Contribute to body, crema, and mouthfeel

**The bad:**
- Extract almost instantly → risk of over-extraction and bitterness
- Migrate during extraction (see Channeling section below)
- Can form a dense layer at the puck bottom, causing uneven flow

Scott Rao notes that "the happy medium amount of fines for a given brewing situation is the amount that minimizes astringency." The goal isn't zero fines — it's the right amount for your grinder, dose, and pressure profile.

### Grind Retention and Shot-to-Shot Consistency

**Retention** = coffee grounds that stay in the grinder between doses (in the burrs, chamber, and chute).

**Exchange** = the portion of your current dose that's actually stale grounds from previous grinds.

High retention → high exchange → stale grounds mixing with fresh → inconsistent shots.

**Retention varies significantly by grinder design** — from under 0.5g on low-retention designs to several grams on traditional home grinders. Check the active grinder's reference for the specific figure. Regardless, the mitigations are:
- Purge a small amount before your first shot of the day (amount depends on your grinder's retention)
- Brief purge if changing beans
- Single-dosing helps (weigh beans in, expect slight retention loss)

---

## Channeling Physics

### The Positive Feedback Loop

Channeling occurs when water finds a path of least resistance through the coffee bed and preferentially flows through that path.

**The mechanism:**
1. Water encounters a weak spot (low density, crack, void)
2. More water flows through the weak spot (path of least resistance)
3. The increased flow erodes coffee from the channel walls
4. The channel widens, reducing resistance further
5. Even more water flows through → cycle repeats

**The result:** Simultaneous over-extraction (in the channel) and under-extraction (everywhere else). This is why channeled shots taste both sour AND bitter — you get the worst of both worlds.

Jonathan Gagné describes this as: "Flow and extraction widen the initial disparity in flow between regions due to a positive feedback loop, in which more flow leads to more extraction, which in turn reduces resistance and leads to more flow."

### Fines Migration

During extraction, water physically moves fine particles through the coffee bed.

**What happens:**
1. Fines are small enough to flow with the water
2. They migrate downward, accumulating at the bottom of the puck
3. This creates a dense "compact layer" at the filter basket
4. The compact layer has uneven density → creates preferential flow paths → channels

**How pressure affects it:**
- Higher pressure → faster water velocity → more fines movement
- Lower pressure → gentler extraction → less fines migration
- This is one reason turbo shots (low pressure, coarse grind) are more forgiving

---

## CO2, Freshness, and Degassing

Fresh-roasted beans contain significant CO2 from the roasting process.

**The freshness curve:**
- First 24 hours: ~40% of CO2 escapes
- Days 1–7: Rapid degassing continues
- Days 7–14: Degassing slows; beans enter "sweet spot" for espresso
- Days 14–30: Flavor develops, CO2 stabilizes
- After 30 days: Gradual staling begins (oxidation)

**Why CO2 matters for espresso:**
- Gas trapped in the puck creates voids and bubbles
- These bubbles interrupt water-coffee contact → uneven extraction
- Gas pockets can become preferential flow paths → channeling
- Excess CO2 produces aggressive, unstable crema that masks flavor

Light roasts degas more slowly than dark roasts (denser structure retains gas longer), so they may need longer rest periods or extended bloom phases.

> *For comprehensive freshness management — peak flavor windows, storage methods, and freezing protocols — see `../BEAN_FRESHNESS_AND_STORAGE.md`.*

---

## Sources

**TDS & Extraction Yield:**
- [Towards a Common Coffee Control Chart](https://www.baristahustle.com/towards-a-common-coffee-control-chart/) — Barista Hustle
- [The 2:1 Ratio](https://www.scottrao.com/blog/2017/12/17/the-21-ratio) — Scott Rao
- [Measuring and Reporting Extraction Yields](https://coffeeadastra.com/2019/02/17/measuring-and-reporting-extraction-yields/) — Coffee ad Astra
- [Coffee Refractometer Accuracy: DiFluid R2 vs VST](https://medium.com/data-science/coffee-refractometer-accuracy-vst-vs-difluid-r2-304036bc55f6) — Robert McKeon Aloe

**Grind Science:**
- [What I learned from analyzing 300 particle size distributions for 24 espresso grinders](https://coffeeadastra.com/2023/09/21/what-i-learned-from-analyzing-300-particle-size-distributions-for-24-espresso-grinders/) — Coffee ad Astra
- [The happy medium amount of fines](https://www.scottrao.com/blog/happymediumfines) — Scott Rao
- [Fines: Fine for Espresso, Not So Fine For Filter](https://www.scottrao.com/blog/2017/8/27/fines-fine-for-espresso-not-so-fine-for-filter) — Scott Rao
- [Pulling Low-Fines Espresso Shots](https://coffeeadastra.com/2021/04/14/pulling-low-fines-espresso-shots/) — Coffee ad Astra

**Channeling & Physics:**
- [Extraction Uniformity and Channeling](https://coffeeadastra.com/2019/10/04/extraction-uniformity-and-channeling/) — Coffee ad Astra
- [The Physics of Fines Migration](https://coffeeadastra.com/2020/02/01/the-physics-of-fines-migration/) — Coffee ad Astra
- [A Study of Espresso Puck Resistance and How Puck Preparation Affects it](https://coffeeadastra.com/2021/01/16/a-study-of-espresso-puck-resistance-and-how-puck-preparation-affects-it/) — Coffee ad Astra
- [The Physics of Espresso](https://www.scottrao.com/products/poe) — Jonathan Gagné (via Scott Rao)

**CO2 & Freshness:**
- [Coffee Degassing Explained: Why Fresh Beans Need Time to Rest](https://berto-online.com/the-science-of-coffee-degassing-understanding-its-impact-on-flavor/) — Berto
- [Espresso De-gassing](https://blog.bluebottlecoffee.com/posts/what-is-espresso-degassing) — Blue Bottle Coffee

---

*This document covers the deep "why" of extraction. For actionable tables and quick reference, see [`../EXTRACTION_SCIENCE.md`](../EXTRACTION_SCIENCE.md). For practical guidance on adjustments, see [`../ESPRESSO_BREWING_BASICS.md`](../ESPRESSO_BREWING_BASICS.md).*
