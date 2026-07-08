# Fájlelnevezési konvenció

Ez a dokumentum leírja, hogy mi alapján vannak elnevezve a repository fájljai.

---

## Könyvtárak (`profiles/`)

Minden kávénak saját könyvtára van. A könyvtár neve a kávé rövid, URL-barát azonosítója:

```
{márka-vagy-eredet}-{kávénév}
```

**Példák:**

| Könyvtár | Kávé |
|---|---|
| `wangera/` | Impresso Kenya Wangera |
| `burundi-mubuga/` | Impresso Burundi Mubuga |
| `colombia-manos-juntas/` | Impresso Colombia Manos Juntas |
| `kirinyaga/` | Impresso Kenya Kirinyaga PB |
| `twenty-eight-caturron/` | Twenty Eight Finca el Recreo Caturron |
| `caturron/` | (korábbi, márka nélküli változat) |

**Szabályok:**
- csak kisbetű
- szavak között kötőjel (`-`)
- ékezet, szóköz, speciális karakter nincs

---

## JSON profilfájlok

A GaggiMate Pro-ba importálható profil. Neve tartalmazza a kávé azonosítóját és a profil legfontosabb paraméterét:

```
{kávé-azonosító}-{profilidő}[{hőmérséklet}].json
```

**Példák:**

| Fájlnév | Mit jelent |
|---|---|
| `wangera-stable-38s-945c.json` | Wangera, Stable Start profil, 38 s, 94.5 °C |
| `wangera-stable-38s.json` | Wangera, Stable Start profil, 38 s (korábbi verzió) |
| `burundi-mubuga-38s.json` | Burundi Mubuga, 38 s profil |
| `colombia-manos-juntas-39s.json` | Colombia Manos Juntas, 39 s profil |
| `kirinyaga-tea-rose-37s.json` | Kirinyaga, Tea Rose profil, 37 s |
| `kirinyaga-37s.json` | Kirinyaga, 37 s (korábbi verzió) |
| `caturron-flavor-42s.json` | Caturron, Flavor profil, 42 s |
| `caturron-42s.json` | Caturron, 42 s (korábbi verzió) |

**Szabályok:**
- Ha egy könyvtárban több JSON van, mindegyik egyedi nevet kap.
- A hőmérséklet csak akkor kerül a névbe, ha különböző hőmérsékletű verziók is léteznek.
- `945c` = 94.5 °C (a pont elhagyva, hogy fájlnév-biztonságos legyen).

---

## PNG grafikonok

A `tools/render_profiles.py` script generálja őket a JSON fájlokból. A PNG neve mindig a JSON nevéből képződik:

```
{json-fájlnév-kiterjesztés-nélkül}-profile.png
```

**Példák:**

| JSON | Generált PNG |
|---|---|
| `wangera-stable-38s-945c.json` | `wangera-stable-38s-945c-profile.png` |
| `wangera-stable-38s.json` | `wangera-stable-38s-profile.png` |
| `burundi-mubuga-38s.json` | `burundi-mubuga-38s-profile.png` |
| `kirinyaga-tea-rose-37s.json` | `kirinyaga-tea-rose-37s-profile.png` |
| `kirinyaga-37s.json` | `kirinyaga-37s-profile.png` |

**Szabály:** Ha egy könyvtárban több JSON van, mindegyikhez külön PNG keletkezik. A script automatikusan kezeli ezt.

> **Megjegyzés:** A `*-profile.png` nevű fájlok (pl. `wangera-profile.png`) a könyvtár névből képzett, kézzel átnevezett korábbi verziók. A script által generáltak a JSON névből képzett neveket kapják.

---

## Markdown receptfájlok

Az olvasható recept, dial-in logika és fázistáblázat:

```
{könyvtárnév}-recipe.md
```

**Példák:**

| Fájlnév | Tartalom |
|---|---|
| `wangera-recipe.md` | Kenya Wangera recept |
| `burundi-mubuga-recipe.md` | Burundi Mubuga recept |
| `colombia-manos-juntas-recipe.md` | Colombia Manos Juntas recept |
| `kirinyaga-recipe.md` | Kirinyaga PB Tea Rose recept |
| `twenty-eight-caturron-recipe.md` | Twenty Eight Caturron Flavor recept |

---

## Changelog fájlok

A profil változástörténete:

```
{könyvtárnév}-changelog.md
```

**Példák:** `wangera-changelog.md`, `burundi-mubuga-changelog.md`, stb.

---

## V4 Scale Edition JSON fájlok

A V4 Bluetooth Scale Edition profilok neve az alap JSON nevéből képződik, `scale-v4` utótaggal:

```
{alap-json-név-kiterjesztés-nélkül}-scale-v4.json
```

**Példák:**

| Alap JSON (V3) | V4 Scale Edition JSON |
|---|---|
| `burundi-mubuga-38s.json` | `burundi-mubuga-38s-scale-v4.json` |
| `wangera-stable-38s-945c.json` | `wangera-stable-38s-945c-scale-v4.json` |
| `kirinyaga-tea-rose-37s.json` | `kirinyaga-tea-rose-37s-scale-v4.json` |
| `colombia-manos-juntas-39s.json` | `colombia-manos-juntas-39s-scale-v4.json` |
| `caturron-flavor-42s.json` | `caturron-flavor-42s-scale-v4.json` |

**Szabály:** A V3 alap profil megmarad; a V4 verzió mindig külön fájl. A régi időalapú profilokat nem töröljük.

---

## Összefoglalás

| Fájltípus | Névképzés alapja | Minta |
|---|---|---|
| **Könyvtár** | kávé neve | `burundi-mubuga/` |
| **JSON (V3)** | kávé + profil paraméterei | `burundi-mubuga-38s.json` |
| **JSON (V4)** | V3 JSON neve + `-scale-v4` | `burundi-mubuga-38s-scale-v4.json` |
| **PNG** | JSON neve + `-profile` | `burundi-mubuga-38s-profile.png` |
| **Recept MD** | könyvtárnév + `-recipe` | `burundi-mubuga-recipe.md` |
| **Changelog MD** | könyvtárnév + `-changelog` | `burundi-mubuga-changelog.md` |

**Általános szabályok minden fájlnévre:**
- csak kisbetű
- szavak és elemek között kötőjel (`-`)
- ékezet, szóköz, pont (kivéve kiterjesztés), speciális karakter nincs
- minden fájlnév egyedi a teljes repository-ban
