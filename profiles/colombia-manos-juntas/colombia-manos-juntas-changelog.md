# Changelog – Colombia Manos Juntas Jam Mango

## V4 – Bluetooth Scale Edition (2026-07-06)

### Added

- Bluetooth Scale support: BOOKOO Themis Ultra párosítva a GaggiMate Pro-val
- Yield-based stop: automatikus shot stop beverage weight alapján
- Automatic shot stop: 43.0 g beverage weight elérésekor
- Weight-based extraction: a GaggiMate Pro a Bluetooth mérleg jelét követi
- Új profil fájl: `colombia-manos-juntas-39s-scale-v4.json`
- Safety timeout: 47 s (Bluetooth disconnect fallback)

### Changed

- Time stop replaced by beverage weight stop az extraction fázisban
- A preinfusion és ramp fázisok időalapúak maradnak (firmware korlát)
- Recipe.md frissítve V4 szakasszal, V4 dial-in logikával

## 2026-07-04 – kezdeti GaggiMate Pro profil
- Új profil Impresso Colombia Manos Juntas kávéhoz.
- Cél: vörösáfonya dzsem, karamell, mangó; szirupos, gyümölcsös espresso.
- Teljes profilidő: 39 s.
- Hőmérséklet: 94.5 °C.
- Dózis: 18.5 g.
- Célhozam: 42-44 g, ideálisan 43 g.
- DF64V Gen 2 baseline: grind 10 körül, 1200 RPM.
- BOOKOO Themis Ultra jelenleg nincs; brew-by-weight nem aktív.
