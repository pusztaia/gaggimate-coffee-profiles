# Twenty Eight Finca el Recreo Caturron Flavor 18.5-42 – GaggiMate Pro recept

**Márka:** Twenty Eight  
**Kávé:** Finca el Recreo Caturron  
**Ízjegyek:** meggy · konyakmeggy · piros gyümölcs · bonbonos édesség  
**Setup:** DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár  
**Őrlőskála:** 0-90, egész jelölések  
**Verzió:** 2026-06-29 – Twenty Eight brand fix, targetless 42s, GitHub-clean

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

## Rövid menthető recept

**Twenty Eight Finca el Recreo Caturron Flavor**

**18.5 g · grind 9 · 1200 RPM · 95 °C · 42 s · 42 g out cél**

---

## Mérleg / stop workflow – jelenlegi állapot

**Jelenleg még nincs BOOKOO Themis Ultra mérleg.**

Ez a recept ezért most **idő/fázis alapú GaggiMate profilként** használandó, nem automatikus brew-by-weight profilként. A célhozamot külön mérlegen figyeld.

A BOOKOO Themis Ultra később opcionálisan hozzáadható a workflow-hoz. Ha a mérleg megérkezik és a GaggiMate-ben működik a Bluetooth mérleges stop, akkor a célhozam lehet automatikus stop:

- Kirinyaga: 43.0 g
- Wangera: 42.0 g
- Caturron: 42.0 g

Addig a profilokban a mérleges automata stop **nem aktív**; a JSON-ban ez `brew_by_weight_active: false` logikával van dokumentálva.
