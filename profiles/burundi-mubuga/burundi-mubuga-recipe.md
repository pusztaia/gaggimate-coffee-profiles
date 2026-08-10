# Impresso - Burundi Mubuga Melon Currant — Scale V4 Fruity dial-in

| Mező | Érték |
|---|---|
| Kávé | Impresso - Burundi Mubuga |
| Feldolgozás | natural |
| Eredet | Burundi, Ngozi, Mubuga |
| Ízjegyek | sárgadinnye · alma · ribizli |
| Setup | DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) |
| Őrlőskála | 0–90, egész jelölések |
| Mérleg | BOOKOO Themis Ultra, Bluetooth brew-by-weight |
| Aktuális profil | **Scale V4 Fruity** |
| Státusz | **gyümölcsösség-optimalizálás; korai vízbevitel csökkentve** |
| Frissítve | **2026-08-10 · 19 g / grind 9 / 1400 RPM teszt után** |

---

## Cél ízprofil

Lédús sárgadinnye-édesség, friss alma és élénk ribizli; tiszta, vibráló csésze, de ne legyen vékony vagy héjasan száraz. A következő fejlesztési cél nem a 7.2 bar mindenáron történő elérése, hanem a **gyümölcsös aromák és a tisztaság visszahozása**.

---

## Aktuális következő baseline — V4 Fruity

A grind 8-as 18.5 g-os shot technikailag stabil volt, de kevésbé hozta a gyümölcsös jegyeket. A következő 19.0 g / grind 9 / 1400 RPM teszt sem lett gyümölcsösebb, miközben a Gentle Ramp végére már **21.2 g** volt a csészében. Ez arra utal, hogy a profil túl sok vizet visz be a fő extrakció előtt.

A V4 ezért **nem a főnyomást emeli**, hanem a korai vízbevitelt csökkenti.

| Paraméter | V4 Fruity következő érték |
|---|---:|
| Dózis | **18.5 g** |
| Végső célhozam | **42.5 g** |
| Arány | **1:2.30** |
| Hőmérséklet | **94.0 °C** |
| Őrlés | **9** |
| Fordulat | **1200 RPM** |
| Profil | **burundi-mubuga-scale-v4-fruity.json** |
| Fruit Wetting | **6.8 ml/s · 3.5 bar soft cap · 5 s** |
| Currant Saturation | **2.2 bar / 3.8 ml/s · 8 s** |
| Melon Bloom | **0.5 bar · 7 s** |
| Juicy Extraction váltás | **38.0 g** |
| Végső pumpastop | **42.5 g** |

### Következő shot

**18.5 g be · grind 9 · 1200 RPM · 94.0 °C · Scale V4 Fruity · 38.0 g-nál Clean Finish · 42.5 g-nál végső stop**

**Elsődleges megfigyelési pont:** a Gentle Ramp végére lehetőleg csak kb. **14–17 g** legyen a csészében. Ha az íz gyümölcsösebb és tisztább, a V4 irány jó. A tényleges nyomás másodlagos diagnosztikai adat; nem cél önmagában a 7.2 bar elérése.

---

## 2026-08-10 — 19 g / grind 9 / 1400 RPM teszt

**Beállítás:** 19.0 g · grind 9 · 1400 RPM · 94.5 °C · Scale V3  
**Eredmény:** **42.6 g / 39.8 s**

| Megfigyelés | Érték / jelentés |
|---|---|
| Gentle Ramp végére | **21.2 g** már a csészében — erősen front-loaded |
| Fő extrakció tényleges nyomása | kb. **2.5–2.7 bar** |
| Végső tömeg | **42.6 g**, a mérleges stop továbbra is pontos |
| Íz | **nem lett gyümölcsösebb** |

### Következtetés

- A **19 g** nem adott érzékelhető ízelőnyt.
- A **1400 RPM** sem hozta vissza a gyümölcsösséget.
- A nagyobb dózis + magasabb RPM ágat egyelőre lezárjuk.
- Visszaállás: **18.5 g / grind 9 / 1200 RPM**.
- Profiloldali változás: kisebb korai flow, hogy több extrakció maradjon a kontrollált Juicy szakaszra.

---

## Shot #135 — grind 8 referencia

**Beállítás:** 18.5 g · grind 8 · 1200 RPM · 94.5 °C · Scale V3  
**Eredmény:** kb. **42.4 g / 41.7 s**

- A stop-logika pontos maradt.
- A főnyomás továbbra is kb. **2.4–2.6 bar** körül alakult.
- A csésze technikailag rendben volt, de **kevésbé jöttek ki a gyümölcsös jegyek**.
- Emiatt nem mentünk tovább finomabb őrlés felé.

---

## Shot #134 — első Scale V3 teszt

**Dátum:** 2026-08-09 11:50  
**Beállítás:** 18.5 g · grind 10 · 1200 RPM · 94.5 °C · Scale V3  
**Eredmény:** **42.6 g / 42.0 s**

- Gentle Ramp végére **17.9 g** volt a csészében.
- Juicy Extraction kb. **11.0 s** után weight stop-pal váltott.
- Clean Finish kb. **6.0 s** után weight stop-pal zárt.
- Fő extrakció tényleges nyomása csak kb. **2.4–2.6 bar** volt.
- A kétlépcsős **38.0 g → 42.5 g** stop-logika validálva lett.

---


## 2026-08-10 – Shot #139 / V4 stop-fix

A #139 shotnál a BOOKOO csatlakozott és a tömegadat érkezett, de a shot `shotStartedVolumetric: false` állapotban indult, ezért a `volumetric` target nem tüzelhetett. A Juicy Extraction 38 g fölött is tovább futott, és a shot 64.9 g-ig ment.

A profil neve és verziója **Scale V4 Fruity** marad. A V4 most kettős stop-biztonságot használ:

- Juicy Extraction: **volumetric >= 38.0 g OR pumped >= 28 ml**
- Clean Finish: **volumetric >= 42.5 g OR pumped >= 6 ml**

Normál, aktív brew-by-weight esetén továbbra is a mérleg targetje tüzel elsőként. Ha a brew-by-weight mód nem aktiválódik, a `pumped` target megakadályozza a 30 s-os Juicy hard capig tartó túlfutást. A `pumped` fallback biztonsági becslés, ezért ilyen shotnál a végső tömeg nem lesz olyan pontos, mint aktív mérleges stopnál.

## Scale V4 Fruity — GaggiMate Pro fázisok

| # | Fázis | Hard cap | Hő | Pump target | Nyomás / Flow | Stop trigger |
|---:|---|---:|---:|---|---:|---|
| 1 | Fruit Wetting | **5 s** | 94.0 °C | flow | **6.8 ml/s · 3.5 bar soft cap** | idő |
| 2 | Currant Saturation | **8 s** | 94.0 °C | pressure | **2.2 bar / 3.8 ml/s** | idő |
| 3 | Melon Bloom | **7 s** | 94.0 °C | pressure | 0.5 bar / 0 ml/s | idő |
| 4 | Gentle Ramp | **6 s** | 94.0 °C | pressure | 7.2 bar / 2.4 ml/s | idő |
| 5 | Juicy Extraction | **30 s** | 94.0 °C | pressure | 7.2 bar / 2.1 ml/s | **≥ 38.0 g OR pumped ≥ 28 ml** |
| 6 | Clean Finish | **8 s** | 94.0 °C | pressure | 5.4 bar / 1.7 ml/s | **≥ 42.5 g OR pumped ≥ 6 ml** |
|  | **JSON maximum** | **64 s** |  |  |  |  |

### Mi változott V3 → V4 Fruity?

- Fruit Wetting flow: **8.0 → 6.8 ml/s**.
- Currant Saturation flow ceiling: **4.5 → 3.8 ml/s**.
- Setpoint: **94.5 → 94.0 °C**.
- A 7 s bloom, a Gentle Ramp, a fő extrakció és a kétlépcsős mérleges stop **változatlan**.
- A cél: kevesebb korai ital, több kontrollált fő extrakció, nyitottabb savasság és több gyümölcsösség.

---

## Kompatibilitási profilok

- **Scale V3:** eredeti 8.0 / 4.5 ml/s korai flow, 94.5 °C, 7 s bloom, 38.0 → 42.5 g stop.
- **Scale V2:** 4 s bloom, nincs 3.5 baros wetting soft cap, ugyanaz a 38.0 → 42.5 g stop.
- **Manual 38 s:** teljesen időalapú fallback profil.

---

## V4 Fruity dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **Gentle Ramp végén 14–17 g, tiszta és gyümölcsös** | marad a V4 és grind 9 |
| **Még mindig 19–21+ g a Gentle Ramp végén** | először prep ellenőrzés; utána Fruit Wetting **6.2–6.5 ml/s** teszt |
| **Savanyú / vékony / zöld** | vissza **94.5 °C-ra**, vagy grind 8 felé egy lépés |
| **Édes, de még tompa** | külön tesztként végsúly **43.5–44.0 g**; csak a V4 stabilizálása után |
| **Száraz / héjas** | marad 94.0 °C, szükség esetén végsúly **42.0 g** |
| **38 g-nál nem vált Clean Finishre** | BOOKOO kapcsolat, tare és volumetric target ellenőrzése |
| **42.5 g-nál nem áll meg** | Clean Finish target és mérlegadat ellenőrzése |

---

## Rövid menthető recept

**Burundi Mubuga Melon Currant — Scale V4 Fruity**

**18.5 g · grind 9 · 1200 RPM · 94.0 °C · Fruit Wetting 6.8 ml/s · Currant Saturation 2.2 bar / 3.8 ml/s · 7 s bloom · 38.0 g-nál Clean Finish · 42.5 g-nál pumpastop**
