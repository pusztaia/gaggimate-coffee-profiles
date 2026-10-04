# Espresso Brewing alapok

Gyors referencia az alapvető változókhoz, hangolási stratégiákhoz és diagnosztikához a dial-in során.

---

## Az alapvető változók

Minden espresso shotot ezek az egymással összefüggő változók határoznak meg:

| Változó | Mit csinál | Tipikus tartomány |
|---|---|---|
| **Dózis** | A bemenő kávé grammban | 15-22g (igazodjon a kosár méretéhez) |
| **Hozam** | A kimenő espresso grammban | 30-50g |
| **Arány** | Dózis:Hozam viszony | 1:2 – 1:3 |
| **Idő** | Extrakció időtartama | 20-35s (stílustól függ) |
| **Őrlés** | Szemcseméret | Finomabb = lassabb, nagyobb extrakció |
| **Hőmérséklet** | Főzővíz hőmérséklete | 88-96°C |
| **Nyomás** | Bar az extrakció alatt | 6-9 bar (stílustól és feldolgozástól függ) |

**Alapelv:** Egyszerre csak egy változót változtass. Ha egyszerre változtatod az őrlést, a dózist ÉS a hőmérsékletet, nem fogod tudni, mi javította (vagy rontotta el) a shotot.

---

## Hangolási stratégiák

### Az 5 grammos szabály (gyors hozam-hangolás)

Mielőtt az őrlési fokozaton változtatnál, próbáld meg a hozamot hangolni:

- **Savanyú/sós/durva?** → Növeld a kimenetet 5g-mal (balanszírozó vegyületeket ad hozzá)
- **Keserű/száraz/karcoló?** → Csökkentsd a kimenetet 5g-mal (megőrzi az édességet, csökkenti a késői extrakcióból eredő keserűséget)

Ez azért működik, mert az extrakció egy idővonal: először a savak jönnek ki, aztán a cukrok, majd a keserű vegyületek. A hozam hangolásával azt változtatod, hol "vágod el" ezt az idővonalat.

**Mikor használj hozam- vagy őrlés-hangolást:**
- Hozam hangolása: Gyors javítás, nem igényli a shot idő újra-dial-in-elését
- Őrlés hangolása: Alapvetőbb változtatás, hatással van a flow sebességére és a teljes extrakcióra
- Hőmérséklet: Finomhangolás, miután az őrlés be van állítva
- Nyomás: Stílusváltás (turbo vs. hagyományos) vagy a durvaság csökkentése

### Hagyományos espresso hangolások

| Probléma | Elsődleges javítás | Másodlagos javítás |
|---|---|---|
| Savanyú, vékony, gyors | Finomabb őrlés | Hőmérséklet növelése |
| Savanyú/sós finom őrlés ellenére | Hozam növelése 5g-mal | Hőmérséklet növelése |
| Keserű, lassú, száraz | Durvább őrlés | Hőmérséklet csökkentése |
| Keserű durva őrlés ellenére | Hozam csökkentése 5g-mal | Nyomáscsökkenés hozzáadása |
| Channeling (egyenetlen flow) | Jobb puck prep | Hosszabb pre-infúzió |
| Nincs test a jó íz ellenére | Alacsonyabb nyomás vagy channeling | Szivárgás ellenőrzése |

### Turbo/modern stílusú hangolások

| Probléma | Elsődleges javítás | Másodlagos javítás |
|---|---|---|
| Túl savanyú | Hosszabb áztatás/pre-infúzió | Kicsit finomabb őrlés |
| Túl keserű | Durvább őrlés | Alacsonyabb nyomás |
| Hiányzik a tisztaság | Durvább őrlés | Hosszabb arány |
| Túl vékony/vizes | Finomabb őrlés | Rövidebb arány |

### Hőmérséklet irányelvek pörkölés szerint

| Pörkölési szint | Hőmérséklet tartomány |
|---|---|
| Világos (skandináv) | 94-96°C |
| Közepes | 92-94°C |
| Közepesen sötét | 90-92°C |
| Sötét | 88-90°C |

**Hangolási szabály:**
- Túl savanyú → növeld 1-2°C-kal
- Túl keserű → csökkentsd 1-2°C-kal

### Miért "kevésbé savas" ízűek a sötét pörkölések

Egy gyakori tévhit: a sötét pörkölésű szemek valójában hasonló savszintet tartalmaznak, mint a világosak. A különbség percepció, nem kémia.

- A sötét pörkölésű szemek kevésbé sűrűek → több szem jut 15g dózisra → hasonló teljes savtartalom
- A sötét pörkölések több keserű vegyületet tartalmaznak (CGA laktonok, fenilindánok), amelyek *elfedik* a savasságot
- A sötét pörkölések törékenyebbek → több fines keletkezik → ez szemcsés, texturális keserűséghez járul hozzá

**Gyakorlati következmény:** Ha a sötét pörkölésű kávéd durva ízű, a keserűség forrása lehet a fines, nem a túlextrakció. Próbálj durvább őrlést, és győződj meg az egyenletes elosztásról.

---

## Arány irányelvek

| Arány | Stílus | Jelleg |
|---|---|---|
| 1:1 – 1:1.5 | Ristretto | Intenzív, koncentrált, nehéz |
| 1:2 | Klasszikus | Balanszos, teltestű |
| 1:2.5 – 1:3 | Lungo/modern | Könnyedebb, több tisztaság, elnyújtott édesség |
| 1:3+ | Allongé/SOUP | Filteres tisztaság, teás jellegű test |

**Mikor hangold az arányt:**
- Több intenzitást akarsz → rövidebb arány
- Több tisztaságot/édességet akarsz → hosszabb arány
- A világos pörkölés savanyú 1:2-nél → próbálj 1:2.5-öt vagy 1:3-at

---

## Változó hierarchia: mit hangolj először

Nem minden változónak egyforma a hatása. Ebben a sorrendben hangolj:

| Prioritás | Változó | Hatás | Mikor hangold |
|---|---|---|---|
| 1 | **Őrlési fokozat** | A legnagyobb hatás az extrakcióra | A shot idő messze van a céltól, vagy az íz egyértelműen savanyú/keserű |
| 2 | **Hozam/arány** | Gyors korrekció az idő újra-dial-in-elése nélkül | A shot idő elfogadható, de az íz nem jó (használd az 5 grammos szabályt) |
| 3 | **Hőmérséklet** | Finomhangolás, miután az őrlés már közel jó | Az őrlés be van állítva, de az íz lapos, éles, vagy hiányzik az édesség |
| 4 | **Nyomás/profil** | Stílusváltás vagy továbbfejlesztés | Az alapok működnek, de más jelleget szeretnél |
| 5 | **Puck prep** | Konzisztencia és channeling | Egyszerre savanyú ÉS keserű, vagy inkonzisztens shotok |

**Alapelv:** Ne ugorj a profil hangolására, ha az őrlés nem megfelelő. Előbb hozd rendbe az alapokat, aztán finomíts. Egy tökéletes profil sem menthet meg egy rossz őrlési beállítást.

---

## Diagnosztikai döntési fa

| Tünet | Shot idő | Első ellenőrzés | Második ellenőrzés | Harmadik ellenőrzés |
|---|---|---|---|---|
| **Savanyú + gyors** | <20s | Finomabb őrlés | — | — |
| **Savanyú + normál idő** | 25-30s | Hozam növelése 5g-mal | Hőmérséklet növelése 1-2°C-kal | Bloom hozzáadása a profilhoz |
| **Savanyú + lassú** | >35s | Valószínűleg channeling (lásd lent) | Jobb puck prep | Hosszabb pre-infúzió |
| **Keserű + lassú** | >35s | Durvább őrlés | — | — |
| **Keserű + normál idő** | 25-30s | Hozam csökkentése 5g-mal | Hőmérséklet csökkentése 1-2°C-kal | Nyomáscsökkenés hozzáadása |
| **Keserű + gyors** | <20s | Esetleg túlpörkölés vagy vízprobléma | Szem frissességének ellenőrzése | Víz minőségének ellenőrzése |
| **Savanyú ÉS keserű** | Bármi | **Channeling** — javítsd a puck prep-et | Finomabb őrlés + hosszabb PI | Daráló ellenőrzése csomósodásra |
| **Balanszos, de lapos** | 25-30s | Hőmérséklet növelése 1°C-kal | Próbálj hosszabb arányt | Frissesség ellenőrzése |
| **Balanszos, de vékony** | 25-30s | Rövidebb arány | Finomabb őrlés (test növelése) | Kosár szivárgásának ellenőrzése |

**Kritikus meglátás (Scott Rao):** Ha a shotod **egyszerre savanyú és keserű**, az szinte biztosan channeling — a víz a legkisebb ellenállású utakat keresi, egyes szemcséket túlextrahálva, másokat alulextrahálva. A javítás a puck prep (WDT, elosztás, egyenletes tamp), nem az őrlés hangolása. A finomabbra őrlés channeling jelenlétében csak ront a helyzeten.

---

## Problémák szétválasztása

Amikor egy shot nem jó, a kihívás azonosítani, *melyik* változó a bűnös:

**Az őrlés a hibás?**
- A shot idő jelentősen eltér a céltól (>5 másodperc eltérés)
- Az íz egyezik az idővel — gyors + savanyú, vagy lassú + keserű
- Megoldás: Hangold az őrlést, minden más maradjon ugyanaz

**A hőmérséklet a hibás?**
- A shot idő a tartományban van, de az íz lapos, éles, vagy hiányzik az édesség
- Az őrlés változtatása nem javítja az ízt (csak gyorsabbá/lassabbá teszi, ugyanazokkal a problémákkal)
- Megoldás: Hangold a hőmérsékletet 1-2°C-kal a megfelelő irányba

**Az arány a hibás?**
- A shot idő és a hőmérséklet jónak tűnik, de a balansz kicsit nem megfelelő
- Az 5 grammos szabály gyorsan megoldja
- Megoldás: Adj hozzá vagy vonj le 5g-ot a hozamból

**A profil a hibás?**
- Az őrlés és a hőmérséklet be van állítva, a shot idő helyes, de a kávé "befejezetlennek" érződik
- Több édességet, más testet, vagy más jelleget szeretnél
- Megoldás: Próbálj másik profilstílust (bloom, decline, turbo), vagy hangold a profil fázisait

**A puck prep a hibás?**
- Egyszerre savanyú ÉS keserű
- Inkonzisztens shotok (azonos beállítások, eltérő eredmények)
- A telemetria egyenetlen flow-t vagy nyomáscsúcsokat mutat
- Megoldás: WDT elosztás, egyenletes tamp, csomók ellenőrzése; ne változtass az őrlésen, amíg a prep nem konzisztens

---

*A shot stílusokhoz (hagyományos, turbo, allongé, SOUP, ristretto, lungo), pre-infúzió & nyomásfázisokhoz, dial-in módszertanhoz, salami shot technikához, több kávé kezeléséhez és gyakori hibákhoz lásd a `reference/ESPRESSO_BREWING_REFERENCE.md` fájlt. Kóstolási útmutatáshoz lásd az `ESPRESSO_TASTING_GUIDE.md` fájlt. Profil létrehozásához lásd a `GAGGIMATE_PROFILE_CREATION_GUIDE.md` fájlt.*
