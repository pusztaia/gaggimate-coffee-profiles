# Twenty Eight Finca el Recreo Caturron Flavor 18.5-42 – GaggiMate Pro recept

| Mező | Érték |
|---|---|
| Márka | Twenty Eight |
| Kávé | Finca el Recreo Caturron |
| Ízjegyek | meggy · konyakmeggy · piros gyümölcs · bonbonos édesség |
| Setup | DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) |
| Őrlőskála | 0-90, egész jelölések |
| Verzió | 2026-06-29 – Twenty Eight brand fix, targetless 42s, GitHub-clean |

---

## Cél ízprofil

Sűrű, tiszta, gyümölcsös espresso: **meggy · konyakmeggy · piros gyümölcs · bonbonos édesség**. Nem cél a túl hosszú, híg 45-47 g irány.

---

## Alap recept

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Cél hozam | **40.5-43 g** |
| Ideális hozam | **42 g** |
| Teljes profilidő | **42 s** |
| Cél idő | **40-42 s** |
| Hőmérséklet | **95 °C** |
| Őrlés indulás | **9** |
| Őrlés tartomány | **8-10** |
| Fordulat | **1200 RPM** |
| Fordulat megjegyzés | **DF64V Gen 2 változtatható fordulatú; ez a recept 1200 RPM baseline-ra van hangolva** |
| Kosár | **IMS B682TH24.5M** |

### Következő shot

**18.5 g be · grind 9 · 1200 RPM · 95 °C · 42 s teljes profil · cél 40.5-43 g ki**

---

## GaggiMate Pro fázisok

| # | Fázis | Idő | Hő | Pump target | Nyomás / Flow |
|---:|---|---:|---:|---|---:|
| 1 | Fast Wetting | **4 s** | 95 °C | flow | 8 ml/s |
| 2 | Low Pressure Saturation | **7 s** | 95 °C | pressure | 2.0 bar / 4.5 ml/s |
| 3 | Bloom | **6 s** | 95 °C | pressure | 0.4 bar |
| 4 | Gentle Ramp | **6 s** | 95 °C | pressure | 7.2 bar / 2.4 ml/s |
| 5 | Fruit Extraction | **13 s** | 95 °C | pressure | 7.2 bar / 2.2 ml/s |
| 6 | Sweet Decline | **6 s** | 95 °C | pressure | 5.6 bar / 1.8 ml/s |
|  | **Összesen** | **42 s** |  |  |  |

Automatikus előreléptető targetek nincsenek; a profil idő alapján fut végig.

---

## Dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **40.5-43 g, jó íz** | marad **grind 9**, 42 s |
| **43 g fölé fut, vékony/savas** | menj **8** felé vagy állítsd meg 42 g körül |
| **40 g alatt marad, fojtott/száraz** | menj **10** felé |
| **savanyú, de a hozam jó** | hő marad **95 °C**, engedd 42.5-43 g-ig |
| **nehéz, alkoholosan keserű** | hő **94.5 °C** vagy rövidebb hozam **40.5-41.5 g** |
| **naked portafilteren spriccel** | WDT a széleken/aljon, egyenes tamp, tiszta/száraz puck screen |

---

## Mérleg / stop workflow – V1 (időalapú)

Ez a recept **idő/fázis alapú GaggiMate profil** (`caturron-flavor-42s.json`). A célhozamot külön mérlegen kell figyelni és kézzel megállítani.

---

## V2 – Bluetooth Scale Edition

**Szükséges hardver:** BOOKOO Themis Ultra + GaggiMate Pro Bluetooth kapcsolat

**V2 profil fájl:** [`caturron-flavor-42s-scale-v2.json`](caturron-flavor-42s-scale-v2.json)

### V2 paraméterek

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Target Yield | **42.0 g** |
| Arány | **1:2.27** |
| Hőmérséklet | **95 °C** |
| Stop mód | **beverage weight** |
| Stop | **42.0 g beverage weight** |
| Safety timeout | **50 s** |

### V2 fázis stop logika

| Fázis | Stop trigger | Duration (hard cap) |
|---|---|---:|
| Fast Wetting | időalapú | 4 s |
| Low Pressure Saturation | időalapú | 7 s |
| Bloom | időalapú | 6 s |
| Gentle Ramp | időalapú | 6 s |
| Fruit Extraction | **volumetric target: 42.0 g** | 35 s |
| Sweet Decline | időalapú (csak ha a target korán tüzel) | 8 s |

> **Firmware viselkedés (`pro` típus):** A `targets` tömb fázis szinten működik — minden 100 ms-ban kiértékeli. Az OR feltételek közül az első tüzelés zárja a fázist. A `duration` mindig hard cap: ha a volumetric target 42.0 g-nál tüzel, a Fruit Extraction fázis azonnal véget ér. Ha a scale nem csatlakozik vagy a target nem tüzel, a 35 s-os duration zárja a fázist (safety fallback). A `volumetric` target csak aktív Bluetooth scale + brew-by-weight mód esetén működik.

### V2 dial-in

| Eredmény | Következő lépés |
|---|---|
| **40.5-43 g, meggy/konyakmeggy/bonbonos, tiszta** | A Scale V2 profil helyes, nincs teendő. |
| **Savas, vékony, 43 g fölé fut** | stop_at_g értéket csökkentsd 41.5 g-ra, vagy menj 8 felé az őrlésen. |
| **Nehéz, alkoholosan keserű** | stop_at_g értéket csökkentsd 40.5-41.0 g-ra, vagy próbálj 94.5 °C-ot. |
| **Safety timeout (50 s) lép életbe** | Bluetooth megszakadt vagy flow túl lassú. |

---

## Rövid menthető recept

**Twenty Eight Finca el Recreo Caturron Flavor**

**V1 (időalapú):** 18.5 g · grind 9 · 1200 RPM · 95 °C · 42 s · 42 g out cél

**V2 (Scale):** 18.5 g · grind 9 · 1200 RPM · 95 °C · stop 42.0 g beverage weight · safety 50 s
