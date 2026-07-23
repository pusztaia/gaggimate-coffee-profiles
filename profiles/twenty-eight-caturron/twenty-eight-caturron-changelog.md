
# Changelog – Twenty Eight Finca el Recreo Caturron (twenty-eight-caturron)

## V2 – Bluetooth Scale Edition (2026-07-06)

### Added

- Bluetooth Scale support: BOOKOO Themis Ultra párosítva a GaggiMate Pro-val
- Yield-based stop: automatikus shot stop beverage weight alapján
- Automatic shot stop: 42.0 g beverage weight elérésekor
- Weight-based extraction: a GaggiMate Pro a Bluetooth mérleg jelét követi
- Új profil fájl: `caturron-flavor-42s-scale-v2.json`
- Safety timeout: 50 s (Bluetooth disconnect fallback)

### Changed

- Time stop replaced by beverage weight stop az extraction fázisban
- A preinfusion és ramp fázisok időalapúak maradnak (firmware korlát)
- Recipe.md frissítve V2 szakasszal, V2 dial-in logikával

## 2026-06-29 – DF64V Gen 2 pontosítás
- Daráló megnevezése pontosítva: **DF64V Gen 2**.
- RPM marad aktív receptparaméterként: **1200 RPM baseline**.
- Dokumentálva: DF64V Gen 2 változtatható fordulatú, 800-1800 RPM tartományban.

# Changelog – Twenty Eight Finca el Recreo Caturron

## 2026-06-29 – Twenty Eight brand fix + GitHub-clean verzió
- A kávé márkája javítva: **Twenty Eight**.
- Profilnév és fájlnév frissítve, hogy tartalmazza a márkát és a kávé nevét.
- Setup egységesítve: Gaggia Classic Pro 2025 + GaggiMate Pro, DF64V Gen 2, SSP Sweet Lab Espresso V3, IMS B682TH24.5M.
- DF64V Gen 2 0-90 egész jelöléses őrléslogika.
- MD recept JSON blokk nélkül.
- Targetless, determinisztikus 42 s profil.

## 2026-06-24 – eredeti Caturron Flavor recept
- Cél: meggy, konyakmeggy, piros gyümölcs, bonbonos édesség.
