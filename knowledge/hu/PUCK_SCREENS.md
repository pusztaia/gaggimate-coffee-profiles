# Puck Screenek

Gyorsreferencia a puck screenekhez (fémlap, amit a puck tetejére, a kávéágy és a zuhanyfej közé helyezünk) és azok extrakcióra gyakorolt hatásához.

> *A mélyebb fizikáért — hőpuffer-számok, hidraulikus ellenállás adatai, hőmérséklet-kompenzációs táblázat — lásd [`reference/PUCK_SCREENS_REFERENCE.md`](../reference/PUCK_SCREENS_REFERENCE.md).*

---

## Screen Osztályozás

Két tengely vezérli az ajánlásokat: **vastagság** és **lyuktípus**. Minden további szakasz az alábbi kanonikus tokenekkel jelöli az alkalmazhatóságát.

### Vastagság tengely

| Token | Tartomány | Példák |
|-------|-------|----------|
| **thin (≤ 1mm)** | 0,2 mm – 1,0 mm | Normcore 0.8mm, IMS 0.5mm mesh |
| **thick (> 1mm)** | 1,0 mm felett | BPlus 1.7mm, Pesado 1.7mm |

A vastagság határozza meg a hőviselkedést. A **thin (≤ 1mm)** screenek kevés hőtömeget hordoznak, és előmelegítve ≤ 1°C-ot veszítenek a felületen; a **thick (> 1mm)** screenek hidegen 2–3°C-ot is elvonhatnak, ami bojlerkompenzációt igényelhet.

### Lyuktípus tengely

| Token | Leírás | Példák |
|-------|-------------|----------|
| **round-hole** | Diszkrét fúrt lyukak (jellemzően 7–19 lyuk, 0,18–0,4 mm) | Normcore round-hole, MHW-3BOMBER round-hole |
| **mesh** | Szőtt vagy lézerszinterelt finom mesh (~150–250 µm) | IMS mesh, Pesado mesh, Sworks mesh |

A lyuktípus határozza meg a vízeloszlást, az olajvisszatartást és a tisztítási gyakoriságot. A **round-hole** könnyebben tisztítható és kevesebb olajat tart vissza, de egyenetlenebbül oszlatja el a vizet. A **mesh** oszlatja el legjobban a vizet, de több olajat tart vissza és több karbantartást igényel.

A `user-setup.md` Felszerelés táblázata mindkét tengelyt rögzíti (pl. `Normcore 58.5mm round-hole, 0.8mm` → **thin round-hole**).

---

## Mikor Használjuk

A puck screen egy passzív elosztási segédeszköz. Kiegészíti a puck előkészítést; nem helyettesíti azt.

- **Channeling a zuhanyfej sugaraiból** (a víz koncentrált sugarakban érkezik a puck felszínére) — vonatkozik a **thin** és **thick**, **round-hole** és **mesh** típusokra egyaránt. A screen kiegyenlíti a víz érkezését.
- **Felszíni kopás / "screen kiss"** — minden screenre vonatkozik. A lap megvédi a puck tetejét a lenyomattól és a kopástól.
- **Light roastok** — közösségi tapasztalat alapján előny: a sűrű, lassan nedvesedő light roast puckok egyenletesebb kezdeti telítődést mutathatnak screennel. Ez az állítás **anekdotikus** és **nem kontrollált** — nem található kontrollált A/B teszt, így a hatás mértéke nem igazolt. Ne kezeld ezt a kiindulási őrlet, hőmérséklet vagy arány megváltoztatásának okaként a `/new-coffee` során; csak döntő érvként (tiebreaker) kezeld.
- **Már kiváló zuhanyfejek** — csökkenő hozam. A modern, Gaggimate-tel felszerelt gépeknek jó az eloszlásuk; a screen hozzáadásának marginális haszna kicsi.

---

## Hatások az Extrakcióra

### Channeling csökkentés

Vonatkozik a **thin** és **thick**, **round-hole** és **mesh** típusokra. A puck screenek csökkentik a **zuhanyfej okozta** channelinget azáltal, hogy szétterítik a koncentrált vízsugarakat a puck felszínén. **NEM** csökkentik a **puck-előkészítés okozta** channelinget (csomók, egyenetlen eloszlás, ferde tamp). A puck-előkészítés okozta channeling esetén a puck előkészítést kell javítani — lásd `EXTRACTION_SCIENCE.md`.

### Hőviselkedés

A puck screen fém, és hőpufferként viselkedik. A **thin (≤ 1mm)** screenek elhanyagolható hőt veszítenek előmelegítve (a portafilterbe zárva az öblítés alatt). A **thick (> 1mm)** screenek több hőtömeget hordoznak, és indokolhatják a bojler-hőmérséklet kompenzációt. A vastagság-osztályok szerinti számszerű kompenzációs értékekért lásd a `reference/PUCK_SCREENS_REFERENCE.md` fájlt.

### Pre-infúziós viselkedés

Kvalitatívan: a puck screen egyenletesebbé teszi a kezdeti nedvesítést, ami lehetővé teszi, hogy a pre-infúzió egyenletesebben telítse a puckot, mielőtt a nyomás felfut. Kifejezetten a sűrű **light roast** puckok esetében egy kissé hosszabb pre-infúzió lehet előnyös; ez egy profilhangolási tipp, nem kötelező változtatás.

### Flow / nyomás

Mérsékelt. A screen újraelosztja a flow-t, nem korlátozza. **Thin (≤ 1mm) round-hole** screenek esetén nem indokolt őrletváltoztatás.

---

## Gyakori Buktatók

- **Hideg screen → savanyú shot.** Egy nem előmelegített screen hőt von el a puck felszínéről, ami csökkenti az extrakciós hőmérsékletet az első shotnál. **Melegítsd elő a screent úgy, hogy az öblítés alatt a portafilterbe zárod.** Ez a leggyakoribb puck-screen-félrediagnosztizálási csapda (lásd lent a Diagnosztikai Védőkorlátok szakaszt).
- **Túladagolás → eldugulás vagy meghajlott screen.** A screen hozzáadása csökkenti a hézagot a puck és a zuhanyfej között. Ha a felhasználó már határeseti túladagolásban van, a screen hidraulikus leállást ("sneeze") okoz vagy meghajlik. Tartsd az adagot = kosárméret; ne növeld az adagot a screen vastagságának kompenzálására.
- **Fejjel lefelé fordított screen.** A legtöbb screennek van egy sima és egy textúrázott/perforált oldala. A fejjel lefelé telepített screen csökkenti az eloszlás hatékonyságát; egyes kivitelek megfordítva meghajolnak vagy rosszul illeszkednek. Mindig ellenőrizd a tájolást a gyártó útmutatása szerint.
- **Rossz méret.** Egy 58,5mm-es screen egy 54mm-es kosárban (vagy fordítva) nyomáscsúcsokat, bypass channelinget okoz, vagy nem illeszkedik. Illeszd a screen méretét a kosárhoz.
- **Meghajlott screen.** Egy korábban túladagolt vagy rosszul tárolt screen maradandóan deformálódhat. A meghajlott screen egyenetlenül ül fel, és a vetemedett széle mentén channelinget okoz. A meghajlott screeneket cseréld ki.
- **Olajvisszatartás meshen.** A **mesh** screenek sokkal jobban visszatartják az olajokat, mint a **round-hole** screenek. Rendszeres tisztítás nélkül az olajok avasodnak, és keserű/áporodott jegyeket adnak a következő shotoknak.
- **Csökkenő hozam.** Olyan gépeken, amelyeknek már kiváló a zuhanyfejük, a marginális haszon kicsi. Ne kergess egy screent olyan extrakciós probléma megoldásaként, amely máshol gyökerezik (őrlet, adag, előkészítés).
- **Megvédi a puckot a zuhanyfej-lenyomattól** — a screen megakadályozza a túladagolt puckoknál egyébként megjelenő felszíni kopást és "screen kiss"-t; ez azt jelenti, hogy a BASKETS.md lenyomat-alapú hézagellenőrzése elfedett, ha puck screen van felszerelve (helyette a flow-viselkedésre és a mért hézagra támaszkodj).

---

## Tisztítás és Karbantartás

| Gyakoriság | Teendő | Megjegyzések |
|---------|--------|-------|
| Naponta | Öblítés forró vízzel | Mind **round-hole**, mind **mesh** esetén |
| Hetente | Cafiza (puly caff) áztatás | **A mesh screenek esetén ez szigorúbban kötelező** — a finom meshben gyorsabban rakódik be az olaj, mint a diszkrét fúrt lyukakban |
| Igény szerint | Hajlás, deformáció, szennyeződés ellenőrzése | Cseréld, ha meghajlott; mélytisztítsd, ha a mesh eloszlása romlik |

A **round-hole** screenek (pl. Normcore 0,18mm × 19 lyuk) könnyebben karbantarthatók — kevesebb visszatartott olaj, gyorsabb öblítés.
A **mesh** screenek (pl. IMS, Pesado, Sworks) szigorúbb heti zsírtalanítást igényelnek; számíts a round-hole 2–3-szorosára a tisztítási ráfordításban.

A 316-os rozsdamentes acél korrózióálló, de nem immunis a foltosodásra vagy a sókárra; kerüld, hogy bármelyik screen álló vízben maradjon.

---

## Diagnosztikai Védőkorlátok

Ez a szakasz az **egyetlen hiteles forrás** (Single Source of Truth) a skill-oldali puck-screen védőkorlátokhoz. A skillek (`/diagnose`, `/shot-feedback`) név szerint hivatkoznak erre a szakaszra; NEM tartják saját másolatban a szöveget.

### Hideg Screen Savanyúság Védőkorlát

**Mikor**: egy shot savanyú ÉS a felhasználónak van felszerelt puck screenje (Felszerelés sor értéke ≠ `None`).

**Teendő**: KÉRDEZZ rá az előmelegítési fegyelemre, mielőtt finomabb őrlést javasolnál. Konkrétan: a screen be volt zárva a portafilterbe az öblítés alatt, vagy utólag lett hozzáadva?

**Miért**: a hideg fém hőt von el a puck felszínéről az első shotnál, ami csökkenti az effektív extrakciós hőmérsékletet, és savanyú, alulextrahált eredményt ad. **Az előmelegítés megoldja az okot; a finomabb őrlés rontja a helyzetet** (a finomabb őrlés fokozza az alulextrakció fanyarságát, és lelassítja a flow-t a még mindig hideg screenbe).

**Megoldási út**: ha az előmelegítés kimaradt, futtasd újra a shotot megfelelő előmelegítéssel, mielőtt bármilyen őrletváltoztatást végeznél. Ha az előmelegítés rendben volt és a savanyúság megmarad, térj vissza a standard savanyú-shot hangolási létrához (hőmérséklet fel, majd finomabb őrlés).

### Channeling-árnyalat Megjegyzés

**Mikor**: savanyú-ÉS-keserű shot diagnosztizálásakor (a klasszikus channeling aláírás) ÉS puck screen van felszerelve.

**Értelmezés**: a fennmaradó channeling **valószínűleg** (NEM "szinte biztosan") puck-előkészítés okozta, **mert** a zuhanyfej okozta channeling már mérséklődött a screen által. A valószínűségi súly a WDT / eloszlás / tamp problémák felé tolódik.

**KIVÉVE**: amikor maga a screen lehet a forrás — először ellenőrizd a tájolást/illeszkedést:
- A screen a megfelelő oldalával felfelé van (sima vs. textúrázott oldal a gyártó szerint)?
- A megfelelő méretű a kosárhoz (58,5mm screen → 58mm kosár)?
- Meghajlott vagy vetemedett a korábbi túladagolástól?

Ha a tájolás, méret és állapot mind rendben van, a diagnózis alapértelmezetten puck-előkészítés okozta channelingre esik.

**Ajánlás**: a CLAUDE.md Alapszabálya szerint a javítás továbbra is **a puck előkészítés javítása, NEM az őrlet**. A screen jelenléte nem változtatja meg az ajánlást; a bizonossági szintet változtatja meg, és hozzáadja a tájolás-előellenőrzést. A finomabb őrlés a screen jelenlététől függetlenül rontja a channelinget.

---

## Biztonság: soha ne javasolj screent diagnosztikai megoldásként

Az ügynök **soha nem fog javasolni** puck screen felszerelését egy diagnosztikai probléma megoldásaként. A puck screenek passzív módosítói a diagnosztikai elvárásoknak, ha a felhasználónak már van telepítve; nem ajánlott gyógymódok channeling, savanyúság, keserűség, test vagy bármely más extrakciós probléma esetén. Ha egy felhasználó megkérdezi "segítene egy puck screen a channelingemen?", az őszinte válasz: először javítsd a puck előkészítést; a screen legjobb esetben is csak egy marginális kiegészítő segédeszköz, legrosszabb esetben pedig elvonja a figyelmet a valódi októl.

---

## Szélsőséges Esetek (feldolgozás és kezelés)

A `user-setup.md` Felszerelés táblázata a Puck Screen mezőt több állapotban is megjelenítheti. Az alábbiak szerint kezeld mindegyiket:

- **hiányzó sor** — a Felszerelés táblázatban egyáltalán nincs Puck Screen sor (régebbi, ezen funkció előtti user-setup.md). Kezeld `None`-ként; ne töltsd be ezt a tudásfájlt; ne ágazz el.
- **üres érték** — a sor létezik, de az értékcella üres. Kezeld `None`-ként; ugyanúgy, mint a hiányzó sort.
- **nem kanonikus érték** — az értékcella olyan szabad szöveget tartalmaz, amely nem feleltethető meg tisztán a thin/thick vagy round-hole/mesh kategóriáknak (pl. csak egy márkanév specifikáció nélkül). Legjobb törekvés: töltsd be ezt a tudásfájlt, és kérd meg a felhasználót a pontosításra, ha egy továbbviteli ajánlás a besorolástól függ.
- **mesh screen** — az érték mesh kivitelt jelez. Alkalmazd a mesh-specifikus útmutatást (szigorúbb tisztítási gyakoriság, jobb eloszlás, több olajvisszatartás).
- **thick screen** — az érték > 1mm vastagságot jelez. Alkalmazd a thick-screen útmutatást (bojler-hőmérséklet kompenzáció jelölt; a számokért lásd a referenciafájlt).
- **fejjel lefelé fordított screen** — a Channeling-árnyalat Megjegyzés által felvetett diagnosztikai lehetőség. Nem a beállítási táblázat értéke; hipotézis, amit akkor kell ellenőrizni, ha a channeling a screen jelenléte ellenére is fennáll.

A kanonikus tokenekért és a teljes feldolgozási szerződésért lásd a `CLAUDE.md` fájlt.

---

*Lásd a referenciát a mélyebb fizikáért: [`reference/PUCK_SCREENS_REFERENCE.md`](../reference/PUCK_SCREENS_REFERENCE.md).*
