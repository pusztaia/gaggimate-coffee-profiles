# Bagira Costa Rica Finca San Calletano 19-42 – Scale V1 40s 93.5C

| Mező | Érték |
|---|---|
| Kávé | Bagira - Costa Rica Finca San Calletano |
| Ízjegyek | cseresznyebefőtt · csokoládé · krémes |
| Setup | DF64V Gen 2 + Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) / BOOKOO Themis Ultra Bluetooth mérleg |
| Őrlőskála | 0-90, egész jelölések |
| Fordulat | 1200 RPM baseline |
| Státusz | bevált baseline – 42 g körüli hozam |
| Verzió | 2026-01 – Scale V1, szoftver-vezérelt stop logika |

---

## Aktuális bevált baseline

A 93.5 °C-os Scale V1 profil **42 g körüli hozamot adott**, amikor az őrlés a **grind 11** volt állítva.

| Paraméter | Érték |
|---|---:|
| Dózis | **19 g** |
| Célhozam | **42 g** |
| Pumpastop | **41.0 g** |
| Teljes profilidő | **kb. 40 s** |
| Hőmérséklet | **93.5 °C** |
| Őrlés | **11** |
| Fordulat | **1200 RPM** |
| Kosár | **IMS B682TH24.5M** |
| Stop | **Bluetooth mérleggel, 41.0 g pumpastop targettel** |

### Következő shot

**19 g be · grind 11 · 1200 RPM · 93.5 °C · kb. 42 g végső hozam**

---

## Korai hozam diagnosztika

A Gentle Ramp indulása előtt kb. **17 s** telik el. A bevált tartomány ezen a ponton kb. **6-9 g**.

| 17 s / Gentle Ramp előtti hozam | Értelmezés | Teendő |
|---:|---|---|
| **3-4 g** | fojtott indulás, várhatóan alacsonyabb végső hozam | WDT/tamp/screen ellenőrzés; ha stabil a prep, menj picit 11 felé |
| **6-9 g** | egészséges indulás | marad a profil és az őrlési zóna |
| **10 g+** | túl gyors indulás vagy channeling gyanú | puck prep ellenőrzés; ha kell, picit 10 felé / finomabbra |

---

## GaggiMate Pro fázisok

| # | Fázis | Maximum idő | Hő | Pump target | Nyomás / Flow |
|---:|---|---:|---:|---|---:|
| 1 | Cherry Wetting | **5 s** | 93.5 °C | flow | 5.5 ml/s |
| 2 | Gentle Saturation | **7 s** | 93.5 °C | pressure | 2.2 bar / 3.8 ml/s |
| 3 | Soft Bloom | **5 s** | 93.5 °C | pressure | 0.6 bar |
| 4 | Gentle Ramp | **5 s** | 93.5 °C | pressure | 6.8 bar / 2.4 ml/s |
| 5 | Cherry Chocolate Extraction | **17 s** | 93.5 °C | pressure | 6.8 bar / 2.2 ml/s |
| 6 | Creamy Finish | **8 s hard cap** | 93.5 °C | pressure | 5.0 bar / 1.7 ml/s |

A tényleges shotidőt a Bluetooth mérleg targetje rövidíti. A `duration` értékek biztonsági maximumok, nem kötelezően végigfutó idők.

---

## Dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **17 s körül 6-9 g, végén 41.5-42.5 g, jó ízjegyek** | marad a Scale V1 profil |
| **17 s körül 3-4 g, végén 41 g alatt** | fojtott indulás: WDT/tamp/screen; ha stabil, picit 11 felé |
| **17 s körül 10 g+, spriccelés vagy 43 g fölötti vég** | channeling/túl gyors indulás: puck prep; ha kell, picit 10 felé / finomabbra |
| **42 g körül jó, de túl savas** | a végső pumpastop target emelhető 41.5 g-ra |
| **42 g körül jó, de száraz/fagyos** | a végső pumpastop target csökkenthető 40.5 g-ra, vagy hő 93.0 °C-ra |

---

## Rövid menthető recept

**Bagira Costa Rica Finca San Calletano Scale V1 – 19 g · grind 11 · 1200 RPM · 93.5 °C · pumpastop 41.0 g · kb. 42 g végső hozam**

---

## Scale V1 gyors ellenőrzőlista

1. BOOKOO Themis Ultra csatlakoztatva és kalibrálva.
2. A mérleg nullázva a csésze felhelyezése után.
3. Brew-by-weight / volumetric target aktív.
4. A betöltött fájl neve: `costa-rica-san-calletano-40s-scale-v1.json`.
5. Pumpastop target: **41.0 g** (vagy dial-in alapján módosítva).
6. Cherry Chocolate Extraction target: **39.5 g** (fázisvégzés trigger).
7. Creamy Finish pumpastop: **41.0 g**.
8. Várható végső hozam: **kb. 42 g**.
