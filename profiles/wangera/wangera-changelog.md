# Changelog – Kenya Wangera Creamy Fruit

## Repo konzisztencia (2026-07-23)

- A két V2 JSON `label`/`description` mezőjében javítva egy elgépelés: "Scale V5" → "Scale V2" (a PNG grafikonok újragenerálva az új címmel).

## V2 – Bluetooth Scale Edition (2026-07-06)

### Added

- Bluetooth Scale support: BOOKOO Themis Ultra párosítva a GaggiMate Pro-val
- Yield-based stop: automatikus shot stop beverage weight alapján
- Automatic shot stop: 42.0 g beverage weight elérésekor
- Weight-based extraction: a GaggiMate Pro a Bluetooth mérleg jelét követi
- Új profil fájl: `wangera-stable-38s-945c-scale-v2.json`
- Új profil fájl: `wangera-stable-38s-scale-v2.json` (94.0 C változat)
- Safety timeout: 45 s (Bluetooth disconnect fallback)

### Changed

- Time stop replaced by beverage weight stop az extraction fázisban
- A preinfusion és ramp fázisok időalapúak maradnak (firmware korlát)
- Recipe.md frissítve V2 szakasszal, V2 dial-in logikával

## 2026-07-04 – bevált 42g baseline rögzítve
- A **Stable Start 38s 94.5C** profil 42 g hozamot adott.
- Bevált őrlési pont: **10-11 között, inkább 11 felé**.
- Soft Ramp előtt kb. **9 g** korai hozam volt, és ez 42 g végső hozamhoz vezetett.
- Korai hozam célzóna frissítve: **6-8 g → 6-9 g**.
- Profilidő, fázisidők, nyomás/flow értékek változatlanok.

## 2026-07-04 – Wangera Stable Start hőmérséklet 94.5C
- A jó Stable Start 38s profil megtartva.
- Csak a hőmérséklet emelve: **94.0C → 94.5C**.
- Fázisidők, nyomás/flow értékek, őrlési zóna, dózis és célhozam változatlan.
- Cél: kicsit gyümölcsösebb / nyitottabb Wangera, a stabil 42g körüli lefolyás megtartásával.

## 2026-07-04 – mérleg státusz pontosítás
- Jelenleg még nincs BOOKOO Themis Ultra mérleg.
- A profilok jelenleg idő/fázis alapúak, nem aktív brew-by-weight profilok.
- BOOKOO / Bluetooth mérleges stop később opcionális: Wangera 42.0 g.
- Windows-barát rövid fájlnevek bevezetve.

## 2026-06-29 – g10 Stable Start 38s revízió
- Probléma: ugyanazzal a 38s profillal néha kb. 36g, néha kb. 43g jött le.
- Megfigyelés: a különbség már az elején látszott; rossz shotnál kb. 3g, jó shotnál kb. 7-8g korai hozam.
- Wetting módosítva: 4s / 7.5 ml/s → **5s / 8.0 ml/s**.
- Saturation módosítva: 7s / 2.1 bar → **8s / 2.3 bar**.
- Bloom rövidítve: 5s → **4s**.
- Blackberry Extraction rövidítve: 12s → **11s**.
- Teljes profilidő marad **38s**.

## 2026-06-29 – DF64V Gen 2 pontosítás
- Daráló megnevezése pontosítva: **DF64V Gen 2**.
- RPM marad aktív receptparaméterként: **1200 RPM baseline**.
- Dokumentálva: DF64V Gen 2 változtatható fordulatú, 800-1800 RPM tartományban.
