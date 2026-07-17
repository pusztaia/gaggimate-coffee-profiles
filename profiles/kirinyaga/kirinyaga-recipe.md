# Kirinyaga PB Tea Rose 18.5-43 37s – GaggiMate Pro recept

| Mező | Érték |
|---|---|
| Kávé | Impresso Kenya Kirinyaga PB |
| Ízjegyek | hibiszkusz · csipkebogyó · fekete tea |
| Feldolgozás | washed |
| Eredet | Kenya, Kirinyaga |
| Setup | DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) |
| Őrlőskála | 0-90, egész jelölések |
| Verzió | 2026-06-29 – 37s, targetless, GitHub-clean |

---

## Cél ízprofil

Elegáns fekete tea, hibiszkuszos-piros sav, csipkebogyós édesség; ne legyen vékony, citromosan savanyú vagy száraz.

---

## Alap recept

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Cél hozam | **42-44 g** |
| Ideális hozam | **43 g** |
| Teljes profilidő | **37 s** |
| Cél idő | **36-38 s** |
| Hőmérséklet | **94.5 °C** |
| Őrlés indulás | **9** |
| Őrlés tartomány | **9-10** |
| Fordulat | **1200 RPM** |
| Fordulat megjegyzés | **DF64V Gen 2 változtatható fordulatú; ez a recept 1200 RPM baseline-ra van hangolva** |
| Kosár | **IMS B682TH24.5M** |

### Következő shot

**18.5 g be · grind 9 · 1200 RPM · 94.5 °C · 37 s teljes profil · cél 42-44 g ki**

---

## GaggiMate Pro fázisok

| # | Fázis | Idő | Hő | Pump target | Nyomás / Flow |
|---:|---|---:|---:|---|---:|
| 1 | Tea Wetting | **4 s** | 94.5 °C | flow | 7.5 ml/s |
| 2 | Even Saturation | **6 s** | 94.5 °C | pressure | 2.1 bar / 4.5 ml/s |
| 3 | Hibiscus Bloom | **4 s** | 94.5 °C | pressure | 0.5 bar |
| 4 | Gentle Ramp | **5 s** | 94.5 °C | pressure | 7.6 bar / 2.4 ml/s |
| 5 | Black Tea Extraction | **12 s** | 94.5 °C | pressure | 7.6 bar / 2.1 ml/s |
| 6 | Rosehip Finish | **6 s** | 94.5 °C | pressure | 5.6 bar / 1.8 ml/s |
|  | **Összesen** | **37 s** |  |  |  |

Automatikus előreléptető targetek nincsenek; a profil idő alapján fut végig.

---

## Dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **42-44 g, jó íz** | marad **grind 9**, 37 s |
| **44 g fölé fut, vékony vagy száraz** | állíts meg 43 g körül, vagy menj egy jelöléssel finomabbra |
| **42 g alatt marad, fojtott vagy lassú** | menj **10** felé |
| **savanyú, vékony, citromos** | egy teljes jelöléssel finomabb, vagy hő **95 °C** |
| **fanyar, tanninos tea** | rövidebb hozam **42 g** körül, vagy hő **94 °C** |

---

## Mérleg / stop workflow – V3 (időalapú)

Ez a recept **idő/fázis alapú GaggiMate profil** (`kirinyaga-tea-rose-37s.json`). A célhozamot külön mérlegen kell figyelni és kézzel megállítani.

---

## V4 – Bluetooth Scale Edition

**Szükséges hardver:** BOOKOO Themis Ultra + GaggiMate Pro Bluetooth kapcsolat

**V4 profil fájl:** [`kirinyaga-tea-rose-37s-scale-v4.json`](kirinyaga-tea-rose-37s-scale-v4.json)

### V4 paraméterek

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Target Yield | **43.0 g** |
| Arány | **1:2.32** |
| Hőmérséklet | **94.5 °C** |
| Stop mód | **beverage weight** |
| Stop | **43.0 g beverage weight** |
| Safety timeout | **45 s** |

### V4 fázis stop logika

| Fázis | Stop trigger | Duration (hard cap) |
|---|---|---:|
| Tea Wetting | időalapú | 4 s |
| Even Saturation | időalapú | 6 s |
| Hibiscus Bloom | időalapú | 4 s |
| Gentle Ramp | időalapú | 5 s |
| Black Tea Extraction | **volumetric target: 43.0 g** | 30 s |
| Rosehip Finish | időalapú (csak ha a target korán tüzel) | 8 s |

> **Firmware viselkedés (`pro` típus):** A `targets` tömb fázis szinten működik — minden 100 ms-ban kiértékeli. Az OR feltételek közül az első tüzelés zárja a fázist. A `duration` mindig hard cap: ha a volumetric target 43.0 g-nál tüzel, a Black Tea Extraction fázis azonnal véget ér. Ha a scale nem csatlakozik vagy a target nem tüzel, a 30 s-os duration zárja a fázist (safety fallback). A `volumetric` target csak aktív Bluetooth scale + brew-by-weight mód esetén működik.

### V4 dial-in

| Eredmény | Következő lépés |
|---|---|
| **42-44 g, hibiszkuszos-csipkebogyós, fekete tea** | A Scale V4 profil helyes, nincs teendő. |
| **Savanyú, vékony, citromos** | stop_at_g értéket emeld 43.5-44.0 g-ra, vagy finomabb őrlés, vagy 95 °C. |
| **Hibiszkusz szép, de fanyar/száraz** | stop_at_g értéket csökkentsd 42.0-42.5 g-ra. |
| **Safety timeout (45 s) lép életbe** | Bluetooth megszakadt vagy flow túl lassú. |

---

## Rövid menthető recept

**Kirinyaga PB Tea Rose 37s**

**V3 (időalapú):** 18.5 g · grind 9 · 1200 RPM · 94.5 °C · 37 s · 43 g out cél

**V4 (Scale):** 18.5 g · grind 9 · 1200 RPM · 94.5 °C · stop 43.0 g beverage weight · safety 45 s
