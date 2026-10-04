# Espresso Nyomás Útmutató

Referencia arra vonatkozóan, hogy az extrakciós nyomás hogyan hat az ízre, és hogyan illesszük a nyomást a pörköltségi fokhoz, a feldolgozási módhoz és a shot stílusához.

> *A mélyebb magyarázatokért — mátrix indoklás, ízanyag-hatások, változók közötti kölcsönhatások, tévhitek — lásd [`reference/PRESSURE_REFERENCE.md`](../reference/PRESSURE_REFERENCE.md).*

---

## Miért számít a nyomás

A nyomás határozza meg az espresso jellegét. ~9 bar nyomáson a víz olyan lipideket, emulgeált olajokat és oldott anyagokat extrahál, amelyek gravitációs alapú főzésnél oldhatatlanok maradnak. De a 9 bar nem mindig optimális.

### A fizika

- **Az elsődleges pogácsa-tömörödés** ~4 bar nyomáson következik be. A pre-infúziónak ez alatt kell maradnia.
- **A flow (átfolyási sebesség) ~9 bar-on tetőzik.** E fölött a másodlagos tömörödés sűrűbbé teszi a pogácsát, ami *csökkenti* a flow-t. Ezért vált a 9 bar szabvánnyá.
- **~10 bar fölött** a másodlagos tömörödés channeling-et és durva túlextrakciót okoz.
- **A shot előrehaladtával** a pogácsa erodálódik. A fix 9 bar egyre nagyobb flow-t kényszerít a gyengülő csatornákon keresztül — emiatt előnyös a nyomáscsökkenés (decline).

> *A channeling fizikájáért, a finomrész-vándorlásért és a megelőzési stratégiákért lásd az `EXTRACTION_SCIENCE.md` fájlt*

### Mit szabályoz a nyomás

| Magasabb nyomás (8-9+ bar) | Alacsonyabb nyomás (5-7 bar) |
|----------------------------|--------------------------|
| Több testesség, viszkozitás | Nagyobb tisztaság, átlátszóság |
| Több crema | Kevesebb crema |
| Több olaj extrahálódik | Tisztább, teás jelleg |
| Channeling kockázata, ahogy a pogácsa degradálódik | Elnézőbb a pogácsa-előkészítéssel szemben |
| Jobb sűrű, nehezen extrahálható szemekhez | Jobb oldható, könnyen extrahálható szemekhez |

---

## Az átfogó nyomás-mátrix

### Pörköltségi fok + feldolgozási mód szerint

Ez a táblázat a **fő extrakciós nyomást** adja meg (a fenntartott nyomás a brew fázisban, a pre-infúzió után). A pre-infúziónak mindig 2-4 bar-nak kell lennie, függetlenül a célzott extrakciós nyomástól.

| | **Világos pörkölés** | **Közepes pörkölés** | **Sötét pörkölés** |
|---|---|---|---|
| **Washed (mosott)** | 8-9 bar | 9 bar | 7-8 bar |
| **Natural (natúr)** | 7-8 bar | 8-9 bar | 6-7 bar |
| **Honey (Yellow)** | 8-9 bar | 9 bar | 7-8 bar |
| **Honey (Red/Black)** | 7-8 bar | 8-9 bar | 7-8 bar |
| **Anaerobic** | 6-8 bar | 7-8 bar | 6-7 bar |
| **Carbonic Maceration** | 6-8 bar | 7-8 bar | 6-7 bar |

---

## Nyomás a shot stílusa szerint

A különböző shot stílusok eltérően használják a nyomást. A cél extrakciós nyomás, a profil alakja és az időzítés mind kölcsönhatásban állnak egymással.

### Hagyományos espresso (fix nyomás)

| Paraméter | Érték |
|-----------|-------|
| Pre-infúzió | 2-4 bar, 4-8 másodperc |
| Fő extrakció | Fix a célértéken (lásd a fenti mátrixot) |
| Decline | Nincs (vagy enyhe lefutás az utolsó 5 mp-ben) |
| Arány | 1:2 |
| Idő | 25-32 másodperc |

Ajánlott: Közepes pörkölésekhez, washed kávékhoz, mindennapi espressóhoz. Olyan kávékhoz, amelyek alacsonyabb nyomást igényelnek (naturalok, anaerobicok), egyszerűen állítsuk alacsonyabbra a célnyomást.

### Blooming espresso

| Paraméter | Érték |
|-----------|-------|
| Enyhe feltöltés (gentle fill) | Flow 2 ml/s, 5-8 másodperc |
| Bloom (pumpa kikapcsolva) | 0 bar, 8-15 másodperc |
| Ráfutás az extrakcióra | Lágy indítás (ease-in), 3-5 másodperc |
| Fő extrakció | 7-9 bar (mátrix szerint), opcionális decline-nal |
| Arány | 1:2 – 1:2,5 |
| Idő | 30-40 másodperc összesen |

Ajánlott: Világos pörkölésekhez, naturalokhoz, anaerobicokhoz — minden olyan kávéhoz, ahol maximális édességet és egyenletes telítettséget szeretnénk.

**Nyomás megjegyzés:** Bloom alkalmazásakor néha a mátrix által javasoltnál kissé magasabb extrakciós nyomás is használható, mert a bloom biztosítja az egyenletes extrakciót.

### Turbo Shot

| Paraméter | Érték |
|-----------|-------|
| Pre-wet (előnedvesítés) | 5-6 bar, 2-3 másodperc |
| Extrakció | 5-6 bar, konstans flow |
| Arány | 1:2,5 – 1:3 |
| Idő | 12-20 másodperc |
| Őrlet | Jóval durvább, mint a hagyományosnál |

Ajánlott: Világos–közepes pörkölésekhez, ahol maximális tisztaságot és édességet szeretnénk. Durvább őrlet + alacsonyabb nyomás = egyenletesebb vízeloszlás, kevesebb channeling, és meglepően magas extrakciós hozamok (19-22%).

**Nyomás megjegyzés:** Hendon és munkatársai kimutatták, hogy a 6 baros shotok következetesen *magasabb* extrakciós hozamot értek el, mint a 9 baros shotok ugyanazon őrlet mellett — mert a 9 bar több channeling-et okoz.

### Allongé

| Paraméter | Érték |
|-----------|-------|
| Pre-infúzió | 2-3 bar, 5-8 másodperc |
| Ráfutás (ramp) | 6 bar csúcsértékig |
| Fő extrakció | Konstans flow (~2-3 ml/s), a nyomás természetesen emelkedik, majd csökken |
| Arány | 1:4 – 1:5 |
| Idő | 25-40 másodperc |
| Őrlet | Kicsit durvább, mint a hagyományosnál |

Ajánlott: Világos pörkölésekhez, az origó jellegének bemutatásához. Akár 27%-os extrakciós hozam, egyenletes, fokozatos extrakción keresztül.

**Nyomás megjegyzés:** Flow-szabályozást használ nyomásszabályozás helyett. A nyomás természetesen a shot közepén tetőzik, majd csökken — ez egy kézi emelős (lever) gép működését utánozza.

### Lever Decline

| Paraméter | Érték |
|-----------|-------|
| Pre-infúzió | 2-4 bar, 5-8 másodperc |
| Csúcs | 8-9 bar, 3-5 másodperc |
| Decline | Lineáris a csúcsról 3-5 bar-ra, 20-30 másodperc alatt |
| Arány | 1:2 |
| Idő | 28-35 másodperc |

Ajánlott: Közepes pörkölésekhez, natural és honey kávékhoz — szirupos testesség tiszta lecsengéssel. A csökkenő nyomás kompenzálja a pogácsa degradációját, megelőzve a shot végi channeling-et.

---

## Döntési keretrendszer: hogyan válasszunk nyomást

### 1. lépés: Kezdjük a mátrixszal

Nézzük meg a kávénk pörköltségi fokát + feldolgozási módját a fenti mátrixban. Ez adja a cél extrakciós nyomás tartományát.

### 2. lépés: Igazítsuk a shot stílusához

- **Hagyományos** → Használjuk közvetlenül a mátrix nyomását
- **Blooming** → Mehetünk 0,5-1 bar-ral magasabbra a mátrixnál (a bloom kompenzál)
- **Turbo** → 5-6 bar a mátrixtól függetlenül (a stílus felülírja)
- **Allongé** → 6 bar csúcs, flow-szabályozott (a stílus felülírja)
- **Lever decline** → Kezdjük a mátrix nyomásán, csökkentsünk a mátrix mínusz 4-5 bar-ra

### 3. lépés: Igazítsunk az íz alapján

| Ha a shot... | Igazítsuk a nyomást... | Miért |
|--------------------|--------------------|-----|
| Savanyú/vékony a helyes idő ellenére | 0,5-1 bar-ral feljebb | Nagyobb extrakciós erő |
| Keserű/durva/fanyar | 0,5-1 bar-ral lejjebb | Kevésbé agresszív extrakció |
| Zavaros/túlzottan fermentált (naturaloknál) | 1 bar-ral lejjebb | Kevesebb fermentációs vegyület extrahálódik |
| Lapos/jellegtelen | 0,5 bar-ral feljebb, vagy próbáljunk decline profilt | Nagyobb kezdeti extrakció, tisztább lecsengés |
| Jó egyensúly, de vékony testesség | 0,5 bar-ral feljebb | Több olaj és oldott anyag |
| Jó egyensúly, de túl nehéz | 0,5 bar-ral lejjebb | Kevesebb testesség, nagyobb tisztaság |

---

*A nyomás csak egy a sok kezelőszerv közül. A legjobb shot abból születik, hogy a nyomást az adott kávéhoz igazítjuk — annak pörköltségéhez, feldolgozásához, korához — nem pedig abból, hogy egy olyan számra hagyatkozunk, ami valaki más szemeinél bevált. A mélyebb referenciáért — mátrix magyarázatok, ízanyagok, változók kölcsönhatása, tévhitek — lásd [`reference/PRESSURE_REFERENCE.md`](../reference/PRESSURE_REFERENCE.md).*
