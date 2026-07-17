# Brew Guidelines

Általános irányelvek az espresso dial-in folyamathoz ezzel a setuppal.

**Setup:** Gaggia Classic Pro 2025 + GaggiMate Pro · DF64V Gen 2 (SSP Sweet Lab Espresso V3) · IMS B682TH24.5M · IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) · BOOKOO Themis Ultra

---

## 1. Dózis

Az összes profil **18.5 g** dózissal van hangolva az IMS B682TH24.5M kosárhoz.

| Paraméter | Érték |
|---|---:|
| Dózis | 18.5 g |
| Kosár kapacitás | 18-21 g |
| Mérési pontosság | ±0.1 g ajánlott |

**Dózis változtatásának hatása:**

- Magasabb dózis → több ellenállás → lassabb flow → magasabb hozam elérési idő
- Alacsonyabb dózis → kevesebb ellenállás → gyorsabb flow → hamarabb éri el a stop értéket

Ha dózist változtatsz, a `stop_at_g` értéket és az arányokat is igazítsd hozzá.

---

## 2. Arány és hozam

### Jelenlegi profilok arányai

| Kávé | Dózis | Target Yield | Arány |
|---|---:|---:|---|
| Kenya Wangera | 18.5 g | 42.0 g | 1:2.27 |
| Burundi Mubuga | 18.5 g | 42.5 g | 1:2.30 |
| Colombia Manos Juntas | 18.5 g | 43.0 g | 1:2.32 |
| Kenya Kirinyaga PB | 18.5 g | 43.0 g | 1:2.32 |
| Twenty Eight Caturron | 18.5 g | 42.0 g | 1:2.27 |

### Arány hatása az ízre

| Arány | Jellemzők |
|---|---|
| 1:1.5 – 1:2.0 | Ristretto – sűrű, intenzív, rövid |
| 1:2.0 – 1:2.3 | Standard espresso – balanszos |
| 1:2.3 – 1:2.7 | Lungo espresso – könnyedebb, több édesség |

**Ökölszabály:**

- Ha száraz, fanyar, tanninos: növeld az arányt (több hozam)
- Ha vékony, savas, híg: csökkentsd az arányt (kevesebb hozam)
- Ha keserű, nehéz, alkoholos: csökkentsd az arányt vagy a hőmérsékletet

---

## 3. Őrlés

### DF64V Gen 2 skála

A DF64V Gen 2 0-90-es skálán egész jelöléseket használunk. Tizedes értékek nem megbízhatóan reprodukálhatók ezen a gyűrűn.

| Skálaérték | Jellemzők ezzel a setuppal |
|---|---|
| 7-8 | Nagyon finom – erős ellenállás, lassú flow |
| 9-10 | Espresso tartomány – a profilok többsége innen indul |
| 11-12 | Kicsit durvább – gyorsabb flow, könnyebb test |

### Őrlés beállítás logika

**Fojtott shot (túl finom):**

- Hozam nem éri el a célt a safety timeout lejárta előtt
- Savanyú, préselt, homályos íz
- Megoldás: egy jelöléssel durvábbra

**Túl gyors shot (túl durva):**

- Hozam hamarabb éri el a célt (pl. 25-30 s alatt)
- Híg, vizes, kevés test
- Megoldás: egy jelöléssel finomabbra

**Ideális flow (beverage weight alapú stop esetén):**

- Az extraction fázis 20-30 s között triggerel a stop értéket
- Az íz balanszos, gyümölcsös, nem száraz

### RPM hatása

Az összes profil 1200 RPM baseline-ra van hangolva. Az RPM a DF64V Gen 2-n változtatható (800-1800 RPM).

- **Alacsonyabb RPM (800-1000):** finomabb szemcse hasonló skálaértéknél, több fines
- **Magasabb RPM (1400-1800):** durvább szemcse hasonló skálaértéknél, kevesebb fines, más textúra

Ha RPM-et változtatsz, az egész profilon újra kell dial-in-elni.

---

## 4. Hőmérséklet

### Profilok hőmérsékletei

| Kávé | Hőmérséklet |
|---|---:|
| Kenya Wangera (V4 főprofil) | 94.5 °C |
| Kenya Wangera (alternatív) | 94.0 °C |
| Burundi Mubuga | 94.5 °C |
| Colombia Manos Juntas | 94.5 °C |
| Kenya Kirinyaga PB | 94.5 °C |
| Twenty Eight Caturron | 95.0 °C |

### Hőmérséklet hatása

| | Alacsonyabb hő | Magasabb hő |
|---|---|---|
| Savasság | csökkenti | növeli |
| Édesség | általában növeli | változó |
| Test | csökkenti | növeli |
| Keserűség | csökkenti | növeli |

**Mikor változtass hőmérsékleten:**

- Savas, vékony shot jó hozamnál → próbálj alacsonyabb hőt
- Lapos, édességhiányos shot jó hozamnál → próbálj magasabb hőt
- Keserű, nehéz shot → csökkents hőt, ne arányt

---

## 5. Puck prep

A stabil, reprodukálható puck prep alapja a konzisztens dial-in-nek. Beverage weight alapú stopnál különösen fontos, mert a channeling eltorzítja a flow-t és ezzel a mért hozamot.

### Kötelező lépések

1. **WDT (Weiss Distribution Technique)** – egyenletes kávéeloszlás a kosárban; különösen a széleknél és az aljánál fontos
2. **Tamp** – egyenes, egyenletes, kb. 15-20 kg nyomással; döntött tamp channelinget okoz
3. **Puck screen** – száraz és tiszta legyen; a nedves screen alap-channelinget okozhat

### Diagnosztika naked portafilterrel

Ha naked portafilter elérhető:

| Tünet | Probléma |
|---|---|
| Egyenletes, középről induló csepegés | Jó puck prep |
| Oldalról induló csepegés | WDT nem egyenletes, vagy döntött tamp |
| Spriccelés a first drop előtt | Channeling – WDT és tamp ellenőrzés |
| Spriccelés extraction közben | Puck összeomlás vagy grind too coarse |

---

## 6. Shot értékelés

### Mit mérj minden shotnál

1. **Dózis** (g) – a receptnek megfelelően
2. **Hozam** (g) – a mérleg mutatja (V4 profilnál automatikus stop)
3. **Idő** (s) – a GaggiMate profil futási ideje
4. **Íz** – azonnali értékelés (savanyú/édes/keserű/test/lecsengés)

### Shot log ajánlott mezői

| Mező | Leírás |
|---|---|
| Dátum | |
| Kávé | |
| Profil | JSON fájlnév és verzió (V3/V4) |
| Dózis | g |
| Hozam | g |
| Idő | s |
| Hőmérséklet | °C |
| Őrlés | skálajelölés |
| RPM | |
| Stop trigger | beverage weight / safety timeout / kézi |
| Íz értékelés | részletes megjegyzés |
| Következő lépés | mi változzon a következő shotnál |

### Értékelési szempontok

**Savasság:**
- Jó: élénk, gyümölcsös, kerek
- Rossz: hegyes, citrusos, maró, préselt

**Édesség:**
- Jó: karamelles, gyümölcsös, hosszan maradó
- Rossz: semleges, hiányzó, mesterséges

**Test:**
- Jó: szirupos, krémes, telt
- Rossz: vizes, vékony, vagy nehéz és alkoholos

**Lecsengés:**
- Jó: gyümölcsös, hosszan maradó, kellemes
- Rossz: keserű, száraz, héjas, tanninok

---

## 7. Dial-in folyamat

### Sorrend

1. **Dózis rögzítése** – ne változtasd dial-in közben
2. **Hőmérséklet rögzítése** – a profil értéke
3. **Hozam célérték rögzítése** – a profil `stop_at_g` értéke
4. **Őrlés beállítása** – ez az elsődleges változó
5. **Hozam és íz értékelése** – legalább 2-3 konzisztens shot után dönts
6. **Ha az őrlés optimális** és az íz még nem megfelelő → hőmérséklet vagy hozam finom hangolása

### Egy változtatás egyszerre

Minden dial-in lépésben csak egy paramétert változtass. Párhuzamos változtatás esetén nem tudod azonosítani a hatást.

### Konzisztencia ellenőrzése

Két egymást követő, azonos paraméterű shot hozamának max. ±1.0 g eltérése elfogadható. Ha nagyobb az ingadozás:

- Puck prep stabilitása az elsődleges gyanúsított
- Dózis mérési pontosság ellenőrzése
- Mérleg kalibráció ellenőrzése

---

## 8. V3 vs V4 dial-in különbségek

| | V3 (Time Based) | V4 (Scale Edition) |
|---|---|---|
| Hozam variabilitás | Magas (flow-függő) | Alacsony (gramm kontroll) |
| Dial-in elsődleges változó | Őrlés (hozam és idő) | Őrlés (flow sebesség és idő) |
| Hozam állítása | Profil időtartamával | stop_at_g értékkel |
| Konzisztencia | Shotonként változhat | Reprodukálható |
| Manuális beavatkozás | Kézi stop szükséges | Automatikus stop |
