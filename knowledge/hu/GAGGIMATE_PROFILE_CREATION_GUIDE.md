# Gaggimate profil készítési útmutató

## Áttekintés

Gyorsreferencia kártya a Gaggimate profil JSON szerkezetéhez. A teljes profilkészítési workflow-hoz használd a `/gaggimate-profiles`-t. Teljes példákért, transition részletekért és haladó technikákért lásd: [`reference/PROFILE_CREATION_REFERENCE.md`](../reference/PROFILE_CREATION_REFERENCE.md).

> **Kész, használatra kész profilokat keresel?** Lásd a `PROFILE_LIBRARY.md`-t, amely roastszint, feldolgozási mód és shot-stílus szerint rendezett, válogatott gyűjteményt tartalmaz.

## Profil verziók

- **Gaggimate Standard**: Alap hőmérséklet-szabályozás, volumetrikus adagolás, időzített fázisok
- **Gaggimate Pro**: Haladó nyomás/flow profilozás, valós idejű nyomásfigyelés, komplex transitionök, több stop feltétel

---

## A JSON profil szerkezete

### Felső szintű mezők

```json
{
  "label": "Profile Name",
  "type": "pro",
  "description": "Optional description of the profile",
  "temperature": 93,
  "phases": [...]
}
```

| Mező | Típus | Kötelező | Leírás | Érvényes értékek |
|-------|------|----------|-------------|--------------|
| `label` | string | Igen | A gépen megjelenő megjelenítési név | Bármilyen string |
| `type` | string | Igen | A profil komplexitási szintje | `"simple"` vagy `"pro"` |
| `description` | string | Nem | Opcionális megjegyzések a profilról | Bármilyen string |
| `temperature` | number | Igen | Globális célhőmérséklet °C-ban | 70-100 (tipikus: 88-96) |
| `phases` | array | Igen | A fázisok sorrendben felsorolt listája | Fázis objektumok tömbje |

---

## Fázis szerkezete

### Fázis mezők referencia

| Mező | Típus | Kötelező | Leírás | Érvényes értékek |
|-------|------|----------|-------------|--------------|
| `name` | string | Igen | A brewelés közben megjelenő név | Bármilyen string (pl. "Pre-infusion", "Ramp", "Hold") |
| `phase` | string | Igen | A fázis kategóriája a megjelenítéshez | `"preinfusion"`, `"brew"`, `"decline"` |
| `valve` | number | Igen | A háromutas szelep pozíciója | `0` = zárt, `1` = nyitott |
| `duration` | number | Igen | A fázis maximális időtartama másodpercben | 1-60 (tipikus: 3-30) |
| `temperature` | number | Nem | Felülírja a globális hőmérsékletet (0 = a globálist használja) | 0 vagy 70-100 |
| `transition` | object | Igen (Pro) | Hogyan történik az átmenet a célértékekre | Lásd a Transition szakaszt |
| `pump` | object | Igen | A pumpa vezérlési konfigurációja | Lásd a Pump szakaszt |
| `targets` | array | Nem | Stop feltételek (korán kilép a fázisból) | Lásd a Targets szakaszt |

### Fázistípus irányelvek

- **`preinfusion`**: Alacsony flow-jú nedvesítő fázis (tipikusan 2-5 másodperc)
- **`brew`**: Fő extrakciós fázis (nyomás/flow vezérlés)
- **`decline`**: Nyomás lecsengető/befejező fázis (opcionális)

---

## Pump konfiguráció

### Pump mezők

| Mező | Típus | Kötelező | Leírás | Érvényes értékek |
|-------|------|----------|-------------|--------------|
| `target` | string | Igen | Vezérlési mód | `"pressure"`, `"flow"`, `"power"`, `"off"` |
| `pressure` | number | Igen | Cél-/korlátnyomás barban | 0-12 (tipikus: 6-9) |
| `flow` | number | Igen | Cél-/korlát flow ml/s-ban | 0-10 (tipikus: 2-5), `-1` = adaptív |

### Pump target módok

- **Pressure** (`"pressure"`) — Adott nyomás tartása. A `flow` opcionális korlátként működik.
- **Flow** (`"flow"`) — Adott flow ráta tartása. A `pressure` felső korlátként (ceiling) működik. Használd a `flow: -1` értéket adaptív flow-hoz (automatikusan a puck ellenállásához igazodik).
- **Power** (`"power"`) — Fix pumpa-százalék (csak Standard). Használj `pressure: 0, flow: 0` értékeket a **bloom-hoz (pumpa kikapcsolva)**.

> **Flow limit vs ease-in a kíméletes build-hez (channeling megelőzés).** `pressure` módban a
> `flow` érték egy *opcionális korlát*, de egy **áteresztő puck**-on egy alacsony korlát (pl. `flow: 4`)
> *kötő korláttá* válhat, és a nyomást **a cél alatt** rögzíti – a pumpa a korlátnál ragad, miközben a
> nyomás megtorpan, ami híg, savanyú, alulextrahált shot-ot eredményez. Ha olyan kíméletes build-et
> szeretnél, amely **mégis eléri a teljes nyomást**, inkább hosszabbítsd meg az **ease-in transitiont**
> (ez a nyomás *rámpáját* lassítja), mintsem a flow-t korlátoznád (ez a nyomás *plafonját* korlátozza).
> Állítsd `flow: 0`-ra (nincs korlát) a ramp/hold fázisban, és hagyd, hogy a hosszabb ease-in végezze
> a finomítást. Az alacsony flow korlátot tartsd fenn azokra az esetekre, amikor szándékosan flow-korlátos
> shotot szeretnél. (Lásd a megfelelő telemetria-jelenséget, a "Capped below target"-et a
> `diagnose/references/TELEMETRY_PATTERNS.md`-ben.)

---

## Transition konfiguráció

### Transition mezők

| Mező | Típus | Kötelező | Leírás | Érvényes értékek |
|-------|------|----------|-------------|--------------|
| `type` | string | Igen | A ramp görbe alakja | `"instant"`, `"linear"`, `"ease-in"`, `"ease-out"`, `"ease-in-out"` |
| `duration` | number | Igen | A ramp időtartama másodpercben | 0-10 (0 = azonnali) |
| `adaptive` | boolean | Igen | Az aktuális vagy az előző célértékből induljon | `true` = aktuális, `false` = előző célérték |

### Transition típusok

- **Instant** — Azonnali ugrás. Fázisok elejéhez használd.
- **Linear** — Állandó sebesség. Standard nyomásrámpákhoz használd.
- **Ease-in** — Lassú indulás, gyors befejezés. Pre-infúzió → extrakció átmenethez használd.
- **Ease-out** — Gyors indulás, lassú befejezés. Lecsengetéshez/decline-hoz használd.
- **Ease-in-out** — Lassú indulás és befejezés. Komplex nyomásváltozásokhoz használd.

---

## Stop feltételek (Targets)

### Target mezők

| Mező | Típus | Kötelező | Leírás | Érvényes értékek |
|-------|------|----------|-------------|--------------|
| `type` | string | Igen | Mérési típus | `"volumetric"`, `"pumped"`, `"pressure"`, `"flow"` |
| `operator` | string | Igen | Összehasonlító operátor | `"gte"` (>=), `"lte"` (<=), `"gt"` (>), `"lt"` (<) |
| `value` | number | Igen | Küszöbérték | A type-tól függ |

### Target típusok

- **Volumetric** — Kilépés a mérlegen mért súlynál (BT mérleg szükséges hozzá). A végső shot-súlyhoz a leggyakrabban használt.
- **Pumped** — Kilépés X ml pumpálás után. Mérlegtől független. (A token `"pumped"` – mind a firmware profilok, mind a `phase_exits` telemetria ezt használja; az útmutató egy korábbi változata `"water_pumped"`-et írt, ami hibás volt.)
- **Pressure** — Kilépés, amikor a nyomás átlépi a küszöböt (felfelé vagy lefelé).
- **Flow** — Kilépés, amikor a flow átlépi a küszöböt.

Egy fázison belül több target esetén **OR logika** érvényesül – a fázis akkor lép ki, amikor BÁRMELYIK feltétel teljesül.

> **Mindig párosíts egy hosszú volumetrikus fázist egy `pumped` biztonsági hálóval.** Ha a BT mérleg a shot közben leválik (ez egy dokumentált Bookoo/Gaggimate hibamód), a volumetrikus target soha nem tud tüzelni, és a fázis a teljes `duration` timeoutig fut – ez akár a tervezett ital mennyiségének 3×-osa is lehet. Adj hozzá egy `{"type": "pumped", "operator": "gte", "value": N}` targetet, ahol N egy normál shot teljes pumpált mennyiségét ~15–20%-os ráhagyással fedi le (megfigyelt normál össztérfogatok egy 22g/55g shot esetén: ~90–115 ml → biztonsági háló 130-nál). Élő eszközön megerősítve 2026 júliusában.

### Eszközön megfigyelt firmware-viselkedések (2026. júl., eredetileg fw 1.8.0-n, strukturálisan újra megerősítve a `gaggimate-source` firmware fa 1.8.1-es verziója ellen)

- **A `phase: "decline"` normalizálódik `"brew"`-ra** — megerősítve a `src/display/models/profile.h`-ban: a `PhaseType` enum csak `PHASE_TYPE_PREINFUSION`/`PHASE_TYPE_BREW` értékeket tartalmaz; bármilyen `"phase"` érték a `"preinfusion"`-on kívül (beleértve a `"decline"`-t is) `BREW`-ra parse-olódik, és a szerializáció is mindig csak `"preinfusion"`-t vagy `"brew"`-t ír vissza. Ez a parser egy séma szintű ténye, nem egy adott patch-verzióhoz kötött – a repo JSON-jait `"brew"`-val írd a decline fázisokhoz, hogy a repo és az eszköz bájtra egyezzen.
- **A `transition.duration` a dokumentált 10s-os maximum felett is helyesen fut** — megerősítve a forráskódban: a `transition.duration` korlátlan `float`-ként kerül beolvasásra, felső határ ellenőrzés nélkül a parserben bárhol. A 38–40s-os lineáris decline-ok a megírtaknak megfelelően futnak (telemetriával megerősítve 1.8.0-n), ami konzisztens ezzel. A transition táblázatban szereplő 0–10s-os tartomány elavult dokumentáció a ramp-stílusú transitionökhöz, nem firmware korlát.
- **Egy pumpa-kikapcsolt fázis `{"target": "flow", "pressure": 0, "flow": 0}`-ként kódolódik** — a `pro` profilok `PumpTarget` enumja csak `PUMP_TARGET_FLOW`/`PUMP_TARGET_PRESSURE` értékeket tartalmaz (nincs `"power"`/`"off"` ezen a szinten); a `"power"` csak a `type: "standard"` profilok egyszerű egész szám `pump` mezőjénél értelmezhető. A flow/0/0 az a minta, amit a jelenlegi firmware profilok bloom/áztatás fázishoz használnak.
- A **`pumped` biztonsági háló margó számai** (~90–115 ml normál összmennyiség, 130 ml biztonsági háló egy 22g/55g shot esetén) a 2026 júliusi fw-1.8.0 teszt empirikus mérései, nem lettek újramérve 1.8.1-en – a *mechanizmust* (párosítsd a volumetrikust egy `pumped` biztonsági hálóval) tekintsd szilárdnak, mivel a fenti séma szintű tényekre épül, de a *számokat* ellenőrizd újra a saját gépeden, mielőtt biztonsági margóként megbíznál bennük.

---

## Flow-alapú változó nyomás technika

A modsmthng_57901 nevű felhasználó úttörő munkája a Gaggimate Discordon. Ez a technika **önszabályozó nyomást** hoz létre — egy flow rátát célzol meg egy nyomás-plafonnal, és a gép automatikusan alkalmazkodik a puck ellenállásához.

```json
"pump": {
  "target": "flow",      // Primary: maintain this flow rate
  "pressure": 9,         // Secondary: never exceed this pressure
  "flow": 1.8            // Target flow in g/s
}
```

**Hogyan működik**: Magas puck ellenállás (finom őrlés) → a nyomás felépül a plafonig, a flow a cél alá eshet. Alacsony ellenállás (durvább őrlés) → a nyomás alacsony marad, a flow tartva marad. A profil kézi beavatkozás nélkül alkalmazkodik.

**Előnyök**: Őrléstolerancia, channeling megelőzés (alacsonyabb kezdeti nyomás), ízegyensúly (a nyomás-plafon megakadályozza a keserűséget), konzisztencia különböző kávéknál.

**Flow skálázása a dózishoz**: `Flow = Dose × 2 / 20s` (pl. 16g → 1.6 g/s, 18g → 1.8 g/s, 22g → 2.2 g/s)

> **A Gaggimate beépített Automatic Pro profilja** ezt a technikát valósítja meg egy 5 fázisú architektúrával, amely tartalmaz egy csökkenő flow-jú extrakciót is. Lásd: [`automatic-pro/AUTOMATIC_PRO_GUIDE.md`](automatic-pro/AUTOMATIC_PRO_GUIDE.md).

---

## Best practice táblázatok

Hőmérséklet, arány és beállítási stratégiákért lásd az `ESPRESSO_BREWING_BASICS.md`-t.
Nyomás kiválasztásához roast és feldolgozási mód szerint lásd a `PRESSURE_GUIDE.md`-t.
Kész, használatra kész profilmintákért lásd a `PROFILE_LIBRARY.md`-t.

### Fázis időtartam irányelvek

| Fázistípus | Tipikus időtartam | Cél |
|------------|------------------|---------|
| Gyors feltöltés | 2-3 másodperc | Gyors nedvesítés alacsony nyomáson |
| Lassú pre-infúzió | 4-8 másodperc | Egyenletes telítődés, gázmentesítés |
| Bloom/áztatás | 5-10 másodperc | Édesség fokozása |
| Nyomás ramp | 3-5 másodperc | Felépülés az extrakciós nyomásig |
| Hold fázis | 15-30 másodperc | Fő extrakció |
| Decline/lecsengés | 3-6 másodperc | Sima befejezés |

> **Duration vs volumetrikus stop:** Volumetrikus stoppal rendelkező fázisokon a volumetrikus target a valódi kilépési feltétel — ez szabályozza a csésze súlyát. A duration egy biztonsági timeout. Állítsd bőkezűen (legalább 1,5×-öse a várt extrakciós időnek), hogy normál körülmények között soha ne vágja le idő előtt a shot-ot.

### Flow ráta irányelvek

| Flow ráta | Felhasználási eset | Nyomás |
|-----------|------|----------|
| 1.5-2.5 ml/s | Nagyon kíméletes pre-infúzió | <3 bar |
| 2.5-4 ml/s | Standard pre-infúzió | 3-6 bar |
| 4-5 ml/s | Fő extrakció (flow limittel) | 8-9 bar |
| Adaptív (-1) | Végső fázis, alkalmazkodik az ellenálláshoz | Változó |

---

*Teljes profilpéldákért, transition részletekért, íz-vezérelt profilhangolásért, haladó technikákért, hibaelhárításért, lever szimulációért és volumetrikus becslésért — lásd a [`reference/PROFILE_CREATION_REFERENCE.md`](../reference/PROFILE_CREATION_REFERENCE.md)-t. A teljes profilkészítési workflow-hoz — használd a `/gaggimate-profiles`-t.*
