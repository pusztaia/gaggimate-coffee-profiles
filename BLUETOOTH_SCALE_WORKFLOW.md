# Bluetooth Scale Workflow

**Hardver:** BOOKOO Themis Ultra + GaggiMate Pro + Gaggia Classic Pro 2025

---

## 1. Párosítás

### Előfeltételek

- A GaggiMate Pro firmware legújabb verziója telepítve
- A BOOKOO Themis Ultra mérleg töltve (min. 50%)
- A GaggiMate Web UI elérhető a helyi hálózaton

### Párosítás lépései

1. Kapcsold be a BOOKOO Themis Ultra mérleget
2. Nyisd meg a GaggiMate Web UI-t (IP cím a GaggiMate kijelzőjén)
3. Navigálj a **Settings → Scale** menüpontra
4. Kattints a **Scan** gombra – a BOOKOO Themis Ultra megjelenik a listában
5. Válaszd ki és kattints a **Connect** gombra
6. A kapcsolat sikerességét a Web UI státuszsor és a mérleg LED jelzi
7. A GaggiMate megjegyzi a mérleget; következő bekapcsoláskor automatikusan kapcsolódik

### Ellenőrzés

- A GaggiMate Web UI-ban a mérleg státusza **Connected** legyen
- Helyezz egy ismert súlyú tárgyat a mérlegre és ellenőrizd, hogy a Web UI-ban megjelenik-e a súly
- Ha a mérleg nem jelenik meg a Scan listában: kapcsold ki és vissza, majd próbáld újra

---

## 2. Kalibráció

### Mikor kell kalibrálni?

- Első használat előtt
- Ha a mért érték eltér a valóstól (±0.5 g-nál több)
- Ha a mérleget ejtés vagy ütés érte
- Havonta egyszer ellenőrzés ajánlott

### Kalibráció lépései

1. Kapcsold be a mérleget és hagyd bemelegedni 2-3 percig
2. Győződj meg róla, hogy a mérleg vízszintes felületen áll
3. Távolíts el minden tárgyat a mérlegről
4. Nyomd meg és tartsd a **Tare** gombot a nullázáshoz
5. A BOOKOO Themis Ultra belső kalibrációhoz: lásd a mérleg kézikönyvét
6. Ellenőrzés: helyezz egy ismert tömegű kalibrációs súlyt a mérlegre

### Tare workflow shotonként

1. Csésze felhelyezése a mérlegre
2. **Tare** (nullázás) – a kijelző 0.0 g-t mutat
3. Portafilter behelyezése a gépbe
4. Shot indítása

> **Fontos:** A tare-t mindig a shot indítása előtt, a csészével végezd. A GaggiMate a tare utáni beverage weight értéket méri.

---

## 3. Shot workflow

### Teljes workflow (V2 Scale Edition profil)

1. **Mérleg bekapcsolása** – hagyd 1-2 percig stabilizálódni
2. **GaggiMate Web UI** – ellenőrizd, hogy a mérleg státusza Connected
3. **Profil betöltése** – importáld a kívánt `*-scale-v2.json` fájlt a Web UI-ban (**Profiles → Import**)
4. **Kávé adagolása** – 18.5 g (DF64V Gen 2, a profilnak megfelelő jelölésen)
5. **Puck prep** – WDT, tamp, puck screen (száraz és tiszta)
6. **Portafilter behelyezése**
7. **Csésze a mérlegre** – üres csésze, mérleg tare
8. **Shot indítása** – a GaggiMate elindítja a profilt
9. **Automatikus stop** – a GaggiMate megáll, amikor a beverage weight eléri a `stop_at_g` értéket
10. **Hozam ellenőrzése** – a mérleg mutatja a végső értéket; rögzítsd a shot log-ban

### V2 profil stop logika (GaggiMate 1.8.1 firmware)

| Fázis | Stop trigger | Megjegyzés |
|---|---|---|
| Preinfusion (Wetting, Saturation, Bloom) | Időalapú (duration hard cap) | Nincs volumetric target beállítva |
| Ramp | Időalapú (duration hard cap) | Nincs volumetric target beállítva |
| Extraction | **volumetric target (gramm)** | OR feltétel: ha a target tüzel, fázis véget ér |
| Extraction – fallback | duration hard cap | Ha scale nem csatlakozik vagy target nem tüzel |
| Finish | Időalapú (duration hard cap) | Csak ha az Extraction target tüzelt |

**Hogyan működik a `targets` a firmware-ben:**

- A `targets` tömb **fázis szintű** — minden phase-ben külön definiálható
- Kiértékelés: minden **100 ms**-ban
- Az OR logika: az első tüzelő target azonnal zárja a fázist
- `pro` típusnál a `duration` **mindig hard cap** — a target csak hamarabb zárhatja a fázist, de tovább nem tarthatja nyitva
- `volumetric` target csak aktív Bluetooth scale **és** brew-by-weight mód esetén működik; ha ezek hiányoznak, a target csendesen nem tüzel és a duration veszi át a stopot

---

## 4. Tipikus hibák és elhárítás

### A mérleg nem jelenik meg a Scan listában

**Okok és megoldások:**

| Ok | Megoldás |
|---|---|
| Mérleg nincs bekapcsolva | Kapcsold be és várj 5 másodpercet |
| Bluetooth távolság nagy | Helyezd a mérleget közelebb a GaggiMate-hez |
| Más eszköz foglalja | Kapcsold ki a Bluetooth-t minden más eszközön |
| Firmware verzió nem megfelelő | Frissítsd a GaggiMate firmware-t |

### A Bluetooth kapcsolat megszakad shot közben

**Tünetek:** A safety timeout lép életbe; a shot nem a céltömegnél áll meg.

**Megoldások:**

1. Ellenőrizd a távolságot – max. 1-2 méter javasolt
2. Távolítsd el a közelben lévő elektromos interferenciát (mikrohullámú sütő, WiFi router)
3. Frissítsd a BOOKOO Themis Ultra firmware-t (BOOKOO app)
4. Ha folyamatosan megszakad: párosítsd újra a mérleget

### A mért hozam eltér a várttól

**Tünetek:** A mérleg 42.0 g-nál megáll, de a tényleges hozam más.

**Lehetséges okok:**

| Ok | Megoldás |
|---|---|
| Tare nem volt nullán | Mindig tare-zelj a csésze felhelyezése után |
| Csésze elmozdult | Rögzítsd a csészét |
| Mérleg nem vízszintes | Ellenőrizd és állítsd be a mérleg lábait |
| Csepegés a stop után | Normális; a GaggiMate záró nyomás csökkentése segíthet |

### A shot hamarabb áll meg a céltömegnél

**Okok:**

- A beverage weight trigger az extraction elején triggerel (ritka, ha korai csepegés van)
- Mérleg nullázás problémája

**Megoldás:** Ellenőrizd a tare értéket a shot előtt; ha szükséges, emeld a `stop_at_g` értéket 0.5-1.0 g-val.

### A safety timeout lép életbe (nem a beverage weight)

**Tünetek:** A shot a timeout másodpercnél áll meg, nem a céltömegnél.

**Okok és megoldások:**

| Ok | Megoldás |
|---|---|
| Bluetooth kapcsolat megszakadt | Ellenőrizd a párosítást és közelséget |
| Flow túl lassú (fojtott puck) | WDT, tamp, screen ellenőrzés; durvábbra az őrlésen |
| Safety timeout túl rövid | Növeld a `safety_timeout_s` értéket a JSON-ban |

---

## 5. Troubleshooting összefoglaló

| Tünet | Valószínű ok | Megoldás |
|---|---|---|
| Mérleg nem kapcsolódik | Firmware, távolság | Frissítés, közelebb |
| Disconnect shot közben | Interferencia, távolság | Közelebb, újrapárosítás |
| Hozam eltér | Tare hiba, mérleg dőlt | Tare ellenőrzés, vízszintes felület |
| Safety timeout lép be | BT megszakad / fojtott | Párosítás + puck prep |
| Shot túl rövid | Korai trigger | stop_at_g növelése 0.5 g-val |
| Shot túl hosszú | Timeout fut le | Bluetooth ellenőrzés, flow javítás |

---

## 6. Javasolt beállítások profilonként

| Profil | stop_at_g | safety_timeout_s |
|---|---:|---:|
| Kenya Wangera 94.5C | 42.0 g | 45 s |
| Kenya Wangera 94.0C | 42.0 g | 45 s |
| Burundi Mubuga | 42.5 g | 45 s |
| Colombia Manos Juntas | 43.0 g | 47 s |
| Kenya Kirinyaga PB | 43.0 g | 45 s |
| Twenty Eight Caturron | 42.0 g | 50 s |

A `stop_at_g` és `safety_timeout_s` értékeket a JSON profilban módosíthatod, ha a dial-in eltérő hozamot kíván.
