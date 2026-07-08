# Kenya Wangera Creamy Fruit 18.5-42 – Stable Start 38s 94.5C

![Profile graph](wangera-profile.png)

**Kávé:** Impresso Kenya Wangera  
**Ízjegyek:** szeder · tejszín · pomelo  
**Setup:** DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár  
**Őrlőskála:** 0-90, egész jelölések  
**Fordulat:** 1200 RPM baseline  
**Státusz:** bevált baseline – 42 g hozam  
**Verzió:** 2026-07-04 – Stable Start 38s 94.5C, grind 10-11 között inkább 11 felé

---

## Aktuális bevált baseline

A 94.5 °C-os Stable Start 38s profil **42 g hozamot adott**, amikor az őrlés a **10-11 közötti zónában, inkább 11 felé** volt állítva.

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Cél hozam | **41-43 g** |
| Ideális hozam | **42 g** |
| Teljes profilidő | **38 s** |
| Hőmérséklet | **94.5 °C** |
| Őrlés indulás | **10-11 között, inkább 11 felé** |
| Fordulat | **1200 RPM** |
| Kosár | **IMS B682TH24.5M** |
| Stop | **időalapú profil + kézi mérleges figyelés** |

### Következő shot

**18.5 g be · grind 10-11 között, inkább 11 felé · 1200 RPM · 94.5 °C · 38 s teljes profil · 42 g cél**

---

## Korai hozam diagnosztika

A Soft Ramp indulása előtt kb. **17 s** telt el. Eddig a pontig a mostani tesztben kb. **9 g** jött le, és a végső hozam **42 g** lett. Ez alapján a korábbi 6-8 g célzónát ennél a beállításnál **6-9 g**-ra bővítjük.

| 17 s / Soft Ramp előtti hozam | Értelmezés | Teendő |
|---:|---|---|
| **3-4 g** | fojtott indulás, várhatóan 36-40 g vége | WDT/tamp/screen ellenőrzés; ha stabil a prep, menj picit 11 felé |
| **6-9 g** | egészséges indulás | marad a profil és az őrlési zóna |
| **10 g+** | túl gyors indulás vagy channeling gyanú | puck prep ellenőrzés; ha kell, picit 10 felé / finomabbra |

---

## GaggiMate Pro fázisok

| # | Fázis | Idő | Hő | Pump target | Nyomás / Flow |
|---:|---|---:|---:|---|---:|
| 1 | Stronger Wetting | **5 s** | 94.5 °C | flow | 8.0 ml/s |
| 2 | Stable Saturation | **8 s** | 94.5 °C | pressure | 2.3 bar / 4.5 ml/s |
| 3 | Cream Bloom | **4 s** | 94.5 °C | pressure | 0.5 bar |
| 4 | Soft Ramp | **6 s** | 94.5 °C | pressure | 7.4 bar / 2.4 ml/s |
| 5 | Blackberry Extraction | **11 s** | 94.5 °C | pressure | 7.4 bar / 2.1 ml/s |
| 6 | Cream Finish | **4 s** | 94.5 °C | pressure | 5.8 bar / 1.7 ml/s |
|  | **Összesen** | **38 s** |  |  |  |

Automatikus előreléptető targetek nincsenek; a profil idő alapján fut végig.

---

## Dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **17 s körül 6-9 g, végén 41-43 g, jó íz** | marad a Stable Start 38s 94.5C profil |
| **17 s körül 3-4 g, végén 36-40 g** | fojtott indulás: WDT/tamp/screen; ha stabil, picit 11 felé |
| **17 s körül 10 g+, végén 43 g fölött vagy spriccel** | channeling/túl gyors indulás: puck prep; ha kell, picit 10 felé / finomabbra |
| **42 g körül jó, de túl savas/pomelós** | először hozam 42.5-43 g; további hőemelés csak újabb teszt után |
| **42 g körül jó, de száraz/naturalos** | hozam 41 g körül, vagy hő 94 °C-ra vissza |

---

## Rövid menthető recept

**Kenya Wangera Creamy Fruit Stable Start 38s 94.5C**

**18.5 g · grind 10-11 között, inkább 11 felé · 1200 RPM · 94.5 °C · 38 s · 42 g out cél**

---

## Mérleg / stop workflow – V3 (időalapú)

Ez a recept **idő/fázis alapú GaggiMate profil** (`wangera-stable-38s-945c.json`). A célhozamot külön mérlegen kell figyelni és kézzel megállítani.

---

## V4 – Bluetooth Scale Edition

**Szükséges hardver:** BOOKOO Themis Ultra + GaggiMate Pro Bluetooth kapcsolat

**V4 profil fájl:** [`wangera-stable-38s-945c-scale-v4.json`](wangera-stable-38s-945c-scale-v4.json)

### V4 paraméterek

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Target Yield | **42.0 g** |
| Arány | **1:2.27** |
| Hőmérséklet | **94.5 °C** |
| Stop mód | **beverage weight** |
| Stop | **42.0 g beverage weight** |
| Safety timeout | **45 s** |

### V4 fázis stop logika

| Fázis | Stop trigger | Duration (hard cap) |
|---|---|---:|
| Stronger Wetting | időalapú | 5 s |
| Stable Saturation | időalapú | 8 s |
| Cream Bloom | időalapú | 4 s |
| Soft Ramp | időalapú | 6 s |
| Blackberry Extraction | **volumetric target: 42.0 g** | 30 s |
| Cream Finish | időalapú (csak ha a target korán tüzel) | 8 s |

> **Firmware viselkedés (`pro` típus):** A `targets` tömb fázis szinten működik — minden 100 ms-ban kiértékeli. Az OR feltételek közül az első tüzelés zárja a fázist. A `duration` mindig hard cap: ha a volumetric target 42.0 g-nál tüzel, a Blackberry Extraction fázis azonnal véget ér, és a Cream Finish indul. Ha a scale nem csatlakozik vagy a target nem tüzel, a 30 s-os duration zárja a fázist (safety fallback). A `volumetric` target csak aktív Bluetooth scale + brew-by-weight mód esetén működik.

### V4 dial-in

| Eredmény | Következő lépés |
|---|---|
| **42 g körül megáll, szederes/krémes, jó** | A Scale V4 profil helyes, nincs teendő. |
| **Mérleg korán áll meg, hozam 38-40 g, fojtott** | WDT/tamp/screen ellenőrzés; Bluetooth kapcsolat ellenőrzés; ha stabil, picit 11 felé az őrlésen. |
| **Safety timeout (45 s) lép életbe** | Bluetooth megszakadt vagy flow túl lassú. Mérleg párosítás és puck prep ellenőrzés. |
| **42 g körüli hozam, savas/pomelós** | stop_at_g értéket emeld 42.5-43.0 g-ra a JSON-ban. |
| **42 g körüli hozam, száraz/naturalos** | stop_at_g értéket csökkentsd 41.0-41.5 g-ra a JSON-ban. |
