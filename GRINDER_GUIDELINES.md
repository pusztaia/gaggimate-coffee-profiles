# Darálási útmutató – DF64V Gen 2

Ez a dokumentum a darálással és az espresso dial-in folyamattal kapcsolatos legfontosabb tudnivalókat foglalja össze a repository-ban használt setuphoz.

**Kapcsolódó dokumentumok:**

- [`BREW_GUIDELINES.md`](BREW_GUIDELINES.md) – teljes espresso dial-in folyamat
- [`PROFILE_CREATION_GUIDE.md`](PROFILE_CREATION_GUIDE.md) – profilkészítési alapértékek
- [`SUMMARY.md`](SUMMARY.md) – aktuális kávéprofilok és kiinduló őrlések
- [`speciality_kave_feldolgozasok.md`](speciality_kave_feldolgozasok.md) – feldolgozások és várható ízprofilok

---

## 1. Setup referencia

| Komponens | Érték |
|---|---|
| Daráló | DF64V Gen 2 |
| Kések | SSP Sweet Lab Espresso V3 |
| Fordulatszám-tartomány | 800–1800 RPM |
| Repository baseline | 1200 RPM |
| Őrlőskála | 0–90, egész jelölések |
| Gép | Gaggia Classic Pro 2025 + GaggiMate Pro |
| Kosár | IMS B682TH24.5M, 18–21 g |
| Rögzített dózis | 18.5 g |
| Mérleg | BOOKOO Themis Ultra Bluetooth |

A repository összes kávéspecifikus profilja **18.5 g dózisra és 1200 RPM-re** van hangolva. Ettől eltérő dózis vagy RPM esetén az őrlést újra be kell állítani.

---

## 2. Mit szabályoz az őrlés?

Az őrlés határozza meg a kávépogácsa hidraulikai ellenállásának jelentős részét. Ez közvetlenül befolyásolja:

- a first drop idejét;
- az espresso lefolyási sebességét;
- a céltömeg elérésének idejét;
- az extrakció egyenletességét;
- a testet, tisztaságot, savasságot, édességet és lecsengést;
- a channeling és spriccelés kockázatát.

### Finomabb őrlés

Általában:

- nagyobb ellenállást ad;
- lassítja a flow-t;
- később éri el a shot a céltömeget;
- növelheti a testet és az intenzitást;
- túl finom állásnál fojtott, egyenetlen vagy száraz shotot okozhat.

### Durvább őrlés

Általában:

- kisebb ellenállást ad;
- gyorsítja a flow-t;
- hamarabb éri el a shot a céltömeget;
- könnyebb, tisztább csészét adhat;
- túl durva állásnál híg, vizes, savas vagy instabil shotot okozhat.

Az őrlési beállítás önmagában nem ízcél. A megfelelő beállítás az, amely a kiválasztott profil, dózis és hozam mellett stabil flow-t és jó ízt eredményez.

---

## 3. A DF64V Gen 2 skálájának használata

A projektben a DF64V Gen 2 skáláját **egész jelölésekkel** dokumentáljuk. Tizedes értékek nem reprodukálhatók elég megbízhatóan.

| Skálaérték | Jellemző használat ezzel a setuppal |
|---:|---|
| 7–8 | Nagyon finom, nagy ellenállás, lassú flow |
| 9–10 | Általános espresso tartomány |
| 11–12 | Durvább espresso, gyorsabb flow, könnyebb test |

### Fontos szabályok

1. Mindig az adott daráló tényleges nullpontjához viszonyíts.
2. A dokumentált számok kiindulási pontok, nem univerzális értékek.
3. Más nullpont, késbeállítás, kávé, pörkölés vagy páratartalom eltérő számot eredményezhet.
4. Egy dial-in lépésben legfeljebb **egy egész jelölést** változtass.
5. A következő döntést lehetőleg 2–3 konzisztens shot alapján hozd meg.

---

## 4. Kiinduló őrlések a jelenlegi profilokhoz

Az alábbi értékek **1200 RPM, 18.5 g dózis és az IMS B682TH24.5M kosár** mellett értendők.

| Kávé | Feldolgozás | Kiinduló őrlés |
|---|---|---:|
| Kenya Wangera | washed | 10–11 |
| Burundi Mubuga | natural | 10–11 |
| Colombia Manos Juntas | anaerobic natural | 10–11 |
| Kenya Kirinyaga PB | washed | 9–10 |
| Twenty Eight Caturron | natural | 8–10 |

Ezek nem végleges értékek. A kávé öregedése, a levegő páratartalma, a kés állapota és a puck prep miatt a megfelelő beállítás változhat.

---

## 5. Fordulatszám és ízhatás

A DF64V Gen 2 fordulatszáma 800 és 1800 RPM között állítható. A repository minden profiljának baseline-ja **1200 RPM**.

Az RPM nem egyszerűen „erősebb” vagy „gyengébb” ízt szabályoz. Megváltoztathatja a szemcseeloszlást, a fines mennyiségét, a kávé áthaladását a késeken, a statikusságot és ezeken keresztül a puck ellenállását.

### Alacsonyabb RPM – 800–1000

A repository-ban használt irányelv szerint azonos skálaértéknél jellemzően:

- finomabb effektív őrleményt;
- több fines-t;
- nagyobb puck-ellenállást;
- lassabb flow-t adhat.

Lehetséges csészehatás:

- nagyobb test és intenzitás;
- koncentráltabb ízek;
- túlzott fines esetén homályosabb ízek, szárazság vagy egyenetlen lefolyás.

### Közepes RPM – 1100–1300

- A projekt alapbeállítása: **1200 RPM**.
- Jó általános egyensúlyt ad a reprodukálhatóság, test és íztisztaság között.
- Új kávét vagy új profilt mindig innen célszerű elindítani.

### Magasabb RPM – 1400–1800

A repository-ban használt irányelv szerint azonos skálaértéknél jellemzően:

- durvább effektív őrleményt;
- kevesebb fines-t;
- kisebb puck-ellenállást;
- gyorsabb flow-t és eltérő textúrát adhat.

Lehetséges csészehatás:

- tisztább, elkülönülőbb ízek;
- könnyebb test;
- túl gyors flow esetén vékonyabb vagy savasabb csésze.

> Az RPM hatása függ a kávétól, a késgeometriától, az adagolás módjától és az őrlési beállítástól. Ezért az ízhatásokat irányként, nem garantált eredményként kell kezelni.

### RPM-változtatási szabály

Ha megváltoztatod az RPM-et:

1. tartsd változatlanul a dózist, hőmérsékletet, profilt és céltömeget;
2. számíts arra, hogy a flow megváltozik;
3. állítsd újra az őrlést a megfelelő lefolyási időhöz;
4. csak ezután hasonlítsd össze az ízt.

Azonos skálaérték mellett készített 900 és 1600 RPM-es shot nem tiszta íz-összehasonlítás, mert az eltérő flow és extrakció is megváltoztatja az eredményt.

---

## 6. Ajánlott dial-in sorrend

A stabil dial-in során a lehető legtöbb paraméter maradjon rögzített.

1. **RPM:** 1200.
2. **Dózis:** 18.5 g.
3. **Profil és hőmérséklet:** a recept szerint.
4. **Célhozam:** a profil `volumetric` célértéke vagy a receptben megadott hozam.
5. **Őrlés:** elsődleges hangolási változó.
6. **Puck prep:** minden shotnál azonos WDT, tamp és puck screen használat.
7. **Ízértékelés:** csak stabil flow után változtass hozamon vagy hőmérsékleten.
8. **RPM-kísérlet:** csak a hagyományos dial-in befejezése után.

### Egy változtatás egyszerre

Ne változtasd egyszerre az őrlést, RPM-et, dózist és hőmérsékletet. Több párhuzamos változtatás esetén nem állapítható meg, melyik okozta az ízbeli vagy flow-változást.

---

## 7. V3 és V4 profilok darálási logikája

### V3 – Time Based

A V3 profilok beállított időtartamig futnak. Az őrlés egyszerre befolyásolja:

- a flow-t;
- a teljes hozamot;
- a shot időn belüli lefutását.

Ha túl durva az őrlés, a profil végére túl sok ital kerülhet a csészébe. Ha túl finom, a kívánt hozam nem érhető el a profilidő alatt.

### V4 – Bluetooth Scale Edition

A V4 profilok beverage weight alapján állnak meg. Az őrlés elsősorban azt határozza meg:

- milyen gyorsan éri el a shot a célhozamot;
- melyik fázisban tüzel a tömegalapú stop;
- mennyire stabil és egyenletes az extrakció.

A V4 profil azonos hozamot képes adni túl finom és túl durva őrlésnél is, de az eltérő elérési idő és flow miatt az íz jelentősen különbözhet.

### V4 célzóna

Általános irányelvként az extraction fázisban a céltömeg stopja jellemzően **20–30 másodpercen belül** legyen elérhető. A profil teljes kijelzett ideje a preinfusion fázisok miatt ennél hosszabb lehet.

Ha a safety timeout zárja a shotot, az őrlés valószínűleg túl finom, vagy a Bluetooth scale stop nem működött.

---

## 8. Tünetek és őrlési korrekciók

| Tünet | Valószínű ok | Következő lépés |
|---|---|---|
| A célhozam nem érkezik meg a safety timeout előtt | Túl finom őrlés vagy scale-hiba | Ellenőrizd a scale kapcsolatot; ha jó, egy jelöléssel durvábbra |
| A célhozam túl hamar érkezik meg | Túl durva őrlés vagy channeling | Egy jelöléssel finomabbra; ellenőrizd a puck prep-et |
| Híg, vizes, kevés test | Túl gyors flow | Finomabb őrlés |
| Fojtott, préselt, homályos íz | Túl nagy ellenállás | Durvább őrlés |
| Éles, kellemetlen savasság és gyors shot | Alulextrakció / túl durva őrlés | Finomabb őrlés |
| Keserű, száraz, tanninos és lassú shot | Túl magas extrakció vagy egyenetlenség | Durvább őrlés; utána hozam és hő ellenőrzése |
| Spriccelés már a first drop előtt | Channeling | WDT és tamp javítása, ne az RPM legyen az első változó |
| Spriccelés extraction közben | Puck összeomlás vagy túl durva őrlés | Finomabb őrlés és puck prep ellenőrzése |
| Shotonként nagy időeltérés | Inkonzisztens puck prep, dózis vagy retention | Dózis, WDT, tamp, daráló tisztaság ellenőrzése |

Az ízt és a lefolyást együtt kell értékelni. Egyetlen időadat alapján nem dönthető el biztosan, hogy az őrlés megfelelő-e.

---

## 9. Puck prep és az őrlemény kapcsolata

A jó őrlési beállítás sem ad stabil eredményt rossz puck prep mellett.

### Kötelező lépések

1. Mérj be **18.5 g** kávét legalább ±0.1 g pontossággal.
2. Oszlasd el az őrleményt WDT-vel a kosár teljes mélységében, különösen az alján és a széleken.
3. Tömöríts egyenesen és reprodukálhatóan.
4. A puck screen legyen tiszta és száraz.
5. Naked portafilterrel figyeld a lefolyás kezdetét és az esetleges spriccelést.

### Miért fontos?

A channeling helyi, gyors vízutat hoz létre. Emiatt a shot egyszerre lehet:

- összességében gyors;
- bizonyos részeken alulextrahált;
- más részeken túlextrahált;
- savas és száraz ugyanabban a csészében.

Ilyenkor az őrlés önmagában történő finomítása akár ronthatja is a problémát.

---

## 10. Kávé és feldolgozás szerinti kiindulási irány

A feldolgozás nem határoz meg egyetlen helyes őrlést, de segíthet az ízcél kiválasztásában.

| Feldolgozás | Jellemző csésze | Darálási cél |
|---|---|---|
| Washed | Tiszta, élénk, virágos, tea-szerű | Stabil, egyenletes flow; ne fojtsd túl, hogy megmaradjon a tisztaság |
| Natural | Édesebb, testesebb, lekvárosabb | Közepes ellenállás; túl finoman könnyen nehéz és fermentált lehet |
| Honey | Édes, kerek, balanszos | Test és tisztaság közötti egyensúly |
| Anaerobic | Intenzív, trópusi, gyakran funky | Kerüld a túlzott extrakciót és száraz lecsengést |
| Carbonic maceration | Boros, szőlős, parfümös | Az aromák tisztasága fontosabb lehet a maximális testnél |

A feldolgozás alapján ne módosíts közvetlenül RPM-et. Először 1200 RPM-en állítsd be az őrlést, majd ízcél alapján tesztelj más fordulatot.

---

## 11. Konzisztencia és naplózás

Minden shotnál érdemes rögzíteni:

| Mező | Példa |
|---|---|
| Kávé | Kenya Wangera |
| Profil | `wangera-stable-38s-945c-scale-v4.json` |
| Dózis | 18.5 g |
| Őrlés | 10 |
| RPM | 1200 |
| Hozam | 42.0 g |
| Teljes idő | 38 s |
| Stop trigger | beverage weight |
| Puck viselkedés | egyenletes / spriccelt |
| Íz | savasság, édesség, test, lecsengés |
| Következő lépés | egy jelöléssel finomabb |

Két egymást követő, azonos paraméterű shot hozamának legfeljebb ±1.0 g eltérése elfogadható. V4 profilnál a hozam automatikusan stabilabb, ezért az idő és a flow változása különösen fontos diagnosztikai adat.

---

## 12. Gyors döntési fa

```text
A céltömeg túl gyorsan érkezik meg?
├─ Igen → ellenőrizd a channelinget
│  ├─ Spriccel / egyenetlen → WDT és tamp javítása
│  └─ Egyenletes → egy jelöléssel finomabb őrlés
└─ Nem
   ├─ A céltömeg túl lassan vagy egyáltalán nem érkezik meg?
   │  ├─ Scale kapcsolat hibás → Bluetooth / brew-by-weight ellenőrzése
   │  └─ Scale rendben → egy jelöléssel durvább őrlés
   └─ Idő és flow megfelelő
      ├─ Íz balanszos → beállítás rögzítése
      └─ Íz nem megfelelő → hozam vagy hő finomhangolása
```

---

## 13. RPM-kísérlet ajánlott módszere

Az RPM ízhatásának összehasonlításához:

1. Készíts stabil baseline-t 1200 RPM-en.
2. Rögzítsd a dózist, profilt, hőmérsékletet és hozamot.
3. Próbálj egy alacsonyabb fordulatot, például 900 RPM-et.
4. Állítsd újra az őrlést, hogy a céltömeg közel azonos idő alatt érkezzen meg.
5. Próbálj egy magasabb fordulatot, például 1600 RPM-et.
6. Ezt is külön dial-in-eld azonos idő- és hozamcélra.
7. Vakon vagy kihűlés közben hasonlítsd össze a testet, tisztaságot, édességet és lecsengést.

Csak az újradial-inelt shotok ízbeli különbsége tulajdonítható érdemben az RPM-változtatásnak.

---

## 14. Rövid összefoglaló

- A repository alapja: **18.5 g, 1200 RPM, egész őrlési jelölések**.
- Dial-in közben az őrlés legyen az elsődleges változó.
- Túl gyors shothoz általában finomabb, fojtott shothoz durvább őrlés kell.
- Spriccelésnél először a puck prep-et ellenőrizd.
- RPM-változtatás után mindig újra kell dial-in-elni.
- A V4 tömegalapú stop stabil hozamot ad, de a jó ízhez az elérési időnek és a flow-nak is megfelelőnek kell lennie.
- Egyszerre csak egy paramétert változtass, és minden shotot naplózz.
