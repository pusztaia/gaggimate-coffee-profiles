# Projekt Changelog – Coffee Profiles

---

## Repo konzisztencia takarítás (2026-07-17)

### Removed

- **`profiles/caturron/`** – törölve, mert a `profiles/twenty-eight-caturron/` pontos duplikátuma volt (a JSON leírás is erre utalt: "caturron könyvtár" változat). A `profiles/twenty-eight-caturron/caturron-flavor-42s-scale-v2.json` marad az egyetlen kanonikus verzió.

### Changed

- **`profiles/adaptive v2/` → `profiles/adaptive-v2/`** – a könyvtárnév szóközt tartalmazott, ami sérti a FILE_NAMING.md konvenciót; átnevezve, `index.html` hivatkozásai frissítve.
- **`FILE_NAMING.md`** – eltávolítva a törölt `caturron/` könyvtárra és `caturron-42s.json` fájlra mutató, már érvénytelen példasorok.
- **`README.md`, `SUMMARY.md`, `PROFILE_GALLERY.md`** – pótolva a hiányzó, nem kávé-specifikus profilok (9 Bar Espresso, Cremina lever machine, Damian's LM Leva, Adaptive v2) dokumentációja.

## V2 – Bluetooth Scale Edition (2026-07-06)

### Added

- **BOOKOO Themis Ultra Bluetooth Scale** integráció – a mérleg Bluetooth-on csatlakozik a GaggiMate Pro-hoz
- **Beverage weight stop** minden profilhoz – a shot automatikusan megáll a céltömegnél
- **7 új Scale V2 JSON profil:**
  - `profiles/wangera/wangera-stable-38s-945c-scale-v2.json` – Wangera 94.5 °C, stop 42.0 g, timeout 45 s
  - `profiles/wangera/wangera-stable-38s-scale-v2.json` – Wangera 94.0 °C, stop 42.0 g, timeout 45 s
  - `profiles/burundi-mubuga/burundi-mubuga-38s-scale-v2.json` – Burundi Mubuga, stop 42.5 g, timeout 45 s
  - `profiles/colombia-manos-juntas/colombia-manos-juntas-39s-scale-v2.json` – Colombia, stop 43.0 g, timeout 47 s
  - `profiles/kirinyaga/kirinyaga-tea-rose-37s-scale-v2.json` – Kirinyaga Tea Rose, stop 43.0 g, timeout 45 s
  - `profiles/kirinyaga/kirinyaga-37s-scale-v2.json` – Kirinyaga korábbi alap Scale V2 változata
  - `profiles/caturron/caturron-42s-scale-v2.json` – Caturron (caturron könyvtár), stop 42.0 g, timeout 50 s
  - `profiles/twenty-eight-caturron/caturron-flavor-42s-scale-v2.json` – Caturron Flavor, stop 42.0 g, timeout 50 s
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

- Impresso Burundi Mubuga Melon Currant 38s profil – új kávé
- Impresso Colombia Manos Juntas Jam Mango 39s profil – új kávé

---

## V1 – Alapprofilok (2026-06-29)

### Added

- Impresso Kenya Wangera Stable Start 38s profil
- Impresso Kenya Kirinyaga PB Tea Rose 37s profil
- Twenty Eight Finca el Recreo Caturron Flavor 42s profil
- `tools/render_profiles.py` – JSON → PNG grafikon generáló script
- `equipment/setup.md` – gép és daráló dokumentáció
- `speciality_kave_feldolgozasok.md` – kávé feldolgozási módszerek leírása

### Changed

- DF64V Gen 2 megnevezés egységesítve minden profilban
- RPM baseline 1200 RPM dokumentálva
- DF64V Gen 2 0-90 egész jelöléses őrléslogika rögzítve
- Automatikus előreléptető targetek eltávolítva a profilokból (targetless, determinisztikus időprofilok)
