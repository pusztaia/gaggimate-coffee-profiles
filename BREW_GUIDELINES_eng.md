# Brew Guidelines

General principles for the espresso dial-in process with this setup.

**Setup:** Gaggia Classic Pro 2025 + GaggiMate Pro · DF64V Gen 2 (SSP Sweet Lab Espresso V3) · IMS B682TH24.5M · IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 holes, DS58.5) · BOOKOO Themis Ultra Bluetooth scale

---

## 1. Dose

All profiles are tuned with an **18.5 g** dose for the IMS B682TH24.5M basket.

| Parameter | Value |
|---|---:|
| Dose | 18.5 g |
| Basket capacity | 18-21 g |
| Measurement accuracy | ±0.1 g recommended |

**Effect of changing dose:**

- Higher dose → more resistance → slower flow → higher yield reached later
- Lower dose → less resistance → faster flow → reaches the stop value sooner

If you change the dose, also adjust the `stop_at_g` value and the ratios.

---

## 2. Ratio and yield

### Current profile ratios

| Coffee | Dose | Target Yield | Ratio |
|---|---:|---:|---|
| Kenya Wangera | 18.5 g | 42.0 g | 1:2.27 |
| Burundi Mubuga | 18.5 g | 42.5 g | 1:2.30 |
| Colombia Manos Juntas | 18.5 g | 43.0 g | 1:2.32 |
| Kenya Kirinyaga PB | 18.5 g | 43.0 g | 1:2.32 |
| 28 Caturron | 18.5 g | 42.0 g | 1:2.27 |

### Effect of ratio on flavor

| Ratio | Characteristics |
|---|---|
| 1:1.5 – 1:2.0 | Ristretto – dense, intense, short |
| 1:2.0 – 1:2.3 | Standard espresso – balanced |
| 1:2.3 – 1:2.7 | Lungo espresso – lighter, more sweetness |

**Rule of thumb:**

- If it tastes dry, sharp, tannic: increase the ratio (more yield)
- If it tastes thin, acidic, watery: reduce the ratio (less yield)
- If it tastes bitter, heavy, alcoholic: reduce the ratio or lower the temperature

---

## 3. Grind

### DF64V Gen 2 scale

On the DF64V Gen 2, we use whole-number markings on the 0–90 scale. Decimal values are not reliably reproducible on this ring.

| Scale value | Characteristics with this setup |
|---|---|
| 7–8 | Very fine – strong resistance, slow flow |
| 9–10 | Espresso range – most profiles start here |
| 11–12 | Slightly coarser – faster flow, lighter body |

### Grind adjustment logic

**Choked shot (too fine):**

- Yield does not reach the target before the safety timeout expires
- Sour, pressed, cloudy taste
- Fix: move one notch coarser

**Too-fast shot (too coarse):**

- Yield reaches the target too early (for example, in 25–30 s)
- Thin, watery taste, little body
- Fix: move one notch finer

**Ideal flow (when using beverage weight-based stop):**

- The extraction phase triggers the stop value in the 20–30 s range
- The taste is balanced, fruity, not dry

### Effect of RPM

All profiles are tuned to a 1200 RPM baseline. RPM on the DF64V Gen 2 is adjustable (800–1800 RPM).

- **Lower RPM (800–1000):** finer particles at the same grind setting, more fines
- **Higher RPM (1400–1800):** coarser particles at the same grind setting, fewer fines, different texture

If you change the RPM, the entire profile needs to be dialed in again.

---

## 4. Temperature

### Profile temperatures

| Coffee | Temperature |
|---|---:|
| Kenya Wangera (V2 main profile) | 94.5 °C |
| Kenya Wangera (alternative) | 94.0 °C |
| Burundi Mubuga | 94.5 °C |
| Colombia Manos Juntas | 94.5 °C |
| Kenya Kirinyaga PB | 94.5 °C |
| 28 Caturron | 95.0 °C |

### Effect of temperature

| | Lower temperature | Higher temperature |
|---|---|---|
| Acidity | reduces | increases |
| Sweetness | usually increases | varies |
| Body | reduces | increases |
| Bitterness | reduces | increases |

**When to change the temperature:**

- Sour, thin shot at good yield → try a lower temperature
- Flat, sweet-deficient shot at good yield → try a higher temperature
- Bitter, heavy shot → reduce the temperature, not the ratio

---

## 5. Puck prep

Stable, repeatable puck prep is the foundation of a consistent dial-in. It is especially important when using beverage weight-based stopping, because channeling distorts flow and therefore the measured yield.

### Required steps

1. **WDT (Weiss Distribution Technique)** – even coffee distribution in the basket; especially important at the edges and bottom
2. **Tamp** – straight, even, around 15–20 kg of pressure; a tilted tamp causes channeling
3. **Puck screen** – should be dry and clean; a wet screen can create basic channeling

### Diagnosis with a naked portafilter

If a naked portafilter is available:

| Symptom | Problem |
|---|---|
| Even dripping starting from the center | Good puck prep |
| Dripping starting from the side | Uneven WDT or tilted tamp |
| Spurting before the first drop | Channeling – check WDT and tamp |
| Spurting during extraction | Puck collapse or grind too coarse |

---

## 6. Shot evaluation

### What to measure on every shot

1. **Dose** (g) – according to the recipe
2. **Yield** (g) – shown by the scale (automatic stop in V2 profile)
3. **Time** (s) – the runtime of the GaggiMate profile
4. **Taste** – immediate assessment (sour/sweet/bitter/body/finish)

### Recommended shot log fields

| Field | Description |
|---|---|
| Date | |
| Coffee | |
| Profile | JSON filename and version (V1/V2) |
| Dose | g |
| Yield | g |
| Time | s |
| Temperature | °C |
| Grind | scale value |
| RPM | |
| Stop trigger | beverage weight / safety timeout / manual |
| Taste evaluation | detailed notes |
| Next step | what to change on the next shot |

### Evaluation criteria

**Acidity:**
- Good: lively, fruity, rounded
- Bad: sharp, citrusy, abrasive, pressed

**Sweetness:**
- Good: caramelized, fruity, long-lasting
- Bad: neutral, absent, artificial

**Body:**
- Good: syrupy, creamy, full
- Bad: watery, thin, or heavy and alcoholic

**Finish:**
- Good: fruity, long-lasting, pleasant
- Bad: bitter, dry, husky, tannic

---

## 7. Dial-in process

### Sequence

1. **Set the dose** – do not change it during dial-in
2. **Set the temperature** – the profile value
3. **Set the target yield** – the profile `stop_at_g` value
4. **Set the grind** – this is the primary variable
5. **Evaluate yield and taste** – decide after at least 2–3 consistent shots
6. **If the grind is optimal and taste is still not right** → fine-tune by temperature or yield

### Change only one variable at a time

In every dial-in step, change only one parameter. When changing multiple things at once, you cannot identify the effect.

### Consistency check

Two consecutive shots with the same parameters should differ by at most ±1.0 g in yield. If the variation is larger:

- Puck prep stability is the primary suspect
- Check dose measurement accuracy
- Check scale calibration

---

## 8. V1 vs V2 dial-in differences

| | V1 (Time Based) | V2 (Scale Edition) |
|---|---|---|
| Yield variability | High (flow-dependent) | Low (gram control) |
| Dial-in primary variable | Grind (yield and time) | Grind (flow speed and time) |
| Yield control | Profile duration | `stop_at_g` value |
| Consistency | Can vary from shot to shot | Reproducible |
| Manual intervention | Manual stop needed | Automatic stop |
