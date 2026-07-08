# Changelog – Adaptive v2

## 2026-07-07 – dokumentáció és analízis

- Profil részletes analízise elvégezve.
- Fázis-logika dokumentálva: target-vezérelt adaptív preinfusion, kétszintű hőmérséklet (93°C → 88°C).
- `flow: -1` sentinel viselkedés és `pumped` target mechanizmus leírva.
- Recipe.md létrehozva: fázis-analízis, alap recept táblázat, dial-in logika, firmware megjegyzések.
- Könyvtár átnevezési megjegyzés: az `adaptive v2` könyvtárnév szóközt tartalmaz — fájlrendszer kompatibilitáshoz érdemes átnevezni `adaptive-v2`-re.

## 2026-07-07 – beépítés az index.html-be

- Profil kártya hozzáadva a Profilok tabhoz az index.html-ben.
- Recept és changelog modal tartalomként beágyazva.
- Fázis sávok megjelenítve a kártyán (max duration alapján, mert az adaptive profil valós ideje változó).
