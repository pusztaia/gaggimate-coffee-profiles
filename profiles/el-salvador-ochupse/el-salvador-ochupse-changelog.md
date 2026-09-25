# Changelog – El Salvador Ochupse

## V3 – Gentle Flow Extraction with Grind 11 (2026-09-25)

- Harmadik BOOKOO Themis Ultra kompatibilis profil az Impresso - El Salvador Ochupse kávéhoz (`el-salvador-ochupse-93c-scale-v3.json`).
- **Dózis:** 18.5 g. **Célhozam:** 41.0 g. **Hőmérséklet:** 93 °C. **Grinder:** DF64V Gen 2, grind 11.
- **Előáztatás:** Kíméletes wetting (5.5 ml/s flow helyett az előző 7.5 ml/s-ból csökkent), hogy megőrizze a finom aromákat.
- **Fő extrakció:** Flow-alapú, **nyomáscsökkentéssel 7.2 bar-ról 5.2 bar-ra** lineáris átmenettel. Flow target: **1.8 ml/s**.
- **Volumetric target:** 41.0 g a fő extrakciós fázisban, BOOKOO Bluetooth mérleggel.
- **Teljes profil hard cap:** 50 másodperc.
- **Ajánlott őrlési pont:** grind 11 (korábban 10–11 között ajánlott volt).

## Repo konzisztencia (2026-07-25)

- A JSON fájlnevek átalakítva: `el-salvador-ochupse-31s-93c.json` → `el-salvador-ochupse-manual.json`, `el-salvador-ochupse-31s-93c-scale-v2.json` → `el-salvador-ochupse-scale.json` (a `kirigomix` naming convention helyett).

## V1 – Grape Rose 31s 93C (2026-07-23)

- Első GaggiMate Pro profil az Impresso - El Salvador Ochupse kávéhoz (`el-salvador-ochupse-manual.json`).
- A pörkölő ajánlásából indult: 18 g be, 40 g ki, 93 °C, 10 s előáztatás, 29 s teljes idő.
- A felhasználó 18.5 g-os IMS kosarához a célhozam **41 g** lett.
- 10 másodperces előáztatás: 4 s flow wetting + 6 s 2.2 bar saturation.
- Kíméletes 7.2 bar fő extrakció és 5.4 baros declining finish.
- Teljes profilidő **31 s**, kézi 41 g stop-pal.
- Kiinduló őrlés: DF64V Gen 2, **10–11 között, inkább 10 felé**, 1200 RPM.

## Repo konzisztencia (2026-07-23)

- A recept és changelog fájlok egyesítve `el-salvador-ochupse-recipe.md` / `el-salvador-ochupse-changelog.md` néven, a repo többi kávéjánál használt egy-fájlos (V1 + V2 szakasz) konvenció szerint.
- A könyvtárban talált `el-salvador-ochupse-manual-manual.json` és `-manual-profile.png` törölve, mert byte-azonos duplikátumai voltak a `el-salvador-ochupse-manual.json` / `-profile.png` fájloknak.
- Az időalapú profil PNG-je (`el-salvador-ochupse-manual-profile.png`) megmarad az V1 referenciájaként.
- Setup kiegészítve: IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5).
