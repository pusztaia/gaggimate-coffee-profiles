# Changelog – Honduras Las Calaveras

## V1 – Initial BOOKOO Scale Profile (2026-07-23)

### Added

- Első GaggiMate Pro profil az Impresso Honduras Las Calaveras kávéhoz.
- BOOKOO Themis Ultra alapú automatikus stop **39.0 g** italnál.
- **18.5 g** dózis, **92 °C**, **8 s** előáztatás.
- Kiinduló őrlési zóna: **10–11**, elsőre inkább **10 felé**.
- Setup dokumentálva: IMS B682TH24.5M, IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5), SSP Sweet Lab Espresso V3 és DF64V Gen 2.
- Rövid JSON description mező.

### Profile design

- 8 s alacsony nyomású előáztatás.
- Egyetlen, 39.0 g-os súlytargettel lezárt fő extrakciós fázis.
- 4 s lágy nyomásfelépítés 7.2 barra.
- 33 s teljes hard cap Bluetooth/target hiba esetére.

### Source recipe adaptation

- Impresso ajánlás: 18 g → 38 g, 92 °C, 8 s előáztatás, 22 s teljes idő.
- 18.5 g dózishoz arányosan igazított cél: **39.0 g**, arány **1:2.11**.

## Repo konzisztencia (2026-07-23)

- A recept és changelog fájl átnevezve `honduras-las-calaveras-recipe.md` / `honduras-las-calaveras-changelog.md` névre (a JSON-fájlnév-alapú `-39g-92c-scale-recipe.md` helyett), a FILE_NAMING.md könyvtárnév-alapú konvenciója szerint.
- A JSON átnevezve `honduras-las-calaveras-39g-92c-scale.json` → `honduras-las-calaveras-scale-v2.json`, a repo többi profiljánál használt `-scale-v2` végződés szerint (nincs külön időalapú V1 verzió, ezért nincs profilidő a névben); a PNG újragenerálva az új névvel.
