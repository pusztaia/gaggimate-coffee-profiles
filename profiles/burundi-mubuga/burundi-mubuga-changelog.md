# Changelog – Burundi Mubuga Melon Currant

## V4 – Bluetooth Scale Edition (2026-07-06)

### Added

- Bluetooth Scale support: BOOKOO Themis Ultra párosítva a GaggiMate Pro-val
- Yield-based stop: automatikus shot stop beverage weight alapján
- Automatic shot stop: 42.5 g beverage weight elérésekor
- Weight-based extraction: a GaggiMate Pro a Bluetooth mérleg jelét követi
- Új profil fájl: `burundi-mubuga-38s-scale-v4.json`
- Safety timeout: 45 s (Bluetooth disconnect fallback)

### Changed

- Time stop replaced by beverage weight stop az extraction fázisban
- A preinfusion és ramp fázisok időalapúak maradnak (firmware korlát)
- Recipe.md frissítve V4 szakasszal, V4 dial-in logikával

## 2026-07-04 – kezdeti GaggiMate Pro profil
- Új profil Impresso Burundi Mubuga kávéhoz.
- Cél: sárgadinnye, alma, ribizli; tiszta, lédús, nem száraz espresso.
- Teljes profilidő: 38 s.
- Hőmérséklet: 94.5 °C.
- Dózis: 18.5 g.
- Célhozam: 42-43 g, ideálisan 42.5 g.
- DF64V Gen 2 baseline: grind 10 körül, 1200 RPM.
- BOOKOO Themis Ultra jelenleg nincs; brew-by-weight nem aktív.
