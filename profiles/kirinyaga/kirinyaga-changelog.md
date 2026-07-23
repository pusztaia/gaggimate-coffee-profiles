
## 2026-06-29 – DF64V Gen 2 pontosítás
- Daráló megnevezése pontosítva: **DF64V Gen 2**.
- RPM marad aktív receptparaméterként: **1200 RPM baseline**.
- Dokumentálva: DF64V Gen 2 változtatható fordulatú, 800-1800 RPM tartományban.

# Changelog – Kirinyaga PB Tea Rose

## V2 – Bluetooth Scale Edition (2026-07-06)

### Added

- Bluetooth Scale support: BOOKOO Themis Ultra párosítva a GaggiMate Pro-val
- Yield-based stop: automatikus shot stop beverage weight alapján
- Automatic shot stop: 43.0 g beverage weight elérésekor
- Weight-based extraction: a GaggiMate Pro a Bluetooth mérleg jelét követi
- Új profil fájl: `kirinyaga-tea-rose-37s-scale-v2.json`
- Új profil fájl: `kirinyaga-37s-scale-v2.json` (korábbi alap Scale V2 változata)
- Safety timeout: 45 s (Bluetooth disconnect fallback)

### Changed

- Time stop replaced by beverage weight stop az extraction fázisban
- A preinfusion és ramp fázisok időalapúak maradnak (firmware korlát)
- Recipe.md frissítve V2 szakasszal, V2 dial-in logikával

## 2026-06-29 – 37s targetless stabil profil
- Teljes profilidő: 37 s.
- Automatikus előreléptető targetek eltávolítva.
- DF64V Gen 2 0-90 skála, egész jelölések.
- Setup egységesítve: Gaggia Classic Pro 2025 + GaggiMate Pro, DF64V Gen 2, SSP Sweet Lab Espresso V3, IMS B682TH24.5M.

## 2026-06-24 – eredeti ízre optimalizált recept
- Tea Rose irány: hibiszkusz, csipkebogyó, fekete tea.
