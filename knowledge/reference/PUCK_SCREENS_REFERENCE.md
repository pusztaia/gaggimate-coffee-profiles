# Puck Screens — Deep Reference

> *Quick reference: For the at-a-glance summary used during dialing-in, see [`../PUCK_SCREENS.md`](../PUCK_SCREENS.md).*

A puck screen is a thin perforated metal disc placed on top of the coffee puck, between the puck surface and the group head's shower screen. This deep reference covers the physics behind the most consequential effect — heat transfer at the puck surface — and the temperature compensation guidance that follows from it.

---

## Heat-Buffer Physics

A puck screen is, before anything else, a piece of cold metal sitting between hot brew water and the coffee puck. Its presence changes the thermal boundary condition at the puck surface in ways that matter for extraction.

### Why screens steal energy from the puck surface

When water leaves the shower screen at brew temperature and contacts a cold metal disc, the screen acts as a heat sink. The first millilitres of water passing through the screen lose energy to the screen's thermal mass before they ever reach the coffee. The cooling-on-contact effect is largest at the very start of the shot, when:

1. The temperature gradient between water and screen is largest.
2. The puck has not yet been pre-wetted, so the surface layer of grounds depends entirely on incoming water temperature for its own heating.
3. Pre-infusion flow rates are low, giving each parcel of water more contact time with the cold surface to give up energy.

The result is a measurable temperature drop in the water that arrives at the puck surface, relative to the temperature delivered by the group head. The puck surface — the layer that controls early-shot wetting and where channels are seeded — is the part of the bed that gets the cold water first.

### Thermal mass scales with thickness, not vendor

The energy a screen can absorb is proportional to its mass, which for a fixed disc diameter (58mm or 58.5mm) scales linearly with thickness. Material differences within the stainless-steel family (304 vs 316) are minor compared to thickness; only the thickness *class* drives behavior.

The practical consequence is that the temperature compensation a screen needs is governed by **how thick** it is, not by who made it or what coating it carries. Vendor specifications drift over time and across product revisions; thickness class does not.

### Why preheating helps

Preheating the screen — typically by locking it into the portafilter during the flush, or by sitting it on the group head warm-up — closes the temperature gap between the screen and the brew water. A preheated screen still has the same thermal mass, but if it starts at near brew temperature, it absorbs much less energy from the first water that hits it. For thin screens, preheating largely eliminates the need for boiler-temperature compensation. For thick screens, preheating reduces but does not erase the need.

### Why this only matters at the start of the shot

After a few seconds of contact with brew water, the screen reaches thermal equilibrium with the water passing through it and stops acting as a heat sink. Steady-state extraction temperature is unaffected. The heat-buffer effect is a transient — but a transient that happens precisely during the most extraction-sensitive phase of the shot (pre-infusion and early bloom), so its impact on cup quality is disproportionate to its duration.

---

## Temperature Compensation by Thickness Class

Use these numbers as boiler-temperature offsets relative to the temperature you would otherwise set for the same coffee with no puck screen in place.

| Thickness class | Example product range | Preheated? | Suggested boiler offset |
|-----------------|-----------------------|------------|-------------------------|
| **Thin (~0.8mm)** | Normcore 0.8mm round-hole | Yes (locked into PF during flush) | 0°C — no compensation needed |
| **Thin (~0.8mm)** | Normcore 0.8mm round-hole | No | +1°C |
| **Thick (~1.7mm+)** | BPlus and similar heavy screens | Either | +2–3°C |

### How to read the table

- **Thin + preheated = no offset.** This is the default workflow most users should adopt. Preheating costs nothing and removes the variable.
- **Thin + unpreheated = +1°C.** A small but real correction. Use only if you cannot or will not preheat (e.g., you are doing a back-to-back shot session where the screen never cools down anyway, in which case it is effectively preheated already).
- **Thick = +2–3°C.** Thick screens have enough thermal mass that preheating helps but does not eliminate the cold-start drop. Manufacturer guidance for these screens has converged on +2–3°C boiler compensation regardless of preheat state.

### What to do if you are between classes

If the screen sits between the thin and thick classes (e.g., a 1.0–1.4mm screen), use the unpreheated thin value (+1°C) as a floor and adjust upward by taste. A sour, thin shot relative to your no-screen baseline at the same grind and dose suggests under-compensation; nudge by 0.5–1°C and re-pull.

### Why these numbers are conservative

The thin-screen value is derived from community consensus rather than a single controlled measurement; it is intentionally on the smaller side to avoid over-correcting and pushing shots into bitter territory. The thick-screen range is the manufacturer-recommended band for screens in that class, which has been stable across multiple vendors and product generations.

---

## Diagnostic Implications

Because the heat-buffer effect is transient and front-loaded, it presents in the cup as **sourness in the first sip / first half of the shot** rather than as a flat under-extraction across the whole cup. If you taste sourness that resolves as the shot progresses — and you have a puck screen in place that was not preheated — suspect the cold-screen effect before reaching for grind or pressure changes.

Conversely, if a shot tastes uniformly sour from start to finish, the screen is unlikely to be the cause; the diagnosis points to grind, dose, or pre-infusion length instead.

---

## Sources

home-barista.com community threads on screen thickness and preheating; BPlus boiler-compensation guidance for thick screens; Normcore care instructions; Decent Espresso community discussion of screen thermal effects. Vendor-specific marketing claims (extraction yield percentages, channeling reduction percentages, exotic-material conductivity claims) are excluded from this reference because they lack reproducible primary sources.
