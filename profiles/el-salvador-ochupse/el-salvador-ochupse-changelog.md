# Changelog – El Salvador Ochupse

## V4 – Initial BOOKOO Scale Profile (2026-07-23)

- Első BOOKOO Themis Ultra kompatibilis profil az Impresso El Salvador Ochupse kávéhoz (`el-salvador-ochupse-31s-93c-scale-v4.json`).
- Dózis: **18.5 g**. Célhozam: **41.0 g**. Hőmérséklet: **93 °C**.
- Daráló baseline: **DF64V Gen 2, 1200 RPM**. Ajánlott induló őrlés: **10–11 között, elsőre inkább 10 felé**.
- A profil első **10 másodperce** időalapú előáztatás, ezt **5 másodperces gentle ramp** követi.
- A **41.0 g-os volumetric target a 15. másodperctől aktív** a fő declining-pressure extrakciós fázisban.
- BOOKOO Themis Ultra Bluetooth kapcsolat mellett a GaggiMate a mérleg tömegadata alapján állítja meg a shotot.
- A fő extrakciós fázis maximum **30 másodperc**, így a teljes profil hard capje **45 másodperc**.
- A mérlegnek a főzés előtt bekapcsolt, csatlakoztatott és nullázott állapotban kell lennie.

## V3 – Grape Rose 31s 93C (2026-07-23)

- Első GaggiMate Pro profil az Impresso El Salvador Ochupse kávéhoz (`el-salvador-ochupse-31s-93c.json`).
- A pörkölő ajánlásából indult: 18 g be, 40 g ki, 93 °C, 10 s előáztatás, 29 s teljes idő.
- A felhasználó 18.5 g-os IMS kosarához a célhozam **41 g** lett.
- 10 másodperces előáztatás: 4 s flow wetting + 6 s 2.2 bar saturation.
- Kíméletes 7.2 bar fő extrakció és 5.4 baros declining finish.
- Teljes profilidő **31 s**, kézi 41 g stop-pal.
- Kiinduló őrlés: DF64V Gen 2, **10–11 között, inkább 10 felé**, 1200 RPM.

## Repo konzisztencia (2026-07-23)

- A recept és changelog fájlok egyesítve `el-salvador-ochupse-recipe.md` / `el-salvador-ochupse-changelog.md` néven, a repo többi kávéjánál használt egy-fájlos (V3 + V4 szakasz) konvenció szerint.
- A könyvtárban talált `el-salvador-ochupse-31s-93c-manual.json` és `-manual-profile.png` törölve, mert byte-azonos duplikátumai voltak a `el-salvador-ochupse-31s-93c.json` / `-profile.png` fájloknak.
- A V4 JSON átnevezve `el-salvador-ochupse-41g-93c-scale.json` → `el-salvador-ochupse-31s-93c-scale-v4.json`, a repo többi profiljánál használt `{v3-alap}-scale-v4.json` minta szerint; a PNG újragenerálva az új névvel.
- Setup kiegészítve: IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5).
