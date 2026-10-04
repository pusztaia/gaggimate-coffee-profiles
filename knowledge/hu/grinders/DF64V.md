# DF64V Daráló Referencia

Gyors referencia az őrlési beállításokhoz és azok finomhangolásához a **DF64V Gen-3 változtatható fordulatszámú, single-dose darálóhoz**, gyárilag szerelt **SSP Cast Lab Sweet V3 Red Speed espresso késekkel** (64 mm-es flat, előre felszerelve). A saját, bevált őrlési beállításaidért lásd a projekt gyökerében a `grind-map.md` fájlt. Minden beállítást a [`_NOTATION.md`](_NOTATION.md) formátuma szerint naplózz.

> **Mélyebb áttekintés:** a seasoning ütemterv, az RDT/bellows munkafolyamat, az üzembe helyezés, a stallhibák elhárítása és a kés jegyzetek itt találhatók: [`../reference/DF64V_REFERENCE.md`](../../reference/DF64V_REFERENCE.md).

---

## Beállítási rendszer

A DF64V egy **fokozatmentes gyűrűt (stepless collar)** használ — nincsenek rögzített makro vagy mikro lépések. Az őrlési finomságot a felső késtartó gyűrű elforgatásával állítod be; finomabb az óramutató járásával megegyező irányban (befelé), durvább azzal ellentétesen.

### A nullpont megkeresése (Chirp Point)

A DF64V nullázása motoros segítséggel, ún. chirp dialing módszerrel történik:

1. Indítsd el a motort a munkafordulatszámodon.
2. Lassan forgasd a gyűrűt finomabb irányba, amíg a kések első érintkezésbe nem kerülnek — ezt egy halk, rövid csippanás vagy súrlódó hang jelzi.
3. Azonnal lazíts 1–2 jelöléssel. Ez lesz a **nullponti referenciád**.
4. Naplózd ezt a nullpont-dátumot a `grind-map.md`-ben `zero set: ÉÉÉÉ-HH-NN` formában (lásd [`_NOTATION.md`](_NOTATION.md)).

Kés eltávolítása, visszaszerelése vagy beállítás-igazítás után mindig nullázz újra. A korábbi epoch sorai a grind map-edben nem érvényesek tovább — lásd a [`_NOTATION.md`](_NOTATION.md) felülíró konvencióját.

### A beállítás naplózása

Az őrlést egy **egyszerű egész számként** rögzítsd, amely azt mutatja, hány jelölésnyire van nyitva a gyűrű az aktuális chirp nullponttól (pl. `11`). A grind-log táblázat egyszer, a fejlécében/lábjegyzetében deklarálja: **"Őrlés = jelölések száma a chirp nullponttól nyitva (DF64V)"**, így a puszta szám egyértelmű; e fejléc-deklaráció nélkül egy puszta szám értelmezhetetlen. A rögzített szám továbbra is a chirp-relatív operátori koordináta — a fejléc adja hozzá a "chirp-től" horgonypontot; ez **nem** az abszolút, nyomtatott tárcsapozíció. Ez egy operátori koordináta, nem mikron- vagy szemcseméret-állítás. A DF64V fokozatmentes gyűrűjéhez nem tartozik mikron/jelölés érték; ne kezeld a jelölésszámokat abszolút rés-mérésként. Lásd [`_NOTATION.md`](_NOTATION.md).

### Espresso kiindulási ablak

Espresso esetén kezdd a dial-int kb. **10–20 (jelölés a chirp-től)** tartományban a nullponttól. Ez csak egy kiindulási ablak — a tényleges beállításod a kávétól, a dózistól, a pörköléstől és a frissességtől függ. Ebből a tartományból indulj a dial-innel; ne feltételezd, hogy ez már egy működő shot.

---

## Motor fordulatszáma (RPM)

A DF64V Gen-3 változtatható fordulatszámú. Espressóhoz az ajánlott üzemi tartomány körülbelül **1000–1200 RPM**:

- **~1000–1200 RPM** a független tesztelők által egységesen javasolt standard espresso ablak.
- **~1400 RPM** egy kereskedő által preferált érték, amelyet nagyobb test eléréséhez jelentettek (vendor-framed; lásd a Kés karakter jegyzetet lent); ez nem egy alsó határ vagy alapértelmezett érték.
- **~700–800 RPM alatt** fennáll az alacsony fordulatszámú stall kockázata sűrű, light roast kávéval, ha egyszerre adagolod be a szemeket — ez egy szélsőséges eset, nem a motor nyomatékhibája (lásd a Deep Dive-ot a részletekért).

Kezdj **~1000–1100 RPM**-ről. Az RPM változtatása eltolja a szemcseeloszlást, ezért szükségessé teheti az őrlési beállítás újra-dial-inelését; kezeld az RPM-et durva, nem finomhangoló eszközként. Mielőtt az RPM-hez nyúlnál mint dial-in eszközhöz, olvasd el a lenti **RPM mint dial-in eszköz** jegyzetet — az RPM és a csésze teste közötti kapcsolat vitatott, nem egy letisztult szabályozó.

---

## RPM mint dial-in eszköz

**Mikor nyúlj hozzá.** Az RPM az utolsó eszköz, nem az első. Elsőként az őrlést, az arányt, a hőmérsékletet és a puck prep-et állítsd be — ezek sokkal többet számítanak, sokkal kiszámíthatóbban. Csak akkor nyúlj az RPM-hez, ha ezek már stabilak, és egy *tudatos, naplózott* test/tisztaság kísérletet szeretnél futtatni. Az RPM **soha** nem lehet a nyitólépés, és **soha** nem channeling-javítás (a savanyú *és* keserű íz egyszerre puck prep probléma — lásd a Gyors Beállítási Útmutatót).

**Az egyetlen vitathatatlan tény — igazodj a shot időzítődhöz.** Az RPM megváltoztatása eltolja a szemcseeloszlást, ezért bármilyen RPM-változtatás után **újra be kell állítanod az őrlést**, hogy visszaállítsd a célzott shot időt. Hagyd, hogy a shot időzítőd mondja meg, melyik irányba mozdulj — ne feltételezz irányt. (Szándékosan nincs itt kinyomtatva olyan szabály, hogy "magasabb RPM → finomabb őrlés" — az időzítő dönt.)

**Miért vitatott, hogy "több RPM → több test".** Az a népszerű elképzelés, hogy a magasabb RPM nagyobb testet ad, **vitatott**, nem bizonyított tény:

- Egy alapos, független mérés (McKeon Aloe) azt találta, hogy a magasabb RPM *durvább* irányba tolta el a szemcseeloszlást, kevesebb fines-szel — ez pont az ellentéte a vendor "nagyobb test" történetének.
- Hoffmann vak kóstolása nem talált itt tiszta korrelációt (nulla eredmény).
- A vendor-framed "az RPM egy test-szabályozó" állítás nem bizonyított; kezeld legfeljebb hihetőként, nem kalibrált szabályzóként.

Tehát ne az RPM-re építs úgy, mintha az "RPM = test" megerősített tény lenne. **A saját, naplózott RPM↔eredmény adataid jelentik a valódi jelzést** — rögzítsd az RPM-et minden shotnál, és hagyd, hogy a saját csészéd mondja meg, egy adott RPM-változtatás tett-e bármit *ezzel a kávéval*, *a te gépeden*.

> **Mélyebb áttekintés:** a McKeon/Hoffmann bizonyítékok és az újra-dial-in mechanika részletesen itt találhatók: [`../reference/DF64V_REFERENCE.md`](../../reference/DF64V_REFERENCE.md) → "RPM mint test/tisztaság szabályozó".

---

## Espresso tartomány

Espressóhoz az SSP Cast V3 Red Speed késsel, jellemző kiindulási ablakok pörkölési szint szerint:

A **Jellemző kiindulási ablak** oszlop értékei jelölések a chirp nullponttól nyitva.

| Pörkölési szint | Jellemző kiindulási ablak (jelölés a chirp-től) | Megjegyzés |
|-------------|----------------------|-------|
| Light       | 10–15  | Finom vég; lassabb célidő valószínűleg szükséges |
| Medium      | 13–18  | Standard espresso tartomány |
| Dark        | 16–22  | Durvább, hogy elkerüld a túlextrakciót |

**Ezek csak kiindulópontok.** A tényleges beállítás függ a kávé frissességétől (frissebb = kicsit durvább), a dózistól, a célzott aránytól/időtől és az aktuális nullpont-epochtól. A DF64V az SSP Cast késekkel az átlagosnál szűkebb dial-in ablakáról híres — számíts arra, hogy módszeresen kell dolgoznod a tartományban.

---

## Gyors Beállítási Útmutató

Egy már működő shotból kiindulva az őrlési beállítást kis lépésekben változtasd:

| Probléma | Beállítás | Mértéke |
|---------|------------|-----------|
| A shot túl gyors, savanyú | Finomabbra | 1–3 jelölés |
| A shot túl lassú, keserű | Durvábbra | 1–3 jelölés |
| Nagy korrekció szükséges | Mozgass több jelölést, majd finomhangolj | 5+ jelölés |
| Egyszerre savanyú és keserű | Ne az őrlést állítsd — javítsd a puck prep-et (channeling) | — |

**Alapszabály:** Apró lépésekben állíts — 1–3 jelölés változtatásonként. Kóstolj, majd ha szükséges, állíts újra. A fokozatmentes gyűrű érzékeny; a nagy mozdulatok könnyen túllőnek a célon.

---

## Kés karakter jegyzet

> **Ez egy tendencia/vendor-framed jellemzés, nem mért garancia. Mindig a tényleges csészéd alapján dönts.**

Az SSP Cast Lab Sweet V3 Red Speed egy **64 mm-es flat espresso kés**. A flat kések a konikus késekhez képest a tisztaság (elkülönülő, letisztult ízek) irányába hajlanak — de ez vitatott tendencia, nem determinisztikus szabály (Hoffmann vak kóstolása nem talált tiszta összefüggést a kés geometriája és a test/tisztaság között).

Az SSP flat tartományon belül a **Cast** vonal **magasabb fines-tartalmat** ad, mint a tipikus alacsony fines-ű flat kések (például az SSP Multipurpose). Ez azt jelenti, hogy a "flat = tisztaság, kevesebb test" jellemzés itt gyengébben érvényesül, mint az alacsonyabb fines-ű flat késeknél.

A **Red Speed** TiAlCN bevonatot a gyártó úgy írja le, hogy a Silver Knight (DLC) változathoz képest nagyobb testet ad; maga a gyártó is megjegyzi, hogy ez "másodlagos és darálófüggő". Kezeld hihetőként, nem bizonyítottként.

**Gyakorlati következmény:** Mivel a kés rögzített, a test szabályozására ténylegesen rendelkezésre álló eszközeid a **dózis és az arány** (kiszámíthatók) — és, bizonyos fenntartásokkal, az **RPM**. Az RPM *nem* egy letisztult test-szabályozó: a "több RPM → több test" kapcsolat vitatott (lásd a fenti **RPM mint dial-in eszköz** jegyzetet a McKeon-durvább / Hoffmann-null eredményekért és a saját-adat ajánlásért). Elsőként a dózishoz és az arányhoz nyúlj; az RPM-et csak tudatos, naplózott kísérletként futtasd. A csésze karakterének részletei a konkrét extrakciódtól és ízlésedtől függenek, nem a kés specifikációjától.

---

*A saját, bevált beállításaidért lásd a projekt gyökerében a `grind-map.md` fájlt. A naplózási formátumért és az epoch konvenciókért lásd a [`_NOTATION.md`](_NOTATION.md) fájlt.*
