# Profile Library Reference

> **Quick lookup:** For the profile summary table, selection guides, and condensed parameters, see [`../PROFILE_LIBRARY.md`](../PROFILE_LIBRARY.md).

Full profile definitions with descriptions, usage notes, detailed parameters, flavor expectations, and complete JSON blocks.

---

## Profiles by Roast Level

### Light Roast

#### Light Roast Bloom

Designed for Nordic-style light roasts that need high extraction and benefit from a bloom phase to enhance sweetness and reduce sourness.

**When to use:** Ethiopian naturals, Kenyan AA, light-roasted Gesha, fruit-forward single origins

**Parameters:**
- Temperature: 95°C
- Ratio: 1:2.5 (22g → 55g)
- Expected time: 28-35 seconds
- Grind: Finer than medium roast settings

**Flavor expectations:** Bright acidity, floral notes, stone fruit sweetness, tea-like body

```json
{
  "label": "Light Roast Bloom [AI]",
  "type": "pro",
  "description": "High-temp bloom profile for light roasts - enhanced sweetness and fruit notes",
  "temperature": 95,
  "phases": [
    {
      "name": "Gentle Fill",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 6,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "flow", "pressure": 9, "flow": 2 }
    },
    {
      "name": "Bloom",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 8,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "power", "pressure": 0, "flow": 0 }
    },
    {
      "name": "Ramp",
      "phase": "brew",
      "valve": 1,
      "duration": 5,
      "temperature": 0,
      "transition": { "type": "ease-in", "duration": 4, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 9, "flow": 0 },
      "targets": [{ "type": "pressure", "operator": "gte", "value": 8.5 }]
    },
    {
      "name": "Extract",
      "phase": "brew",
      "valve": 1,
      "duration": 25,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 9, "flow": 4 },
      "targets": [{ "type": "volumetric", "operator": "gte", "value": 55 }]
    }
  ]
}
```

---

### Medium Roast

#### Classic 9-Bar

The reliable workhorse. A straightforward pre-infusion → ramp → hold pattern that works for most medium roasts.

**When to use:** Colombian, Brazilian, Central American coffees, any "everyday" medium roast

**Parameters:**
- Temperature: 93°C
- Ratio: 1:2 (22g → 44g)
- Expected time: 25-32 seconds
- Grind: Standard espresso

**Flavor expectations:** Balanced, chocolate notes, mild sweetness, medium body

```json
{
  "label": "Classic 9-Bar [AI]",
  "type": "pro",
  "description": "Standard 9-bar extraction with pre-infusion",
  "temperature": 93,
  "phases": [
    {
      "name": "Pre-infusion",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 4,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "flow", "pressure": 9, "flow": 3 }
    },
    {
      "name": "Ramp",
      "phase": "brew",
      "valve": 1,
      "duration": 4,
      "temperature": 0,
      "transition": { "type": "linear", "duration": 3, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 9, "flow": 0 },
      "targets": [{ "type": "pressure", "operator": "gte", "value": 8.5 }]
    },
    {
      "name": "Hold",
      "phase": "brew",
      "valve": 1,
      "duration": 25,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 9, "flow": 4 },
      "targets": [{ "type": "volumetric", "operator": "gte", "value": 44 }]
    }
  ]
}
```

#### Lever Decline

Mimics a spring lever machine with declining pressure throughout extraction. Creates syrupy body and complex sweetness.

**When to use:** Medium roasts where you want more body and sweetness, chocolate-forward beans

**Parameters:**
- Temperature: 91°C
- Ratio: 1:2 (22g → 44g)
- Expected time: 28-35 seconds
- Grind: Slightly finer than classic

**Flavor expectations:** Syrupy body, caramel sweetness, reduced acidity, complex finish

```json
{
  "label": "Lever Decline [AI]",
  "type": "pro",
  "description": "Spring lever-style declining pressure for syrupy body",
  "temperature": 91,
  "phases": [
    {
      "name": "Pre-infusion",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 5,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "flow", "pressure": 9, "flow": 3 }
    },
    {
      "name": "Peak",
      "phase": "brew",
      "valve": 1,
      "duration": 5,
      "temperature": 0,
      "transition": { "type": "linear", "duration": 3, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 9, "flow": 0 },
      "targets": [{ "type": "pressure", "operator": "gte", "value": 8.5 }]
    },
    {
      "name": "Decline",
      "phase": "brew",
      "valve": 1,
      "duration": 30,
      "temperature": 0,
      "transition": { "type": "linear", "duration": 25, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 3, "flow": 0 },
      "targets": [{ "type": "volumetric", "operator": "gte", "value": 44 }]
    }
  ]
}
```

---

### Dark Roast

#### Dark Roast Gentle

Lower temperature and pressure to avoid over-extraction bitterness. Shorter ratio emphasizes body over acidity.

**When to use:** Italian roasts, French roasts, espresso blends intended for milk drinks

**Parameters:**
- Temperature: 89°C
- Ratio: 1:1.5-2 (22g → 33-44g)
- Expected time: 22-28 seconds
- Grind: Coarser than medium roast settings

**Flavor expectations:** Chocolate, caramel, low acidity, full body, no bitterness

```json
{
  "label": "Dark Roast Gentle [AI]",
  "type": "pro",
  "description": "Low temp, lower pressure for dark roasts - avoids bitterness",
  "temperature": 89,
  "phases": [
    {
      "name": "Pre-infusion",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 4,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "flow", "pressure": 8, "flow": 2.5 }
    },
    {
      "name": "Ramp",
      "phase": "brew",
      "valve": 1,
      "duration": 4,
      "temperature": 0,
      "transition": { "type": "ease-in", "duration": 3, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 7.5, "flow": 0 },
      "targets": [{ "type": "pressure", "operator": "gte", "value": 7 }]
    },
    {
      "name": "Hold",
      "phase": "brew",
      "valve": 1,
      "duration": 20,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 7.5, "flow": 4 },
      "targets": [{ "type": "volumetric", "operator": "gte", "value": 39 }]
    },
    {
      "name": "Taper",
      "phase": "decline",
      "valve": 1,
      "duration": 5,
      "temperature": 0,
      "transition": { "type": "ease-out", "duration": 4, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 5, "flow": 0 }
    }
  ]
}
```

---

## Profiles by Processing Method

### Natural/Dry Process

#### Natural Process Bloom

Extended bloom phase helps tame the intensity of natural process coffees while preserving their fruit-forward character.

**When to use:** Ethiopian naturals, Brazilian naturals, any dry-processed coffee with funky/fermented notes

**Parameters:**
- Temperature: 94°C
- Ratio: 1:2-2.5 (22g → 44-55g)
- Expected time: 30-38 seconds
- Grind: Medium-fine, err toward finer

**Flavor expectations:** Blueberry, strawberry, wine-like, controlled ferment funk, juicy body

```json
{
  "label": "Natural Process Bloom [AI]",
  "type": "pro",
  "description": "Extended bloom for natural process coffees - controls intensity, preserves fruit",
  "temperature": 94,
  "phases": [
    {
      "name": "Gentle Fill",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 6,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "flow", "pressure": 9, "flow": 2 }
    },
    {
      "name": "Bloom",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 10,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "power", "pressure": 0, "flow": 0 }
    },
    {
      "name": "Ramp",
      "phase": "brew",
      "valve": 1,
      "duration": 5,
      "temperature": 0,
      "transition": { "type": "ease-in-out", "duration": 4, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 8, "flow": 0 },
      "targets": [{ "type": "pressure", "operator": "gte", "value": 7.5 }]
    },
    {
      "name": "Extract",
      "phase": "brew",
      "valve": 1,
      "duration": 25,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 8, "flow": 4 },
      "targets": [{ "type": "volumetric", "operator": "gte", "value": 49 }]
    },
    {
      "name": "Taper",
      "phase": "decline",
      "valve": 1,
      "duration": 6,
      "temperature": 0,
      "transition": { "type": "linear", "duration": 5, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 5, "flow": 0 }
    }
  ]
}
```

---

## Profiles by Shot Style

### Turbo Shot

#### Turbo Shot

Coarse grind, high flow, fast extraction. Emphasizes clarity and brightness over body. Originally popularized by the specialty coffee competition circuit.

**When to use:** Showcasing origin character, light roasts, when you want tea-like clarity

**Parameters:**
- Temperature: 96°C (high temp compensates for short contact time)
- Ratio: 1:2.5-1:3 (22g → 55-66g)
- Expected time: 15-20 seconds (yes, really)
- Grind: Significantly coarser than normal espresso

**Flavor expectations:** Bright, clean, tea-like, clarity of origin flavors, lighter body

**Note:** Requires a significantly coarser grind than typical espresso — this is a large relative shift from your normal espresso starting point, not a minor adjustment. The longer ratio is essential — with a coarse grind and short contact time, you need more water volume to achieve adequate extraction. A 1:2 turbo will be sour and under-extracted.

**Milk drink note:** Turbo shots have lighter body and higher volume, which can get lost in large milk drinks. If you want turbo clarity in milk, pair with a cortado, piccolo, or flat white rather than a full latte.

```json
{
  "label": "Turbo Shot [AI]",
  "type": "pro",
  "description": "Fast, high-flow extraction for clarity - requires coarse grind",
  "temperature": 96,
  "phases": [
    {
      "name": "Pre-wet",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 3,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "flow", "pressure": 6, "flow": 5 }
    },
    {
      "name": "Extract",
      "phase": "brew",
      "valve": 1,
      "duration": 20,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "flow", "pressure": 6, "flow": 4.5 },
      "targets": [{ "type": "volumetric", "operator": "gte", "value": 66 }]
    }
  ]
}
```

### Allongé

#### Allongé

A long, sweet extraction at extended ratios. Not a lungo (which is just more water) but a true extended extraction that develops sweetness.

**When to use:** Light to medium roasts, when you want a longer, sweeter drink without adding water

**Parameters:**
- Temperature: 94°C
- Ratio: 1:4-5 (22g → 88-110g)
- Expected time: 40-50 seconds
- Grind: Slightly coarser than standard

**Flavor expectations:** Sweet, tea-like, delicate acidity, approachable, long finish

```json
{
  "label": "Allongé [AI]",
  "type": "pro",
  "description": "Long sweet extraction at 1:4-5 ratio - tea-like and approachable",
  "temperature": 94,
  "phases": [
    {
      "name": "Pre-infusion",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 5,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "flow", "pressure": 9, "flow": 2.5 }
    },
    {
      "name": "Ramp",
      "phase": "brew",
      "valve": 1,
      "duration": 5,
      "temperature": 0,
      "transition": { "type": "linear", "duration": 4, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 6, "flow": 0 },
      "targets": [{ "type": "pressure", "operator": "gte", "value": 5.5 }]
    },
    {
      "name": "Extract",
      "phase": "brew",
      "valve": 1,
      "duration": 50,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 6, "flow": 4 },
      "targets": [{ "type": "volumetric", "operator": "gte", "value": 98 }]
    }
  ]
}
```

---

## Specialty Profiles

### Milk Drinks

#### Milk Drink Base

A punchy, concentrated shot with high intensity and full body. The shorter ratio emphasizes sweetness and body over clarity.

**When to use:** When you want maximum intensity — works great as a ristretto-style shot or as a base for larger milk drinks where you want the coffee to remain prominent

**Parameters:**
- Temperature: 92°C
- Ratio: 1:1.5 (22g → 33g)
- Expected time: 22-26 seconds
- Grind: Standard to slightly finer

**Flavor expectations:** Intense, punchy, chocolate/caramel forward, full body

```json
{
  "label": "Milk Drink Base [AI]",
  "type": "pro",
  "description": "Concentrated ristretto-style shot - maximum intensity at 1:1.5 ratio",
  "temperature": 92,
  "phases": [
    {
      "name": "Pre-infusion",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 4,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "flow", "pressure": 9, "flow": 3 }
    },
    {
      "name": "Ramp",
      "phase": "brew",
      "valve": 1,
      "duration": 4,
      "temperature": 0,
      "transition": { "type": "linear", "duration": 3, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 9, "flow": 0 },
      "targets": [{ "type": "pressure", "operator": "gte", "value": 8.5 }]
    },
    {
      "name": "Hold",
      "phase": "brew",
      "valve": 1,
      "duration": 20,
      "temperature": 0,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 9, "flow": 4 },
      "targets": [{ "type": "volumetric", "operator": "gte", "value": 33 }]
    }
  ]
}
```

---

*All profiles marked [AI] were created by your barista assistant and can be safely deleted via the MCP tools.*
