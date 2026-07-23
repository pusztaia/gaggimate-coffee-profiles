# Impresso Burundi Mubuga Melon Currant 18.5-42.5 38s

| Mező | Érték |
|---|---|
| Kávé | Impresso Burundi Mubuga |
| Feldolgozás | natural |
| Eredet | Burundi, Ngozi, Mubuga |
| Ízjegyek | sárgadinnye · alma · ribizli |
| Setup | DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) |
| Őrlőskála | 0-90, egész jelölések |
| Fordulat | 1200 RPM baseline |
| Stop | idő/fázis alapú profil + kézi mérleges figyelés; BOOKOO mérleg jelenleg nincs. |

---

## Cél ízprofil

lédús sárgadinnye-édesség, friss alma, élénk ribizli; tiszta, vibráló, de ne legyen vékony vagy héjasan száraz

---

## Miért ilyen a profil?

A Burundi Mubuga könnyed, tiszta, gyümölcsös karakteréhez a Wangera Stable Start logikájából induló, de kicsit lágyabb főnyomású profil készült. A cél a ribizlis élénkség és a sárgadinnye édesség megtartása száraz/héjas vég nélkül.

---

## Alap recept

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Cél hozam | **42.0-43.0 g** |
| Ideális hozam | **42.5 g** |
| Teljes profilidő | **38 s** |
| Cél idő | **37-39 s** |
| Hőmérséklet | **94.5 °C** |
| Őrlés indulás | **10 körül** |
| Őrlés tartomány | **10-11** |
| Fordulat | **1200 RPM** |
| Kosár | **IMS B682TH24.5M** |

### Első shot

**18.5 g be · grind 10 körül · 1200 RPM · 94.5 °C · 38 s teljes profil · cél 42.5 g ki**

---

## GaggiMate Pro fázisok

| # | Fázis | Idő | Hő | Pump target | Nyomás / Flow |
|---:|---|---:|---:|---|---:|
| 1 | Fruit Wetting | **5 s** | 94.5 °C | flow | 8.0 ml/s |
| 2 | Currant Saturation | **8 s** | 94.5 °C | pressure | 2.2 bar / 4.5 ml/s |
| 3 | Melon Bloom | **4 s** | 94.5 °C | pressure | 0.5 bar / 0 ml/s |
| 4 | Gentle Ramp | **6 s** | 94.5 °C | pressure | 7.2 bar / 2.4 ml/s |
| 5 | Juicy Extraction | **11 s** | 94.5 °C | pressure | 7.2 bar / 2.1 ml/s |
| 6 | Clean Finish | **4 s** | 94.5 °C | pressure | 5.4 bar / 1.7 ml/s |
|  | **Összesen** | **38 s** |  |  |  |

Automatikus előreléptető targetek nincsenek; a profil idő alapján fut végig.

---

## Dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **42-43g, lédús, dinnyés-ribizlis, tiszta** | Marad a profil és a 10 körüli induló őrlés. |
| **40g alatt marad, savas vagy fojtott** | Ellenőrizd WDT/tamp/screen stabilitását; ha stabil, menj egy jelölésen belül 11 felé. |
| **44g fölé fut, vékony vagy spriccel** | Menj 10 felé finomabbra, vagy kézi stop 42.5g körül. |
| **jó hozam, de lapos kevés gyümölcs** | Hő 95C lehet, vagy engedd 43g-ig. |
| **jó hozam, de száraz/héjas** | Hő 94C, vagy rövidíts 41.5-42g körülre. |

---

## Mérleg / stop workflow – V1 (időalapú)

Ez a recept **idő/fázis alapú GaggiMate profil** (`burundi-mubuga-38s.json`). A célhozamot külön mérlegen kell figyelni és kézzel megállítani.

---

## V2 – Bluetooth Scale Edition

**Szükséges hardver:** BOOKOO Themis Ultra + GaggiMate Pro Bluetooth kapcsolat

**V2 profil fájl:** [`burundi-mubuga-38s-scale-v2.json`](burundi-mubuga-38s-scale-v2.json)

### V2 paraméterek

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Target Yield | **42.5 g** |
| Arány | **1:2.30** |
| Hőmérséklet | **94.5 °C** |
| Stop mód | **beverage weight** |
| Stop | **42.5 g beverage weight** |
| Safety timeout | **45 s** |

### V2 fázis stop logika

| Fázis | Stop trigger | Duration (hard cap) |
|---|---|---:|
| Fruit Wetting | időalapú | 5 s |
| Currant Saturation | időalapú | 8 s |
| Melon Bloom | időalapú | 4 s |
| Gentle Ramp | időalapú | 6 s |
| Juicy Extraction | **volumetric target: 42.5 g** | 30 s |
| Clean Finish | időalapú (csak ha a target korán tüzel) | 8 s |

> **Firmware viselkedés (`pro` típus):** A `targets` tömb fázis szinten működik — minden 100 ms-ban kiértékeli. Az OR feltételek közül az első tüzelés zárja a fázist. A `duration` mindig hard cap: ha a volumetric target 42.5 g-nál tüzel, a Juicy Extraction fázis azonnal véget ér. Ha a scale nem csatlakozik vagy a target nem tüzel, a 30 s-os duration zárja a fázist (safety fallback). A `volumetric` target csak aktív Bluetooth scale + brew-by-weight mód esetén működik.

### V2 dial-in

| Eredmény | Következő lépés |
|---|---|
| **42-43 g, lédús, dinnyés-ribizlis, tiszta** | A Scale V2 profil helyes, nincs teendő. |
| **Mérleg korán áll meg, 40 g alatt, fojtott** | WDT/tamp/screen és Bluetooth kapcsolat ellenőrzés; ha stabil, picit 11 felé. |
| **Safety timeout (45 s) lép életbe** | Bluetooth megszakadt vagy flow túl lassú. |
| **Jó hozam, de lapos, kevés gyümölcs** | stop_at_g értéket emeld 43.0 g-ra. |
| **Jó hozam, de száraz/héjas** | stop_at_g értéket csökkentsd 42.0 g-ra. |

---

## Rövid menthető recept

**Burundi Mubuga Melon Currant**

**V1 (időalapú):** 18.5 g · grind 10 körül · 1200 RPM · 94.5 °C · 38 s · 42.5 g out cél

**V2 (Scale):** 18.5 g · grind 10 körül · 1200 RPM · 94.5 °C · stop 42.5 g beverage weight · safety 45 s
