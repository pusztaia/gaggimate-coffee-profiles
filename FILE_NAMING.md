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

**Szabályok:**
- csak kisbetű
- szavak között kötőjel (`-`)
- ékezet, szóköz, speciális karakter nincs

---

## JSON profilfájlok

A GaggiMate Pro-ba importálható profil. Neve a kávé azonosítójából és a profil típusából áll — a minta a `kirinyaga/` könyvtár:

```
{kávé-azonosító}-manual.json   # időalapú (V1) profil
{kávé-azonosító}-scale.json    # BOOKOO Bluetooth scale-alapú (V2) profil
```

Ha egy kávénak több manual vagy több scale változata is van (pl. eltérő hőmérséklet-variánsok), a fájlnév végén sorszám különbözteti meg őket:

```
{kávé-azonosító}-manual-v1.json / -v2.json / ...
{kávé-azonosító}-scale-v1.json  / -v2.json / ...
```

**Példák:**

| Fájlnév | Mit jelent |
|---|---|
| `kirinyaga-manual.json` / `kirinyaga-scale.json` | Kirinyaga — a minta: egy manual + egy scale profil |
| `burundi-mubuga-manual.json` / `burundi-mubuga-scale.json` | Burundi Mubuga — szintén egy-egy profil |
| `colombia-manos-juntas-manual.json` / `colombia-manos-juntas-scale.json` | Colombia Manos Juntas |
| `caturron-manual.json` / `caturron-scale.json` | Twenty Eight Caturron (a könyvtárnévnél rövidebb `caturron` azonosítóval) |
| `wangera-manual-v1.json` / `wangera-manual-v2.json` | Wangera, két hőmérséklet-variáns (94.0 °C / 94.5 °C), időalapú |
| `wangera-scale-v1.json` / `wangera-scale-v2.json` | Wangera, ugyanaz a két variáns, scale-alapú — a `-v1`/`-v2` sorszám a manual és a scale oldalon ugyanazt a variánst jelöli |
| `honduras-las-calaveras-scale.json` | Honduras Las Calaveras — csak scale profil létezik, nincs manual változat |

**Szabályok:**
- Ha egy kávénak csak egy manual és egy scale profilja van, nincs sorszám a néven.
- Ha egy kávénak csak az egyik típusból (manual vagy scale) van profilja, a másik egyszerűen hiányzik — nincs placeholder fájl.
- A `-v1`, `-v2`, ... sorszám kizárólag akkor jelenik meg, ha ugyanabból a típusból (manual vagy scale) több variáns is létezik ugyanabban a könyvtárban.
- Egy meglévő manual profilt új scale verzió hozzáadásakor nem törlünk (a `kirinyaga/` mappa a kivétel, ahol a régi, külön megtartott alap-variáns explicit kérésre lett eltávolítva).

---

## PNG grafikonok

A `tools/render_profiles.py` script generálja őket a JSON fájlokból. A PNG neve mindig a JSON nevéből képződik:

```
{json-fájlnév-kiterjesztés-nélkül}-profile.png
```

**Példák:**

| JSON | Generált PNG |
|---|---|
| `kirinyaga-manual.json` | `kirinyaga-manual-profile.png` |
| `kirinyaga-scale.json` | `kirinyaga-scale-profile.png` |
| `wangera-manual-v1.json` | `wangera-manual-v1-profile.png` |
| `wangera-scale-v2.json` | `wangera-scale-v2-profile.png` |

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

## Összefoglalás

| Fájltípus | Névképzés alapja | Minta |
|---|---|---|
| **Könyvtár** | kávé neve | `burundi-mubuga/` |
| **JSON (V1)** | kávé azonosító + `-manual` (+ `-vN` több variánsnál) | `burundi-mubuga-manual.json` |
| **JSON (V2)** | kávé azonosító + `-scale` (+ `-vN` több variánsnál) | `burundi-mubuga-scale.json` |
| **PNG** | JSON neve + `-profile` | `burundi-mubuga-manual-profile.png` |
| **Recept MD** | könyvtárnév + `-recipe` | `burundi-mubuga-recipe.md` |
| **Changelog MD** | könyvtárnév + `-changelog` | `burundi-mubuga-changelog.md` |

**Általános szabályok minden fájlnévre:**
- csak kisbetű
- szavak és elemek között kötőjel (`-`)
- ékezet, szóköz, pont (kivéve kiterjesztés), speciális karakter nincs
- minden fájlnév egyedi a teljes repository-ban
