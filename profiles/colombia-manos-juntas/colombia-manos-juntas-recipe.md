# Impresso Colombia Manos Juntas Jam Mango 18.5-43 39s

**Kávé:** Impresso Colombia Manos Juntas  
**Feldolgozás:** anaerobic natural  
**Eredet:** Colombia, Cauca, Manos Juntas micromill  
**Ízjegyek:** vörösáfonya dzsem · karamell · mangó  
**Setup:** DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár  
**Őrlőskála:** 0-90, egész jelölések  
**Fordulat:** 1200 RPM baseline  
**Stop:** idő/fázis alapú profil + kézi mérleges figyelés; BOOKOO mérleg jelenleg nincs.

---

## Profil grafikon

![Profile graph](colombia-manos-juntas-profile.png)


## Cél ízprofil

dzsemes vörösáfonya, mangó, karamelles édesség; legyen szirupos és gyümölcsös, de ne fermentáltan nehéz vagy száraz

---

## Miért ilyen a profil?

A Colombia Manos Juntas dzsemes, karamelles és mangós irányához kicsit hosszabb, 39 s-os profil készült. A cél a szirupos gyümölcsösség és édesség, miközben a végnyomás nem engedi túl száraz vagy alkoholosan nehéz irányba a shotot.

---

## Alap recept

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Cél hozam | **42.0-44.0 g** |
| Ideális hozam | **43.0 g** |
| Teljes profilidő | **39 s** |
| Cél idő | **38-40 s** |
| Hőmérséklet | **94.5 °C** |
| Őrlés indulás | **10 körül** |
| Őrlés tartomány | **10-11** |
| Fordulat | **1200 RPM** |
| Kosár | **IMS B682TH24.5M** |

### Első shot

**18.5 g be · grind 10 körül · 1200 RPM · 94.5 °C · 39 s teljes profil · cél 43.0 g ki**

---

## GaggiMate Pro fázisok

| # | Fázis | Idő | Hő | Pump target | Nyomás / Flow |
|---:|---|---:|---:|---|---:|
| 1 | Jam Wetting | **5 s** | 94.5 °C | flow | 8.0 ml/s |
| 2 | Mango Saturation | **8 s** | 94.5 °C | pressure | 2.3 bar / 4.5 ml/s |
| 3 | Sweet Bloom | **4 s** | 94.5 °C | pressure | 0.5 bar / 0 ml/s |
| 4 | Soft Ramp | **6 s** | 94.5 °C | pressure | 7.3 bar / 2.4 ml/s |
| 5 | Jam Extraction | **12 s** | 94.5 °C | pressure | 7.3 bar / 2.1 ml/s |
| 6 | Caramel Finish | **4 s** | 94.5 °C | pressure | 5.5 bar / 1.7 ml/s |
|  | **Összesen** | **39 s** |  |  |  |

Automatikus előreléptető targetek nincsenek; a profil idő alapján fut végig.

---

## Dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **42-44g, dzsemes/mangós/karamelles, szirupos** | Marad a profil és a 10 körüli induló őrlés. |
| **túl savas, kevés mangó/édesség** | Hő 95C vagy engedd 43.5-44g-ig. |
| **túl nehéz, alkoholos, fermentált vagy száraz** | Hő 94C, rövidebb hozam 41.5-42.5g körül. |
| **40g alatt marad** | Ellenőrizd WDT/tamp/screen stabilitását; ha stabil, menj 11 felé. |
| **45g fölé fut vagy vékony** | Menj 10 felé finomabbra, vagy kézi stop 43g körül. |

---

## Mérleg / stop workflow – V3 (időalapú)

Ez a recept **idő/fázis alapú GaggiMate profil** (`colombia-manos-juntas-39s.json`). A célhozamot külön mérlegen kell figyelni és kézzel megállítani.

---

## V4 – Bluetooth Scale Edition

**Szükséges hardver:** BOOKOO Themis Ultra + GaggiMate Pro Bluetooth kapcsolat

**V4 profil fájl:** [`colombia-manos-juntas-39s-scale-v4.json`](colombia-manos-juntas-39s-scale-v4.json)

### V4 paraméterek

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Target Yield | **43.0 g** |
| Arány | **1:2.32** |
| Hőmérséklet | **94.5 °C** |
| Stop mód | **beverage weight** |
| Stop | **43.0 g beverage weight** |
| Safety timeout | **47 s** |

### V4 fázis stop logika

| Fázis | Stop trigger | Duration (hard cap) |
|---|---|---:|
| Jam Wetting | időalapú | 5 s |
| Mango Saturation | időalapú | 8 s |
| Sweet Bloom | időalapú | 4 s |
| Soft Ramp | időalapú | 6 s |
| Jam Extraction | **volumetric target: 43.0 g** | 32 s |
| Caramel Finish | időalapú (csak ha a target korán tüzel) | 8 s |

> **Firmware viselkedés (`pro` típus):** A `targets` tömb fázis szinten működik — minden 100 ms-ban kiértékeli. Az OR feltételek közül az első tüzelés zárja a fázist. A `duration` mindig hard cap: ha a volumetric target 43.0 g-nál tüzel, a Jam Extraction fázis azonnal véget ér. Ha a scale nem csatlakozik vagy a target nem tüzel, a 32 s-os duration zárja a fázist (safety fallback). A `volumetric` target csak aktív Bluetooth scale + brew-by-weight mód esetén működik.

### V4 dial-in

| Eredmény | Következő lépés |
|---|---|
| **42-44 g, dzsemes/mangós/karamelles, szirupos** | A Scale V4 profil helyes, nincs teendő. |
| **Túl savas, kevés mangó/édesség** | stop_at_g értéket emeld 43.5-44.0 g-ra, vagy próbálj 95 °C-ot. |
| **Túl nehéz, alkoholos, fermentált** | stop_at_g értéket csökkentsd 42.0-42.5 g-ra. |
| **Safety timeout (47 s) lép életbe** | Bluetooth megszakadt vagy flow túl lassú. |

---

## Rövid menthető recept

**Colombia Manos Juntas Jam Mango**

**V3 (időalapú):** 18.5 g · grind 10 körül · 1200 RPM · 94.5 °C · 39 s · 43.0 g out cél

**V4 (Scale):** 18.5 g · grind 10 körül · 1200 RPM · 94.5 °C · stop 43.0 g beverage weight · safety 47 s
