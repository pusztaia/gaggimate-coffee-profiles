# GaggiMate Pro – Profil készítési útmutató

Ez a dokumentum minden szükséges információt tartalmaz ahhoz, hogy új espresso profilokat készíts ehhez a setuphoz és repository-hoz.

---

## Setup referencia

| Komponens | Érték |
|---|---|
| Gép | Gaggia Classic Pro 2025 + GaggiMate Pro |
| Daráló | DF64V Gen 2 |
| Kések | SSP Sweet Lab Espresso V3 |
| Kosár | IMS B682TH24.5M |
| Puck screen | IMS E&B Lab, Ø 2.4 mm, 253 lyuk (DS58.5) |
| RPM baseline | 1200 |
| RPM tartomány | 800–1800 |
| Őrlőskála | 0–90, egész jelölések |
| Mérleg | BOOKOO Themis Ultra (Bluetooth) |
| Dózis | 18.5 g (rögzített) |

---

## A JSON profil szerkezete

A GaggiMate Pro firmware a `schema/profile.json` sémát követi. Csak a séma által definiált mezők érvényesek – ismeretlen gyökér mezők érvénytelenek (`additionalProperties: false`). A dokumentációt az `.md` fájlban tartsd, nem a JSON-ban.

### Gyökér mezők

```json
{
  "label": "Kávé neve – dózis/hozam/hő/idő",
  "type": "pro",
  "description": "Egy soros összefoglaló: kávé / dózis / hozam / hő / grind",
  "temperature": 94.5,
  "utility": false,
  "phases": [ ... ]
}
```

| Mező | Típus | Leírás |
|---|---|---|
| `label` | string | UI-ban megjelenő név |
| `type` | `"pro"` | Mindig `pro` – többfázisú, pressure/flow vezérelt |
| `description` | string | Rövid összefoglaló, UI-ban látható |
| `temperature` | number (0–150) | Boiler setpoint °C-ban – az egyes fázisok felülírhatják |
| `utility` | boolean | `false` brew profiloknál, `true` csak backflushnál |
| `phases` | array | Fázisok listája, sorrendben futnak le |

> **`pro` típus viselkedése:** A `duration` mindig hard cap. Ha egy `target` korábban tüzel, a fázis azonnal véget ér. Ha a target nem tüzel (pl. nincs scale), a `duration` zárja a fázist.

---

## Fázis szerkezete

```json
{
  "name": "Fázis neve",
  "phase": "preinfusion",
  "valve": 1,
  "duration": 8,
  "temperature": 94.5,
  "transition": {
    "type": "instant",
    "duration": 0,
    "adaptive": true
  },
  "pump": {
    "target": "pressure",
    "pressure": 2.3,
    "flow": 4.5
  },
  "targets": [
    { "type": "volumetric", "operator": "gte", "value": 42.0 }
  ]
}
```

### Fázis mezők

| Mező | Típus | Értékek | Leírás |
|---|---|---|---|
| `name` | string | bármilyen | Brew képernyőn megjelenő név |
| `phase` | string | `"preinfusion"` / `"brew"` | Fázis kategória |
| `valve` | integer | `0` / `1` | `1` = háromútas szolénoid nyitva (normál brew), `0` = zárva (backflush) |
| `duration` | number (0.5–300) | másodperc | Hard cap; a fázis legkésőbb ennyi másodpercig fut |
| `temperature` | number | 0–160 °C, vagy `0` | `0` = profil szintű hőmérsékletet örökli |
| `transition` | object | lásd alább | Pump setpoint ramp az előző értékről |
| `pump` | object | lásd alább | Pump vezérlés |
| `targets` | array | lásd alább | Stop feltételek (opcionális) |

---

## Pump vezérlés

A pump kétféleképpen vezérelhető:

### Pressure-controlled (nyomásvezérelt)

```json
"pump": {
  "target": "pressure",
  "pressure": 7.4,
  "flow": 2.1
}
```

- A pump a `pressure` értéket tartja (bar)
- A `flow` soft felső korlát (`0` = nincs korlát)

### Flow-controlled (folyás-vezérelt)

```json
"pump": {
  "target": "flow",
  "pressure": 0,
  "flow": 8.0
}
```

- A pump a `flow` értéket tartja (g/s)
- A `pressure` soft felső korlát (`0` = nincs korlát)

### Sentinelek

| Érték | Jelentés |
|---|---|
| `pressure: 0` | Nincs nyomáskorlát (amikor flow a target) |
| `flow: 0` | Nincs flow-korlát (amikor pressure a target) |
| `pressure: -1` | Tartsd a fázis belépésekor mért nyomást |
| `flow: -1` | Tartsd a fázis belépésekor mért flow-t |

### Értéktartományok

| Mező | Min | Max |
|---|---|---|
| `pressure` | 0 | 12 bar |
| `flow` | 0 | 15 g/s |

---

## Transition (ramp)

A fázis elején a pump setpoint az előző értékről rámpál az újra.

```json
"transition": {
  "type": "linear",
  "duration": 6,
  "adaptive": true
}
```

| Mező | Értékek | Leírás |
|---|---|---|
| `type` | `"instant"` / `"linear"` / `"ease-in"` / `"ease-out"` / `"ease-in-out"` | Ramp görbe |
| `duration` | 0–300 s | Ramp hossza (ha > phase duration, a firmware a phase duration-t használja) |
| `adaptive` | `true` / `false` | `true` = a ramp a **mért** értékből indul (nem a setpointból); ajánlott preinfusion → brew átmenetnél |

| Transition type | Jellemzők |
|---|---|
| `instant` | Azonnali ugrás, nincs ramp |
| `linear` | Egyenletes változás |
| `ease-in` | Lassan indul, gyorsul |
| `ease-out` | Gyorsan indul, lassan ér célt |
| `ease-in-out` | Lassan indul, gyorsul, lassan ér célt |

---

## Targets (stop feltételek)

A `targets` tömbben OR logika érvényes – az első tüzelő target zárja a fázist. A kiértékelés **minden 100 ms-ban** történik.

```json
"targets": [
  {
    "type": "volumetric",
    "operator": "gte",
    "value": 42.0
  }
]
```

| Mező | Értékek | Leírás |
|---|---|---|
| `type` | `"volumetric"` / `"pressure"` / `"flow"` / `"pumped"` | Mit mér |
| `operator` | `"gte"` / `"lte"` | `gte` = ≥, `lte` = ≤ |
| `value` | number ≥ 0 | Küszöbérték |

### Target típusok

| Type | Egység | Mikor hasznos |
|---|---|---|
| `volumetric` | gramm (scale weight) | Beverage weight stop – Bluetooth scale kell hozzá + brew-by-weight mód |
| `pressure` | bar | Nyomás elérése után lép tovább (pl. ramp vége) |
| `flow` | ml/s | Flow érték elérésekor |
| `pumped` | ml | Az adott fázisban pumpált víz mennyisége (fázis határon nullázódik) |

> **Fontos:** A `volumetric` target csak akkor működik, ha a BOOKOO Themis Ultra Bluetooth-on csatlakozik **és** a brew-by-weight mód aktív a GaggiMate-ben. Ha ezek hiányoznak, a target csendesen nem tüzel – a `duration` veszi át a stopot.

> **Fontos:** A `value: 0` a `volumetric` target esetén "nincs target" – a fázis a teljes `duration`-ig fut.

> **Fontos:** Az `operator` csak `"gte"` vagy `"lte"` lehet, **kisbetűvel**. Bármilyen más string (pl. `"gt"`, `"GTE"`) ismeretlen → firmware alapértelmezése `lte` lesz, ami hibás viselkedést okoz.

---

## A meglévő profilok szerkezete

Minden profil azonos 6-fázisú felépítést követ. Ez az alap blueprint:

### Fázis blueprint

| # | Kategória | Típus | Időtartam | Pump target | Nyomás | Flow | Transition |
|---:|---|---|---:|---|---:|---:|---|
| 1 | preinfusion | Wetting | 4–5 s | flow | 0 | 7.5–8.0 | ease-out / 2s / adaptive |
| 2 | preinfusion | Saturation | 6–8 s | pressure | 2.0–2.3 | 4.5 | instant / 0s / adaptive |
| 3 | preinfusion | Bloom | 4–6 s | pressure | 0.4–0.5 | 0 | ease-out / 2s / adaptive |
| 4 | brew | Ramp | 5–6 s | pressure | 7.2–7.6 | 2.4 | linear / 5–6s / adaptive |
| 5 | brew | Extraction | 11–13 s | pressure | 7.2–7.6 | 2.1–2.2 | instant / 0s / adaptive |
| 6 | brew | Finish | 4–6 s | pressure | 5.4–5.8 | 1.7–1.8 | linear / 4–7s / adaptive |

### Meglévő profilok összehasonlítása

| Kávé | Hő | P2 sat | P4 ramp | P5 extract | P6 finish | P1 dur | P2 dur | P3 dur | P4 dur | P5 dur | P6 dur | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Wangera 94.5C | 94.5 | 2.3 | 7.4 | 7.4 | 5.8 | 5 | 8 | 4 | 6 | 11 | 4 | 38 s |
| Burundi Mubuga | 94.5 | 2.2 | 7.2 | 7.2 | 5.4 | 5 | 8 | 4 | 6 | 11 | 4 | 38 s |
| Colombia MJ | 94.5 | 2.3 | 7.3 | 7.3 | 5.5 | 5 | 8 | 4 | 6 | 12 | 4 | 39 s |
| Kirinyaga PB | 94.5 | 2.1 | 7.6 | 7.6 | 5.6 | 4 | 6 | 4 | 5 | 12 | 6 | 37 s |
| Caturron | 95.0 | 2.0 | 7.2 | 7.2 | 5.6 | 4 | 7 | 6 | 6 | 13 | 6 | 42 s |

---

## Paraméterek és ízhatásuk

### Hőmérséklet

| Hőmérséklet | Hatás |
|---|---|
| 93–94 °C | Kevesebb sav, több édesség, enyhébb test; washed kávéknál túl lapos lehet |
| 94–94.5 °C | Kiegyensúlyozott; a legtöbb washed profil alaptartománya |
| 94.5–95 °C | Több sav és aromaélénkség; natural/anaerob kávéknál, vagy ha lapos az íz |
| 95+ °C | Intenzívebb, több keserűség kockázata |

### Preinfusion nyomás (Saturation fázis)

| Nyomás | Hatás |
|---|---|
| 1.8–2.0 bar | Óvatosabb nedvesítés; hosszabb bloomhoz, sűrűbb puckhoz |
| 2.1–2.3 bar | Standard; egyenletes nedvesítés |
| 2.4–2.5 bar | Gyorsabb szaturáció; channeling kockázat nő |

### Főnyomás (Extraction fázis)

| Nyomás | Hatás |
|---|---|
| 6.5–7.0 bar | Lágyabb, kerekebb, kevesebb keserűség |
| 7.0–7.6 bar | Standard espresso tartomány; balanszos |
| 7.6–8.5 bar | Intenzívebb, több test, keserűség kockázata nő |
| 9 bar | Tradicionális; erős, sok fines kinyerése |

### Végnyomás (Finish fázis)

| Nyomás | Hatás |
|---|---|
| 4.5–5.0 bar | Könnyű, lágy lecsengés |
| 5.4–5.8 bar | Standard; megakadályozza a channeling-et a shot végén |
| 6.0+ bar | Kemény lecsengés; nem ajánlott |

### Flow limit az Extraction fázisban

| Flow limit | Hatás |
|---|---|
| 1.7–1.8 g/s | Lassabb extraction, több kinyerés |
| 2.0–2.2 g/s | Standard; balanszos kinyerési sebesség |
| 2.4+ g/s | Gyors, kevesebb kinyerés |

### Teljes profilidő és hozam

| Profilidő | Tipikus hozam 18.5 g dózisnál | Arány |
|---:|---|---|
| 35–37 s | 40–42 g | ~1:2.2–1:2.3 |
| 38–39 s | 41–43 g | ~1:2.2–1:2.3 |
| 40–42 s | 42–44 g | ~1:2.3–1:2.4 |

---

## Feldolgozás és profil összefüggések

| Feldolgozás | Ajánlott hő | Főnyomás | Hozam | Logika |
|---|---|---|---|---|
| Washed | 93.5–94.5 °C | 7.4–7.6 bar | 42–44 g | Tiszta savak, kevesebb test – magasabb hő és nyomás hozza ki a gyümölcsösséget |
| Natural | 93.5–94.5 °C | 7.0–7.4 bar | 41–43 g | Sok édesség és test – alacsonyabb nyomás védi az édességet, rövidebb hozam a tömörségért |
| Honey | 94.0–94.5 °C | 7.2–7.5 bar | 42–43 g | Közép út – mézes édesség és élénkség egyszerre |
| Anaerobic | 94.0–94.5 °C | 7.0–7.4 bar | 42–44 g | Komplex aromák – inkább hosszabb hozam, alacsonyabb nyomás |

---

## Új profil készítésének lépései

### 1. Kiindulópont kiválasztása

Válaszd a kávéhoz legközelebb álló meglévő profilt feldolgozás alapján:

- **Washed Kenya/Ethiopia** → Kirinyaga Tea Rose mint alap
- **Natural Burundi/Ethiopia** → Burundi Mubuga mint alap
- **Anaerobic/Honey Colombia** → Colombia Manos Juntas mint alap
- **Natural Guatemala/Közép-Amerika** → Caturron mint alap
- **Általános washed** → Wangera Stable Start mint alap

### 2. JSON fájl létrehozása

**Fájlnév konvenció:**
```
profiles/{kávé-azonosító}/{kávé-azonosító}-{idő}[{hő}].json
```

Példák:
- `profiles/ethiopia-yirgacheffe/ethiopia-yirgacheffe-37s-945c.json`
- `profiles/kenya-gathugu/kenya-gathugu-38s.json`

**V4 Scale Edition fájlnév** (ha scale-t is készítesz):
```
{alap-json-neve-kiterjesztés-nélkül}-scale-v4.json
```

### 3. JSON sablon (V3, időalapú)

```json
{
  "label": "Kávé neve – 18.5g / célhozam g / hőC / grind X-Y",
  "type": "pro",
  "description": "Kávé neve – 18.5 g / célhozam g / hőC / grind X-Y",
  "temperature": 94.5,
  "utility": false,
  "phases": [
    {
      "name": "Wetting",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 5,
      "temperature": 94.5,
      "transition": { "type": "ease-out", "duration": 2, "adaptive": true },
      "pump": { "target": "flow", "pressure": 0, "flow": 8.0 }
    },
    {
      "name": "Saturation",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 8,
      "temperature": 94.5,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 2.3, "flow": 4.5 }
    },
    {
      "name": "Bloom",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 4,
      "temperature": 94.5,
      "transition": { "type": "ease-out", "duration": 2, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 0.5, "flow": 0 }
    },
    {
      "name": "Ramp",
      "phase": "brew",
      "valve": 1,
      "duration": 6,
      "temperature": 94.5,
      "transition": { "type": "linear", "duration": 6, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 7.4, "flow": 2.4 }
    },
    {
      "name": "Extraction",
      "phase": "brew",
      "valve": 1,
      "duration": 11,
      "temperature": 94.5,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 7.4, "flow": 2.1 }
    },
    {
      "name": "Finish",
      "phase": "brew",
      "valve": 1,
      "duration": 4,
      "temperature": 94.5,
      "transition": { "type": "linear", "duration": 4, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 5.8, "flow": 1.7 }
    }
  ]
}
```

### 4. JSON sablon (V4, Scale Edition)

A V4 az V3 másolata, de az Extraction fázisban `targets` tömb kerül, és a `duration` nagyobb (safety cap):

```json
{
  "label": "Kávé neve Scale V4 – 18.5g / stop Xg / hőC / grind X-Y",
  "type": "pro",
  "description": "Kávé neve Scale V4 – 18.5 g / stop Xg volumetric / hőC / grind X-Y",
  "temperature": 94.5,
  "utility": false,
  "phases": [
    {
      "name": "Wetting",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 5,
      "temperature": 94.5,
      "transition": { "type": "ease-out", "duration": 2, "adaptive": true },
      "pump": { "target": "flow", "pressure": 0, "flow": 8.0 }
    },
    {
      "name": "Saturation",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 8,
      "temperature": 94.5,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 2.3, "flow": 4.5 }
    },
    {
      "name": "Bloom",
      "phase": "preinfusion",
      "valve": 1,
      "duration": 4,
      "temperature": 94.5,
      "transition": { "type": "ease-out", "duration": 2, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 0.5, "flow": 0 }
    },
    {
      "name": "Ramp",
      "phase": "brew",
      "valve": 1,
      "duration": 6,
      "temperature": 94.5,
      "transition": { "type": "linear", "duration": 6, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 7.4, "flow": 2.4 }
    },
    {
      "name": "Extraction",
      "phase": "brew",
      "valve": 1,
      "duration": 30,
      "temperature": 94.5,
      "transition": { "type": "instant", "duration": 0, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 7.4, "flow": 2.1 },
      "targets": [
        { "type": "volumetric", "operator": "gte", "value": 42.0 }
      ]
    },
    {
      "name": "Finish",
      "phase": "brew",
      "valve": 1,
      "duration": 8,
      "temperature": 94.5,
      "transition": { "type": "linear", "duration": 4, "adaptive": true },
      "pump": { "target": "pressure", "pressure": 5.8, "flow": 1.7 }
    }
  ]
}
```

### 5. Recipe.md fájl létrehozása

**Fájlnév:** `{könyvtárnév}-recipe.md`

Kötelező tartalom:
- Kávé neve, márka, feldolgozás, eredet, ízjegyek
- Alap recept táblázat (dózis, hozam, hő, idő, arány, őrlés, RPM, kosár)
- GaggiMate Pro fázistáblázat (fázisnév, idő, hő, pump target, nyomás/flow)
- Dial-in logika táblázat (tünet → következő lépés)
- V3 és V4 rövid recept sor

### 6. Changelog.md fájl létrehozása

**Fájlnév:** `{könyvtárnév}-changelog.md`

```markdown
# Changelog – Kávé neve

## YYYY-MM-DD – első profil

- Új profil: kávé neve, feldolgozás.
- Cél: ízjegyek.
- Profilidő: X s, hőmérséklet: Y °C, dózis: 18.5 g, célhozam: Z g.
- Őrlés baseline: grind N, 1200 RPM.
```

---

## Import a GaggiMate-be

1. Nyisd meg a GaggiMate Web UI-t (IP cím a GaggiMate kijelzőjén)
2. **Profiles → Import**
3. Válaszd ki a JSON fájlt
4. A profil megjelenik a listában

**Megjegyzés:** Az `id` mezőt ne tedd a JSON-ba – a firmware importáláskor generál egyet.

---

## JSON validáció

Az elkészült JSON fájl gyorsan ellenőrizhető:

```bash
python3 -c "import json; json.load(open('profiles/uj-kave/uj-kave-38s.json'))" && echo OK
```

Teljes schema-ellenőrzés (minden fájlra):

```bash
python3 -c "
import json
from pathlib import Path
VALID_ROOT = {'id','label','type','description','temperature','favorite','selected','utility','phases'}
VALID_PHASE = {'name','phase','valve','duration','temperature','transition','pump','targets'}
VALID_PUMP = {'target','pressure','flow'}
VALID_TR = {'type','duration','adaptive'}
VALID_TGT = {'type','operator','value'}
issues = []
for p in sorted(Path('profiles').glob('**/*.json')):
    data = json.loads(p.read_text())
    extra = {k for k in data if not k.startswith('_')} - VALID_ROOT
    if extra: issues.append(f'{p.name}: extra root keys: {sorted(extra)}')
    for ph in data.get('phases', []):
        extra_ph = set(ph) - VALID_PHASE
        if extra_ph: issues.append(f'{p.name} / {ph[\"name\"]}: extra phase keys: {sorted(extra_ph)}')
print('Issues:', len(issues))
for i in issues: print(i)
"
```

---

## Grafikonok generálása

```bash
# Összes profil
python3 tools/render_profiles.py

# Egy adott profil
python3 tools/render_profiles.py profiles/uj-kave/uj-kave-38s.json
```

A script a JSON neve alapján hozza létre a PNG-t: `{json-stem}-profile.png`.

---

## Fájlelnevezési összefoglaló

| Fájl | Minta |
|---|---|
| Könyvtár | `profiles/{eredet-kave}/` |
| JSON (V3) | `{eredet-kave}-{idő}[{hő}].json` |
| JSON (V4) | `{v3-json-stem}-scale-v4.json` |
| PNG | `{json-stem}-profile.png` (auto) |
| Recept | `{könyvtárnév}-recipe.md` |
| Changelog | `{könyvtárnév}-changelog.md` |

Szabályok: kisbetű, kötőjel elválasztó, ékezet nélkül, nincs szóköz.
