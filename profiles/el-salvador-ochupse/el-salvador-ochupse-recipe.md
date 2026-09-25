# El Salvador Ochupse – Grape Rose 18.5-41 – 93C Scale V3

| Mező | Érték |
|---|---|
| Pörkölő | Impresso |
| Kávé | El Salvador Ochupse |
| Régió | Apaneca-Ilamatepec |
| Farm | Ochupse, Santa Ana parcella |
| Variáns | Pacas |
| Feldolgozás | natural anaerob, 60 óra |
| Ízjegyek | szőlő · csipkebogyó · sárgabarack · étcsokoládé |
| Setup | Gaggia Classic Pro 2025 + GaggiMate Pro / DF64V Gen 2 + SSP Sweet Lab Espresso V3 / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) |
| Őrlőskála | 0-90, egész jelölések |
| Fordulat | 1200 RPM baseline |
| Stop | V1: idő/fázis alapú profil + kézi mérleges figyelés. V3: BOOKOO Themis Ultra automatikus beverage-weight stop. |

---

## Ízcél

A profil célja, hogy a natural anaerob feldolgozásból származó **szőlős és csipkebogyós gyümölcsösséget** megőrizze, miközben a nyomáscsökkentett befejezés visszahozza az **étcsokoládé** kellemes balansz-záró ízét. A V3 profil még kíméletesebbé vált az előáztatásban, hogy a finom aromák konzerválódnak.

---

## Kiinduló recept – V1 (időalapú)

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Célhozam | **40–42 g** |
| Ideális hozam | **41 g** |
| Arány | **1:2.22** |
| Hőmérséklet | **93 °C** |
| Előáztatás | **10 s** |
| Profilidő | **31 s** |
| Célidő | **29–34 s** |
| Őrlés indulás | **10–11 között, elsőre inkább 10 felé** |
| Stop | **41 g körül kézzel** |

Az Impresso saját ajánlása 18 g bemenő, 40 g kijövő, 93 °C, 10 másodperc előáztatás és 29 másodperc teljes idő. A 18.5 g-os dózisra arányosan számolva a célhozam kb. 41 g.

### Első shot – V1

**18.5 g · 1200 RPM · őrlés 10–11 között, inkább 10 felé · 93 °C · 41 g ki · 29–34 s**

---

## GaggiMate Pro fázisok – V1

| # | Fázis | Idő | Hő | Pump target | Nyomás / Flow |
|---:|---|---:|---:|---|---:|
| 1 | Grape Wetting | **4 s** | 93 °C | flow | 7.5 ml/s |
| 2 | Rosehip Saturation | **6 s** | 93 °C | pressure | 2.2 bar / 4.2 ml/s |
| 3 | Gentle Ramp | **5 s** | 93 °C | pressure | 7.2 bar / 2.4 ml/s |
| 4 | Apricot Extraction | **12 s** | 93 °C | pressure | 7.2 bar / 2.1 ml/s |
| 5 | Chocolate Finish | **4 s** | 93 °C | pressure | 5.4 bar / 1.7 ml/s |
|  | **Összesen** | **31 s** |  |  |  |

A profil targetless, ezért idő alapján fut végig. A célhozamot külön mérlegen figyeld, és 41 g körül állítsd meg.

---

## Dial-in logika – V1

| Eredmény | Következő lépés |
|---|---|
| **40–42 g, 29–34 s, stabil stream** | marad a profil és az őrlés |
| **41 g 25–27 s alatt vagy spriccel** | picit finomabbra 10 felé; WDT és tamp ellenőrzés |
| **41 g 36–40 s felett, fojtott** | picit durvábbra 11 felé |
| **túl savas / éretlen sárgabarackos** | először 42 g-ig engedd; ha kell, 93.5 °C |
| **túl fermentált / boros** | 40 g körül állítsd meg; szükség esetén 92.5 °C |
| **száraz vagy keserű csokoládés** | rövidebb hozam 39.5–40.5 g vagy 92.5 °C |
| **több stream / oldalirányú spricc** | puck prep javítása; ne csak az őrlést változtasd |

---

## Mérleg / stop workflow – V1 (időalapú)

Ez a recept **idő/fázis alapú GaggiMate profil** (`el-salvador-ochupse-manual.json`). A célhozamot külön mérlegen kell figyelni és kézzel megállítani.

---

## V3 – Bluetooth Scale Edition (Grind 11)

**Szükséges hardver:** BOOKOO Themis Ultra + GaggiMate Pro Bluetooth kapcsolat

**V3 profil fájl:** [`el-salvador-ochupse-93c-scale-v3.json`](profiles/el-salvador-ochupse/el-salvador-ochupse-93c-scale-v3.json)

A BOOKOO Themis Ultra legyen bekapcsolva, párosítva és nullázva a főzés előtt. A gyártó szerint a Themis Ultra Bluetooth 5.0 kapcsolatot használ; az eszköz neve jellemzően `BOOKOO_SC U...`.

### V3 paraméterek

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Grinder Setting | **Grind 11** |
| Target Yield | **41.0 g** |
| Arány | **1:2.22** |
| Hőmérséklet | **93 °C** |
| Előáztatás | **10 s (4 s wetting + 6 s saturation)** |
| Main Extraction | **Flow-based, declining pressure** |
| Stop mód | **GaggiMate volumetric target, BOOKOO Bluetooth mérleggel** |
| Safety timeout | **50 s** |

### V3 fázis stop logika

| # | Fázis | Max. idő | Hő | Pump target | Nyomás / Flow | Stop |
|---:|---|---:|---:|---|---:|---|
| 1 | Grape Wetting | **4 s** | 93 °C | flow | 5.5 ml/s | idő |
| 2 | Rosehip Saturation | **6 s** | 93 °C | pressure | 2.2 bar / 4.2 ml/s | idő |
| 3 | Gentle Ramp | **5 s** | 93 °C | pressure | 7.2 bar / 2.4 ml/s | idő |
| 4 | Grape Rose Extraction | **35 s** | 93 °C | flow decline | 5.2 bar / 1.8 ml/s | **volumetric target: 41.0 g** |
|  | **Teljes hard cap** | **50 s** |  |  |  |  |

A V3 profil kíméletes előáztatást használ (5.5 ml/s wetting helyett 7.5 ml/s-ról csökkent), és a fő extrakció flow-alapú, nyomáscsökkentéssel. Az 1.8 ml/s flow extraction az ízjegyek megőrzésére van optimalizálva. A **41.0 g-os target a fő extrakciós fázisban aktív**, így a GaggiMate a csésze alatt lévő mérleg súlyadata alapján automatikusan leállítja a shotot.

### Első shot – V3

**18.5 g · 1200 RPM · grind 11 · 93 °C · BOOKOO stop 41.0 g**

### V3 dial-in

| Eredmény | Következő lépés |
|---|---|
| **41 g, kb. 30–36 s, stabil stream, jó gyümölcsösség és csokoládé** | marad a profil |
| **41 g 25–28 s alatt vagy spriccel** | picit finomabbra; WDT/tamp/screen ellenőrzés |
| **41 g 37–42 s, fojtott start** | picit durvábbra, grind 12 felé |
| **túl savas / éretlen szőlős** | target **42.0 g**, vagy 93.5 °C csak stabil flow után |
| **túl fermentált / alkoholos boros** | target **40.0 g**, szükség esetén 92.5 °C |
| **száraz / keserű / étcsokoládé túl erős** | target **39.5–40.0 g** vagy 92.5 °C |
| **41 g-nál nem lép ki Grape Rose fázisból** | Bluetooth kapcsolat, mérleg-adat és brew-by-weight mód ellenőrzése |

### BOOKOO indulási ellenőrzés – V3

1. Kapcsold be a mérleget.
2. Ellenőrizd a GaggiMate-ben, hogy csatlakozott.
3. Tedd rá a csészét és tárázd.
4. Finoman nyomd meg a csészét: a GaggiMate kijelzett tömegének változnia kell.
5. Csak ezután indítsd a profilt.

A mérleg a végső hozamot stabilizálja, de a spriccelést, több streamet vagy channelinget nem javítja meg; ezeknél továbbra is a puck prep és az őrlés a döntő.

---

## Rövid menthető recept

**El Salvador Ochupse Grape Rose – Grind 11**

**V1 (időalapú):** 18.5 g · grind 10–11 között, inkább 10 felé · 1200 RPM · 93 °C · 31 s · 41 g out cél

**V3 (Scale):** 18.5 g · grind 11 · 1200 RPM · 93 °C · stop 41.0 g beverage weight · safety 50 s
