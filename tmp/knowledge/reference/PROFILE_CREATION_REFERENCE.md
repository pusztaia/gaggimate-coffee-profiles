# Profile Creation — Deep Reference

> *Quick reference: For JSON schema, pump modes, stop conditions, examples (Classic 9-Bar, Blooming), and best practice tables, see [`../GAGGIMATE_PROFILE_CREATION_GUIDE.md`](../GAGGIMATE_PROFILE_CREATION_GUIDE.md).*

---

## Transition Types — Detailed Examples

### Instant (`"instant"`)
- Immediate jump to new target
- No ramping
- Use for: Phase starts, step changes

```json
"transition": {
  "type": "instant",
  "duration": 0,
  "adaptive": true
}
```

### Linear (`"linear"`)
- Constant rate change
- Predictable, smooth
- Use for: Standard pressure ramps

```json
"transition": {
  "type": "linear",
  "duration": 4,
  "adaptive": true
}
```

### Ease-In (`"ease-in"`)
- Slow start, fast finish
- Gradual pressure build
- Use for: Gentle pre-infusion to main extraction

```json
"transition": {
  "type": "ease-in",
  "duration": 3,
  "adaptive": true
}
```

### Ease-Out (`"ease-out"`)
- Fast start, slow finish
- Smooth pressure decline
- Use for: Tapering at end of shot

```json
"transition": {
  "type": "ease-out",
  "duration": 5,
  "adaptive": true
}
```

### Ease-In-Out (`"ease-in-out"`)
- Slow start and finish, fast middle
- Most natural feeling
- Use for: Complex pressure profiles

```json
"transition": {
  "type": "ease-in-out",
  "duration": 4,
  "adaptive": true
}
```

### Adaptive Behavior

**`adaptive: true`** (Start from current value)
- If Phase 1 targets 3 bar but only reaches 2 bar
- Phase 2 ramps from 2 bar → 7 bar
- More responsive to puck resistance

**`adaptive: false`** (Start from previous target)
- If Phase 1 targets 3 bar but only reaches 2 bar
- Phase 2 ramps from 3 bar → 7 bar
- More predictable, ignores actual performance

---

## Example Profile: Spring Lever Simulation

Declining pressure profile mimicking manual lever machines.

```json
{
  "label": "Cremina Lever",
  "type": "pro",
  "description": "Spring lever-style declining pressure",
  "temperature": 90,
  "phases": [
    {
      "name": "Pre-infusion",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 5,
      "temperature": 0,
      "transition": {
        "type": "instant",
        "duration": 0,
        "adaptive": true
      },
      "pump": {
        "target": "flow",
        "pressure": 9,
        "flow": 3
      }
    },
    {
      "name": "Peak Pressure",
      "phase": "brew",
      "valve": 1,
      "duration": 5,
      "temperature": 0,
      "transition": {
        "type": "linear",
        "duration": 3,
        "adaptive": true
      },
      "pump": {
        "target": "pressure",
        "pressure": 9,
        "flow": 0
      },
      "targets": [
        {
          "type": "pressure",
          "operator": "gte",
          "value": 8.5
        }
      ]
    },
    {
      "name": "Decline",
      "phase": "brew",
      "valve": 1,
      "duration": 30,
      "temperature": 0,
      "transition": {
        "type": "linear",
        "duration": 25,
        "adaptive": true
      },
      "pump": {
        "target": "pressure",
        "pressure": 3,
        "flow": 0
      },
      "targets": [
        {
          "type": "volumetric",
          "operator": "gte",
          "value": 36
        }
      ]
    }
  ]
}
```

---

## Troubleshooting Profiles

### Issue: Shot Channeling

**Symptoms:** Fast flow, under-extracted, sour
**Fixes:**
- Increase pre-infusion duration (5-8 seconds)
- Reduce pre-infusion flow (2-2.5 ml/s)
- Add bloom phase (6-8 seconds soak)

### Issue: Over-Extraction

**Symptoms:** Bitter, harsh, astringent
**Fixes:**
- Reduce temperature (-2°C)
- Shorten extraction time
- Reduce hold phase duration
- Add declining pressure phase

### Issue: Under-Extraction

**Symptoms:** Sour, weak, thin body
**Fixes:**
- Increase temperature (+2°C)
- Extend extraction time
- Increase hold pressure (9 bar)
- Add bloom phase for better saturation

### Issue: Inconsistent Shots

**Symptoms:** Different results with same profile
**Fixes:**
- Use volumetric stop condition (requires scale)
- Enable adaptive transitions
- Add pressure-based stop conditions
- Increase pre-infusion time for consistency

### Issue: Pump Strain / Loud Operation

**Symptoms:** Grinding sounds, pressure spikes
**Fixes:**
- Start with flow mode, not pressure
- Use gentler ramp transitions (ease-in)
- Reduce target pressure to 8-8.5 bar
- Check grind isn't too fine

---

## Advanced Techniques

### Multi-Stage Extraction

Create complex flavor profiles with 5+ phases:

```
1. Fast fill (2s, 4 ml/s) → Saturate quickly
2. Bloom (6s, 0 ml/s) → De-gas, enhance sweetness
3. Ramp (4s, ease-in to 9 bar) → Build pressure gently
4. High pressure (8s, 9 bar) → Extract body
5. Medium pressure (12s, 7 bar) → Extract sweetness
6. Low pressure (8s, 5 bar) → Extract acidity
7. Taper (4s, ease-out to 3 bar) → Smooth finish
```

### Adaptive Flow Profiling

Use adaptive flow for the final phase to automatically adjust to puck resistance:

```json
"pump": {
  "target": "flow",
  "pressure": 9,
  "flow": -1
}
```

This maintains consistent extraction across:
- Different grind settings
- Bean varieties
- Freshness levels

---

## Taste-Driven Profile Tuning

This section covers modifying the *profile itself* based on taste feedback — adjusting phases, transitions, and parameters to shape flavor. This is distinct from adjusting grind, temperature, or ratio, which should be dialed in first.

### When to Tune Profiles vs Other Variables

**Profile tuning is for:** Enhancing specific flavor characteristics once the fundamentals are working — more sweetness, different body, cleaner finish, more complexity.

**Profile tuning is NOT for:**
- Fixing under/over-extraction → adjust grind first (see `../ESPRESSO_BREWING_BASICS.md`)
- Adjusting strength → change ratio
- Fixing channeling → improve puck prep
- Changing overall extraction level → change temperature

**Rule of thumb:** If your shot time is wrong, fix the grind. If your shot time is right but the flavor is off, try temperature and ratio. Only tune the profile after those fundamentals are working.

### Pre-Infusion Flow Rate Tuning

The flow rate during pre-infusion controls how aggressively water saturates the puck. Lower flow = gentler, more even saturation but slower. Higher flow = faster fill but more risk of disturbing the puck.

| Flow Rate | Pressure Generated | Flavor Effect | Best For |
|---|---|---|---|
| **1.5-2.0 ml/s** | Very low (<2 bar) | Ultra-gentle saturation, maximum clarity, most delicate flavor | Very fresh beans, anaerobics, coffees with poor puck integrity |
| **2.0-2.5 ml/s** | Low (2-3 bar) | Even saturation, good sweetness development | Light roasts, naturals, bloom profiles |
| **3.0-3.5 ml/s** | Moderate (3-4 bar) | Standard balance of speed and saturation | Medium roasts, washed coffees, everyday use |
| **4.0-5.0 ml/s** | Higher (approaching 4 bar) | Fast fill, less patient saturation, more body | Dark roasts with good integrity, turbo-style quick wetting |

**If shots taste uneven or channel-prone:** Try reducing pre-infusion flow by 0.5 ml/s. Slower fill gives water more time to distribute evenly through the puck.

**If shots taste flat or over-developed:** Try increasing pre-infusion flow by 0.5 ml/s. Faster fill preserves brightness by spending less time at low extraction temperatures.

### Bloom Duration Tuning

Bloom (a pause after pre-infusion where the pump stops) allows water to fully saturate the puck via capillary action while CO2 escapes. Scott Rao's research with the Decent DE1 showed that bloom increases extraction by 1-1.5% while *simultaneously reducing* astringency and bitterness — more extraction AND less harshness.

| Bloom Duration | Effect | When to Use |
|---|---|---|
| **No bloom (0s)** | Standard extraction; relies on pre-infusion alone for saturation | Dark roasts (highly soluble), well-rested beans (>3 weeks), when maximum body is the goal |
| **Short (5-8s)** | Moderate improvement in saturation; minimal impact on total shot time | Medium roasts, slightly fresh beans, first experiment with bloom |
| **Standard (8-12s)** | Significant improvement in sweetness and clarity; the sweet spot for most coffees | Light-medium roasts, naturals and anaerobics, fresh beans (<14 days) |
| **Long (15-30s)** | Maximum saturation and extraction yield; filter-like character | Ultra-light roasts, pushing extraction above 24-25%, Rao-style blooming profiles |

**When bloom helps most:**
- Natural and anaerobic process coffees (high CO2, intense fermentation compounds)
- Fresh beans (<10 days off roast — need more degassing time)
- Light roasts where sourness persists despite fine grind — bloom may resolve uneven saturation
- Any coffee where you want more sweetness without increasing bitterness

**When bloom may not help:**
- Dark roasts (already highly soluble, extract easily)
- Well-rested beans (>3 weeks, most CO2 already released)
- When you specifically want maximum body — bloom shifts toward clarity

**Risk of too-long bloom:** Heat loss during the pause can flatten the shot. If your bloom profile tastes muted or lacks vibrancy, reduce bloom duration by 3-5 seconds.

### Ramp Speed & Transition Type Effects

How fast pressure rises from pre-infusion to extraction pressure directly affects flavor:

| Transition | Duration | Flavor Effect | Body | Clarity | Best For |
|---|---|---|---|---|---|
| **Instant** | 0s | Aggressive initial extraction, most body, highest channeling risk | Highest | Lowest | Dark roasts with strong puck integrity, maximum body goal |
| **Linear** | 3-5s | Predictable, balanced extraction | High | Moderate | Default choice for most coffees |
| **Ease-in** (slow start, fast finish) | 3-5s | Gentle initial build, reduces puck shock, more sweetness | Moderate | High | Light roasts, channeling-prone coffees, pre-infusion → extraction transition |
| **Ease-out** (fast start, slow finish) | 3-8s | Quick movement with smooth arrival at target | Moderate | Moderate | Decline/taper phases, lever-style profiles |
| **Ease-in-out** | 4-6s | Most natural feeling, layered flavor transitions | Moderate | High | Complex profiles with large pressure changes between phases |

**General principle:** Faster ramps produce more body and intensity. Slower ramps produce more clarity and sweetness. The Decent community's default recommendation is a 3-5 second ease-in ramp for most profiles.

**Channeling risk:** Instant ramps into high pressure are the most common cause of profile-induced channeling, especially with light roasts that have less puck integrity. If you see channeling on telemetry, switching from instant to ease-in is often the first fix.

### Decline Phase: When & How Aggressive

As extraction progresses, the puck erodes — less mass means less resistance. Fixed pressure forces increasing flow through weakening channels. A decline phase compensates for this puck degradation.

**When to add decline:**
- Dark roasts (highly soluble; late-extraction bitterness is the primary risk)
- Natural/anaerobic process coffees (intense compounds that become harsh when over-extracted)
- Any coffee where the shot tastes good initially but the finish is bitter or astringent
- Lever-style profiles for syrupy body and caramel sweetness

**When to skip decline:**
- Turbo shots (too fast for decline to matter; 15-20 second total)
- Light roasts that are hard to extract (you need sustained pressure to reach adequate extraction)
- Short ristretto shots (already cutting early at 1:1 to 1:1.5)
- When shots taste thin or under-extracted (decline reduces extraction further)

| Aggressiveness | Pressure Drop | Duration | Flavor Effect | Best For |
|---|---|---|---|---|
| **Gentle** | 9 → 7 bar | 5-8s | Subtle smoothing, slightly cleaner finish | Medium roasts, first experiment with decline |
| **Moderate** | 9 → 5 bar | 10-15s | Noticeably sweeter finish, reduced bitterness | Most coffees, the "safe default" |
| **Steep** | 9 → 2-3 bar | 20-30s | Dramatic lever character: syrupy body, caramel sweetness, reduced acidity | Dark roasts, honey/natural process, maximum sweetness goal |

**Timing rule:** At least 60-70% of your target yield should be reached before decline starts. Declining too early cuts extraction short and produces under-developed flavor.

### Phase Duration Indicators

How to tell if each phase is too short or too long:

**Pre-infusion:**

| Symptom | Likely Cause | Fix |
|---|---|---|
| Sharp acidity, inconsistent shots | Too short — dry spots remain in puck | Extend to 5-8 seconds minimum |
| Sour despite adequate grind fineness | Too short — uneven saturation | Add 2-3 seconds; consider adding bloom |
| Flat, muted flavors | Too long — early bitter compounds dissolving | Reduce by 2-3 seconds |

**Bloom:**

| Symptom | Likely Cause | Fix |
|---|---|---|
| Sourness persists despite fine grind | Too short — puck not fully saturated | Extend by 3-5 seconds |
| Muddy, undefined flavors | Too long — heat loss, early bitter dissolution | Reduce by 3-5 seconds |
| Good sweetness but no brightness | Too long — over-saturation homogenizing extraction | Reduce by 2-3 seconds |

**Ramp:**

| Symptom | Likely Cause | Fix |
|---|---|---|
| Channeling (fast uneven flow, sour) | Too fast — pressure shock | Use ease-in transition, extend by 2-3s |
| Thin body despite adequate time | Too slow — never reaches peak pressure long enough | Shorten ramp, use linear instead of ease-in |
| Pressure spike above target | Too aggressive, overshooting | Use ease-in-out or reduce ramp speed |

**Hold/Extraction:**

| Symptom | Likely Cause | Fix |
|---|---|---|
| Sour, under-developed | Too short | Extend duration or increase yield target |
| Bitter, dry, astringent finish | Too long | Reduce yield, add decline phase |
| Good initially but finish degrades | Right duration but needs decline | Add taper (9 → 5-6 bar) in final 5-8 seconds |

### Temperature Profiling Within Phases

Gaggimate supports per-phase temperature overrides (the `temperature` field in each phase object; `0` = use global temperature). Three approaches exist:

**Flat/Constant (standard):** Same temperature throughout. Most predictable and well-understood. The default recommendation — combined with pressure profiling, this covers most needs.

**Declining (lever-machine natural behavior):** Starts hot, finishes cooler. The natural behavior of spring-lever machines. Accentuates sweetness and acidity early while decreasing late-extraction bitterness. Particularly effective for dark roasts. Rao's blooming profile uses this: 98°C during fill, dropping to 92°C during bloom and extraction.

**Rising (ascending profile):** Starts cool, finishes hot. Can enhance acid notes in delicate coffees and help extract late-dissolving sugars. Some argue the main benefit is simply bringing the cold puck up to temperature faster.

**Practical recommendation:** Temperature profiling is a second-order optimization — pressure profiling and bloom have larger effects on flavor. Get your pressure profile dialed in first. Temperature profiling becomes relevant when you want to fine-tune further. Start with a flat temperature and only add per-phase temperature changes after you understand what the pressure curve is doing.

> *For temperature guidelines by roast level, see `../ESPRESSO_BREWING_BASICS.md`*

### Decision Framework: What to Tune First

When you want to change a specific aspect of your shot's flavor, here's what to adjust:

| Goal | First Adjustment | Second Adjustment |
|---|---|---|
| **More sweetness** | Add or extend bloom by 3-5s | Add gentle-to-moderate decline (9 → 6 bar) |
| **More body** | Faster ramp (instant or short linear) | Shorter ratio (1:2 instead of 1:2.5) |
| **More clarity** | Add bloom for even extraction | Slower ramp (ease-in, 4-5s) |
| **Less bitterness** | Add decline phase (9 → 5 bar, last 5-8s) | Reduce temperature 1-2°C |
| **More brightness/acidity** | Remove or shorten decline phase | Increase temperature 1-2°C |
| **Smoother finish** | Add ease-out decline (9 → 5 bar, 10-15s) | Extend taper duration |
| **More complexity** | Use lever decline (9 → 3 bar, 20-30s linear) | Consider multi-stage pressure |
| **Reduce channeling** | Extend pre-infusion + add bloom | Use ease-in ramp instead of instant |

**The order of profile modifications when iterating:**
1. **Bloom** — biggest single impact on sweetness and extraction evenness
2. **Decline phase** — biggest impact on reducing bitterness and improving finish
3. **Ramp speed / transition type** — fine-tunes body vs clarity balance
4. **Pre-infusion flow rate** — fine-tunes saturation behavior
5. **Temperature profiling** — smallest incremental improvement, most complex

### Worked Example: Natural Process Coffee

Starting from a classic 9-bar flat profile with a natural-process Ethiopian:

**Shot 1 — Classic 9-Bar:** Grind dialed, 25-second shot at 1:2.2. Tastes balanced but finish is slightly harsh, lacks the fruit sweetness expected from the tasting notes. Rating: 3/5.

**Adjustment 1 — Add bloom:** Insert an 8-second bloom (pump off) after pre-infusion. This allows CO2 to escape and the puck to saturate evenly.

**Shot 2 — With bloom:** Same grind. Shot time extends to ~33 seconds (bloom adds time). More sweetness emerges, fruity notes are clearer, but the finish is still a bit dry. Rating: 3.5/5.

**Adjustment 2 — Add gentle decline:** Change the extraction phase from flat 9 bar to a 5-second taper from 9 → 6 bar at the end. Use ease-out transition for smooth landing.

**Shot 3 — Bloom + decline:** Sweet, fruit-forward, clean finish. The harsh late-extraction character is gone. Could use slightly more body. Rating: 4/5.

**Adjustment 3 — Tune ramp:** Change the pre-infusion → extraction ramp from ease-in (5s) to linear (3s). Slightly faster ramp should add body without reintroducing harshness.

**Shot 4 — Final profile:** Good body, clear fruit notes, sweet finish, no harshness. Rating: 4.5/5. Save the profile.

> *For pressure selection by roast and processing method, see `../PRESSURE_GUIDE.md`. For ready-to-use profiles, see `../PROFILE_LIBRARY.md`. For grind and temperature adjustments, see `../ESPRESSO_BREWING_BASICS.md`.*

---

## File Management

### Exporting Profiles

1. Navigate to `http://gaggimate.local/profiles`
2. Click export icon on profile card
3. Save `.json` file

### Importing Profiles

1. Navigate to `http://gaggimate.local/profiles`
2. Click "Import" (top right)
3. Upload `.json` file
4. Click star icon to make available on machine

### Sharing Profiles

- Join Gaggimate Discord: https://discord.gg/APw7rgPGPf
- Share in #profiles channel
- Include coffee recommendations in description
- Test thoroughly before sharing

---

## Volumetric Estimation (No Scale)

Without a Bluetooth scale, Gaggimate estimates volume using:
- Pressure curve analysis
- Flow rate integration
- Time-based modeling

**Calibration Process:**

1. First shot: Let profile run with volumetric target
2. Weigh actual output on regular scale
3. Adjust profile's volumetric value:
   - If 30g target → 35g actual: Change to 27g
   - If 30g target → 25g actual: Change to 33g
4. Re-test and fine-tune

After 2-3 shots, estimation typically becomes accurate within ±2g.

---

## Quick Reference Card

For essential settings by coffee type (temperature, ratio, timing), see `../ESPRESSO_BREWING_BASICS.md`.
For pressure by roast and processing, see `../PRESSURE_GUIDE.md`.
For ready-to-use profiles, see `../PROFILE_LIBRARY.md`.

### Most Common Mistakes

1. **Too short pre-infusion** → Add 2-4 seconds
2. **No volumetric target** → Always set weight target
3. **Instant transitions everywhere** → Use linear/ease for ramps
4. **Ignoring temperature** → Adjust by 1-2°C increments
5. **Same profile for all coffees** → Customize per bean

---

## Resources

- **Documentation**: https://docs.gaggimate.eu/
- **Discord Community**: https://discord.gg/APw7rgPGPf
- **Profile Library**: Discord #profiles channel
- **Web Interface**: http://gaggimate.local/profiles
- **GitHub Repository**: https://github.com/jniebuhr/gaggimate

**Profile tuning sources:**
- Scott Rao: [Advanced Mode on the DE1+](https://www.scottrao.com/blog/2018/7/18/advanced-mode-on-the-de1) — Blooming technique origin, +1-1.5% extraction yield
- Scott Rao: [Best Practice Espresso Profile](https://www.scottrao.com/blog/2021/5/18/best-practice-espresso-profile) — Evolved blooming profile with softened pressure rise
- Lance Hedrick: [Pressure Profiles for Espresso](https://flairespresso.com/blog/espresso-university-pressure-profiles-for-espresso/) — Three-part light roast extraction, 6-8 bar for light roasts
- Jonathan Gagne: [Adaptive Profile (Coffee ad Astra)](https://coffeeadastra.com/2020/12/31/an-espresso-profile-that-adapts-to-your-grind-size/) — Flow-based self-regulating profile
- Decent Espresso: [How Pressure Profiling Changes Flavor](https://decentespresso.com/blog/new_video_how_pressure_profiling_changes_flavor)
- Espresso Aficionados: [Profiling Guide](https://espressoaf.com/guides/profiling.html) — Community profiling consensus

---

## Version History

- **v1.0** (January 2026): Initial comprehensive guide
- Based on Gaggimate firmware v1.6.0+
- Pro profile features documented
- Examples from real-world usage and community

---

This guide was written by Julian Leopold using Claude in order to assist users and LLM agents in creating effective Gaggimate espresso profiles.
