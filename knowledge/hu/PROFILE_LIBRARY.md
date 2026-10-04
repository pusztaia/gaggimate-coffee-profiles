# Profilkönyvtár

Azonnal használható extrakciós profilok Gaggimate Pro-hoz. Ezek **generikus sablonok** — a dialing során létrehozott, kávéspecifikus profilok a `coffees/{roaster}-{coffee-name}/` könyvtárban kerülnek mentésre.

> **Mélyebb betekintés:** A teljes profildefiníciók JSON-nal, paraméterekkel és ízjegy-elvárásokkal itt találhatók: [`reference/PROFILE_LIBRARY_REFERENCE.md`](../reference/PROFILE_LIBRARY_REFERENCE.md).

> **Megjegyzés:** Minden profil **22 g dózisra** van méretezve. A volumetrikus célok a megadott arányt tükrözik 22 g bemenetnél. Ha a kosárméret változik, számold újra: `cél = dózis × arány`.

---

## Gyors referencia

| Profil | Pörkölés | Hő | Arány | Idő | Mire jó |
|---------|-------|------|-------|------|----------|
| [Classic 9-Bar](#classic-9-bar) | Közepes | 93°C | 1:2 | 25-32s | Mindennapi espresso |
| [Light Roast Bloom](#light-roast-bloom) | Világos | 95°C | 1:2.5 | 28-35s | Gyümölcsös, virágos kávék |
| [Dark Roast Gentle](#dark-roast-gentle) | Sötét | 89°C | 1:1.5-2 | 22-28s | Olasz pörkölések, tejes italok |
| [Natural Process Bloom](#natural-process-bloom) | Világos-közepes | 94°C | 1:2-2.5 | 30-38s | Natural/száraz feldolgozású szemek |
| [Turbo Shot](#turbo-shot) | Bármilyen | 96°C | 1:2.5-3 | 15-20s | Tisztaság, élénkség |
| [Allongé](#allongé) | Világos-közepes | 94°C | 1:4-5 | 40-50s | Hosszú, édes, teás jellegű |
| [Lever Decline](#lever-decline) | Közepes | 91°C | 1:2 | 28-35s | Szirupos test, komplex |
| [Milk Drink Base](#milk-drink-base) | Közepes-sötét | 92°C | 1:1.5 | 22-26s | Koncentrált, intenzív test |

---

## Profil összefoglalók

### Classic 9-Bar
A megbízható munkaló — pre-infúzió → ramp → hold a legtöbb közepes pörkölésű kávéhoz.
`93°C | 1:2 | 25-32s | Standard őrlés | Kiegyensúlyozott, csokoládés, enyhe édesség`

### Light Roast Bloom
A bloom fázis fokozza az édességet a skandináv stílusú világos pörkölésekben.
`95°C | 1:2.5 | 28-35s | Finomabb a közepesnél | Élénk savasság, virágos, csonthéjas gyümölcs`

### Dark Roast Gentle
Alacsonyabb hő és nyomás a keserűség elkerülésére; rövidebb arány a testért.
`89°C | 1:1.5-2 | 22-28s | Durvább a közepesnél | Csokoládé, karamell, teljes test`

### Natural Process Bloom
A kibővített bloom megfékezi a natural feldolgozás intenzitását, megőrzi a gyümölcsösséget.
`94°C | 1:2-2.5 | 30-38s | Közepesen finom | Áfonya, eper, lédús test`

### Turbo Shot
Durva őrlés, nagy flow, gyors extrakció a tisztaságért. Az aránynak 1:2.5-3-nak kell lennie — egy 1:2 turbo savanyú lesz.
`96°C | 1:2.5-3 | 15-20s | Jelentősen durvább | Élénk, tiszta, teás jellegű`

### Allongé
Hosszú, édes extrakció kibővített arányokon — nem lungo, hanem valódi kibővített extrakció.
`94°C | 1:4-5 | 40-50s | Kicsit durvább | Édes, teás jellegű, finom savasság`

### Lever Decline
A rugós lever-t utánozza csökkenő nyomással, szirupos testért és komplex édességért.
`91°C | 1:2 | 28-35s | Kicsit finomabb a classicnál | Szirupos, karamell, csökkentett savasság`

### Milk Drink Base
Erőteljes, koncentrált ristretto-stílusú shot maximális intenzitással.
`92°C | 1:1.5 | 22-26s | Standard vagy kicsit finomabb | Intenzív, csokoládés/karamelles, teljes test`

---

## Firmware beépített profilok

### Automatic Pro (vIT3)

Az **Automatic Pro** a Gaggimate fejlesztője által karbantartott, firmware-be épített profil — nem agent által létrehozott profil. Előre telepítve szállítják a Gaggimate Pro eszközökön, több dózisváltozatban (16g, 18g, 20g, 22g). *(Empirikus/nem igazolt a forrásban: a repóhoz ellenőrzött `gaggimate-source` firmware fa csak azt mutatja, hogy a `ProfileManager.cpp` első bootkor egyetlen generikus `"Default"` standard-típusú profilt hoz létre automatikusan — a forráskódban nem található beágyazott "Automatic Pro" JSON vagy `vIT3` címke, így ez az állítás eszköz-/közösségi megfigyelésen alapul, nem a firmware forráskódján.)*

Flow-alapú változó nyomást használ, csökkenő flow-jú extrakcióval. Válaszd ki a megfelelő dózisváltozatot a gép kijelzőjén, majd állítsd be a hőmérsékletet és a célsúlyt/időt.

> **Teljes dokumentáció**: [`automatic-pro/AUTOMATIC_PRO_GUIDE.md`](automatic-pro/AUTOMATIC_PRO_GUIDE.md) — 5-fázisú architektúra, dózisskálázás és a Second Blooming hatás.

---

## Profilválasztási útmutató

### Ízcél alapján

| Amiből többet akarsz... | Próbáld ezt a profilt | Fő változtatás |
|--------------|------------------|------------|
| Élénkség/savasság | Light Roast Bloom | Magasabb hő, hosszabb arány |
| Édesség | Lever Decline vagy Natural Process Bloom | Bloom fázis, csökkenő nyomás |
| Test | Dark Roast Gentle | Alacsonyabb hő, rövidebb arány |
| Tisztaság | Turbo Shot | Durva őrlés, nagy flow |
| Egyensúly | Classic 9-Bar | Standard paraméterek |

### Probléma alapján

| Probléma | Javasolt profil | Miért |
|-------|-------------------|-----|
| A shotok túl savanyúak | Light Roast Bloom | Magasabb hő, bloom a jobb extrakcióért |
| A shotok túl keserűek | Dark Roast Gentle | Alacsonyabb hő/nyomás, elvékonyodás a végén |
| Több intenzitás kell | Milk Drink Base | Rövidebb arány koncentrálja az ízt |
| Következetlen | Automatic Pro (firmware) | Önszabályozó flow-vezérlés |
| Channeling | Natural Process Bloom | Kibővített pre-infúzió, kíméletes feltöltés |

---

*A [AI] jelölésű profilokat a barista asszisztensed hozta létre, és biztonságosan törölhetők az MCP eszközökkel.*
