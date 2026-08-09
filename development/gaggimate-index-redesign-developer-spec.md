# GaggiMate Coffee Profiles — UX/UI és frontend újratervezési specifikáció

**Dokumentum célja:** részletes megvalósítási brief senior / profi webfejlesztő számára  
**Kiindulási oldal:** `index.html`  
**Dátum:** 2026-08-09  
**Fő cél:** a legfontosabb felhasználói feladat — **kávéprofil gyors megtalálása, kiválasztása és megnyitása/letöltése** — kerüljön az oldal elejére.

---

## 1. Vezetői összefoglaló

A jelenlegi oldal vizuálisan igényes és technikailag sok hasznos funkciót tartalmaz, de az információs hierarchia fordított a valós felhasználói feladathoz képest.

A jelenlegi sorrend nagyjából:

1. sticky fejléc;
2. nagy hero;
3. nagyméretű dekoratív „V2 Bluetooth Scale” kártya;
4. 6 statisztikai metrika;
5. profilkatalógus;
6. setup referencia;
7. dokumentáció;
8. új profil hozzáadásának fejlesztői leírása.

A redesign során a sorrendet **feladatalapúvá** kell tenni:

1. fejléc és kompakt oldalazonosítás;
2. **profilkereső és legfontosabb szűrők**;
3. **profilkatalógus / ajánlott profilok**;
4. kompakt rendszerállapot és baseline;
5. setup referencia;
6. dokumentáció;
7. fejlesztői / karbantartási információk.

### Legfontosabb változtatás

A profilkatalógusnak az első viewportban vagy közvetlenül annak alján el kell kezdődnie.

A jelenlegi hero nem lehet magasabb annál, mint amennyi ahhoz szükséges, hogy a felhasználó megértse:

- hol van;
- mit tud itt csinálni;
- hogyan találja meg a megfelelő kávét/profilt.

**A dekoráció nem előzheti meg a feladatot.**

---

# 2. Az oldal elsődleges felhasználói feladatai

A fejlesztő minden komponensről tegye fel a kérdést:

> Segíti ez a felhasználót abban, hogy gyorsabban megtalálja és használja a megfelelő GaggiMate profilt?

A prioritás:

## P1 — Profil megtalálása

A felhasználó tudjon keresni:

- kávé neve;
- pörkölő;
- ország / eredet;
- feldolgozás;
- ízjegy;
- profil típusa;
- Scale / Manual variáns alapján.

## P1 — Profil használata

Egy kártyáról egyértelműen elérhető legyen:

- profil részletes oldala;
- ajánlott recept;
- megfelelő JSON;
- Scale / Manual választás.

## P2 — Gyors döntés

A kártya első pillantásra válaszolja meg:

- melyik kávé;
- milyen feldolgozás;
- mi az ajánlott dózis;
- mennyi a hozam;
- milyen hőmérséklet;
- Scale vagy Manual;
- melyik az ajánlott/default variáns.

## P2 — Dial-in támogatás

Másodlagos információként jelenhet meg:

- őrlési tartomány;
- várható idő;
- profilfázisok;
- grafikon;
- ízjegyek;
- recept;
- changelog.

## P3 — Rendszerinformáció

A felhasználó szükség esetén érje el:

- gép;
- daráló;
- kosár;
- mérleg;
- baseline dózis;
- RPM.

## P4 — Fejlesztői dokumentáció

A repository karbantartásához szükséges információk:

- új profil hozzáadása;
- JSON séma;
- fájlelnevezés;
- projekt changelog;
- lokális HTTP szerver használata.

Ezek **nem kerülhetnek a fogyasztói főfolyamat elé**.

---

# 3. Mi a probléma a jelenlegi információs hierarchiával?

## 3.1 Túl nagy a hero

A jelenlegi hero:

- nagy `h1`;
- kétoszlopos layout;
- külön, minimum 400 px magas vizuális kártya;
- dekoratív kávéscsésze;
- több chip;
- utána még 6 metrika.

Ez desktopon látványos, de eltolja lefelé a valódi alkalmazásfunkciót.

Mobilon még kritikusabb, mert a felhasználónak több képernyőnyit kell görgetnie, mire a profilokhoz jut.

### Teendő

A hero legyen **kompakt utility hero**.

Javasolt magasság desktopon:

- körülbelül 220–300 px tartalomtól függően.

Mobilon:

- lehetőleg 180–240 px.

A hero tartalma:

- `H1`: **GaggiMate kávéprofilok**
- egy mondatos leírás;
- opcionálisan 2–3 rendszer badge;
- **keresőmező**;
- gyors szűrők.

A nagy dekoratív kávéscsésze grafika megszüntethető, vagy csak desktop háttérelemként maradhat.

---

# 4. Javasolt új oldalstruktúra

```text
┌─────────────────────────────────────────────────────────────┐
│ Sticky header                                               │
│ GaggiMate Coffee Profiles    Profilok  Setup  Dokumentáció │
│                                        ☀/☾                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ GaggiMate kávéprofilok                                      │
│ Keresd meg a kávét, válassz Scale vagy Manual profilt.      │
│                                                             │
│ [ 🔎 Keresés kávé, ország, ízjegy alapján...             ] │
│ [Összes] [Scale] [Manual] [Washed] [Natural]   [Rendezés] │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Profilok                                      12 találat    │
│                                                             │
│ [kártya]                               [kártya]             │
│ [kártya]                               [kártya]             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Aktuális setup / baseline                                   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Dokumentáció                                                │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Fejlesztői információk                                      │
└─────────────────────────────────────────────────────────────┘
```

---

# 5. Above-the-fold specifikáció

Az első képernyő a legfontosabb terület.

## Kötelezően látható legyen

Desktopon 1366×768 környékén:

1. fejléc;
2. oldal címe;
3. rövid magyarázat;
4. kereső;
5. gyors szűrők;
6. legalább az első profilsor felső része.

Mobilon 390×844 környékén:

1. kompakt fejléc;
2. H1;
3. kereső;
4. 3 legfontosabb filter;
5. az első profilkártya címe és alapadatai.

## Ne legyen az első viewportban

- setup részletes lista;
- repository-metrikák;
- fejlesztői dokumentáció;
- „Új profil hozzáadása” folyamat;
- nagy dekoratív SVG;
- több sor technikai marketing szöveg.

---

# 6. Hero redesign

## Jelenlegi problémák

A jelenlegi H1:

> „Kávéprofilok egy helyen”

érthető, de a hero túl sok helyet kap.

A hosszú magyarázat arról, hogy a kártyák `catalog.json` és JSON fájlok alapján épülnek fel, **fejlesztői információ**, nem elsődleges felhasználói információ.

## Új javasolt hero copy

### H1

**GaggiMate kávéprofilok**

### Lead

**Találd meg a kávédhoz tartozó profilt, válassz Scale vagy Manual verziót, majd nyisd meg vagy töltsd le a JSON-t.**

### Technikai státusz

Kisebb badge-ekben:

- `Gaggia Classic Pro`
- `GaggiMate Pro`
- `BOOKOO Scale`

A „JSON-alapú”, „GitHub Pages kompatibilis” stb. kerüljön a fejlesztői részbe.

---

# 7. A keresés legyen a fő CTA

A kereső jelenleg jó funkció, de túl későn jelenik meg.

## Teendő

A keresőt mozgasd közvetlenül a hero szöveg alá.

Javasolt placeholder:

> `Keresés kávé, pörkölő, ország, feldolgozás vagy ízjegy alapján…`

## Funkció

Keresés maradjon kliensoldali és azonnali.

A keresés vegye figyelembe:

- `title`;
- `subtitle`;
- `origin`;
- `process`;
- `grind`;
- `notes`;
- opcionálisan később a `roaster`, `country`, `variety` külön mezőket.

## Találatszám

A katalógus fejlécében jelenjen meg:

> `8 profil`

vagy aktív kereséskor:

> `3 találat`

Ez fontosabb információ, mint a teljes repository globális profil- és variánsszáma.

---

# 8. Szűrők új hierarchiája

A jelenlegi külön filter sor és két select funkcionális, de egységesebb control bar szükséges.

## Elsődleges gyorsfilterek

Mindig látható:

- Összes
- Scale
- Manual
- Kávéspecifikus

## Másodlagos filter

Dropdown / filter button:

- Feldolgozás
  - Washed
  - Natural
  - Honey
  - Anaerobic
  - Carbonic
  - stb.

## Rendezés

Dropdown:

- Ajánlott
- Név
- Hőmérséklet
- később: legutóbb frissített

## Mobil

Mobilon ne legyen három egymás alatti teljes szélességű select.

Javasolt:

```text
[ Összes ] [ Scale ] [ Manual ] [ Szűrők ⚙ ]
```

A „Szűrők” gomb nyisson bottom sheetet vagy egyszerű `dialog`-ot.

---

# 9. Profilkártyák újratervezése

A jelenlegi kártyák információban túl sűrűek.

Egy kártyán egyszerre van:

- process;
- profil típus;
- title;
- subtitle;
- origin;
- több ízjegy-pill;
- variant select;
- 4 stat;
- grafikon;
- legend;
- akár 7 profilfázis;
- 5 action.

Ez egy részletes adatlapnak megfelelő információmennyiség.

## 9.1 Kártya első szintje — mindig látható

```text
BURUNDI · WASHED                         SCALE

Burundi Mubuga
Coffea Circulor · Burundi

barack · citrus · tea

18.5 g  →  42 g     93.5 °C     38 s

[ Profil megnyitása ]     [ ⋯ ]
```

### Mindig látható

- ország / process;
- név;
- pörkölő / eredet;
- max. 3 ízjegy;
- default variáns;
- dózis;
- target yield;
- hőmérséklet;
- idő;
- elsődleges CTA.

## 9.2 Második szint — kibontva

A részletek alatt:

- Scale / Manual variánsváltó;
- grafikon;
- profilfázisok;
- őrlés;
- JSON;
- PNG;
- recept;
- changelog.

### Javasolt megoldás

Használj natív:

```html
<details>
  <summary>Profil részletei</summary>
  ...
</details>
```

vagy egy jól implementált „Részletek” controlt.

A fontos információt **nem szabad elrejteni**; csak a haladó, ritkábban szükséges adatokat.

---

# 10. CTA hierarchia

A jelenlegi kártyán minden action majdnem azonos vizuális súlyú:

- Profil megnyitása
- JSON
- PNG
- Recept
- Changelog

Ez döntési zajt okoz.

## Új hierarchia

### Primary

**Profil megnyitása**

### Secondary

**JSON letöltése**

### Tertiary / overflow

`⋯`

Alatta:

- Recept
- Profilgrafikon / PNG
- Changelog

Ha a fő felhasználói workflow valójában a JSON letöltés, akkor a két CTA felcserélhető:

1. `JSON letöltése`
2. `Profil megnyitása`

Ezt valós használat alapján kell eldönteni.

---

# 11. Scale / Manual variáns kezelése

A variáns egy kulcsfontosságú tulajdonság, ezért vizuálisan egyértelműbbnek kell lennie.

## Javaslat

A select helyett desktopon segmented control:

```text
[ Scale V2 ] [ Manual ]
```

Mobilon ugyanez két gombbal.

### Elvárás

Variánsváltáskor frissüljön:

- yield / stop;
- hőmérséklet;
- max idő;
- grafikon;
- fázisok;
- JSON URL;
- PNG URL;
- profil típus badge.

A váltás alatt ne essen össze a kártya.

Használj fix vagy minimum magasságot az adatblokknak, hogy csökkenjen a layout shift.

---

# 12. Grafikon kezelése

A grafikon hasznos, de nem minden felhasználó számára elsődleges.

## Új szabály

A fő katalógusban:

- desktopon opcionálisan kis sparkline / mini chart;
- mobilon alapból ne jelenjen meg nagy, 230 px magas chart.

A teljes chart jelenjen meg:

- kártya kibontásakor;
- vagy a profil részletes oldalán.

## Miért?

Egy 230 px magas chart minden kártyában jelentősen növeli:

- a vertikális oldalméretet;
- a renderelési munkát;
- a vizuális zajt.

---

# 13. Profilfázisok

A jelenlegi kártya legfeljebb 7 fázist közvetlenül listáz.

Ez túl részletes katalógusnézetben.

## Új elv

Katalógusban:

> `7 fázis · max 38 s · 6.0 bar peak`

Kibontva:

```text
1. Preinfusion
2. Bloom
3. Ramp
4. Extraction
...
```

A teljes technikai target lista csak a részletes nézetben legyen.

---

# 14. A 6 felső metrika sorsa

Jelenleg:

- Profilcsalád
- JSON variáns
- Scale profil
- Manual profil
- Dózis
- RPM

## Probléma

Ezek közül a legtöbb nem segít a profil kiválasztásában.

## Javaslat

A hero alatti 6 kártyás metrics blokk megszüntetendő.

Helyette opcionális egyetlen kompakt sor:

```text
12 profil · 22 variáns · 18.5 g baseline · DF64V 1200 RPM
```

Ez kerüljön:

- a profilkatalógus fejlécébe;
- vagy a Setup blokk elejére.

A „Scale profil / Manual profil darabszám” dashboard-jellegű információ, nem főoldali prioritás.

---

# 15. Setup referencia

A setup fontos kontextus, de nem kell a profilok elé.

## Új megjelenés

Egy kompakt blokk:

```text
Setup baseline

Gaggia Classic Pro + GaggiMate Pro
DF64V Gen 2 · SSP Sweet Lab Espresso V3
IMS B682TH24.5M · BOOKOO Themis Ultra
18.5 g · 1200 RPM

[ Részletes setup ]
```

A teljes 8 kártyás grid helyett elég egy rendezett leíró blokk.

Ha szükséges, `<details>` alatt jelenjen meg minden technikai mező.

---

# 16. Dokumentáció újratervezése

A jelenlegi dokumentáció 11 külön kártyából áll.

Ez túl nagy vizuális súlyt kap egy profil-katalógus főoldalán.

## Új csoportosítás

### Kávékészítés

- Brew Guidelines
- Darálási útmutató
- Kávévíz recept
- Feldolgozások

### GaggiMate

- Bluetooth Scale Workflow
- Profilkészítési útmutató
- Profile Gallery

### Projekt

- README
- Summary
- Fájlelnevezés
- Changelog

## Megjelenés

Ne 11 nagy kártya legyen.

Javasolt kompakt lista:

```text
Kávékészítés
  Brew Guidelines                 →
  Darálási útmutató               →
  Kávévíz — Epsom + bikarbonát    →
  Kávéfeldolgozások               →
```

---

# 17. „Új profil hozzáadása” áthelyezése

Ez fejlesztői workflow.

## Teendő

A teljes „Új profil hozzáadása” blokk kerüljön:

- a Dokumentáció / Fejlesztők részbe;
- vagy külön `CONTRIBUTING.md` / `PROFILE_CREATION_GUIDE.md` dokumentumba.

A főoldalon csak egy rövid link szükséges:

> **Új profil hozzáadása → Fejlesztői útmutató**

A JSON példa nem szükséges teljes terjedelemben a főoldalon.

---

# 18. Navigáció

A jelenlegi desktop nav:

- Profilok
- Setup
- Dokumentáció
- Új profil
- téma

Ez alapvetően jó.

## Kritikus mobilprobléma

A jelenlegi CSS 980 px alatt elrejti a `.nav a` elemeket.

Így mobilon a navigációs linkek eltűnnek, miközben nincs helyettük menügomb.

## Kötelező javítás

980 px alatt jelenjen meg:

```text
[GaggiMate]                    [☰] [◐]
```

A hamburger nyisson:

- Profilok
- Setup
- Dokumentáció
- Fejlesztők

### Minimum követelmény

A menü:

- billentyűzettel használható;
- Escape-pel bezárható;
- fókuszt kezel;
- rendelkezik egyértelmű accessible name-mel;
- legalább 44×44 px ajánlott tappolható területtel.

---

# 19. Mobil-first viselkedés

A mobilverzió ne csak a desktop layout összetört változata legyen.

## 390 px körül

### Header

- brand rövidített változat;
- menü;
- téma.

### Hero

- 32–40 px körüli H1;
- 1 rövid mondat;
- kereső.

### Filterek

Horizontálisan görgethető chip sor vagy „Szűrők” panel.

### Profilkártya

Egy oszlop.

Stat blokk:

```text
18.5 g → 42 g
93.5 °C · 38 s
```

Nem szükséges 2×2 mini-dashboard.

### Action

Primary button teljes szélességben.

Secondary:

- JSON
- részletek

### Chart

Alapból zárt.

---

# 20. Desktop layout

## Max szélesség

A jelenlegi ~1180 px megfelelő.

Javasolt:

```css
--content-max: 1200px;
```

## Profilgrid

- 1200 px: 2 oszlop;
- 1600+ px esetén opcionálisan 3 oszlop csak akkor, ha a kártyák tovább egyszerűsödnek;
- 900–1100 px: 2 oszlop;
- 900 alatt: 1 oszlop.

A kártyák ne legyenek túl keskenyek a technikai adatok miatt.

---

# 21. Tipográfia

A jelenlegi design karakteres, de az extrém nagy H1 túlzottan domináns.

## Ajánlott skála

```css
--font-xs:   0.75rem;
--font-sm:   0.875rem;
--font-base: 1rem;
--font-lg:   1.125rem;
--font-xl:   1.375rem;
--font-2xl:  1.75rem;
--font-3xl:  clamp(2.1rem, 5vw, 3.5rem);
```

A főoldali H1-hez nincs szükség 6.4 rem körüli maximumra.

## Címsorhierarchia

- egy `h1`;
- fő oldalblokkok: `h2`;
- kártyacímek: `h3`;
- részletek: `h4`.

A vizuális méretet CSS-sel kell megoldani, nem heading level átugrásával.

---

# 22. Térközök

A jelenlegi oldal sok nagy vertikális paddinget használ.

## Standard spacing rendszer

```css
--space-1: 0.25rem;
--space-2: 0.5rem;
--space-3: 0.75rem;
--space-4: 1rem;
--space-5: 1.5rem;
--space-6: 2rem;
--space-7: 3rem;
--space-8: 4rem;
```

### Javaslat

Fő section:

- desktop: 48–64 px;
- mobil: 32–48 px.

Hero:

- ne használjon 5.5 rem felső paddinget a tartalom kezdetén.

---

# 23. Szín és vizuális hierarchia

A bordó / krém identitás megtartható.

## Javítandó

Kevesebb:

- shadow;
- gradient;
- eltérő card-background;
- pill;
- dekoratív szín.

A főoldalon egyszerre túl sok elem kap kártyaszerű vizuális kezelést.

## Új elv

**Nem minden információ kártya.**

Kártyát csak arra használj, ami ténylegesen önálló objektum:

- profil;
- esetleg setup summary.

A dokumentumlista és statisztikák lehetnek egyszerű sorok.

---

# 24. Accessibility — WCAG 2.2 cél

Cél: legalább **WCAG 2.2 AA**.

## 24.1 Szemantika

Maradjon / legyen:

- `<header>`;
- `<nav>`;
- `<main>`;
- `<section>`;
- `<article>`;
- `<footer>`;
- helyes címsorhierarchia.

A jelenlegi skip link jó irány, meg kell tartani.

## 24.2 Target size

WCAG 2.2 AA minimum:

- legalább 24×24 CSS px target vagy megfelelő spacing.

Praktikus mobilcél:

- fontos gomboknál 44×44 px körüli aktív terület.

Különösen:

- téma gomb;
- hamburger;
- modal close;
- filter chipek;
- overflow menu;
- Scale/Manual toggle.

## 24.3 Focus

Minden interaktív elem:

- kapjon jól látható `:focus-visible` állapotot;
- sticky header vagy modal ne takarja el a fókuszált elemet.

## 24.4 Billentyűzet

Tesztelendő:

- Tab;
- Shift+Tab;
- Enter;
- Space;
- Escape.

## 24.5 Modal

A jelenlegi Markdown modal továbbfejlesztendő.

Kötelező:

- fókusz a modalba kerüljön nyitáskor;
- fókuszcsapda;
- bezáráskor fókusz térjen vissza a nyitó elemre;
- háttér ne legyen tabolható;
- Escape bezárás;
- `aria-labelledby`;
- szükség esetén `aria-describedby`.

Natív `<dialog>` használata megfontolandó.

---

# 25. Performance

A profilkatalógus több JSON-t tölt be, majd minden kártyához SVG grafikont generál.

Ez kis katalógusnál megfelelő lehet, de skálázáskor felesleges munka.

## 25.1 Első render

Első renderkor:

1. `catalog.json`;
2. kártyák alapmetaadatai;
3. látható kártyák default JSON-jai.

Ne feltétlenül töltsd be egyszerre az összes profil JSON-t.

## 25.2 Lazy loading

`IntersectionObserver` segítségével:

- csak viewport közelében töltsd be a részletes JSON-t;
- chart csak akkor generálódjon, amikor szükséges.

## 25.3 Layout stability

Minden async blokknak legyen fenntartott helye.

Kerülendő:

- JSON betöltés után nagy magasságugrás;
- chart betöltés utáni kártyaugrás;
- eltérő magasságú loading / loaded állapot.

## 25.4 Core Web Vitals cél

Javasolt célérték:

- LCP ≤ 2.5 s;
- INP ≤ 200 ms;
- CLS ≤ 0.1;

a page view-k 75. percentilisén.

---

# 26. JavaScript architektúra

A jelenlegi single-file HTML egyszerű deploy szempontból kényelmes, de a CSS és JS mérete miatt karbantartási határhoz közeledik.

## Javasolt struktúra

```text
/
├── index.html
├── assets/
│   ├── css/
│   │   ├── tokens.css
│   │   ├── base.css
│   │   ├── layout.css
│   │   └── components.css
│   └── js/
│       ├── app.js
│       ├── catalog.js
│       ├── filters.js
│       ├── profile-card.js
│       ├── chart.js
│       ├── markdown.js
│       └── modal.js
└── profiles/
    └── catalog.json
```

Ha továbbra is egyetlen HTML fájl a cél, legalább belső moduláris logikai szekciók legyenek jól dokumentálva.

---

# 27. Adatmodell javasolt bővítése

A `catalog.json` legyen a kártya első renderjének teljes adatforrása.

Ne kelljen minden JSON-t letölteni csak ahhoz, hogy a katalógus megjelenjen.

## Példa

```json
{
  "id": "burundi-mubuga",
  "title": "Burundi Mubuga",
  "roaster": "…",
  "country": "Burundi",
  "process": "washed",
  "notes": ["barack", "citrus", "tea"],
  "recommendedVariant": "scale",
  "summary": {
    "dose": 18.5,
    "yield": 42,
    "temperature": 93.5,
    "expectedTime": 38,
    "grind": "9–10"
  }
}
```

Így a kártya azonnal renderelhető.

A részletes profil JSON csak akkor kell, ha:

- grafikon kell;
- fázislista kell;
- variánst vált a felhasználó;
- JSON-t akar letölteni.

---

# 28. Állapotok

A fejlesztő explicit kezelje:

## Loading

Ne egy általános:

> „A profilkatalógus betöltése folyamatban…”

szöveg legyen csak.

Használható skeleton, de ne animáld túl.

## Empty

Példa:

> **Nincs találat.**  
> Próbáld meg törölni a feldolgozás szűrőt vagy használj másik keresőkifejezést.

CTA:

`Szűrők törlése`

## Error

A normál felhasználó számára:

> **A profilok most nem tölthetők be.**

Másodlagosan:

`Újrapróbálás`

Fejlesztői technikai részlet opcionálisan `<details>` alatt.

---

# 29. URL state

A keresés és a filterek lehetőleg kerüljenek URL query paraméterbe.

Példa:

```text
?search=burundi&type=scale&process=washed
```

Előny:

- linkelhető állapot;
- browser Back működik;
- bookmarkolható;
- hibakeresés egyszerűbb.

---

# 30. Profil linkelhetőség

Minden profil kapjon stabil URL-t.

Például:

```text
/profiles/burundi-mubuga/
```

vagy főoldali anchor:

```text
/#burundi-mubuga
```

A részletes profiloldal előnyösebb, ha hosszú tartalom van.

---

# 31. Dokumentum-megjelenítő

A Markdown modal jó funkció, de ne legyen a fő navigation modell helyettesítője.

## Javaslat

Két lehetőség:

### A — Modal megtartása

Gyors dokumentum-előnézetre.

### B — Dedikált dokumentumoldal

Például:

```text
/docs/kaveviz
/docs/grinder
/docs/bluetooth-scale
```

Hosszú dokumentumoknál a B változat jobb:

- URL linkelhető;
- back/forward természetes;
- mobilon könnyebb;
- SEO és accessibility tisztább.

---

# 32. Dark mode

A dark mode megtartható.

## Javítás

A kezdeti theme alkalmazása lehetőleg ne okozzon flash-t.

Megoldás:

- nagyon korai inline script a `<head>`-ben;
- vagy `prefers-color-scheme`;
- localStorage érték azonnali alkalmazása.

Ellenőrizni kell mindkét témában:

- kontraszt;
- chart vonalak;
- focus ring;
- muted text;
- accent text.

---

# 33. Tartalmi frontloading

Minden cím és gomb azzal kezdődjön, amit a felhasználó keres.

Jó:

- `Profil megnyitása`
- `JSON letöltése`
- `Scale profil`
- `Kávévíz recept`
- `Darálási útmutató`

Gyengébb:

- `Megnyitás`
- `További információ`
- `Részletek itt`
- `Összefoglaló információk`

A címsorok legyenek feladatorientáltak.

---

# 34. Mit kell eltávolítani vagy hátrébb sorolni?

## Első körben eltávolítandó a fő vizuális hierarchiából

- nagy dekoratív hero card;
- csésze SVG;
- 6 külön metric card;
- fejlesztői JSON marketing a hero leadben;
- 11 nagy dokumentumkártya;
- teljes új-profil JSON példa a főoldalon;
- teljes fázislista minden összecsukott kártyában;
- teljes chart minden mobilkártyában.

## Megtartandó

- keresés;
- filterek;
- variánsváltás;
- JSON-alapú dinamikus katalógus;
- theme;
- recipe/changelog megnyitás;
- setup;
- Markdown dokumentáció;
- accessible skip link.

---

# 35. Javasolt komponensrendszer

```text
AppShell
 ├── Header
 │    ├── Brand
 │    ├── DesktopNav
 │    ├── MobileMenu
 │    └── ThemeToggle
 │
 ├── CatalogHero
 │    ├── PageTitle
 │    ├── Lead
 │    ├── Search
 │    └── QuickFilters
 │
 ├── CatalogSection
 │    ├── CatalogHeader
 │    ├── FilterBar
 │    ├── ResultStatus
 │    └── ProfileGrid
 │         └── ProfileCard
 │              ├── Summary
 │              ├── KeyMetrics
 │              ├── VariantToggle
 │              ├── PrimaryActions
 │              └── AdvancedDetails
 │                   ├── Chart
 │                   └── PhaseList
 │
 ├── SetupSummary
 ├── Documentation
 ├── DeveloperSection
 └── Footer
```

---

# 36. Fokozatos megvalósítás

## Phase 1 — Információs hierarchia

Első commit:

- hero felezése;
- metrics eltávolítása;
- search + filter felmozgatása;
- profilkatalógus közvetlenül hero után;
- setup/docs/dev hátrébb.

**Semmilyen backend/adatmodell változás nem szükséges.**

## Phase 2 — Profilkártya egyszerűsítése

- chart összecsukása;
- fázislista összecsukása;
- CTA-k új hierarchiája;
- stat sor egyszerűsítése;
- overflow menu.

## Phase 3 — Mobil navigation

- hamburger;
- accessible dialog/drawer;
- touch targetek;
- mobil filter UX.

## Phase 4 — Performance

- catalog summary mezők;
- lazy JSON loading;
- lazy chart;
- Core Web Vitals mérés.

## Phase 5 — Codebase refactor

- CSS tokenek;
- komponens CSS;
- JS modulok;
- Markdown renderer külön modul;
- testek.

---

# 37. QA checklist

## Desktop

Teszt:

- 1280×720;
- 1366×768;
- 1440×900;
- 1920×1080.

## Mobil

Teszt:

- 320 px;
- 360 px;
- 390 px;
- 430 px.

## Böngészők

Legalább:

- Chrome;
- Safari;
- Firefox;
- Edge;
- iOS Safari;
- Android Chrome.

---

# 38. Accessibility QA

Manuálisan:

- csak billentyűzettel teljes oldal;
- 200% zoom;
- 400% zoom alapvető funkciók;
- VoiceOver vagy NVDA gyors ellenőrzés;
- dark/light contrast;
- focus order;
- modal focus;
- mobile menu focus.

Automatikusan:

- Lighthouse;
- axe DevTools vagy hasonló WCAG ellenőrző.

Az automatikus teszt **nem helyettesíti** a manuális ellenőrzést.

---

# 39. Performance QA

Mérni kell:

- Lighthouse mobil;
- PageSpeed Insights, ha publikus;
- DevTools Performance;
- Network slow 4G;
- CPU throttling.

Külön figyelni:

- `catalog.json`;
- egyedi profile JSON-ok;
- SVG chart generálás;
- Markdown render;
- layout shift variánsváltáskor.

---

# 40. Elfogadási kritériumok

A redesign akkor tekinthető sikeresnek, ha:

- [ ] A profilkereső az első viewportban látható.
- [ ] Desktopon a profilkatalógus legfeljebb egy rövid hero után kezdődik.
- [ ] Mobilon az első profil elérhető legfeljebb ~1 viewportnyi kezdő tartalom után.
- [ ] A nagy dekoratív hero card nem tolja le a katalógust.
- [ ] A 6 metric card nem foglal külön főoldali blokkot.
- [ ] A kártya összecsukott állapotban csak döntéshez szükséges adatokat mutat.
- [ ] Grafikon és fázislista alapból haladó részlet.
- [ ] Scale/Manual váltás egyértelmű.
- [ ] A primary CTA vizuálisan egyértelmű.
- [ ] Mobilon van működő fő navigáció.
- [ ] Minden fontos interaktív elem megfelelő touch targettel rendelkezik.
- [ ] Billentyűzetes navigáció működik.
- [ ] Modal / drawer fókuszkezelése korrekt.
- [ ] Helyes heading hierarchy van.
- [ ] A filterek és keresés üres / error állapota felhasználóbarát.
- [ ] A profilok nem ugrálnak jelentősen async betöltés közben.
- [ ] LCP cél ≤ 2.5 s.
- [ ] INP cél ≤ 200 ms.
- [ ] CLS cél ≤ 0.1.
- [ ] A teljes profilkatalógus továbbra is `catalog.json`-ból épül.
- [ ] Új profil hozzáadásakor továbbra sem kell kézzel új HTML kártyát létrehozni.

---

# 41. Javasolt végső sorrend

## 1. Header

Kompakt, sticky.

## 2. Catalog hero

- H1;
- 1 mondat;
- kereső;
- gyorsfilter.

## 3. Profilkatalógus

A fő tartalom.

## 4. Setup baseline

Rövid összefoglaló.

## 5. Dokumentáció

Csoportosított, kompakt lista.

## 6. Fejlesztőknek

- új profil;
- séma;
- fájlelnevezés;
- repository működés.

## 7. Footer

Projekt / GitHub / verzió információ.

---

# 42. Ajánlott első implementáció

Ha csak egyetlen redesign iteráció fér bele, pontosan ezt kell megcsinálni:

1. töröld a nagy jobb oldali hero-cardot;
2. csökkentsd a hero vertikális paddingjét;
3. cseréld a H1-et `GaggiMate kávéprofilok` szövegre;
4. rövidítsd a leadet egy felhasználói mondatra;
5. mozgasd a keresőt és a gyorsfiltereket a hero aljába;
6. távolítsd el a 6 metric cardot;
7. a profilkatalógus következzen azonnal;
8. a profilkártyán csak a summary + fő statok + CTA legyen alapból nyitva;
9. chart + phase list menjen `Profil részletei` alá;
10. a dokumentáció és `Új profil hozzáadása` kerüljön az oldal aljára;
11. készíts mobil hamburger menüt;
12. futtass accessibility és Lighthouse ellenőrzést.

Ez már önmagában lényegesen rendezettebb, gyorsabban értelmezhető és feladatorientált oldalt ad anélkül, hogy a meglévő dinamikus profilrendszert újra kellene írni.

---

# 43. Kutatási háttér és szakmai alapelvek

A specifikáció a jelenlegi HTML konkrét felépítésének vizsgálatára, valamint az alábbi webes szakmai irányelvekre épül.

## W3C / WCAG 2.2

Felhasznált témák:

- programozottan meghatározható információs struktúra;
- leíró headings és labels;
- focus;
- pointer target méret;
- WCAG 2.2 AA.

Források:

- W3C — WCAG 2.2  
  https://www.w3.org/TR/WCAG22/
- W3C — Understanding Target Size (Minimum)  
  https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum
- W3C — Understanding Info and Relationships  
  https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships
- W3C — Understanding Headings and Labels  
  https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html

## MDN

Felhasznált témák:

- semantic HTML;
- source order;
- navigation landmarks;
- responsive web design;
- skip navigation.

Források:

- MDN — HTML: A good basis for accessibility  
  https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML
- MDN — Responsive web design  
  https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design

## web.dev / Google Chrome team

Felhasznált témák:

- Core Web Vitals;
- LCP;
- INP;
- CLS;
- terepi és labor mérés.

Forrás:

- web.dev — Core Web Vitals  
  https://web.dev/articles/vitals

## GOV.UK / ONS content design

Felhasznált témák:

- user-need first;
- frontloading;
- inverted pyramid;
- scan-friendly content;
- descriptive headings;
- progressive disclosure.

Források:

- GOV.UK — Understand content design  
  https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/plan-manage-content/understand-content-design/
- ONS Service Manual — Structuring content  
  https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content
- GOV.UK Design System — Details  
  https://design-system.service.gov.uk/components/details/

---

# 44. Rövid utasítás a fejlesztőnek

> **Ne új designt rajzolj a meglévő tartalom köré; először rendezd újra a tartalom fontossági sorrendjét.**
>
> A főoldal elsődleges terméke a **profilkatalógus**, ezért a keresés, szűrés és profilválasztás legyen a vizuális és funkcionális fókusz.
>
> A setup, repository-statisztika, dokumentáció és profilkészítési útmutató támogató tartalom. Ezek maradjanak könnyen elérhetők, de ne versenyezzenek a profilokkal a first-screen figyelemért.
