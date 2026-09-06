# Espresso Brewing — Deep Reference

Shot styles, extraction theory, dialing-in methodology, and advanced techniques. For the quick-reference version used during dialing-in, see `knowledge/ESPRESSO_BREWING_BASICS.md`.

---

## Extraction Basics

Espresso extraction happens in stages:

1. **First out:** Acids (fruity, sour notes)
2. **Middle:** Sugars, oils (sweetness, body)
3. **Last out:** Bitter compounds, plant fibers (bitterness, astringency)

**Under-extraction** = stopped too early -> sour, thin, lacking sweetness
**Over-extraction** = went too far -> bitter, dry, astringent
**Good extraction** = balanced -> sweetness present, pleasant acidity, hint of bitterness for depth

> *For the science behind extraction (TDS, extraction yield, grind physics), see `EXTRACTION_SCIENCE.md`*

---

## Shot Styles Overview

### Traditional Espresso
- **Pressure:** 9 bar
- **Grind:** Fine
- **Ratio:** 1:2
- **Time:** 25-35 seconds
- **Character:** Full body, syrupy, classic espresso
- **Best for:** Medium-dark roasts, balanced everyday espresso

### Turbo Shot
- **Pressure:** ~6 bar (naturally low from coarse grind)
- **Grind:** Coarser (medium-fine; noticeably coarser than your traditional setting — consult your grinder's reference for the expected step count)
- **Ratio:** 1:2.5 to 1:3 (longer ratio is essential — coarse grind + short time needs more water for adequate extraction)
- **Time:** 10-20 seconds
- **Temperature:** 96C (high temp compensates for short contact time)
- **Character:** Sweeter, more clarity, less body
- **Best for:** Light-medium roasts, showcasing origin character
- **Why it works:** Coarser grind + lower pressure = more even extraction, less channeling
- **Milk pairing:** Turbo's lighter body can get lost in large milk drinks. Pair with cortado, piccolo, or flat white rather than full lattes

### Allonge
- **Pressure:** 9 bar (or declining)
- **Grind:** Slightly coarser than traditional
- **Ratio:** 1:3 to 1:5
- **Time:** 25-40 seconds
- **Character:** Lighter body, bright, fruit-forward
- **Best for:** Light roasts, highlighting origin character

### SOUP (Spro Only Un-Pressurized)
- **Pressure:** <2 bar (often <1 bar)
- **Grind:** Very coarse (near filter grind)
- **Ratio:** 1:3 to 1:8
- **Time:** Fast flow after full saturation
- **Character:** Tea-like, juicy, extreme clarity
- **Best for:** Ultra-light roasts, filter-style flavor in concentrated form
- **Key technique:** Gentle soak until puck fully saturated, then fast flow

### Ristretto
- **Pressure:** 9 bar (same as traditional)
- **Grind:** Finer than traditional (to maintain resistance with less water)
- **Ratio:** 1:1 to 1:1.5
- **Time:** 15-20 seconds
- **Character:** Intense, syrupy, concentrated, heavy body
- **Best for:** Dark roasts, milk drinks where you want the coffee to punch through, or when you prefer maximum intensity
- **Key difference from traditional:** Same profile shape and pressure — a ristretto is a recipe adjustment (shorter ratio, finer grind), not a distinct extraction style. Use the Classic 9-Bar or Milk Drink Base profile and simply set a shorter volumetric stop.

### Lungo vs Allonge

A **lungo** ("long" in Italian) is often confused with an allonge, but they're different approaches:

- **Lungo:** More water pushed through the same puck at the same grind setting. The extra volume comes from extended extraction time, which pulls increasingly bitter compounds. The result is a larger, weaker drink that's often harsh — it's over-extraction by default. Not recommended as a deliberate strategy.
- **Allonge:** A properly engineered extended extraction. The grind is adjusted coarser, pressure is often lower (6 bar), and the longer ratio (1:4-1:5) is *designed for* from the start. The result is a sweet, tea-like drink with high extraction yield but no harshness, because the coarser grind and lower pressure prevent over-extraction of bitter compounds.

If someone asks for a "lungo," what they usually want is an allonge — or an Americano (espresso + hot water), which achieves volume without over-extraction.

---

## Pre-Infusion & Pressure Phases

Modern espresso benefits from phased extraction:

### Pre-Infusion (Saturation Phase)
- **Pressure:** 1-3 bar (below 4 bar to avoid puck compression)
- **Purpose:** Evenly wet the puck, allow CO2 to escape
- **Duration:** 3-10 seconds depending on freshness
- **Why it matters:** Prevents channeling, enables more even extraction

### Ramp / Main Extraction
- **Pressure:** Build to target (6-9 bar depending on roast, processing, and shot style)
- **Transition:** Linear or ease-in works well
- **Purpose:** Main extraction of flavor compounds
- See `PRESSURE_GUIDE.md` for the full roast x processing pressure matrix

### Decline / Taper (Optional)
- **Pressure:** Reduce toward end of shot
- **Purpose:** Reduces harsh late-extraction bitterness
- **When to use:** Dark roasts, shots tasting harsh at the end

**Key insight (from Lance Hedrick):** The puck compresses at ~4 bar. Pre-infusion should stay below this to achieve proper saturation. Above 10 bar causes secondary compression issues.

---

## Dialing-In Process

Dialing in is the iterative process of adjusting variables until a coffee tastes its best. It's not a failure state — it's the normal path to great espresso. Every new bag requires it. Most coffees take 3-5 shots to dial in; the first shot is calibration, not a finished product.

### Starting Point Strategy

There are two schools of thought on where to begin:

**Start coarse, go finer (Hoffmann approach):** Begin with a grind that's clearly too coarse. The shot runs fast and sour. Grind finer in small steps until the shot slows to the target range and sourness resolves. *Advantage:* Less waste of good coffee (fast shots use less). Easier to identify the correct zone by approaching from one direction.

**Start in the middle (La Marzocco / Rao approach):** Set grind to a known starting point (from your grind map or grinder reference), pull a shot, and adjust based on taste. *Advantage:* Faster when you have historical data for similar coffees.

**Recommendation for home baristas with Gaggimate:** If you have a grind-map entry for a similar coffee, start there (adjusting for freshness). If not, start slightly coarser than your best guess — it's easier to diagnose an under-extracted shot than an over-extracted one, and you waste less coffee on fast shots.

### The Iteration Loop

The core loop is simple: **pull -> taste -> evaluate -> adjust one variable -> repeat.**

1. Pull a shot with your starting parameters
2. Taste it (let it cool to ~50C for best evaluation — see `ESPRESSO_TASTING_GUIDE.md`)
3. Identify the primary issue (sour, bitter, or balanced but lacking something)
4. Adjust **one variable** in the appropriate direction
5. Pull again and compare

**Realistic expectations:**
- **Shot 1:** Calibration. Tells you which direction to go. Rarely good.
- **Shots 2-3:** Narrowing in. Major improvements happen here.
- **Shots 4-5:** Fine-tuning. Diminishing returns set in.
- **Beyond shot 5:** You're chasing the last 10%. A 4-star shot taken to 5 stars takes disproportionate effort — and the difference is often subjective.

### The Salami Shot Technique

A diagnostic tool for understanding what your profile is doing at each stage of extraction. Named because you "slice" the shot into segments.

**How to do it:**
1. Place 3 small cups in a row
2. Pull your normal shot, switching cups every ~8-10 seconds
3. Taste each cup separately

**What each phase reveals:**

| Cup | Timing | Expected Taste | What It Tells You |
|---|---|---|---|
| Cup 1 (early) | 0-10s | Intense, sour, concentrated | Pre-infusion and early extraction — acids dominate |
| Cup 2 (middle) | 10-20s | Sweet, balanced, best flavor | The "sweet spot" — sugars and oils at their peak |
| Cup 3 (late) | 20-30s+ | Weak, bitter, thin | Late extraction — bitter compounds, diminishing returns |

**Interpretation:**
- If cup 1 is overwhelmingly sour -> pre-infusion needs more time or bloom
- If the sweet spot (cup 2) is very narrow -> extraction is uneven; improve puck prep or add bloom
- If cup 3 turns bitter very quickly -> add a pressure decline phase or cut the shot earlier
- If all cups taste similar -> extraction is very even (good sign); adjust recipe rather than profile

**When to use it:** When you're fine-tuning a profile and want to understand *where* in the extraction the problems are. Not for daily use — it's a diagnostic, not a routine.

> *For detailed profile modification based on salami shot findings, see the Taste-Driven Profile Tuning section in `PROFILE_CREATION_REFERENCE.md`*

### Managing Multiple Coffees

If you rotate between different bags:

- **Record everything** in your `grind-map.md` — coffee, grind setting, profile, ratio, temperature, days off roast, rating
- **When returning to a coffee**, check your grind map and adjust for freshness: fresher beans (fewer days off roast) typically need a slightly coarser grind — CO2 adds puck resistance, so compensate to hit target time
- **Purge grinder retention** when switching coffees — run 2-3g through to clear the old grounds. Even with low-retention grinders, stale grounds from a previous coffee will affect the first shot
- **Don't compare across coffees** — a grind setting that works for one bean won't work for another, even at the same roast level. Origin, variety, density, and processing all affect extraction

### When to Abandon an Approach

Sometimes the right move is to stop iterating and try something fundamentally different:

**Signs it's time to change approach:**
- 6+ shots with no meaningful improvement
- Persistent sour AND bitter (channeling that puck prep can't fix)
- Good shots but wildly inconsistent (may indicate equipment issues)
- The coffee just doesn't taste like the roaster's tasting notes at all

**What to try instead:**
1. **Different profile style** — switch from traditional 9-bar to turbo, or from flat pressure to bloom
2. **Cup the beans** — brew as filter (or dilute espresso 1:1 with hot water) to check if the beans themselves have issues. If filter tastes good but espresso doesn't, the problem is the espresso recipe
3. **Check the grinder** — burrs may need cleaning or alignment; clumping causes channeling
4. **Verify freshness** — beans >4-5 weeks off roast lose volatile aromatics and produce flat, papery shots
5. **Check water quality** — metallic or flat-tasting shots across all coffees suggest water issues (ideal: 75-250 ppm TDS, zero iron, pH 6.5-7.5)

---

## Common Mistakes

1. **Changing multiple variables at once** — Can't isolate what helped
2. **Ignoring pre-infusion** — Leads to channeling, especially with fresh beans
3. **Same settings for all coffees** — Different origins/roasts need different approaches
4. **Judging turbo shots by traditional standards** — Less body is expected, judge on clarity
5. **Volumetric stops without scale** — Use water-pumped stops if no Bluetooth scale

---

## Equipment Notes (GaggiaMate Specific)

### Stop Conditions
- **Volumetric** — Requires Bluetooth scale; most accurate
- **Water pumped** — Works without scale; needs calibration (coffee absorbs ~25-30ml)
- **Time-based** — Least accurate but always works

### Profile Phases
- Use **flow control** for pre-infusion (prevents channeling better than pressure control)
- Use **adaptive transitions** to respond to actual puck resistance
- Add **decline phase** for dark roasts or harsh finishes

---

## Sources & Resources

**Key sources for this guide:**
- Lance Hedrick: [Why your Coffee is Sour or Bitter (and how to fix it)](https://www.youtube.com/watch?v=Z2zsmehysHk) — 5g adjustment rule, extraction timeline, dark roast fines insight
- Scott Rao: [Best Practice Espresso Profile](https://www.scottrao.com/blog/2021/5/18/best-practice-espresso-profile) — Blooming technique, "sour AND bitter = channeling" diagnostic, salami shot analysis
- James Hoffmann: [The Ultimate Espresso Dial-In](https://www.youtube.com/watch?v=aTFaoYT03mE) — Start coarse approach, realistic expectations
- Barista Hustle: [The Espresso Compass](https://www.baristahustle.com/the-espresso-compass/) — Matt Perger's extraction/strength diagnostic framework
- Barista Hustle: [Extract More Better](https://www.baristahustle.com/extract-more-better/) — Diminishing returns of grinding finer, channeling as extraction ceiling
- La Marzocco: [Dialing In: How to Reduce Your Sink Shots](https://home.lamarzoccousa.com/dialing-in-how-to-reduce-your-sink-shots-and-still-make-a-beautiful-espresso/) — Practical home barista methodology

**Further learning:**
- **Lance Hedrick YouTube** — Excellent visual guides on extraction theory
- **Espresso Aficionados Discord** — Community knowledge, turbo/SOUP guidance
- **Barista Hustle** — In-depth extraction science
- **GaggiaMate Docs** — https://docs.gaggimate.eu/
