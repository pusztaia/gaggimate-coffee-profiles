# GaggiMate Backflush -- használati útmutató

## Profil

A Backflush profil automatikusan **5 ciklust** hajt végre:

-   **5 másodperc Pressurize** -- pumpa 100%, szelep zárva
-   **10 másodperc Depressurize** -- pumpa kikapcsolva, nyomásleeresztés
-   A ciklus **5 alkalommal** ismétlődik.
-   A teljes program időtartama **75 másodperc**.
-   Az utolsó Pressurize szakaszt is Depressurize követi.

## Tisztítószeres backflush

1.  Melegítsd fel a gépet normál üzemi hőmérsékletre.
2.  Tedd a karba a **vakkosarat**.
3.  Tegyél bele a használt espresso-gép tisztítószer gyártója által
    előírt mennyiségű tisztítószert.
4.  Helyezd fel és megfelelően húzd meg a kart.
5.  A GaggiMate-en válaszd ki a **`[Utility] Backflush`** profilt.
6.  Indítsd el a profilt.
7.  A program automatikusan végrehajtja az 5 × **5 s Pressurize + 10 s
    Depressurize** ciklust.
8.  A Depressurize szakaszok alatt normális, hogy a víz és a
    tisztítószer a 3-járatú szelepen keresztül a csepptálcába távozik.
9.  A program után a tisztítószert a tisztítószer gyártójának előírása
    szerint hagyd dolgozni.
10. Vedd le a kart, és alaposan öblítsd ki a vakkosarat.

## Tiszta vizes öblítés

1.  Helyezd vissza az **üres, tiszta vakkosarat**.
2.  Futtasd le újra a **`[Utility] Backflush`** profilt tiszta vízzel.
3.  Ismételd meg szükség szerint, hogy a rendszerből minden
    tisztítószer-maradvány eltűnjön.
4.  Vedd le a kart és öblítsd át.
5.  Vakkosár nélkül engedj vizet a főzőfejből.
6.  Tisztítószeres backflush után célszerű egy kevés kávéból egy
    eldobható shotot is készíteni.

## Mire figyelj?

Az első futásnál figyeld a gépet. Vakkosár használatakor a nyomás
gyorsan felépül; ez a backflush működésének része.

A Pressurize fázis alatt:

-   pumpa: **100%**
-   idő: **5 s**

A Depressurize fázis alatt:

-   pumpa: **0%**
-   idő: **10 s**

Ha rendellenes hangot, szivárgást vagy más szokatlan működést
tapasztalsz, állítsd le a ciklust és ellenőrizd a gépet.

## Kapcsolódó profil

`profile-flush-5x5s-10s.json`
