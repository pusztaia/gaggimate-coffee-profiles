# Bagira Ethiopia Halo Beriti 19-43.5 – Smooth Start 39s 94.0C

| Mező | Érték |
|---|---|
| Kávé | Bagira - Ethiopia Halo Beriti |
| Ízjegyek | virágos · citrusos · tiszta |
| Setup | DF64V Gen 2 + Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) / BOOKOO Themis Ultra Bluetooth mérleg |
| Őrlőskála | 0-90, egész jelölések |
| Fordulat | 1200 RPM baseline |
| Státusz | baseline – 43.5 g körüli célhozam |
| Verzió | 2026-01 – Scale V2, kétlépcsős tömeg-targettel |

---

## Ajánlott baseline

A 94.0 °C-os Scale V2 profil **43.5 g körüli végső hozamra** készült, a kiinduló őrlésbeállítás **grind 11**.

| Paraméter | Érték |
|---|---:|
| Dózis | **19 g** |
| Célhozam | **43.5 g** |
| Pumpastop | **42.0 g** |
| Teljes profilidő | **kb. 39 s** |
| Hőmérséklet | **94.0 °C** |
| Őrlés | **11** |
| Fordulat | **1200 RPM** |
| Kosár | **IMS B682TH24.5M** |
| Stop | **Bluetooth mérleggel, kétlépcsős volumetric targettel** |

### Következő shot

**19 g be · grind 11 · 1200 RPM · 94.0 °C · kb. 43.5 g végső hozam**

---

## Korai hozam diagnosztika

A Smooth Ramp indulása előtt kb. **17 s** telik el. A bevált kiindulási tartomány ezen a ponton kb. **6-9 g**.

| 17 s / Smooth Ramp előtti hozam | Értelmezés | Teendő |
|---:|---|---|
| **3-4 g** | fojtott indulás, várhatóan alacsonyabb végső hozam | WDT/tamp/screen ellenőrzés; ha stabil a prep, menj picit 11 felé |
| **6-9 g** | egészséges indulás | marad a profil és az őrlési zóna |
| **10 g+** | túl gyors indulás vagy channeling gyanú | puck prep ellenőrzése; ha kell, picit 10 felé / finomabbra |

---

## GaggiMate Pro fázisok

| # | Fázis | Maximum idő | Hő | Pump target | Nyomás / Flow |
|---:|---|---:|---:|---|---:|
| 1 | Gentle Wetting | **6 s** | 94.0 °C | flow | 4.5 ml/s |
| 2 | Saturation | **7 s** | 94.0 °C | pressure | 2.0 bar / 3.5 ml/s |
| 3 | Bloom | **4 s** | 94.0 °C | pressure | 0.5 bar |
| 4 | Smooth Ramp | **5 s** | 94.0 °C | pressure | 6.8 bar / 2.3 ml/s |
| 5 | Main Extraction | **17 s** | 94.0 °C | pressure | 7.0 bar / 2.1 ml/s |
| 6 | Clean Finish | **8 s hard cap** | 94.0 °C | pressure | 5.0 bar / 1.6 ml/s |

A teljes névleges fázisidő kb. **47 s**, de a tömeg-targetek a tényleges shotot várhatóan kb. **39 s** körül lezárják. A `duration` értékek biztonsági maximumok, nem kötelezően végigfutó idők.

---

## Kétlépcsős stop-logika

A `pro` profilban a `targets` az aktuális fázist zárják le, ezért a célhozamhoz két külön stop szükséges:

1. **39.5 g-nál** a Main Extraction lezárul, és elindul a Clean Finish.
2. **42.0 g-nál** a Clean Finish is lezárul, ezért a pumpa leáll.
3. A puckból és a kifolyóból érkező maradék ital várhatóan **kb. 43.5 g** végső tömeget eredményez.

---

## Dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **17 s körül 6-9 g, végén 43.0-44.0 g, tiszta és jó íz** | marad a Scale V2 profil |
| **17 s körül 3-4 g, végén 43 g alatt** | fojtott indulás: WDT/tamp/screen; ha stabil, picit 11 felé |
| **17 s körül 10 g+, spriccelés vagy 44 g fölötti vég** | channeling/túl gyors indulás: puck prep; ha kell, picit 10 felé / finomabbra |
| **43.5 g körül jó, de túl savas vagy vékony** | a hőmérséklet maradjon 94.0 °C; ellenőrizd a prep-et, szükség esetén kissé finomabb őrlés |
| **43.5 g körül száraz vagy túl intenzív** | a Clean Finish target csökkenthető **41.5 g-ra**, vagy a hőmérséklet 93.5 °C-ra állítható |
| **44 g fölé fut** | a Clean Finish targetet csökkentsd **41.5 g-ra** |
| **43 g alatt áll meg** | a Clean Finish targetet emeld **42.5 g-ra** |
| **39.5 g-nál nem vált Clean Finishre** | Bluetooth kapcsolat, mérleg-adat és brew-by-weight mód ellenőrzése |

---

## Rövid menthető recept

**Bagira Ethiopia Halo Beriti Smooth Start 39s 94.0C – Scale V2**

**19 g · grind 11 · 1200 RPM · 94.0 °C · 39.5 g-nál Clean Finish · 42.0 g-nál pumpastop · kb. 43.5 g végső hozam**

---

## Scale V2 gyors ellenőrzőlista

1. BOOKOO Themis Ultra csatlakoztatva és kalibrálva.
2. A mérleg nullázva a csésze felhelyezése után.
3. Brew-by-weight / volumetric target aktív.
4. A betöltött fájl neve: `ethiopia-halo-beriti-39s-scale-v2.json`.
5. Main Extraction target: **39.5 g**.
6. Clean Finish target / pumpastop: **42.0 g**.
7. Várható végső hozam: **kb. 43.5 g**.
8. Ha a mérleg-target nem működik, a fázisok hard capjei jelentik a biztonsági fallbacket.
