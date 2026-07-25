# Moduláris GaggiMate index

## Fájlok

- `index.html` – dinamikus, egységes UI.
- `profiles/catalog.json` – a profilkártyák egyetlen katalógusa.

A repository-ban helyezd el őket így:

```text
index.html
profiles/
├── catalog.json
├── 9-bar/
├── wangera/
└── ...
```

## Új profil hozzáadása

1. Hozd létre a profil mappáját a `profiles/` alatt.
2. Tedd bele a GaggiMate JSON-t, az abból generált `*-profile.png` fájlt, a recipe MD-t és a changelog MD-t.
3. Adj hozzá egy bejegyzést a `profiles/catalog.json` `profiles` tömbjéhez.
4. Az `index.html` fájlt nem kell módosítani.

A kártya az aktuálisan választott JSON-ból számolja:
- a gyökérhőmérsékletet;
- a maximális idővonalat;
- a volumetric stopot;
- a fázislistát;
- az aktív pressure/flow setpointokat;
- a dinamikus SVG előnézeti grafikont.

## Helyi futtatás

A Fetch API miatt ne `file://` módban nyisd meg:

```bash
python -m http.server 8000
```

Ezután:

```text
http://localhost:8000/
```
