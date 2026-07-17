# GaggiMate profilok: milyen kávéhoz és pörköléshez illenek?

Ez az összefoglaló a három feltöltött profil alapján készült:

- `profile-lever.json` – **Cremina lever machine**
- `profile-9bar.json` – **9 Bar Espresso**
- `profile-lmleva.json` – **Damian's LM Leva**

A cél: gyorsan eldönteni, melyik profilt milyen kávéhoz, pörköléshez és ízirányhoz érdemes használni.

---

## Rövid döntési táblázat

| Profil | Legjobb kávé | Ajánlott pörkölés | Várható karakter |
|---|---|---|---|
| **Cremina lever machine** | klasszikus, testes espresso | **közepes-sötét / sötét** | édes, kerek, alacsony sav, csokis-diós |
| **9 Bar Espresso** | klasszikus espresso baseline | **közepes / közepes-sötét** | direkt, egyszerű, klasszikus 9 bar |
| **Damian's LM Leva** | modern specialty espresso | **világos-közepes / közepes** | tiszta, gyümölcsösebb, hosszabb lefolyás |

---

## 1. Cremina lever machine

**Profil jellege:** lever gép karaktert utánzó profil.

A profil leírása szerint: **„Darker Roasts – Very Fine – 40–60s – 1:1.5–2.2”**.

### Fő profilkarakter

- alacsony nyomású előáztatás,
- hosszabb soak,
- fokozatos felmenetel 9 bar köré,
- hosszú nyomáscsökkenés 3 bar felé,
- alacsonyabb hőmérséklet-tartomány.

### Legjobban ehhez illik

- közepes-sötét vagy sötét espresso roast,
- brazil, blend, csokis-diós kávék,
- klasszikus olaszosabb espresso,
- alacsonyabb savú, testes kávék,
- rövidebb, testesebb arányok: kb. **1:1.5–1:2.2**.

### Ízben várható

- több test,
- alacsonyabb savérzet,
- csokisabb / diósabb / karamellesebb karakter,
- kerekebb, kevésbé gyümölcsös csésze.

### Mikor nem ezt választanám?

Nem ezt használnám elsőnek olyan világosabb, gyümölcsös specialty kávékhoz, mint például:

- Kenya Wangera,
- Kirinyaga PB,
- Burundi Mubuga,
- Colombia Manos Juntas.

Ezeknél könnyen túl tompa, túl nehéz vagy kevésbé tiszta lehet a végeredmény.

---

## 2. 9 Bar Espresso

**Profil jellege:** klasszikus, egyszerű 9 baros espresso baseline.

A feltöltött JSON alapján ez egyetlen főzési fázis:

- **28 s** maximum,
- **9 bar** nyomás,
- nincs külön preinfusion,
- nincs bloom,
- nincs declining finish,
- `volumetric >= 40` target.

### Legjobban ehhez illik

- közepes vagy közepes-sötét pörkölés,
- klasszikus espresso blend,
- csokis, mogyorós, karamelles kávék,
- összehasonlító tesztprofilként bármelyik kávéhoz.

### Ízben várható

- direkt, klasszikus espresso karakter,
- erősebb, koncentráltabb benyomás,
- kevesebb profilozott édesség,
- világos specialtynél nagyobb channeling-kockázat,
- naked portafilteren több spriccelés lehet.

### Mire jó különösen?

Ez jó **kontrollprofilnak**. Ha tudni akarod, hogy egy kávé mit csinál sima 9 baron, akkor ezt érdemes lefuttatni.

De nem ez lenne az első választás a modern, gyümölcsös specialty kávéidhoz.

---

## 3. Damian's LM Leva

**Profil jellege:** La Marzocco Leva jellegű, modern lever / pressure profiling irány.

A profil leírása szerint: **„Light to Medium Roasts – Very Fine – 20–45 – 1:2.0–2.5”**.

### Fő profilkarakter

- hosszabb fill / preinfusion,
- fokozatos nyomásfelépítés,
- rövid magasabb nyomású szakasz,
- hosszú declining pressure szakasz,
- világosabb és közepes pörkölésekhez optimalizált irány.

### Legjobban ehhez illik

- világos-közepes specialty,
- közepes specialty,
- mosott afrikai kávék,
- gyümölcsös latin-amerikai kávék,
- teás, virágos, savasabb kávék,
- hosszabb arányok: kb. **1:2.0–1:2.5**.

### Ízben várható

- tisztább gyümölcsösség,
- kevésbé agresszív sav,
- jobb édesség,
- kevesebb száraz vég,
- modernebb specialty espresso karakter.

### A te kávéidhoz

Ez áll legközelebb a mostani gyümölcsös profiljaidhoz, például:

- Kenya Wangera,
- Kirinyaga PB Tea Rose,
- Burundi Mubuga,
- Colombia Manos Juntas,
- Twenty Eight Finca el Recreo Caturron.

A saját **Wangera Stable Start 38s 94.5C** profilod még célzottabb, mert már a te gépedhez, darálódhoz és kosaradhoz lett hangolva, de általános irányként az LM Leva profil passzol legjobban a specialty kávéidhoz.

---

## Ajánlás a jelenlegi setupodra

Setup:

- **Gaggia Classic Pro 2025 + GaggiMate Pro**
- **DF64V Gen 2**
- **SSP Sweet Lab Espresso V3**
- **IMS B682TH24.5M**
- **IMS E&B Lab puck diffuser screen (Ø 2.4 mm, 253 lyuk, DS58.5)**
- **1200 RPM baseline**

### Profilválasztás kávétípus szerint

| Kávé típusa | Ajánlott profil |
|---|---|
| Világos, virágos, teás Kenya | **LM Leva jelleg / saját specialty profil** |
| Gyümölcsös natural / anaerob specialty | **LM Leva jelleg / Stable Start jelleg** |
| Közepes specialty, karamell + gyümölcs | **LM Leva vagy 9 Bar tesztként** |
| Klasszikus blend, csoki, mogyoró | **9 Bar Espresso** |
| Sötétebb, testes, alacsony savú kávé | **Cremina lever machine** |
| Olaszosabb espresso | **Cremina vagy 9 Bar** |

---

## Konkrét döntési szabály

### Ha gyümölcsös, tiszta, specialty shotot akarsz

Használd:

**Damian's LM Leva** vagy saját, kávéra hangolt profil.

Pörkölés:

**világos-közepes / közepes**

### Ha klasszikus, direkt espressót akarsz

Használd:

**9 Bar Espresso**

Pörkölés:

**közepes / közepes-sötét**

### Ha testes, édes, leveres, alacsony savú shotot akarsz

Használd:

**Cremina lever machine**

Pörkölés:

**közepes-sötét / sötét**

---

## Rövid összefoglaló

A három profil közül:

- **Cremina lever machine**: sötétebb, testes, klasszikus leveres espresso.
- **9 Bar Espresso**: egyszerű, klasszikus baseline, főleg közepes és közepes-sötét pörköléshez.
- **Damian's LM Leva**: legjobb modern specialty irány, főleg világos-közepes és közepes pörköléshez.

A te eddigi gyümölcsös Impresso / Twenty Eight kávéidhoz a **Damian's LM Leva irány** vagy a saját, kávéra optimalizált **Stable Start** profilok illenek legjobban.

---

## Források

- GaggiMate Profiles dokumentáció: https://docs.gaggimate.eu/docs/profiles/
- La Marzocco – Pre-Brew, Pre-Infusion, Pressure Manipulation: https://home.lamarzoccousa.com/pre-brew-pre-infusion-and-pressure-manipulation-explained/
- La Marzocco Leva X: https://lamarzocco.com/mktcenter/machine/leva-x/
- Complete Home Barista – Pressure Profiling Espresso: https://completehomebarista.com/guides/pressure-profiling/
