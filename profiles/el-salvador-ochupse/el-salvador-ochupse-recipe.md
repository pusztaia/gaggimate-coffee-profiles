# El Salvador Ochupse – Grape Rose

| Mező | Érték |
|---|---|
| Pörkölő | Impresso Micro Roastery |
| Kávé | El Salvador Ochupse |
| Régió | Apaneca-Ilamatepec |
| Farm | Ochupse, Santa Ana parcella |
| Variáns | Pacas |
| Feldolgozás | natural anaerob, 60 óra |
| Ízjegyek | szőlő · csipkebogyó · sárgabarack · étcsokoládé |
| Setup | Gaggia Classic Pro 2025 + GaggiMate Pro / DF64V Gen 2 + SSP Sweet Lab Espresso V3 / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) |
| Őrlőskála | 0-90, egész jelölések |
| Fordulat | 1200 RPM baseline |
| Stop | V1: idő/fázis alapú profil + kézi mérleges figyelés. V2: BOOKOO Themis Ultra automatikus beverage-weight stop. |

---

## Ízcél

A profil célja, hogy a natural anaerob feldolgozásból származó **szőlős és csipkebogyós gyümölcsösséget** megőrizze, miközben a nyomáscsökkentett befejezés visszahozza az **étcsokoládés lecsengést**, és nem engedi túl dominánssá válni a fermentált karaktert.

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

### Első shot

**18.5 g · 1200 RPM · grind 10–11 között, inkább 10 felé · 93 °C · 41 g ki · 29–34 s**

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

Ez a recept **idő/fázis alapú GaggiMate profil** (`el-salvador-ochupse-31s-93c.json`). A célhozamot külön mérlegen kell figyelni és kézzel megállítani.

---

## V2 – Bluetooth Scale Edition

**Szükséges hardver:** BOOKOO Themis Ultra + GaggiMate Pro Bluetooth kapcsolat

**V2 profil fájl:** [`el-salvador-ochupse-31s-93c-scale-v2.json`](el-salvador-ochupse-31s-93c-scale-v2.json)

A BOOKOO Themis Ultra legyen bekapcsolva, párosítva és nullázva a főzés előtt. A gyártó szerint a Themis Ultra Bluetooth 5.0 kapcsolatot használ; az eszköz neve jellemzően `BOOKOO_SC U XXXX` formátumú. A GaggiMate dokumentációja szerint a `volumetric` target Bluetooth mérleggel működik a legpontosabban.

### V2 paraméterek

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Target Yield | **41.0 g** |
| Arány | **1:2.22** |
| Hőmérséklet | **93 °C** |
| Előáztatás | **10 s** |
| Stop mód | **GaggiMate volumetric target, BOOKOO Bluetooth mérleggel** |
| Safety timeout | **45 s** |

### V2 fázis stop logika

| # | Fázis | Max. idő | Pump target | Nyomás / Flow | Stop |
|---:|---|---:|---|---:|---|
| 1 | Grape Wetting | **4 s** | flow | 7.5 ml/s | idő |
| 2 | Rosehip Saturation | **6 s** | pressure | 2.2 bar / 4.2 ml/s | idő |
| 3 | Gentle Ramp | **5 s** | pressure | 7.2 bar / 2.4 ml/s | idő |
| 4 | Grape Chocolate Extraction to 41g | **30 s** | pressure decline | 7.2 → 5.2 bar | **volumetric target: 41.0 g** |
|  | **Teljes hard cap** | **45 s** |  |  |  |

Ez az El Salvador Ochupse profil első BOOKOO Themis Ultra kompatibilis verziója. A 41.0 g-os target már a 15. másodperctől induló fő extrakciós fázisban aktív, így a GaggiMate a csészében mért tömeg alapján tudja befejezni a shotot. Ha a scale nem csatlakozik vagy a target nem tüzel, a 30 s-os duration zárja a fázist (safety fallback).

### Első shot – V2

**18.5 g · 1200 RPM · őrlés 10–11 között, inkább 10 felé · 93 °C · BOOKOO stop 41.0 g**

### V2 dial-in

| Eredmény | Következő lépés |
|---|---|
| **41 g, kb. 29–35 s, stabil stream, jó íz** | marad a profil |
| **41 g 26–28 s alatt vagy spriccel** | picit finomabbra; WDT/tamp/screen ellenőrzés |
| **41 g 36–42 s, fojtott** | picit durvábbra, 11 felé |
| **túl savas / éretlen** | target **42.0 g**, vagy 93.5 °C csak stabil flow után |
| **túl fermentált / boros** | target **40.0 g**, szükség esetén 92.5 °C |
| **száraz / keserű** | target **39.5–40.0 g** vagy 92.5 °C |

### BOOKOO indulási ellenőrzés

1. Kapcsold be a mérleget.
2. Ellenőrizd a GaggiMate-ben, hogy csatlakozott.
3. Tedd rá a csészét és tárázd.
4. Finoman nyomd meg a csészét: a GaggiMate kijelzett tömegének változnia kell.
5. Csak ezután indítsd a profilt.

A mérleg a végső hozamot stabilizálja, de a spriccelést, több streamet vagy channelinget nem javítja meg; ezeknél továbbra is a puck prep és az őrlés a döntő.

---

## Rövid menthető recept

**El Salvador Ochupse Grape Rose**

**V1 (időalapú):** 18.5 g · grind 10–11 között, inkább 10 felé · 1200 RPM · 93 °C · 31 s · 41 g out cél

**V2 (Scale):** 18.5 g · grind 10–11 között, inkább 10 felé · 1200 RPM · 93 °C · stop 41.0 g beverage weight · safety 45 s
