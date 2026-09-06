# Special Categories: Decaf & Blends

Extraction strategies for decaffeinated beans and espresso blends.

> **Deep dive:** Decaffeination science, process comparisons, blend philosophy, and SO vs blend analysis in [`reference/SPECIAL_CATEGORIES_REFERENCE.md`](reference/SPECIAL_CATEGORIES_REFERENCE.md).

---

## Decaf Espresso

### Extraction Adjustments for Decaf

Decaf's higher porosity and lower density mean it needs a gentler approach across the board:

| Variable | Regular Espresso | Decaf Adjustment | Why |
|----------|-----------------|-----------------|-----|
| **Grind** | Your baseline | Substantially FINER (often several steps) | Porous, brittle structure offers less flow resistance — at your regular setting the puck gushes; grind finer to rebuild resistance |
| **Temperature** | Per roast level | Start AT baseline; raise 1–2°C if sour | Published guidance is split — Swiss Water says 93±3°C; the specialty-espresso camp runs decaf hot (94–96°C, especially lighter roasts). In practice SWP decaf under-extracts to sour far more readily than it over-extracts to bitter: treat heat as an extraction lever, not a hazard. (On-machine: a 75% SWP blend improved monotonically from 89.7→93.3°C effective, shots 527–537, Jul 2026) |
| **Pressure** | Per matrix | -1 to -2 bar | Less force needed; reduces harsh extraction |
| **Ratio** | Per style | Same or slightly longer (1:2.5) | Longer ratio develops sweetness in a less complex cup |
| **Pre-infusion** | Standard | Shorter (3–5 seconds) | Porous puck saturates faster |
| **Dose** | = basket size | Same (never underdose) | Porosity means the basket may look fuller — trust the scale |

**Expect:** Decaf shots flow *noticeably* faster at the same grind setting — the decaffeination soak weakens the cellulose matrix, so the puck offers far less flow resistance. Start a few steps **finer** than your regular setting and let the shot timer set the magnitude; large corrections (3+ steps) are common. Don't confuse the two decaf adjustments: lower temp/pressure manages decaf's *fast flavor extraction*; finer grind manages its *low flow resistance*. (Directionally confirmed on-machine: a ~75% Swiss Water blend at a regular coffee's setting ran 42g in 15s at ≤7 bar — shot 523, Jul 2026.)

### Profile Recommendations

| Profile | Suitability | Notes |
|---------|------------|-------|
| **Soak-start + moderate peak + long decline** | Excellent (field-proven) | Gentle fill → 5–6s pump-off **saturation rest** → ease-in to 7–7.5 bar → linear decline, 1:2.5. The rest phase does nothing for degassing (decaf has no CO2) but structurally wets and consolidates a fines-heavy puck before pressure arrives — it measurably stabilized pucks ground near the fines threshold (Jul 2026, 75% SWP blend, shots 534 vs 536/537) |
| **Dark Roast Gentle** | Excellent | Low pressure (6–7 bar) + decline matches decaf's needs |
| **Classic 9-Bar** (modified) | Good | Reduce to 7–8 bar; shorten pre-infusion |
| **Bloom Profile** | Reframe, don't skip | The pause has no CO2 to release — but keep it 5–6s as a *saturation rest* (see top row); don't slam pressure into a decaf puck |
| **Turbo** | Avoid | Decaf's porosity + coarse grind + low pressure = nearly zero resistance; shot will gush |

**When the puck can't supply classic resistance (decaf-heavy blends):** expect the resistance-vs-grind curve to peak *well before* the collar's fine limit and then invert — past the fines threshold, extra fines fracture the puck instead of packing it (grind-response mapping, Jul 2026: resistance doubled from the regular-coffee setting to ~5 marks finer, peaked, then *fell* at the extreme). Once grind peaks, stop grinding: get contact time from pump-side flow limits or declining profiles, get extraction from temperature (see row above) and ratio (1:2.5), and never chase gauge pressure — a decaf shot's quality lives in contact time × heat, not bar.

### Why Decaf Tastes "Flat" (And How to Fix It)

| Problem | Cause | Fix |
|---------|-------|-----|
| Hollow, lifeless cup | Over-extraction from standard settings | Coarser grind, lower temp, lower pressure |
| No sweetness, all bitterness | Stale beans (decaf stales 2x faster) | Buy fresher; use within 1–2 weeks of roast |
| Cardboard/papery notes | Old beans or MC processing | Try SWP or EA process from a specialty roaster |
| Thin body, watery | Insufficient dose or channeling | Maintain full dose; improve puck prep |
| Bland, no character | Poor-quality green coffee decaffeinated | Seek specialty-grade decaf (EA or SWP from named farms) |

**The freshness rule:** Decaf should be treated as **one freshness tier more urgent** than the equivalent regular coffee. If a medium roast peaks at 10–21 days, aim to use decaf medium roast within 7–14 days.

> *For freshness timelines and storage, see `BEAN_FRESHNESS_AND_STORAGE.md`.*

---

## Espresso Blends

### Temperature Compromise Strategies

Blends often mix roast levels, creating an extraction dilemma — dark components extract faster than light ones at any given temperature.

| Blend Composition | Temperature Strategy | Target | Why |
|-------------------|---------------------|--------|-----|
| Mostly dark + some medium | Target the dark: 89–91°C | Protect the majority from bitterness | Small medium component adds subtle brightness |
| Even dark/medium split | Split the difference: 91–92°C | Neither perfect, both acceptable | Best overall balance |
| Mostly medium + some light | Target the medium: 92–93°C | Medium is the backbone flavor | Light component adds complexity |
| Single roast level | Match to roast level directly | No compromise needed | Easier to dial in |

**Key insight:** Post-blend roasting (all components together) eliminates the mixed-extraction problem. Pre-blend roasting gives more flavor control but creates the challenge. Most specialty blends are post-blended.

### Blend Archetypes

**Italian Traditional** — Dark chocolate, toasted nuts, heavy body, bittersweet finish
`88–91°C, 8–9 bar, 1:1.5–1:2 | Classic 9-Bar or Lever Decline | Straight espresso, cappuccino, latte`

**Australian** — Balanced, medium body, caramel sweetness, approachable
`91–93°C, 9 bar, 1:2 | Classic 9-Bar | Flat white, long black, milk drinks`

**Nordic / Third Wave** — Lighter, origin-forward, seasonal, more acidity, complex
`93–95°C, 8–9 bar, 1:2–1:2.5 | Bloom or gentle ramp | Cortado, flat white, straight`

### Extraction Tips for Blends

1. **Start with the roaster's recommendations.** Blends are designed for a specific approach — the roaster's suggested dose, ratio, and temp are usually well-tested.
2. **Default to 1:2 ratio at the roast-level temperature.** Blends are more forgiving of the classic approach than most single origins.
3. **If the blend has named origins, look them up.** Knowing the components helps you understand what to emphasize.
4. **Blends age more gracefully.** Multiple components mean that as one fades, others may still be contributing.
5. **Pressure profile matters less.** Standard 9-bar flat profiles work well for most blends.

---

*For temperature guidelines by roast level, see `ESPRESSO_BREWING_BASICS.md`. For pressure selection by processing method, see `PRESSURE_GUIDE.md`.*
