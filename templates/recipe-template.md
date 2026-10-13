# {Pörkölő} - {Kávé} {Profilnév} — {Aktuális verzió} dial-in

| Mező | Érték |
|---|---|
| Kávé | {Pörkölő} - {Kávé} |
| Feldolgozás | {washed / natural / honey / anaerobic …} |
| Eredet | {ország, régió, farm / állomás} |
| Ízjegyek | {ízjegy} · {ízjegy} · {ízjegy} |
| Setup | DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) |
| Őrlőskála | 0–90, egész jelölések |
| Mérleg | BOOKOO Themis Ultra, Bluetooth brew-by-weight |
| Aktuális profil | **{Scale V1 / Manual …}** |
| Státusz | **{első dial-in / bevált baseline / optimalizálás: mire}** |
| Frissítve | **{ÉÉÉÉ-HH-NN} · {melyik shot vagy teszt után}** |

---

## Cél ízprofil

_Milyen csészét keresünk: édesség, savasság, test, utóíz — és mit kell elkerülni (vékony, száraz, túl fermentált …). A következő fejlesztési cél egy mondatban._

---

## Aktuális következő baseline — {Verzió}

_Miért ez a baseline: melyik shot vagy teszt után, és mit változtat az előzőhöz képest (egy-két mondat)._

| Paraméter | {Verzió} következő érték |
|---|---:|
| Dózis | **{18.5} g** |
| Végső célhozam | **{42.0} g** |
| Arány | **1:{2.27}** |
| Hőmérséklet | **{94.0} °C** |
| Őrlés | **{10}** |
| Fordulat | **1200 RPM** |
| Profil | **{kave-scale.json}** |
| {Fázis neve} | **{flow vagy nyomás · idő}** |
| {Fő extrakció} váltás | **{38.0} g** |
| Végső pumpastop | **{40.5} g** |

### Következő shot

**{18.5} g be · grind {10} · 1200 RPM · {94.0} °C · {Verzió} · {38.0} g-nál {Finish} · {40.5} g-nál végső stop**

**Elsődleges megfigyelési pont:** _a fő extrakció előtt (kb. {17} s-nál) mennyi ital legyen a csészében, pl. {6–9} g — ebből a shot közben látszik, jó irányba megy-e._

---

## {ÉÉÉÉ-HH-NN} — Shot #{szám} / {mit teszteltünk}

**Beállítás:** {18.5} g · grind {10} · 1200 RPM · {94.0} °C · {Verzió}  
**Eredmény:** **{42.4} g / {39.8} s**

| Megfigyelés | Érték / jelentés |
|---|---|
| {Ramp} végére | **{17.9} g** a csészében |
| Fő extrakció tényleges nyomása | kb. **{x.x} bar** |
| Végső tömeg | **{42.4} g** — a mérleges stop pontos volt? |
| Íz | {mit adott a csésze} |

### Következtetés

- {Mit tanultunk ebből a shotból.}
- {Mi marad, mit zárunk le.}
- {Mi a következő változtatás, és miért.}

_Minden újabb mért shot vagy teszt új szakaszt kap ugyanígy, a legújabb kerül felülre._

---

## {Verzió} — GaggiMate Pro fázisok

| # | Fázis | Hard cap | Hő | Pump target | Nyomás / Flow | Stop trigger |
|---:|---|---:|---:|---|---:|---|
| 1 | {Wetting} | **{5} s** | {94.0} °C | flow | **{6.8} ml/s** | idő |
| 2 | {Saturation} | **{8} s** | {94.0} °C | pressure | **{2.2} bar / {3.8} ml/s** | idő |
| 3 | {Bloom} | **{4} s** | {94.0} °C | pressure | {0.5} bar | idő |
| 4 | {Ramp} | **{6} s** | {94.0} °C | pressure | {7.2} bar / {2.4} ml/s | idő |
| 5 | {Fő extrakció} | **{30} s** | {94.0} °C | pressure | {7.2} bar / {2.1} ml/s | **≥ {38.0} g** |
| 6 | {Finish} | **{8} s** | {94.0} °C | pressure | {5.4} bar / {1.7} ml/s | **≥ {40.5} g** |
|  | **JSON maximum** | **{61} s** |  |  |  |  |

_A `duration` minden fázisban hard cap; a mérleges target csak korábban zárhat. A célhozamhoz két stop kell (fő extrakció → finish → pumpastop), és a pumpastop után még csepeg: a végső tömeg kb. 1–2 g-mal több. A profiloldal a fázistáblázatot a JSON-ból maga is kirajzolja; ez itt a recept önálló olvasásához kell._

### Mi változott {előző verzió} → {Verzió}?

- {Paraméter}: **{régi} → {új}**.
- {Mi maradt változatlan.}
- A cél: {mit vártunk a változtatástól}.

---

## Kompatibilitási profilok

- **{Előző Scale verzió}:** {miben tér el az aktuálistól}.
- **Manual {xx} s:** teljesen időalapú fallback profil, mérleg nélkül.

---

## {Verzió} dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **{megfigyelési pont rendben}, jó íz** | marad a {Verzió} és grind {10} |
| **{megfigyelési pont alatt} — fojtott indulás** | prep ellenőrzés (WDT/tamp/screen); ha stabil, egy lépés durvábbra |
| **{megfigyelési pont felett} — gyors indulás / spriccel** | prep ellenőrzés; ha kell, egy lépés finomabbra |
| **Savanyú / vékony** | {hő +0.5 °C vagy finomabb őrlés} |
| **Száraz / keserű** | {végsúly −0.5–1 g vagy hő −0.5 °C} |
| **{38.0} g-nál nem vált {Finish}-re** | BOOKOO kapcsolat, tare és brew-by-weight mód ellenőrzése |
| **{40.5} g-nál nem áll meg** | {Finish} target és mérlegadat ellenőrzése |

---

## Rövid menthető recept

**{Kávé} {Profilnév} — {Verzió}**

**{18.5} g · grind {10} · 1200 RPM · {94.0} °C · {korai fázisok röviden} · {38.0} g-nál {Finish} · {40.5} g-nál pumpastop**
