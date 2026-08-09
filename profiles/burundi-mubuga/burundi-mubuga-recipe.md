# Impresso - Burundi Mubuga Melon Currant — Scale V3 dial-in

| Mező | Érték |
|---|---|
| Kávé | Impresso - Burundi Mubuga |
| Feldolgozás | natural |
| Eredet | Burundi, Ngozi, Mubuga |
| Ízjegyek | sárgadinnye · alma · ribizli |
| Setup | DF64V Gen 2 + SSP Sweet Lab Espresso V3 / Gaggia Classic Pro 2025 + GaggiMate Pro / IMS B682TH24.5M kosár / IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5) |
| Őrlőskála | 0–90, egész jelölések |
| Fordulat | 1200 RPM baseline |
| Mérleg | BOOKOO Themis Ultra, Bluetooth brew-by-weight |
| Aktuális profil | **Scale V3** |
| Státusz | **stop-logika validálva; őrlés dial-in folyamatban** |
| Frissítve | **2026-08-09 · shot #134 alapján** |

---

## Cél ízprofil

Lédús sárgadinnye-édesség, friss alma és élénk ribizli; tiszta, vibráló csésze, de ne legyen vékony vagy héjasan száraz.

---

## Aktuális következő baseline

A 2026-08-09-i első Scale V3 shot alapján a **10-es őrlés túl durva** ehhez a kávéhoz. A mérleges leállítás pontosan működött, ezért a profil stop-targetjeit most nem módosítjuk; először az őrlést kell finomabbra venni.

| Paraméter | Következő érték |
|---|---:|
| Dózis | **18.5 g** |
| Végső célhozam | **42.5 g** |
| Arány | **1:2.30** |
| Hőmérséklet | **94.5 °C** |
| Őrlés indulás | **8** |
| Előzetes dial-in tartomány | **8–9** |
| Fordulat | **1200 RPM** |
| Profil | **burundi-mubuga-scale-v3.json** |
| Juicy Extraction váltás | **38.0 g** |
| Végső pumpastop | **42.5 g** |

### Következő shot

**18.5 g be · grind 8 · 1200 RPM · 94.5 °C · Scale V3 · 38.0 g-nál Clean Finish · 42.5 g-nál végső stop**

A következő shot fő célja, hogy a Gentle Ramp / Juicy Extraction alatt a puck már tényleges ellenállást adjon, és a nyomás közelebb kerüljön a 7.2 baros profilcélhoz. Első körben **6–7 bar körüli tényleges főnyomás** már jó irány.

---

## Shot #134 — első Scale V3 teszt

**Dátum:** 2026-08-09 11:50  
**Beállítás:** 18.5 g · grind 10 · 1200 RPM · 94.5 °C · Scale V3  
**Eredmény:** **42.6 g / 42.0 s**

| Megfigyelés | Érték / jelentés |
|---|---|
| Gentle Ramp végére | **17.9 g** már a csészében — túl gyors puck |
| Juicy Extraction | **11.0 s**, weight stop működött |
| Juicy végén | **36.5 g mérleg / 38.2 g kalkulált**, majd Clean Finish |
| Clean Finish | **6.0 s**, weight stop működött |
| Végső tömeg | **42.6 g**, a 42.5 g célhoz képest +0.1 g |
| Fő extrakció tényleges nyomása | kb. **2.4–2.6 bar**, miközben a profil 7.2 bart kér |
| Hőmérséklet | beállítás 94.5 °C; shot átlag kb. **93.3 °C**, fő extrakcióban kb. 92.8 °C |

### Diagnózis

- **A kétlépcsős mérleges stop jó:** a végső 42.6 g gyakorlatilag telitalálat.
- **A 10-es őrlés túl durva:** a puck nem épített elegendő ellenállást, ezért a gép a 7.2 baros cél közelébe sem jutott.
- A fő profilt egyelőre **nem módosítjuk**. A következő változó kizárólag az őrlés: **10 → 8**.
- A hőmérséklet-esést érdemes a következő shoton is figyelni, de őrlés-dial-in előtt emiatt még nem változtatunk a 94.5 °C-os setpointon.

---

## Scale V3 — aktuális GaggiMate Pro fázisok

| # | Fázis | Hard cap | Hő | Pump target | Nyomás / Flow | Stop trigger |
|---:|---|---:|---:|---|---:|---|
| 1 | Fruit Wetting | **5 s** | 94.5 °C | flow | 8.0 ml/s · 3.5 bar soft cap | idő |
| 2 | Currant Saturation | **8 s** | 94.5 °C | pressure | 2.2 bar / 4.5 ml/s | idő |
| 3 | Melon Bloom | **7 s** | 94.5 °C | pressure | 0.5 bar / 0 ml/s | idő |
| 4 | Gentle Ramp | **6 s** | 94.5 °C | pressure | 7.2 bar / 2.4 ml/s | idő |
| 5 | Juicy Extraction | **30 s** | 94.5 °C | pressure | 7.2 bar / 2.1 ml/s | **≥ 38.0 g** |
| 6 | Clean Finish | **8 s** | 94.5 °C | pressure | 5.4 bar / 1.7 ml/s | **≥ 42.5 g** |
|  | **JSON maximum** | **64 s** |  |  |  |  |

A tényleges shotidőt a mérleg targetjei rövidítik. A `duration` értékek fázisonkénti hard capek, nem kötelezően végigfutó idők.

### Miért kétlépcsős a stop?

A GaggiMate `pro` profilban a `targets` tömb az **aktuális fázist** zárja le. Ezért:

1. **38.0 g-nál** a Juicy Extraction lezárul és elindul a Clean Finish.
2. **42.5 g-nál** a Clean Finish is lezárul, így a pumpa leáll.
3. Shot #134-ben ez **42.6 g végső tömeget** adott, tehát a jelenlegi stop-logika jól kompenzálja a rendszer késését / kifolyását.

---

## Scale V2 — kompatibilitási profil

A `burundi-mubuga-scale.json` továbbra is megtartott V2 változat. A stop-logika ugyanúgy kétlépcsős (**38.0 g → 42.5 g**), de a V3-hoz képest:

- Fruit Wetting alatt nincs 3.5 baros soft pressure cap;
- a Melon Bloom **4 s** a V3 **7 s**-ával szemben;
- a JSON fázis-hard-cap maximuma **61 s**.

Az aktuális dial-inhez **V3 az elsődleges**.

---

## Manual 38 s profil

A `burundi-mubuga-manual.json` továbbra is teljesen időalapú fallback profil.

| # | Fázis | Idő | Pump target |
|---:|---|---:|---|
| 1 | Fruit Wetting | 5 s | 8.0 ml/s |
| 2 | Currant Saturation | 8 s | 2.2 bar / 4.5 ml/s |
| 3 | Melon Bloom | 4 s | 0.5 bar |
| 4 | Gentle Ramp | 6 s | 7.2 bar / 2.4 ml/s |
| 5 | Juicy Extraction | 11 s | 7.2 bar / 2.1 ml/s |
| 6 | Clean Finish | 4 s | 5.4 bar / 1.7 ml/s |
|  | **Összesen** | **38 s** |  |

A Manual profilnál a célhozamot külön mérlegen kell figyelni és szükség esetén kézzel megállítani.

---

## Dial-in logika — Scale V3

| Eredmény | Következő lépés |
|---|---|
| **42–43 g, főnyomás kb. 6–7+ bar, lédús és tiszta** | marad az aktuális őrlés és a V3 profil |
| **Tényleges főnyomás 4 bar alatt, gyors tömegépülés** | túl durva: menj **finomabbra / kisebb szám felé** |
| **Grind 8 mellett is 4–5 bar alatt marad** | következő próbán **7**; előtte WDT/tamp/screen ellenőrzés |
| **Nagyon lassú, 7.2 baron ül, target későn jön** | menj **9 felé / durvábbra** |
| **Spriccelés, oldalirányú stream vagy ingadozás** | puck prep ellenőrzés; csak stabil prep után módosíts őrlést |
| **42.5 g körül jó, de lapos / kevés gyümölcs** | előbb őrlést stabilizáld; utána lehet 95.0 °C vagy 43.0 g próbát tenni |
| **42.5 g körül száraz / héjas** | előbb őrlést stabilizáld; utána 94.0 °C vagy 42.0 g végső target |
| **38 g-nál nem vált Clean Finishre** | BOOKOO kapcsolat, tare és brew-by-weight / volumetric target ellenőrzése |
| **42.5 g-nál nem áll meg** | Clean Finish target és mérlegadat ellenőrzése; a fázis 8 s hard capre fog kifutni |

---

## Rövid menthető recept

**Burundi Mubuga Melon Currant — Scale V3**

**18.5 g · grind 8 következő próba (8–9 dial-in zóna) · 1200 RPM · 94.5 °C · 38.0 g-nál Clean Finish · 42.5 g-nál pumpastop · shot #134 validálta a stopot 42.6 g végsúllyal**
