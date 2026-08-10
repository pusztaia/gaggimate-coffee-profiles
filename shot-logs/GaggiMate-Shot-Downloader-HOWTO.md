# GaggiMate shot logok letöltése és JSON konvertálása

Ez a HOWTO a `gaggimate_download_192_168_50_68.py` script használatát írja le.

A script alapértelmezett GaggiMate címe:

```text
192.168.50.68
```

A script a GaggiMate shot history bináris indexét és `.slog` fájljait HTTP-n keresztül olvassa le, majd minden shotból külön JSON fájlt készít.

## Mit csinál a script?

A folyamat:

```text
GaggiMate
  |
  +-- /api/history/index.bin
  |
  +-- /api/history/000135.slog
  +-- /api/history/000136.slog
  +-- ...
          |
          v
      dekódolás
          |
          v
gaggimate-shots/
  +-- index.json
  +-- shot-135.json
  +-- shot-136.json
  +-- ...
```

A GaggiMate aktuális forrásában a `/api/history/` URL a belső `/h/` history könyvtárra van kivezetve, az `index.bin` pedig külön HTTP végpontként is elérhető.

A jelenlegi shot log formátum v5, 512 bájtos fejléccel és 26 bájtos mintákkal.

## Követelmények

- Python 3
- A számítógép vagy Raspberry Pi ugyanazon a hálózaton legyen, mint a GaggiMate
- A GaggiMate címe elérhető legyen: `192.168.50.68`
- A script fájl:
  `gaggimate_download_192_168_50_68.py`

Külső Python csomag nem szükséges. A script csak a Python standard library moduljait használja.

## 1. Kapcsolat ellenőrzése

Először ellenőrizd, hogy a GaggiMate elérhető.

### Linux / Raspberry Pi / macOS

```bash
ping 192.168.50.68
```

### Windows

```powershell
ping 192.168.50.68
```

A GaggiMate webes felületét böngészőből is megnyithatod:

```text
http://192.168.50.68
```

Az index közvetlen címe:

```text
http://192.168.50.68/api/history/index.bin
```

Ez bináris fájl, ezért böngészőben nem olvasható szövegként.

## 2. Python ellenőrzése

### Linux / Raspberry Pi / macOS

```bash
python3 --version
```

### Windows

```powershell
py --version
```

Python 3 szükséges.

## 3. A script elhelyezése

Tedd a következő fájlt egy tetszőleges könyvtárba:

```text
gaggimate_download_192_168_50_68.py
```

Például Raspberry Pi-n:

```text
/home/pi/gaggimate/
```

Majd:

```bash
cd /home/pi/gaggimate
```

Windowson például:

```powershell
cd C:\gaggimate
```

## 4. Alap futtatás

A GaggiMate IP-címe már be van állítva a scriptben, ezért nem kell paraméterként megadni.

### Linux / Raspberry Pi / macOS

```bash
python3 gaggimate_download_192_168_50_68.py
```

### Windows

```powershell
py gaggimate_download_192_168_50_68.py
```

A script először letölti:

```text
http://192.168.50.68/api/history/index.bin
```

Ezután az indexben szereplő aktív shotokhoz lekéri a `.slog` fájlokat, például:

```text
/api/history/000135.slog
/api/history/000136.slog
```

majd JSON-ra konvertálja őket.

## 5. Eredmény

Alapértelmezés szerint létrejön:

```text
gaggimate-shots/
```

Például:

```text
gaggimate-shots/
├── index.json
├── shot-1.json
├── shot-2.json
├── ...
├── shot-135.json
├── shot-136.json
└── shot-137.json
```

Az `index.json` az összes indexbejegyzést tartalmazza.

Egy `shot-135.json` többek között a következő adatokat tartalmazhatja:

- shot ID
- dátum/idő
- profil neve és azonosítója
- teljes shot idő
- végső tömeg
- minták száma
- fázisváltások
- fázis kilépési ok
- brew delay
- target és mért hőmérséklet
- target és mért nyomás
- pump flow
- target flow
- puck flow
- mérleg flow
- mérleg tömeg
- becsült tömeg
- puck resistance
- Bluetooth mérleg státusz
- volumetric státusz
- opcionális shot notes

## 6. Már letöltött shotok

Normál futtatásnál a már létező

```text
shot-135.json
```

fájlokat a script nem írja felül.

Ezért ugyanazt a parancsot később újra lefuttathatod:

```bash
python3 gaggimate_download_192_168_50_68.py
```

és jellemzően csak az új shotok készülnek el.

## 7. Minden JSON újragenerálása

Ha a meglévő JSON fájlokat is felül akarod írni:

```bash
python3 gaggimate_download_192_168_50_68.py --force
```

Windows:

```powershell
py gaggimate_download_192_168_50_68.py --force
```

## 8. Az eredeti `.slog` fájlok megtartása

Ha a JSON mellett az eredeti GaggiMate bináris logokat is szeretnéd eltárolni:

```bash
python3 gaggimate_download_192_168_50_68.py --keep-slog
```

Ekkor létrejön például:

```text
gaggimate-shots/
├── index.json
├── shot-135.json
└── raw/
    ├── 000135.slog
    ├── 000136.slog
    └── ...
```

## 9. Az eredeti `index.bin` megtartása

```bash
python3 gaggimate_download_192_168_50_68.py --keep-index-bin
```

Eredmény:

```text
gaggimate-shots/raw/index.bin
```

A két opció együtt:

```bash
python3 gaggimate_download_192_168_50_68.py --keep-slog --keep-index-bin
```

Backup készítéshez ez az ajánlott mód.

## 10. Notes fájlok

A script alapból megpróbálja letölteni az egyes shotok opcionális notes JSON fájlját is.

Például:

```text
/api/history/000135.json
```

Ha ezt nem szeretnéd:

```bash
python3 gaggimate_download_192_168_50_68.py --no-notes
```

## 11. Csak bizonyos shot ID-k letöltése

Csak a 135-ös shottól:

```bash
python3 gaggimate_download_192_168_50_68.py --start-id 135
```

Csak 135 és 150 között:

```bash
python3 gaggimate_download_192_168_50_68.py --start-id 135 --end-id 150
```

Csak 150-ig:

```bash
python3 gaggimate_download_192_168_50_68.py --end-id 150
```

## 12. Másik célkönyvtár

Például:

```bash
python3 gaggimate_download_192_168_50_68.py -o ~/gaggimate-backup
```

Windows:

```powershell
py gaggimate_download_192_168_50_68.py -o C:\gaggimate-backup
```

## 13. Haladó hálózati beállítások

Alapértelmezett HTTP timeout:

```text
15 másodperc
```

Növelés:

```bash
python3 gaggimate_download_192_168_50_68.py --timeout 30
```

Alapértelmezett próbálkozások száma:

```text
3
```

Például 5 próbálkozás:

```bash
python3 gaggimate_download_192_168_50_68.py --retries 5
```

A shotok között alapból 0,05 másodperc szünet van.

Például 0,2 másodperc:

```bash
python3 gaggimate_download_192_168_50_68.py --delay 0.2
```

## 14. Minden opció megjelenítése

Linux / Raspberry Pi / macOS:

```bash
python3 gaggimate_download_192_168_50_68.py --help
```

Windows:

```powershell
py gaggimate_download_192_168_50_68.py --help
```

A jelenlegi opciók:

```text
-o, --output
--force
--keep-slog
--keep-index-bin
--no-notes
--start-id
--end-id
--timeout
--retries
--delay
--indent
```

## 15. Ajánlott parancs

Ha teljes backupot szeretnél JSON + eredeti bináris fájlokkal:

```bash
python3 gaggimate_download_192_168_50_68.py --keep-slog --keep-index-bin
```

A következő futtatáskor a meglévő JSON fájlokat kihagyja, és az új shotokat tölti le.

## 16. Hibakeresés

### `Connection refused`

Példa:

```text
Connection refused
```

Ellenőrizd:

```bash
ping 192.168.50.68
```

és böngészőből:

```text
http://192.168.50.68
```

### Timeout

Ha a hálózat lassú:

```bash
python3 gaggimate_download_192_168_50_68.py --timeout 30 --retries 5
```

### `index.bin` 404

Ha:

```text
/api/history/index.bin
```

404-et ad, ellenőrizd a GaggiMate firmware verzióját és azt, hogy a Shot History funkció elérhető-e az adott buildben.

### Unsupported `.slog` version

A script jelenleg a GaggiMate v5 shot-log formátumát dekódolja.

Ha más verziójú `.slog` fájlt talál, azt nem próbálja hibás struktúrával JSON-ra konvertálni. Az ismeretlen bináris fájlt a `raw/` könyvtárban megőrzi későbbi feldolgozásra.

## 17. A GaggiMate forrásban hol található ez?

A shot-history HTTP publikálása:

```text
src/display/plugins/WebUIPlugin.cpp
```

Aktuális GitHub forrás:

https://github.com/jniebuhr/gaggimate/blob/master/src/display/plugins/WebUIPlugin.cpp

A forrásban a history könyvtár:

```cpp
server.serveStatic("/api/history/", *fs, "/h/")
```

és az index:

```text
/api/history/index.bin
```

A bináris shot formátum definíciója:

```text
src/display/models/shot_log_format.h
```

https://github.com/jniebuhr/gaggimate/blob/master/src/display/models/shot_log_format.h

A jelenlegi forrás szerint:

```text
SHOT_LOG_VERSION = 5
SHOT_LOG_HEADER_SIZE = 512
SHOT_LOG_SAMPLE_INTERVAL_MS = 250
SHOT_LOG_SAMPLE_SIZE = 26
```

A shot-history tárolási logika:

```text
src/display/plugins/ShotHistoryPlugin.cpp
```

https://github.com/jniebuhr/gaggimate/blob/master/src/display/plugins/ShotHistoryPlugin.cpp

A GaggiMate a shot fájlokat a belső `/h/` könyvtárban `.slog` kiterjesztéssel hozza létre.

## 18. Rövid összefoglaló

Normál használat:

```bash
python3 gaggimate_download_192_168_50_68.py
```

Teljes backup:

```bash
python3 gaggimate_download_192_168_50_68.py --keep-slog --keep-index-bin
```

Mindent újragenerál:

```bash
python3 gaggimate_download_192_168_50_68.py --force --keep-slog --keep-index-bin
```

Csak a 135-ös shottól:

```bash
python3 gaggimate_download_192_168_50_68.py --start-id 135
```

Kimenet:

```text
gaggimate-shots/
```

A JSON fájlok:

```text
shot-<ID>.json
```

például:

```text
shot-135.json
```
