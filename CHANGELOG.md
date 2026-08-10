# Projekt Changelog – Coffee Profiles

---

## Shot Log Viewer (2026-08-10)

### Added

- **`shot-logs/shot-viewer.html`** – önálló, szerver nélkül is működő HTML oldal a `gaggimate_shots_to_json.py` script által letöltött `shot-<id>.json` fájlok grafikus megjelenítésére: nyomás/flow/hőmérséklet (mért és cél érték), fázishatárok és a mérleg tömeggörbéje, szinkronizált crosshairrel és tooltippel. Fájl(ok) vagy a teljes `gaggimate-shots` mappa drag-and-droppal vagy fájlválasztóval tölthető be, minden feldolgozás a böngészőben történik.
- **`index.html`** – új "Shot Log Viewer" kártya a Dokumentáció szekcióban, ami a `shot-viewer.html`-t új lapon nyitja meg (nem a Markdown-modálon keresztül, mivel nem `.md` fájl).
- **`shot-logs/GaggiMate-Shot-Downloader-HOWTO.md`** – új 19. szakasz a `shot-viewer.html` használatáról; `README.md` Dokumentumok táblázata kiegészítve.

### Changed

- **`shot-logs/shot-viewer.html`** – "Főoldal" gomb a topbarban, ugyanazzal a `.home-link` mintával, mint a `profiles/*/*.html` profil leíró oldalakon.

## JSON fájlnevek egységesítése: manual/scale minta (2026-07-25)

### Changed

- Minden kávé JSON fájlneve átalakítva a `kirinyaga/` mintájára: `{kávé}-manual.json` (V1, időalapú) / `{kávé}-scale.json` (V2, BOOKOO scale). Ahol egy kávénak több variánsa van ugyanabból a típusból (pl. wangera két hőmérséklet-verziója), `-v1`, `-v2`, ... sorszám különbözteti meg őket.
- Érintett könyvtárak: `burundi-mubuga/`, `colombia-manos-juntas/`, `twenty-eight-caturron/` (`caturron-manual.json`/`caturron-scale.json`), `el-salvador-ochupse/`, `honduras-las-calaveras/` (csak `-scale.json`, nincs manual), `wangera/` (`-manual-v1/v2.json`, `-scale-v1/v2.json`, ahol v1 = 94.0 °C, v2 = 94.5 °C).
- A PNG-k újragenerálva az új JSON nevekkel; minden recipe.md/changelog.md, `README.md`, `SUMMARY.md`, `PROFILE_GALLERY.md`, `index.html`, `FILE_NAMING.md`, `CLAUDE.md`, `PROFILE_CREATION_GUIDE.md` hivatkozása frissítve.

## Kirinyaga JSON egyszerűsítés (2026-07-25)

### Removed

- **`profiles/kirinyaga/kirinyaga-37s.json`, `kirinyaga-37s-scale-v2.json`** – törölve; ez volt a korábbi, külön megtartott "37s" alap-profilpár a fő Tea Rose recept mellett.

### Changed

- **`profiles/kirinyaga/kirinyaga-tea-rose-37s.json` → `kirinyaga-manual.json`**, **`kirinyaga-tea-rose-37s-scale-v2.json` → `kirinyaga-scale.json`** – a könyvtárban innentől csak egy V1 (`manual`) / V2 (`scale`) pár marad. A PNG-k újragenerálva, `README.md`/`SUMMARY.md`/`PROFILE_GALLERY.md`/`index.html`/`FILE_NAMING.md` hivatkozásai frissítve.

## Repo konzisztencia takarítás (2026-07-17)

### Removed

- **`profiles/caturron/`** – törölve, mert a `profiles/twenty-eight-caturron/` pontos duplikátuma volt (a JSON leírás is erre utalt: "caturron könyvtár" változat). A `profiles/twenty-eight-caturron/caturron-scale.json` marad az egyetlen kanonikus verzió.

### Changed

- **`profiles/adaptive v2/` → `profiles/adaptive-v2/`** – a könyvtárnév szóközt tartalmazott, ami sérti a FILE_NAMING.md konvenciót; átnevezve, `index.html` hivatkozásai frissítve.
- **`FILE_NAMING.md`** – eltávolítva a törölt `caturron/` könyvtárra és `caturron-42s.json` fájlra mutató, már érvénytelen példasorok.
- **`README.md`, `SUMMARY.md`, `PROFILE_GALLERY.md`** – pótolva a hiányzó, nem kávé-specifikus profilok (9 Bar Espresso, Cremina lever machine, Damian's LM Leva, Adaptive v2) dokumentációja.

## V2 – Bluetooth Scale Edition (2026-07-06)

### Added

- **BOOKOO Themis Ultra Bluetooth Scale** integráció – a mérleg Bluetooth-on csatlakozik a GaggiMate Pro-hoz
- **Beverage weight stop** minden profilhoz – a shot automatikusan megáll a céltömegnél
- **7 új Scale V2 JSON profil:**
  - `profiles/wangera/wangera-scale-v2.json` – Wangera 94.5 °C, stop 42.0 g, timeout 45 s
  - `profiles/wangera/wangera-scale-v1.json` – Wangera 94.0 °C, stop 42.0 g, timeout 45 s
  - `profiles/burundi-mubuga/burundi-mubuga-scale.json` – Burundi Mubuga, stop 42.5 g, timeout 45 s
  - `profiles/colombia-manos-juntas/colombia-manos-juntas-scale.json` – Colombia, stop 43.0 g, timeout 47 s
  - `profiles/kirinyaga/kirinyaga-tea-rose-37s-scale-v2.json` – Kirinyaga Tea Rose, stop 43.0 g, timeout 45 s
  - `profiles/kirinyaga/kirinyaga-37s-scale-v2.json` – Kirinyaga korábbi alap Scale V2 változata
  - `profiles/caturron/caturron-42s-scale-v2.json` – Caturron (caturron könyvtár), stop 42.0 g, timeout 50 s
  - `profiles/twenty-eight-caturron/caturron-scale.json` – Caturron Flavor, stop 42.0 g, timeout 50 s
- **Safety timeout** minden V2 profilban – Bluetooth disconnect esetén fallback stop
- **BLUETOOTH_SCALE_WORKFLOW.md** – párosítás, kalibráció, shot workflow, troubleshooting
- **BREW_GUIDELINES.md** – dial-in irányelvek, dózis, arány, hozam, shot értékelés
- **V2 szakasz** minden recipe.md fájlban – V2 paraméterek, fázis stop logika, V2 dial-in táblázat
- **V2 changelog bejegyzés** minden profil changelog fájlában

### Changed

- **README.md** – frissítve V2 Bluetooth Scale Edition fejezet, V2 profil táblázat, dokumentum index
- **PROFILE_GALLERY.md** – Time Based és Bluetooth Scale Edition szekciók szétválasztva
- **SUMMARY.md** – frissítve V2 profilokkal és új dokumentumokkal
- **FILE_NAMING.md** – frissítve `scale-v2` fájlnév konvencióval

### Firmware viselkedés (GaggiMate 1.8.1)

A `targets` tömb **fázis szintű** a GaggiMate 1.8.1 firmware-ben. A V2 JSON profilok az extraction fázisba helyezik a `volumetric` target-et (`type: "volumetric"`, `operator: "gte"`, `value: <céltömeg>`). A `duration` `pro` típusnál mindig hard cap — ha a scale nem csatlakozik, a duration zárja a fázist (safety fallback). A preinfusion fázisokban nincs volumetric target beállítva, ezek tisztán időalapúak maradnak.

---

## V1 – Time Based (2026-07-04)

### Added

- Kenya Wangera Stable Start 94.5 °C profil validálva – 42 g baseline rögzítve
- Wangera korai hozam célzóna frissítve: 6-8 g → 6-9 g
- BOOKOO Themis Ultra státusz pontosítva: jelenleg nincs, brew-by-weight nem aktív

### Changed

- Wangera Stable Start hőmérséklet emelve: 94.0 °C → 94.5 °C
- Windows-barát rövid fájlnevek minden profilban

---

## V2 – Profil bővítés (2026-07-04)

### Added

- Impresso - Burundi Mubuga Melon Currant 38s profil – új kávé
- Impresso - Colombia Manos Juntas Jam Mango 39s profil – új kávé

---

## V1 – Alapprofilok (2026-06-29)

### Added

- Impresso - Kenya Wangera Stable Start 38s profil
- Impresso - Kenya Kirinyaga PB Tea Rose 37s profil
- 28 - Finca el Recreo Caturron Flavor 42s profil
- `tools/render_profiles.py` – JSON → PNG grafikon generáló script
- `equipment/setup.md` – gép és daráló dokumentáció
- `speciality_kave_feldolgozasok.md` – kávé feldolgozási módszerek leírása

### Changed

- DF64V Gen 2 megnevezés egységesítve minden profilban
- RPM baseline 1200 RPM dokumentálva
- DF64V Gen 2 0-90 egész jelöléses őrléslogika rögzítve
- Automatikus előreléptető targetek eltávolítva a profilokból (targetless, determinisztikus időprofilok)
