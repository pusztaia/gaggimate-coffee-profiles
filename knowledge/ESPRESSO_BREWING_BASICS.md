# Espresso Brewing Basics

Quick reference for core variables, adjustment strategies, and diagnostics during dialing-in.

---

## The Core Variables

Every espresso shot is controlled by these interconnected variables:

| Variable | What it does | Typical range |
|---|---|---|
| **Dose** | Grams of coffee in | 15-22g (match basket size) |
| **Yield** | Grams of espresso out | 30-50g |
| **Ratio** | Dose:Yield relationship | 1:2 to 1:3 |
| **Time** | Extraction duration | 20-35s (varies by style) |
| **Grind** | Particle size | Finer = slower, more extraction |
| **Temperature** | Brew water temp | 88-96°C |
| **Pressure** | Bar during extraction | 6-9 bar (varies by style and processing) |

**Key principle:** Change one variable at a time. If you change grind AND dose AND temperature, you won't know what fixed (or broke) your shot.

---

## Adjustment Strategies

### The 5g Rule (Quick Yield Adjustment)

Before changing grind size, try adjusting your yield:

- **Sour/salty/harsh?** → Increase output by 5g (adds balancing compounds)
- **Bitter/dry/clawing?** → Decrease output by 5g (preserves sweetness, reduces late-extraction bitterness)

This works because extraction is a timeline: acids come out first, then sugars, then bitter compounds. Adjusting yield changes where you "cut" that timeline.

**When to use yield vs grind:**
- Yield adjustment: Quick fix, doesn't require re-dialing shot time
- Grind adjustment: More fundamental change, affects flow rate and total extraction
- Temperature: Fine-tuning after grind is dialed
- Pressure: Style change (turbo vs traditional) or reducing harshness

### Traditional Espresso Adjustments

| Problem | Primary Fix | Secondary Fix |
|---|---|---|
| Sour, thin, fast | Grind finer | Increase temp |
| Sour/salty despite fine grind | Increase yield by 5g | Increase temp |
| Bitter, slow, dry | Grind coarser | Decrease temp |
| Bitter despite coarse grind | Decrease yield by 5g | Add pressure decline |
| Channeling (uneven flow) | Better puck prep | Longer pre-infusion |
| No body despite good taste | Lower pressure or channeling | Check for leaks |

### Turbo/Modern Style Adjustments

| Problem | Primary Fix | Secondary Fix |
|---|---|---|
| Too sour | Longer soak/pre-infusion | Slightly finer grind |
| Too bitter | Coarser grind | Lower pressure |
| Lacking clarity | Coarser grind | Longer ratio |
| Too thin/watery | Finer grind | Shorter ratio |

### Temperature Guidelines by Roast

| Roast Level | Temperature Range |
|---|---|
| Light (Nordic) | 94-96°C |
| Medium | 92-94°C |
| Medium-Dark | 90-92°C |
| Dark | 88-90°C |

**Adjustment rule:**
- Too sour → increase 1-2°C
- Too bitter → decrease 1-2°C

### Why Dark Roasts Taste "Less Acidic"

A common misconception: dark roasts actually contain similar acid levels to light roasts. The difference is perception, not chemistry.

- Dark roast beans are less dense → more beans per 15g dose → similar total acid content
- Dark roasts have more bitter compounds (CGA lactones, phenylindanes) that *mask* the acidity
- Dark roasts are more brittle → produce more fines → contribute gritty, textural bitterness

**Practical implication:** If your dark roast tastes harsh, the bitterness might be from fines, not over-extraction. Try a coarser grind and ensure even distribution.

---

## Ratio Guidelines

| Ratio | Style | Character |
|---|---|---|
| 1:1 to 1:1.5 | Ristretto | Intense, concentrated, heavy |
| 1:2 | Classic | Balanced, full body |
| 1:2.5 to 1:3 | Lungo/Modern | Lighter, more clarity, extended sweetness |
| 1:3+ | Allongé/SOUP | Filter-like clarity, tea-like body |

**When to adjust ratio:**
- Want more intensity → shorter ratio
- Want more clarity/sweetness → longer ratio
- Light roast tasting sour at 1:2 → try 1:2.5 or 1:3

---

## Variable Hierarchy: What to Adjust First

Not all variables have equal impact. Adjust in this order:

| Priority | Variable | Impact | When to adjust |
|---|---|---|---|
| 1 | **Grind size** | Largest effect on extraction | Shot time is far off target, or taste is clearly sour/bitter |
| 2 | **Yield/Ratio** | Quick correction without re-dialing time | Shot time is acceptable but taste is off (use the 5g rule) |
| 3 | **Temperature** | Fine-tuning after grind is close | Grind is dialed but flavor is flat, sharp, or lacking sweetness |
| 4 | **Pressure/Profile** | Style change or enhancement | Fundamentals are working but you want different character |
| 5 | **Puck prep** | Consistency and channeling | Sour AND bitter simultaneously, or inconsistent shots |

**Key principle:** Don't jump to profile tuning when the grind isn't right. Get the basics working first, then refine. A perfect profile can't save a bad grind setting.

---

## Diagnostic Decision Tree

| Symptom | Shot Time | First Check | Second Check | Third Check |
|---|---|---|---|---|
| **Sour + fast** | <20s | Grind finer | — | — |
| **Sour + normal time** | 25-30s | Increase yield by 5g | Increase temp 1-2°C | Add bloom to profile |
| **Sour + slow** | >35s | Likely channeling (see below) | Better puck prep | Longer pre-infusion |
| **Bitter + slow** | >35s | Grind coarser | — | — |
| **Bitter + normal time** | 25-30s | Decrease yield by 5g | Decrease temp 1-2°C | Add pressure decline |
| **Bitter + fast** | <20s | Possible over-roast or water issue | Check bean freshness | Check water quality |
| **Sour AND bitter** | Any | **Channeling** — fix puck prep | Finer grind + longer PI | Check grinder for clumping |
| **Balanced but flat** | 25-30s | Increase temp 1°C | Try longer ratio | Check freshness |
| **Balanced but thin** | 25-30s | Shorter ratio | Finer grind (increase body) | Check for basket leaks |

**Critical insight (Scott Rao):** If your shot tastes **both sour and bitter at the same time**, it's almost certainly channeling — water is finding paths of least resistance, over-extracting some grounds while under-extracting others. The fix is puck prep (WDT, distribution, even tamp), not grind adjustment. Grinding finer when channeling is present makes it worse.

---

## Separating Problems

When a shot isn't right, the challenge is identifying *which* variable is the culprit:

**Is it the grind?**
- Shot time is significantly off target (>5 seconds away)
- Taste matches the time — fast + sour, or slow + bitter
- Fix: Adjust grind, everything else stays the same

**Is it the temperature?**
- Shot time is in range, but flavor is flat, sharp, or lacks sweetness
- Changing grind doesn't improve taste (just makes it faster/slower with the same issues)
- Fix: Adjust temperature 1-2°C in the appropriate direction

**Is it the ratio?**
- Shot time and temperature feel right, but the balance is slightly off
- The 5g rule resolves it quickly
- Fix: Add or subtract 5g from yield

**Is it the profile?**
- Grind and temperature are dialed, shot time is correct, but the coffee feels "incomplete"
- You want more sweetness, different body, or a different character
- Fix: Try a different profile style (bloom, decline, turbo) or tune profile phases

**Is it puck prep?**
- Sour AND bitter simultaneously
- Inconsistent shots (same settings, different results)
- Telemetry shows uneven flow or pressure spikes
- Fix: WDT distribution, even tamp, check for clumps; don't change grind until prep is consistent

---

*For shot styles (traditional, turbo, allongé, SOUP, ristretto, lungo), pre-infusion & pressure phases, dialing-in methodology, salami shot technique, managing multiple coffees, and common mistakes, see `reference/ESPRESSO_BREWING_REFERENCE.md`. For tasting guidance, see `ESPRESSO_TASTING_GUIDE.md`. For profile creation, see `GAGGIMATE_PROFILE_CREATION_GUIDE.md`.*
