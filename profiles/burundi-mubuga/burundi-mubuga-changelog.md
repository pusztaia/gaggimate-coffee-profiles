# Changelog – Burundi Mubuga Melon Currant

## 2026-08-09 – Shot #134, Scale V3 stop-validálás és őrléskorrekció

### Shot eredmény

- Profil: **Burundi Mubuga Melon Currant Scale V3**
- Dózis: **18.5 g**
- Őrlés: **10**
- Setpoint: **94.5 °C**
- Végső hozam: **42.6 g**
- Teljes shotidő: **42.0 s**
- Gentle Ramp végére már **17.9 g** volt a csészében.
- Juicy Extraction kb. **11.0 s** után weight stop-pal váltott.
- Clean Finish kb. **6.0 s** után weight stop-pal zárt.

### Validated

- A kétlépcsős tömeg-stop működik:
  - Juicy Extraction: **≥ 38.0 g** → Clean Finish
  - Clean Finish: **≥ 42.5 g** → shot vége
- A végső **42.6 g** igazolja, hogy a 42.5 g-os végső targetet jelenleg nem kell módosítani.

### Dial-in változás

- A **10-es őrlés túl durvának** bizonyult.
- A fő extrakció tényleges nyomása csak kb. **2.4–2.6 bar** volt a **7.2 baros** cél mellett.
- Új következő induló érték: **grind 8**.
- Előzetes dial-in tartomány: **8–9**.
- A profil nyomás-, flow- és tömeg-targetjei **változatlanok**; először csak az őrlést finomítjuk.

### Dokumentáció / meta javítások

- `burundi-mubuga-scale-v3.json` label javítva **Scale V3**-ra (korábban tévesen V2 szerepelt benne).
- A V2, V3 és Manual JSON leírások őrlési ajánlása **10–11 → 8–9**.
- A korábbi, JSON-ban nem létező **45 s global safety timeout** hivatkozás kivezetve.
- Tényleges fázis-hard-cap maximum:
  - Scale V2: **61 s**
  - Scale V3: **64 s**
  - Manual: **38 s**

## Scale V3 – soft wetting cap + hosszabb bloom

- Fruit Wetting flow target: **8.0 ml/s**, soft pressure cap: **3.5 bar**.
- Currant Saturation: **2.2 bar**.
- Melon Bloom: **7 s**.
- Gentle Ramp / Juicy Extraction fő target: **7.2 bar**.
- Kétlépcsős mérleges stop: **38.0 g → 42.5 g**.
- Clean Finish: **5.4 bar**, maximum 8 s.
- V3 fázis-hard-cap maximum: **64 s**.

## Repo konzisztencia (2026-07-25)

- A JSON fájlnevek átalakítva: `burundi-mubuga-38s.json` → `burundi-mubuga-manual.json`, `burundi-mubuga-38s-scale-v2.json` → `burundi-mubuga-scale.json` (a `kirinyaga/` mintáját követve).
- A PNG profilgrafikonok újragenerálva.

## V2 – Bluetooth Scale Edition (2026-07-06)

### Added

- BOOKOO Themis Ultra Bluetooth scale support.
- Beverage-weight alapú fázistargetek.
- A jelenlegi V2 fájl kétlépcsős stopot használ:
  - **38.0 g**: Juicy Extraction vége / Clean Finish indul
  - **42.5 g**: Clean Finish vége / pumpastop
- Fázisonkénti hard cap fallback; a V2 fázisidők összege **61 s**.

### Changed

- A preinfusion és a ramp továbbra is időalapú.
- A recipe dokumentáció Scale workflow-val és dial-in logikával bővült.

## 2026-07-04 – kezdeti GaggiMate Pro profil

- Új profil Impresso - Burundi Mubuga kávéhoz.
- Cél: sárgadinnye, alma, ribizli; tiszta, lédús, nem száraz espresso.
- Teljes Manual profilidő: **38 s**.
- Hőmérséklet: **94.5 °C**.
- Dózis: **18.5 g**.
- Célhozam: **42–43 g**, ideálisan **42.5 g**.
- Eredeti DF64V Gen 2 kiindulás: grind 10 körül, 1200 RPM; ezt a 2026-08-09-i első V3 shot később túl durvának mutatta.
