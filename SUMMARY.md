# GaggiMate Coffee Profiles V2 – Összefoglaló

**Verzió:** V2 – Bluetooth Scale Edition

**Gép:** Gaggia Classic Pro 2025 + GaggiMate Pro
**Daráló:** DF64V Gen 2 · SSP Sweet Lab Espresso V3 kések · 1200 RPM baseline
**Kosár:** IMS B682TH24.5M · Dózis: 18.5 g
**Puck screen:** IMS E&B Lab puck diffuser screen, Ø 2.4 mm, 253 lyuk (DS58.5)
**Mérleg:** BOOKOO Themis Ultra (Bluetooth, aktív)
**Stop mód:** beverage weight (V2) / időalapú fallback (V1)

---

## V2 Scale Edition profilok

| Kávé | Target Yield | Arány | Hő | Safety | V2 JSON |
|---|---:|---|---:|---:|---|
| Kenya Wangera | 42.0 g | 1:2.27 | 94.5 °C | 45 s | [wangera-scale-v2.json](profiles/wangera/wangera-scale-v2.json) |
| Kenya Wangera (94C) | 42.0 g | 1:2.27 | 94.0 °C | 45 s | [wangera-scale-v1.json](profiles/wangera/wangera-scale-v1.json) |
| Burundi Mubuga | 42.5 g | 1:2.30 | 94.0 °C | 64 s | [burundi-mubuga-scale-v4-fruity.json](profiles/burundi-mubuga/burundi-mubuga-scale-v4-fruity.json) |
| Colombia Manos Juntas | 43.0 g | 1:2.32 | 94.5 °C | 47 s | [colombia-manos-juntas-scale.json](profiles/colombia-manos-juntas/colombia-manos-juntas-scale.json) |
| Kenya Kirinyaga PB | 43.0 g | 1:2.32 | 94.5 °C | 45 s | [kirinyaga-scale.json](profiles/kirinyaga/kirinyaga-scale.json) |
| 28 Caturron | 42.0 g | 1:2.27 | 95.0 °C | 50 s | [caturron-scale.json](profiles/twenty-eight-caturron/caturron-scale.json) |
| El Salvador Ochupse | 41.0 g | 1:2.22 | 93.0 °C | 45 s | [el-salvador-ochupse-scale.json](profiles/el-salvador-ochupse/el-salvador-ochupse-scale.json) |
| Honduras Las Calaveras | 39.0 g | 1:2.11 | 92.0 °C | 33 s | [honduras-las-calaveras-scale.json](profiles/honduras-las-calaveras/honduras-las-calaveras-scale.json) |

---

## Általános (nem kávé-specifikus) profilok

| Profil | Leírás | JSON | Recept |
|---|---|---|---|
| 9 Bar Espresso | Klasszikus 9 baros baseline | [profile-9bar.json](profiles/9-bar/profile-9bar.json) | [9-bar-recipe.md](profiles/9-bar/9-bar-recipe.md) |
| Cremina lever machine | Sötét pörkölésű, testes, édes, leveres espresso | [profile-lever.json](profiles/cremina-lever/profile-lever.json) | [cremina-lever-recipe.md](profiles/cremina-lever/cremina-lever-recipe.md) |
| Damian's LM Leva | Modern specialty, világos-közepes pörköléshez | [profile-lmleva.json](profiles/damians-lm-leva/profile-lmleva.json) | [damians-lm-leva-recipe.md](profiles/damians-lm-leva/damians-lm-leva-recipe.md) |
| Adaptive v2 | Univerzális, adaptív preinfusion, light-to-medium pörköléshez | [profile-adapt.json](profiles/adaptive-v2/profile-adapt.json) | [adaptive-v2-recipe.md](profiles/adaptive-v2/adaptive-v2-recipe.md) |

---

## V1 Time Based profilok (referencia)

| Kávé | Profil | Idő | Hő | Dózis | Célhozam | Őrlés | JSON | Recept |
|---|---|---:|---:|---:|---:|---:|---|---|
| Kenya Wangera | Stable Start | 38 s | 94.5 °C | 18.5 g | 42 g | 10-11 | [wangera-manual-v2.json](profiles/wangera/wangera-manual-v2.json) | [wangera-recipe.md](profiles/wangera/wangera-recipe.md) |
| Burundi Mubuga | Melon Currant | 38 s | 94.5 °C | 18.5 g | 42.5 g | 8-9 | [burundi-mubuga-manual.json](profiles/burundi-mubuga/burundi-mubuga-manual.json) | [burundi-mubuga-recipe.md](profiles/burundi-mubuga/burundi-mubuga-recipe.md) |
| Colombia Manos Juntas | Jam Mango | 39 s | 94.5 °C | 18.5 g | 43 g | 10-11 | [colombia-manos-juntas-manual.json](profiles/colombia-manos-juntas/colombia-manos-juntas-manual.json) | [colombia-manos-juntas-recipe.md](profiles/colombia-manos-juntas/colombia-manos-juntas-recipe.md) |
| Kenya Kirinyaga PB | Tea Rose | 37 s | 94.5 °C | 18.5 g | 43 g | 9-10 | [kirinyaga-manual.json](profiles/kirinyaga/kirinyaga-manual.json) | [kirinyaga-recipe.md](profiles/kirinyaga/kirinyaga-recipe.md) |
| 28 Caturron | Flavor | 42 s | 95 °C | 18.5 g | 42 g | 8-10 | [caturron-manual.json](profiles/twenty-eight-caturron/caturron-manual.json) | [twenty-eight-caturron-recipe.md](profiles/twenty-eight-caturron/twenty-eight-caturron-recipe.md) |
| El Salvador Ochupse | Grape Rose | 31 s | 93 °C | 18.5 g | 41 g | 10-11 | [el-salvador-ochupse-manual.json](profiles/el-salvador-ochupse/el-salvador-ochupse-manual.json) | [el-salvador-ochupse-recipe.md](profiles/el-salvador-ochupse/el-salvador-ochupse-recipe.md) |

---

## Ízprofilok

| Kávé | Feldolgozás | Ízjegyek |
|---|---|---|
| Kenya Wangera | washed | szeder · tejszín · pomelo |
| Burundi Mubuga | natural | sárgadinnye · alma · ribizli |
| Colombia Manos Juntas | anaerobic natural | vörösáfonya dzsem · karamell · mangó |
| Kenya Kirinyaga PB | washed | hibiszkusz · csipkebogyó · fekete tea |
| 28 Caturron | natural | meggy · konyakmeggy · piros gyümölcs · bonbonos édesség |
| El Salvador Ochupse | natural anaerob | szőlő · csipkebogyó · sárgabarack · étcsokoládé |
| Honduras Las Calaveras | natural anaerob | sangria · sült alma · szegfűszeg |

---

## Általános profilgrafikonok

### 9 Bar Espresso

![9 Bar Espresso](profiles/9-bar/profile-9bar-profile.png)

### Cremina lever machine

![Cremina lever machine](profiles/cremina-lever/profile-lever-profile.png)

### Damian's LM Leva

![Damian's LM Leva](profiles/damians-lm-leva/profile-lmleva-profile.png)

### Adaptive v2

![Adaptive v2](profiles/adaptive-v2/profile-adapt-profile.png)

---

## V1 Profilgrafikonok

### Kenya Wangera – Stable Start 38s 94.5C

![Wangera](profiles/wangera/wangera-profile.png)

### Burundi Mubuga – Melon Currant 38s

![Burundi Mubuga](profiles/burundi-mubuga/burundi-mubuga-manual-profile.png)

### Colombia Manos Juntas – Jam Mango 39s

![Colombia Manos Juntas](profiles/colombia-manos-juntas/colombia-manos-juntas-profile.png)

### Kenya Kirinyaga PB – Tea Rose 37s

![Kirinyaga](profiles/kirinyaga/kirinyaga-profile.png)

### 28 Caturron – Flavor 42s

![28 Caturron](profiles/twenty-eight-caturron/twenty-eight-caturron-profile.png)

### El Salvador Ochupse – Grape Rose 31s 93C

![El Salvador Ochupse](profiles/el-salvador-ochupse/el-salvador-ochupse-manual-profile.png)

---

## Könyvtárszerkezet

```
profiles/
├── wangera/
│   ├── wangera-manual-v2.json                ← V1 időalapú profil (94.5C, fő)
│   ├── wangera-manual-v1.json                ← V1 időalapú profil (94.0C)
│   ├── wangera-scale-v2.json                 ← V2 Scale Edition (94.5C)
│   ├── wangera-scale-v1.json                 ← V2 Scale Edition (94.0C)
│   ├── wangera-profile.png                   ← V1 grafikon
│   ├── wangera-recipe.md                     ← recept (V1 + V2 szakasz)
│   └── wangera-changelog.md
├── burundi-mubuga/
│   ├── burundi-mubuga-manual.json
│   ├── burundi-mubuga-scale.json
│   ├── burundi-mubuga-profile.png
│   ├── burundi-mubuga-recipe.md
│   └── burundi-mubuga-changelog.md
├── colombia-manos-juntas/
│   ├── colombia-manos-juntas-manual.json
│   ├── colombia-manos-juntas-scale.json
│   ├── colombia-manos-juntas-profile.png
│   ├── colombia-manos-juntas-recipe.md
│   └── colombia-manos-juntas-changelog.md
├── kirinyaga/
│   ├── kirinyaga-manual.json          ← V1 időalapú profil
│   ├── kirinyaga-scale.json           ← V2 Scale Edition
│   ├── kirinyaga-profile.png
│   ├── kirinyaga-recipe.md
│   └── kirinyaga-changelog.md
├── twenty-eight-caturron/
│   ├── caturron-manual.json
│   ├── caturron-scale.json
│   ├── twenty-eight-caturron-profile.png
│   ├── twenty-eight-caturron-recipe.md
│   └── twenty-eight-caturron-changelog.md
├── 9-bar/
│   ├── profile-9bar.json
│   ├── 9-bar-recipe.md
│   └── 9-bar-changelog.md
├── cremina-lever/
│   ├── profile-lever.json
│   ├── cremina-lever-recipe.md
│   └── cremina-lever-changelog.md
├── damians-lm-leva/
│   ├── profile-lmleva.json
│   ├── damians-lm-leva-recipe.md
│   └── damians-lm-leva-changelog.md
├── adaptive-v2/
│   ├── profile-adapt.json
│   ├── adaptive-v2-recipe.md
│   └── adaptive-v2-changelog.md
├── el-salvador-ochupse/
│   ├── el-salvador-ochupse-manual.json          ← V1 időalapú profil
│   ├── el-salvador-ochupse-scale.json ← V2 Scale Edition
│   ├── el-salvador-ochupse-manual-profile.png
│   ├── el-salvador-ochupse-scale-profile.png
│   ├── el-salvador-ochupse-recipe.md             ← recept (V1 + V2 szakasz)
│   └── el-salvador-ochupse-changelog.md
├── honduras-las-calaveras/
│   ├── honduras-las-calaveras-scale.json      ← csak V2 Scale Edition
│   ├── honduras-las-calaveras-scale-profile.png
│   ├── honduras-las-calaveras-recipe.md
│   └── honduras-las-calaveras-changelog.md
equipment/
└── setup.md
templates/
├── recipe-template.md
├── shot-log-template.md
└── changelog-template.md
tools/
└── render_profiles.py
```

---

## Dokumentumok

| Fájl | Tartalom |
|---|---|
| [README.md](README.md) | Projekt áttekintő, profilok táblázata, Bluetooth Scale Edition leírás |
| [BLUETOOTH_SCALE_WORKFLOW.md](BLUETOOTH_SCALE_WORKFLOW.md) | Párosítás, kalibráció, shot workflow, troubleshooting |
| [BREW_GUIDELINES.md](BREW_GUIDELINES.md) | Dial-in irányelvek, dózis, arány, hozam, shot értékelés |
| [PROFILE_GALLERY.md](PROFILE_GALLERY.md) | V1 és V2 profilgrafikonok galériája |
| [FILE_NAMING.md](FILE_NAMING.md) | Fájlelnevezési konvenció |
| [CHANGELOG.md](CHANGELOG.md) | Projekt szintű változásnapló |
| [speciality_kave_feldolgozasok.md](speciality_kave_feldolgozasok.md) | Kávé feldolgozási módszerek |
| [equipment/setup.md](equipment/setup.md) | Gép és daráló beállítások |

---

## Grafikonok újragenerálása

```bash
# Összes profil (V1 és V2 egyaránt)
python3 tools/render_profiles.py

# Egyetlen profil
python3 tools/render_profiles.py profiles/wangera/wangera-manual-v2.json
python3 tools/render_profiles.py profiles/wangera/wangera-scale-v2.json
```

A script a JSON neve alapján generálja a PNG-t: `{json-stem}-profile.png`.

---

## JSON import

A JSON profilokat (V1 és V2 egyaránt) a GaggiMate Web UI-ban lehet importálni: **Profiles → Import**.
