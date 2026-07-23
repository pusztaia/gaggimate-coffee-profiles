# Adaptive v2 – Univerzális adaptív profil

| Mező | Érték |
|---|---|
| Profil neve | Adaptive v2 |
| Típus | Univerzális, kávéfüggetlen adaptív preinfusion |
| Leírás | Light to Medium – Fine grind – 25–40 s – 1:2–2.5 arány |
| Setup | DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) |
| Őrlőskála | 0–90, egész jelölések |
| Fordulat | 1200 RPM baseline |
| Verzió | 2026-07-07 – analízis és dokumentáció |

---

## Mi ez a profil?

Az Adaptive v2 egy **univerzális, kávéfüggetlen** profil, amely nem egyetlen kávéra van hangolva, hanem **a puck állapotához alkalmazkodik** a preinfusion fázisban. A többi profilhoz képest két lényeges eltérés jellemzi:

1. **Target-vezérelt fázisváltás:** Több fázisban is `pumped`, `pressure` vagy `flow` targetek döntik el, mikor lép a következő fázisra — nem a fix idő.
2. **Szándékos hőcsökkentés:** Az első két fázis 93 °C, majd a Compressing fázistól kezdve **88 °C** — ez a melegebb preinfusion után egy hűvösebb extrakcióval kombinálva kevesebb keserűséget és finomabb savprofilt eredményez.

**Mikor érdemes használni?**
- Ismeretlen pörkölt / nem beállított kávé első próbaköre
- Light–Medium pörköltök, ahol a kinyerés érzékeny
- Fine őrlési zónában, ahol a channeling kockázata magasabb
- Ha reprodukálható hozamot szeretnél mérleg nélkül is (volumetric target)

---

## Fázis-analízis

### 1. Prefill (preinfusion) — 5 s max, target: 100 ml pumpált víz

| Paraméter | Érték |
|---|---|
| Pump target | flow |
| Flow | 8 ml/s |
| Nyomáskorlát | nincs (0) |
| Hőmérséklet | 93 °C |
| Transition | ease-out / 2 s / adaptive |
| Stop trigger | pumped ≥ 100 ml **vagy** 5 s |

**Logika:** Gyors, magas flow-val tölti meg a portafilter fejét és a szűrőkosarat. A `pumped ≥ 100 ml` target azt garantálja, hogy egy minimális vízmennyiség bejut, mielőtt továbblép — így a puck állapotától függetlenül (tömör vs. laza) biztosítja a Prefill befejezését. Az `ease-out` transition simán indítja a pumpát.

---

### 2. Fill (preinfusion) — 12 s max, két target

| Paraméter | Érték |
|---|---|
| Pump target | flow |
| Flow | 8 ml/s |
| Nyomáskorlát | nincs (0) |
| Hőmérséklet | 93 °C |
| Transition | instant / 0 s / adaptive |
| Stop trigger | pumped ≥ 100 ml **vagy** pressure ≥ 3 bar **vagy** 12 s |

**Logika:** Folytatja a kosár feltöltését magas flow-val. A két target párhuzamosan fut (OR logika):
- `pumped ≥ 100 ml` — ha a kávé ellenállása kicsi (pl. durvább őrlés), gyorsabban visznek be 100 ml-t
- `pressure ≥ 3 bar` — ha a kávé ellenállása nagy (pl. finom őrlés, tömörítés), a növekvő nyomás zárja a fázist

Ez az adaptív viselkedés lényege: **laza pucknál a pumped target tüzel, tömör pucknál a pressure target** — így a preinfusion minden esetben a valós puck állapothoz igazodik.

---

### 3. Compressing (preinfusion) — 12 s max, két target + hőváltás

| Paraméter | Érték |
|---|---|
| Pump target | pressure |
| Nyomás | 3 bar |
| Flow-korlát | nincs (0) |
| Hőmérséklet | **88 °C** (csökkentve) |
| Transition | ease-out / 2 s / adaptive |
| Stop trigger | pumped ≥ 100 ml **vagy** flow ≤ 3 ml/s **vagy** 12 s |

**Logika:** A puckot alacsony, 3 bar-os nyomással telíti és tömöríti. A hőmérséklet itt csökken **93 → 88 °C**-ra, ami két célt szolgál:
- Csökkenti a korai over-extraction kockázatát a saturation alatt
- A hűvösebb víz kevesebb gázt szabadít fel a puckból, egyenletesebb nedvesítést eredményez

A stop trigger `flow ≤ 3 ml/s`: amikor a kávéba szorult levegő kikiszorult és a puck tele van vízzel, a flow drasztikusan csökken — ez jelzi, hogy a szaturáció befejeződött.

---

### 4. Dripping (preinfusion) — 6 s, nincs target

| Paraméter | Érték |
|---|---|
| Pump target | pressure |
| Nyomás | 0.1 bar |
| Flow-korlát | nincs (0) |
| Hőmérséklet | 88 °C |
| Transition | ease-out / 2 s / adaptive |
| Stop trigger | időalapú (6 s hard cap) |

**Logika:** A nyomás szinte nullára esik (0.1 bar — csak a víz gravitációs nyomása). Ez a fázis lehetővé teszi, hogy a tele szaturált puckban a feszültség csökkenjen, a víz egyenletesen szétterjedjen, és a CO₂-buborékok kijöjjenek. Hasonlít a hagyományos "bloom" koncepcióhoz, de aktív pumpanyomás nélkül. Ez csökkenti a channeling kockázatát az extraction megkezdése előtt.

---

### 5. Pressurize (brew) — 6 s max, három target

| Paraméter | Érték |
|---|---|
| Pump target | pressure |
| Nyomás setpoint | **11 bar** |
| Flow-korlát | 3.5 ml/s |
| Hőmérséklet | 88 °C |
| Transition | linear / 6 s / adaptive |
| Stop trigger | pumped ≥ 100 ml **vagy** pressure ≥ 8.8 bar **vagy** volumetric ≥ 38 g **vagy** 6 s |

**Logika:** Ez a ramp-fázis, ahol a nyomás gyorsan emelkedik a főextrakciós szintre. A **11 bar setpoint** magasnak tűnik, de a `flow: 3.5` soft korlát és a `pressure ≥ 8.8 bar` target együttesen szabályozzák: amint eléri a 8.8 bar-t, a fázis véget ér, nem éri el a 11 bar-t. A `linear` transition garantálja az egyenletes rampolást. A `volumetric ≥ 38 g` target itt safety korai stop — ha a mérleg már 38 g-nál jár (rendkívül ritka ebben a fázisban), azonnal átvált.

---

### 6. Extraction (brew) — 60 s max, két target

| Paraméter | Érték |
|---|---|
| Pump target | flow |
| Flow setpoint | **-1** (tartsd a belépéskori értéket) |
| Nyomáskorlát | 9.5 bar |
| Hőmérséklet | 88 °C |
| Transition | instant / 0 s / adaptive |
| Stop trigger | pumped ≥ 100 ml **vagy** volumetric ≥ 38 g **vagy** 60 s |

**Logika:** Ez a leginnovatívabb fázis. A `flow: -1` sentinel azt jelenti, **a firmware tartja a Pressurize végén mért flow értéket** — így az extraction flow-ja automatikusan a puck ellenállásához kalibrálódik. Ha a puck sűrűbb (finomabb őrlés, magasabb tömörítés), alacsonyabb flow-val, ha lazább, magasabb flow-val fut. A `pressure: 9.5` soft korlát megakadályozza a túlnyomást. A stop az első tüzelő target alapján: ha `volumetric ≥ 38 g` (scale csatlakozva), vagy `pumped ≥ 100 ml`, vagy 60 s timeout.

> **Megjegyzés:** A `pumped ≥ 100 ml` target az Extraction fázisban safety paraméter: megakadályozza, hogy a fázis a duration-korlát (60 s) lejártáig fusson, ha a flow megáll vagy blokkol — de normál körülmények között a `volumetric` target tüzel hamarabb.

---

## Alap recept

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Cél hozam | **36–40 g** |
| Ideális hozam | **38 g** |
| Teljes profilidő | **25–40 s** (adaptív) |
| Hőmérséklet (Prefill/Fill) | **93 °C** |
| Hőmérséklet (extraction) | **88 °C** |
| Arány | **1:2.0–1:2.5** |
| Őrlés tartomány | **Fine zóna (DF64V: ~8–11)** |
| Fordulat | **1200 RPM** |
| Kosár | **IMS B682TH24.5M** |
| Volumetric stop | **38 g beverage weight** (ha scale csatlakozik) |
| Safety timeout | **60 s** (Extraction hard cap) |

### Első shot

**18.5 g be · grind 9–10 · 1200 RPM · 93/88 °C · cél 38 g ki · scale csatlakozva ajánlott**

---

## GaggiMate Pro fázisok

| # | Fázis | Kat. | Max idő | Hő | Pump target | Nyomás / Flow | Stop trigger |
|---:|---|---|---:|---:|---|---:|---|
| 1 | Prefill | PI | **5 s** | 93 °C | flow | 8 ml/s | pumped ≥ 100 ml |
| 2 | Fill | PI | **12 s** | 93 °C | flow | 8 ml/s | pumped ≥ 100 ml / pressure ≥ 3 bar |
| 3 | Compressing | PI | **12 s** | 88 °C | pressure | 3 bar | pumped ≥ 100 ml / flow ≤ 3 ml/s |
| 4 | Dripping | PI | **6 s** | 88 °C | pressure | 0.1 bar | időalapú |
| 5 | Pressurize | brew | **6 s** | 88 °C | pressure | 11 bar / 3.5 ml/s | pumped ≥ 100 ml / pressure ≥ 8.8 bar / volumetric ≥ 38 g |
| 6 | Extraction | brew | **60 s** | 88 °C | flow | **-1** / 9.5 bar | pumped ≥ 100 ml / volumetric ≥ 38 g |

> A valós profilidő **25–40 s** között változik a puck ellenállásától és az őrléstől függően. A táblázatban szereplő idők maximális (hard cap) értékek.

---

## Fázis logika összefoglalva

```
Prefill (93°C, flow 8)  ──pumped≥100──►  Fill (93°C, flow 8)
                                              │
                              pumped≥100 OR pressure≥3 bar
                                              │
                                              ▼
                                    Compressing (88°C, 3 bar)
                                              │
                              pumped≥100 OR flow≤3 ml/s
                                              │
                                              ▼
                                     Dripping (88°C, 0.1 bar, 6s fix)
                                              │
                                              ▼
                                   Pressurize (88°C, 11 bar ramp)
                                              │
                              pressure≥8.8 bar OR volumetric≥38g
                                              │
                                              ▼
                                   Extraction (88°C, flow=-1, 9.5 bar cap)
                                              │
                              volumetric≥38g OR pumped≥100 OR 60s
                                              │
                                              ▼
                                            STOP
```

---

## Összehasonlítás a többi profillal

| Jellemző | Adaptive v2 | Wangera / Burundi stb. |
|---|---|---|
| Fázisváltás logikája | Target-vezérelt (adaptív) | Időalapú (fix) |
| Preinfusion struktúra | 4 fázis (Fill → Compressing → Dripping) | 3 fázis (Wetting → Saturation → Bloom) |
| Hőmérséklet | 93°C → 88°C (kétszintű) | Egységes (94.5–95°C) |
| Extraction control | Flow-hold (flow=-1) + pressure cap | Pressure-hold + flow cap |
| Főnyomás | ~8.8–9.5 bar (magasabb) | 7.2–7.6 bar |
| Hozam célszám | 38 g | 42–43 g |
| Arány | 1:2.0–2.5 | 1:2.2–2.3 |
| Pörkölt célcsoport | Light–Medium, fine grind | Profil-specifikus |
| Scale igény | Ajánlott (volumetric stop) | V1: opcionális, V2: kötelező |

---

## Dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **38 g körül megáll, élénk, tiszta, jó extrakt** | Profil helyes. Jegyezd fel az őrlést. |
| **25 s alatt fut le, hozam 38 g alatt, vékony/savas** | Az őrlés túl durva; menj finomabbra 1–2 jelöléssel. |
| **40 s felett jár, slow extraction, sűrű/keserű** | Az őrlés túl finom; menj durvább irányba. |
| **Compressing fázisban megakad, timeout (12 s)** | Túl finom őrlés vagy túltömörítés — ellenőrizd WDT/tamp. |
| **38 g volumetric megáll, de lapos, kevés édesség** | Hozam target emelése 40 g-ra (JSON szerkesztése); vagy hő 90–91 °C-ra. |
| **Jó hozam, de keserű, testes** | Hő csökkentése 86–87 °C-ra, vagy hozam 36 g-ra. |
| **Safety timeout (60 s) lép életbe** | Bluetooth megszakadt vagy flow teljesen blokkolt; scale + puck prep ellenőrzés. |
| **Naked portafilteren spriccel** | WDT fokozott figyelme; Dripping fázis 8 s-ra hosszabbítható. |

---

## Mérleg / stop workflow

A profil Extraction fázisában **`volumetric ≥ 38 g`** target van, tehát:

- **Scale csatlakozva:** automatikus stop 38 g beverage weight elérésekor
- **Scale nélkül:** a `pumped ≥ 100 ml` target viszonylag hamar tüzelhet (a Fill + Compressing + Pressurize fázisokban már pumpált víz beleszámít-e, fázishatáron nullázódik) — de a 60 s hard cap a végleges fallback

> **Fontos:** A `pumped` target fázis szinten nullázódik. Az Extraction fázisba belépve a számlálás nulláról indul. A 100 ml-es pumped target az Extraction fázisban tehát ~100 ml plusz pumpált vizet jelent az extraction során — ez normál körülmények között nem tüzel hamarabb, mint a volumetric target.

---

## Rövid menthető recept

**Adaptive v2 – Univerzális Light–Medium**

**18.5 g · grind 9–10 (fine zóna) · 1200 RPM · 93/88 °C · cél 38 g ki · volumetric stop**

---

## Technikai megjegyzések a firmware-rel kapcsolatban

- **`flow: -1` sentinel** az Extraction fázisban: a firmware a fázisba belépéskori mért flow értéket tartja célnak a teljes Extraction alatt. Ez de facto flow-hold módot jelent.
- **`pumped` target** több fázisban: fázis-szintű számlálás, minden fázishatáron nullázódik.
- **OR logika** a targets tömbökben: az első tüzelő target azonnal zárja a fázist.
- **88 °C hőmérsékletre váltás** a Compressing fázistól: ez nem azonnali — a boiler tényleges hőmérséklete késve követi a setpointot. A valós extraction hőmérséklet 88 és 93 °C között lesz, közelebb a 90–91 °C-hoz, ha a preinfusion rövid volt.
