# Kenya Wangera Creamy Fruit 18.5-42 – Stable Start 38s 94.5C

| Mező | Érték |
|---|---|
| Kávé | Impresso Kenya Wangera |
| Ízjegyek | szeder · tejszín · pomelo |
| Setup | DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) |
| Őrlőskála | 0-90, egész jelölések |
| Fordulat | 1200 RPM baseline |
| Státusz | bevált baseline – 42 g körüli hozam |
| Verzió | 2026-07-17 – Scale V2 stop-logika javítva, a V2 fájlnevek változatlanok |

---

## Aktuális bevált baseline

A 94.5 °C-os Stable Start 38s profil **42 g körüli hozamot adott**, amikor az őrlés a **10-11 közötti zónában, inkább 11 felé** volt állítva.

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Célhozam | **41-43 g** |
| Ideális hozam | **42 g** |
| Teljes profilidő | **kb. 38 s** |
| Hőmérséklet | **94.5 °C** |
| Őrlés indulás | **10-11 között, inkább 11 felé** |
| Fordulat | **1200 RPM** |
| Kosár | **IMS B682TH24.5M** |
| Stop | **Bluetooth mérleggel, kétlépcsős tömeg-targettel** |

### Következő shot

**18.5 g be · grind 10-11 között, inkább 11 felé · 1200 RPM · 94.5 °C · kb. 42 g végső hozam**

---

## Korai hozam diagnosztika

A Soft Ramp indulása előtt kb. **17 s** telik el. A bevált tartomány ezen a ponton kb. **6-9 g**.

| 17 s / Soft Ramp előtti hozam | Értelmezés | Teendő |
|---:|---|---|
| **3-4 g** | fojtott indulás, várhatóan alacsonyabb végső hozam | WDT/tamp/screen ellenőrzés; ha stabil a prep, menj picit 11 felé |
| **6-9 g** | egészséges indulás | marad a profil és az őrlési zóna |
| **10 g+** | túl gyors indulás vagy channeling gyanú | puck prep ellenőrzés; ha kell, picit 10 felé / finomabbra |

---

## GaggiMate Pro fázisok

| # | Fázis | Maximum idő | Hő | Pump target | Nyomás / Flow |
|---:|---|---:|---:|---|---:|
| 1 | Stronger Wetting | **5 s** | 94.5 °C | flow | 8.0 ml/s |
| 2 | Stable Saturation | **8 s** | 94.5 °C | pressure | 2.3 bar / 4.5 ml/s |
| 3 | Cream Bloom | **4 s** | 94.5 °C | pressure | 0.5 bar |
| 4 | Soft Ramp | **6 s** | 94.5 °C | pressure | 7.4 bar / 2.4 ml/s |
| 5 | Blackberry Extraction | **30 s hard cap** | 94.5 °C | pressure | 7.4 bar / 2.1 ml/s |
| 6 | Cream Finish | **8 s hard cap** | 94.5 °C | pressure | 5.8 bar / 1.7 ml/s |

A tényleges shotidőt a Bluetooth mérleg targetjei rövidítik. A `duration` értékek biztonsági maximumok, nem kötelezően végigfutó idők.

---

## Dial-in logika

| Eredmény | Következő lépés |
|---|---|
| **17 s körül 6-9 g, végén 41.5-42.5 g, jó íz** | marad a Scale V2 profil |
| **17 s körül 3-4 g, végén 41 g alatt** | fojtott indulás: WDT/tamp/screen; ha stabil, picit 11 felé |
| **17 s körül 10 g+, spriccelés vagy 43 g fölötti vég** | channeling/túl gyors indulás: puck prep; ha kell, picit 10 felé / finomabbra |
| **42 g körül jó, de túl savas/pomelós** | a végső stop target emelhető 41.0 g-ra |
| **42 g körül jó, de száraz/naturalos** | a végső stop target csökkenthető 40.0 g-ra, vagy hő 94 °C-ra |

---

## Rövid menthető recept

**Kenya Wangera Creamy Fruit Stable Start 38s 94.5C – Scale V2**

**18.5 g · grind 10-11 között, inkább 11 felé · 1200 RPM · 94.5 °C · 37.0 g-nál finish · 40.5 g-nál pumpastop · kb. 42 g végső hozam**

---

## Mérleg / stop workflow – V1, időalapú profil

A mérleg nélküli recept továbbra is idő/fázis alapú GaggiMate profil:

- `wangera-stable-38s-945c.json`
- a célhozamot külön mérlegen kell figyelni;
- szükség esetén kézzel kell megállítani.

---

## V2 – Bluetooth Scale Edition

**Szükséges hardver:** BOOKOO Themis Ultra + GaggiMate Pro Bluetooth kapcsolat

A verziószám **szándékosan V2 maradt**. A meglévő V2 JSON-fájlok tartalma lett felülírva a javított stop-logikával.

**Változatlan fájlnevek:**

- [`wangera-stable-38s-scale-v2.json`](profiles/wangera/wangera-stable-38s-scale-v2.json) – 94.0 °C
- [`wangera-stable-38s-945c-scale-v2.json`](profiles/wangera/wangera-stable-38s-945c-scale-v2.json) – 94.5 °C

### V2 paraméterek

| Paraméter | Érték |
|---|---:|
| Dózis | **18.5 g** |
| Cél végső hozam | **kb. 42 g** |
| Várható tartomány | **41.5-42.5 g** |
| Arány | **kb. 1:2.27** |
| Hőmérséklet | **94.5 °C** |
| Finish indítása | **37.0 g beverage weight** |
| Pumpa leállítása | **40.5 g beverage weight** |
| Stop mód | **Bluetooth scale / volumetric target** |
| Biztonsági fallback | **fázisonkénti hard cap** |

### Miért nem lehetett a 42 g-os target csak a Blackberry Extraction fázisban?

A GaggiMate `pro` profilban a `targets` tömb **az aktuális fázist zárja le**, nem automatikusan az egész shotot.

A korábbi V2 logika így működött:

1. A Blackberry Extraction elérte a **42.0 g** targetet.
2. Ez lezárta a Blackberry Extraction fázist.
3. Elindult a Cream Finish.
4. Mivel a Cream Finishben nem volt tömeg-target, még legfeljebb **8 másodpercig** tovább pumpált.
5. A tesztben ezért lett a végső hozam **53.9 g**.

A javított V2 logika kétlépcsős:

1. **37.0 g-nál** a Blackberry Extraction lezárul, és elindul a Cream Finish.
2. **40.5 g-nál** a Cream Finish is lezárul, ezért a pumpa leáll.
3. A puckból és a kifolyóból érkező maradék ital várhatóan **41.5-42.5 g** környékére viszi a végső tömeget.

### V2 fázis- és stop-logika

| Fázis | Stop trigger | Duration / hard cap |
|---|---|---:|
| Stronger Wetting | időalapú | 5 s |
| Stable Saturation | időalapú | 8 s |
| Cream Bloom | időalapú | 4 s |
| Soft Ramp | időalapú | 6 s |
| Blackberry Extraction | **volumetric target: 37.0 g** | 30 s |
| Cream Finish | **volumetric target: 40.5 g** | 8 s |

> **Firmware-viselkedés (`pro` típus):** a fázisban megadott `targets` feltételek rendszeresen kiértékelődnek. A target teljesülése az aktuális fázist zárja le. A `duration` minden fázisnál hard cap és biztonsági fallback. A `volumetric` target csak aktív Bluetooth-mérleg és brew-by-weight működés mellett használható.

### V2 dial-in

| Eredmény | Következő lépés |
|---|---|
| **41.5-42.5 g körül megáll, szederes/krémes, jó** | a Scale V2 profil helyes, nincs teendő |
| **43 g fölé fut** | a Cream Finish targetet csökkentsd **40.0 g-ra** |
| **41 g alatt áll meg** | a Cream Finish targetet emeld **41.0 g-ra** |
| **37 g-nál nem vált finish-re** | Bluetooth kapcsolat, mérleg-adat és brew-by-weight mód ellenőrzése |
| **A fázis hard cap miatt vált** | flow túl lassú vagy a mérleg targetje nem működik |
| **Spriccelés / több stream** | WDT, tamp, puck screen és őrlés ellenőrzése; szükség esetén finomabb őrlés |
| **42 g körüli hozam, savas/pomelós** | először a Cream Finish targetet emeld **41.0 g-ra** |
| **42 g körüli hozam, száraz/naturalos** | a Cream Finish targetet csökkentsd **40.0 g-ra**, vagy használj 94.0 °C-os V2 profilt |

---

## V2 gyors ellenőrzőlista

1. BOOKOO Themis Ultra csatlakoztatva.
2. A mérleg nullázva a csésze felhelyezése után.
3. Brew-by-weight / volumetric target aktív.
4. A betöltött fájl neve továbbra is `...scale-v2.json`.
5. Blackberry Extraction target: **37.0 g**.
6. Cream Finish target: **40.5 g**.
7. Várható végső hozam: **kb. 42 g**.
