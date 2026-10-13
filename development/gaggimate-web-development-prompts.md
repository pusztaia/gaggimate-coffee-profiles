# GaggiMate Coffee Profiles – fejlesztési promptok fázisonként

Ez a dokumentum egymásra épülő promptokat tartalmaz a  
**https://pusztaia.github.io/gaggimate-coffee-profiles/** oldal továbbfejlesztéséhez.

A cél nem egyszerű vizuális redesign, hanem a jelenlegi profilgyűjtemény fokozatos átalakítása egy:

**Coffee → Recipe → Profile → Brew → Taste → Adjust**

logikájú, mobilbarát **GaggiMate Coffee Profile Manager + Dial-in Assistant** alkalmazássá.

---

## Általános szabályok minden fázishoz

Ezt a blokkot érdemes minden prompt elejére bemásolni.

```text
You are a senior frontend engineer and product designer working on the
GaggiMate Coffee Profiles project.

Project: This folder

Main goals:
- Preserve all currently working profiles and downloads.
- Do not break existing GitHub Pages deployment.
- Prefer static-site-compatible solutions.
- Prefer HTML, CSS and vanilla JavaScript unless a framework is clearly justified.
- Avoid unnecessary dependencies.
- Keep the site usable without a backend.
- Mobile-first design is mandatory.
- The coffee and brew workflow is more important than exposing filenames.
- Existing JSON profile files remain the source of truth for GaggiMate profiles.
- Generated HTML should not contain coffee-specific duplicated data when that data
  can be loaded from structured metadata.
- Keep accessibility, responsive layout, semantic HTML and performance in mind.
- Do not remove functionality without replacing it.
- Do not rename or modify existing GaggiMate JSON schema fields unless required.
- Before changing code, inspect the current repository structure and reuse existing
  utilities where reasonable.
- Target GaggiMate firmware v1.9.0+ for any new profile-field support (e.g. the
  `phases[].transition.target` enum: `time` | `volumetric` | `pumped`, added in
  v1.9.0). Check `schema/profile.json` for the current canonical field list before
  assuming a field exists or is missing.

UX principle:
Coffee → Recipe → Profile → Brew → Taste → Adjust

When implementing:
1. First inspect the existing implementation.
2. Explain the proposed change briefly.
3. Make the smallest coherent set of changes.
4. Preserve backward compatibility where practical.
5. Validate desktop and mobile layouts.
6. List changed files.
7. Mention any migration step if one is needed.
```

---

# Phase 0 – Repository audit and target architecture

## Goal

Before redesigning anything, understand the current repository, duplicated logic,
profile metadata, generated files and dependencies.

## Prompt

```text
Audit the current GaggiMate Coffee Profiles repository before making architectural
changes.

Repository/site:
this folder

Your task is to inspect the project and produce a concrete technical redesign plan.

Analyze:

1. Repository structure
   - root files
   - profiles directory
   - per-coffee folders
   - JSON profiles
   - recipe Markdown files
   - changelog Markdown files
   - generated PNG charts
   - catalog/index metadata
   - JavaScript utilities
   - build/generation scripts

2. Current data flow
   - where coffee names come from
   - where recipe parameters come from
   - where profile descriptions come from
   - where images and graphs come from
   - how profile cards are generated
   - how links are constructed
   - how mobile navigation works

3. Duplication
   Identify information duplicated between:
   - HTML
   - recipe.md
   - catalog.json
   - profile JSON
   - generated images
   - JavaScript

4. Technical debt
   Identify:
   - hardcoded paths
   - duplicated HTML
   - fragile relative URLs
   - mobile layout issues
   - inconsistent profile naming
   - data fields that are missing for a richer coffee catalog
   - content that should move to structured metadata

5. Target architecture

Propose a static GitHub Pages architecture using approximately:

profiles/
  coffee-slug/
    coffee.json
    profile-*.json
    recipe.md
    changelog.md

assets/
js/
css/

The exact structure may differ if the existing repository suggests a better
backward-compatible solution.

6. Define a proposed coffee metadata schema.

At minimum consider:

{
  "id": "",
  "name": "",
  "roaster": "",
  "origin": "",
  "region": "",
  "producer": "",
  "variety": [],
  "process": "",
  "roast": "",
  "taste": [],
  "status": "",
  "recommendedProfile": "",
  "recipe": {
    "dose": null,
    "yield": null,
    "ratio": null,
    "temperature": null,
    "grind": "",
    "rpm": null,
    "targetTime": null
  }
}

Only add fields that have a clear purpose.

7. Migration strategy

Provide a safe phased migration plan so the existing GitHub Pages site keeps working
throughout the transition.

Do not perform a full redesign yet.

Output:
- architecture assessment
- recommended data model
- migration plan
- prioritized technical debt list
- proposed file structure
- files that should be changed in Phase 1
```

---

# Phase 1 – New homepage and coffee-first catalog

## Goal

Transform the homepage from a technical list of profile files into a coffee-first
catalog.

## Prompt

```text
Implement Phase 1 of the GaggiMate Coffee Profiles redesign.

Objective:
Turn the homepage into a modern, mobile-first coffee profile catalog.

The primary entity shown to the user must be the coffee, not the JSON filename.

Create a responsive card-based catalog.

Each coffee card should show, when data is available:

- coffee name
- roaster
- origin
- process
- roast level
- key tasting notes
- dose
- beverage yield
- brew ratio
- temperature
- target shot time
- grinder setting
- grinder RPM
- Bluetooth scale support
- dialed-in / experimental status

Primary actions:

[View profile]
[Download JSON]

If multiple profile variants exist for one coffee, do not create visually duplicated
coffee cards by default. Show one coffee card with available variants inside the
detail view or a compact variant selector.

Design direction:

- modern
- clean
- technical but not developer-centric
- suitable for use beside an espresso machine
- strong typography
- compact but readable cards
- excellent mobile layout
- clear visual hierarchy
- avoid decorative complexity

Navigation:

Profiles
Coffees
Dial-in
Knowledge
Equipment

Only make a navigation item active if a corresponding page actually exists.
Do not create dead links.

Add a search field:

"Search coffee..."

Search should match at least:
- coffee name
- roaster
- country/origin
- tasting notes

Preserve existing working links and profile downloads.

Do not expose long JSON filenames as the primary visible labels.

Implementation requirements:

- GitHub Pages compatible
- no backend
- vanilla JavaScript preferred
- accessible controls
- responsive from approximately 360 px upward
- no horizontal scrolling
- loading and empty states
- graceful behavior if metadata is missing

Deliver:
- implementation
- changed files
- short explanation of the new data flow
- any metadata migration required
```

---

# Phase 2 – Search, filters and sorting

## Goal

Make the growing profile library easy to browse.

## Prompt

```text
Implement advanced discovery for the GaggiMate Coffee Profiles catalog.

Build on the existing Phase 1 coffee-first homepage.

Add client-side search, filters and sorting.

Filters:

Origin
- dynamically generated from available metadata

Process
Examples:
- Washed
- Natural
- Honey
- Anaerobic
- Experimental

Roast
- Light
- Light-medium
- Medium
- Medium-dark
- Dark

Taste
Generate from available tasting tags, for example:
- Fruity
- Floral
- Citrus
- Berry
- Sweet
- Chocolate
- Nutty
- Spicy

Profile style, if reliably derivable:
- Bloom
- Lever
- Classic
- Turbo
- Filter-like
- Adaptive

Scale support:
- Bluetooth scale
- Manual stop

Status:
- Dialed in
- Experimental
- Archived

Sorting:
- Coffee name
- Origin
- Roast
- Recently updated
- Recommended

Requirements:

- Filters must be generated from actual catalog metadata.
- Do not hardcode options that cannot occur.
- Active filters must be clearly visible.
- Add "Clear filters".
- Search and filters must work together.
- The URL should preferably preserve filter state using query parameters or hash
  state so filtered views can be shared.
- Browser back/forward navigation should behave sensibly.
- Mobile filter controls should not dominate the screen.
- Ensure keyboard accessibility.

Add a results summary, for example:

"12 coffees · 4 filters active"

Do not add external search services or backend dependencies.

Deliver:
- implementation
- modified files
- explanation of filtering architecture
- examples of shareable filtered URLs
```

---

# Phase 3 – Coffee / profile detail page redesign

## Goal

Turn each coffee page into a real brew dashboard.

## Prompt

```text
Redesign the individual coffee/profile page into a GaggiMate brew dashboard.

The page should be coffee-centric.

Example visual hierarchy:

Burundi Mubuga

Melon · Blackcurrant · Floral

Natural · Light-medium · Burundi

Recommended recipe

18.5 g → 42.5 g
1:2.30
93 °C
38 s

DF64V
Grind 8
1200 RPM

The page should contain these sections:

1. Coffee overview
   - coffee name
   - roaster
   - origin
   - region if available
   - producer if available
   - process
   - roast
   - variety
   - tasting notes

2. Recommended recipe
   - dose
   - target yield
   - ratio
   - temperature
   - target shot time
   - grinder setting
   - RPM
   - scale stop target if relevant

3. Profile
   - selected profile name
   - version
   - profile type
   - description
   - Bluetooth-scale indicator
   - current/recommended marker

4. Actions
   [Download JSON]
   [Send to GaggiMate] – placeholder or disabled until Phase 5 if required
   [Brew mode]

5. Interactive profile graph
   Implemented in Phase 4 if not yet available.

6. Recipe
   Render recipe Markdown cleanly inside the page instead of forcing the user to
   leave the profile context.

7. Changelog / version history
   Render as a secondary section, collapsed by default on mobile.

8. Advanced section
   Put developer-oriented information here:
   - source JSON filename
   - raw metadata
   - file paths
   - schema/debug information

Requirements:

- filenames must not dominate the UI
- responsive layout
- excellent mobile readability
- preserve direct JSON download
- preserve recipe/changelog content
- use semantic headings
- avoid duplicating data manually in HTML

If coffee data or recipe values are not available, hide the specific field rather
than showing misleading default values.

Deliver the complete implementation and list all changed files.
```

---

# Phase 4 – Interactive profile chart

## Goal

Replace or supplement static PNG graphs with an interactive chart generated from
the actual profile JSON.

## Prompt

```text
Implement an interactive GaggiMate profile visualization.

Do not use a static PNG as the main graph.

The graph must be derived directly from the profile JSON so it cannot drift from
the actual downloadable profile.

Visualize all data that can be reliably derived, such as:

- pressure target
- flow target
- temperature target
- expected or stop weight, when meaningful
- phase boundaries
- time
- ramp/transition shape at the start of each phase, including whether the ramp is
  driven by time, measured volume, or pumped volume (`transition.target`,
  firmware v1.9.0+) rather than assuming every ramp is time-based

Provide toggles:

[x] Pressure
[x] Flow
[ ] Temperature
[x] Weight

Hover/touch inspection should show information such as:

18.2 s
Phase: Extraction
Pressure: 7.8 bar
Flow: 2.4 ml/s
Weight: 10.8 g

Only show values that can genuinely be calculated from the profile.
Do not invent weight curves if the JSON does not contain enough information.

Clearly mark phases:

Wetting
Saturation
Bloom
Extraction
Finish

Use the actual phase names from the profile where possible.

Requirements:

- desktop mouse support
- mobile touch support
- responsive width
- no horizontal overflow
- readable axes
- sensible units
- accessible fallback text/table
- graceful handling of malformed or incomplete profiles
- keep the chart library lightweight

If the project already has chart generation logic, reuse or extract it instead of
creating a second incompatible profile parser.

The same profile parsing logic should become reusable for:
- profile detail
- compare mode
- future Brew Mode

Deliver:
- implementation
- parser architecture
- changed files
- supported profile constructs
- known limitations
```

---

# Phase 5 – Send to GaggiMate

## Goal

Allow profile installation directly from the website to a GaggiMate device on the
user's local network.

## Prompt

```text
Implement a "Send to GaggiMate" workflow for the profile detail page.

Context:
The GitHub Pages site is public/static, while GaggiMate is available on the user's
local network.

The browser running the website may have network access to the GaggiMate device.

UI:

[Send to GaggiMate]

Open a dialog:

GaggiMate address

[ http://gaggimate.local ]

[Test connection]

If successful, show useful device information only if the GaggiMate API actually
exposes it.

Then:

[Install profile]

Requirements:

1. Inspect current GaggiMate documentation/source and determine the supported API
   or upload endpoint for profile import. Re-check this against the firmware version
   actually running on the target device (surfaced via the API/websocket status if
   available) — e.g. firmware v1.9.0 added a `wp` (water pumped) field to the
   WebSocketHandler status response and gear-pump / positive-displacement-pump
   tuning parameters, which may affect what device info is available or how a
   profile validates on upload.

2. Do not invent an API.

3. If the connected device reports a firmware version older than what a profile
   field requires (e.g. `transition.target` needs v1.9.0+), warn the user instead
   of silently uploading a profile the device may not fully support.

4. If browser security, CORS, HTTPS mixed-content rules or GaggiMate firmware
   prevent direct upload, explain the limitation in the UI and implement the best
   technically valid fallback.

5. Store the preferred GaggiMate address locally in the browser, not on a server.

6. Validate the JSON profile before sending.

7. Show clear states:
   - testing
   - connected
   - connection failed
   - uploading
   - installed
   - rejected

8. Never silently overwrite an existing profile without user awareness.

9. Keep normal "Download JSON" available as fallback.

10. Support IP addresses as well as local hostnames.

Example flow:

Send to GaggiMate
↓
192.168.50.xx
↓
Test connection
↓
Connected
↓
Install profile
↓
Profile installed

Security:
- no cloud proxy
- no profile or device data uploaded to third-party services
- no credentials persisted unless absolutely necessary

Deliver:
- implementation
- verified API assumptions
- browser limitations
- fallback behavior
- changed files
```

---

# Phase 6 – Brew Mode

## Goal

Create a simplified mobile view for use beside the espresso machine.

## Prompt

```text
Implement Brew Mode for GaggiMate Coffee Profiles.

The purpose is to show only the information needed while preparing and brewing
the selected coffee.

Brew Mode must be optimized for a phone beside the espresso machine.

Example:

BURUNDI MUBUGA

18.5 g
↓
42.5 g

1:2.30

93 °C

DF64V
8 @ 1200 RPM

Expected profile

0–5 s    Wetting
5–13 s   Saturation
13–17 s  Bloom
17–34 s  Extraction
34–38 s  Finish

[Open profile graph]

Requirements:

- very large essential values
- no developer metadata
- minimal scrolling
- high contrast
- readable at arm's length
- portrait-first
- landscape should still work
- keep screen awake if a safe browser API exists and permission is available
- never require login
- offer exit back to full profile page

Optional:
Allow a user to check preparation steps locally:

[ ] Basket dry
[ ] 18.5 g dose
[ ] WDT
[ ] Tamp
[ ] Puck screen
[ ] Scale connected

Do not turn this into a complicated task manager.

Use existing metadata and profile parsing rather than duplicating recipe data.

Deliver:
- implementation
- changed files
- mobile UX notes
```

---

# Phase 7 – Profile comparison

## Goal

Make profile development and version comparison easier.

## Prompt

```text
Implement Profile Compare mode.

Users should be able to compare:
- two different profiles
- two versions of the same coffee profile
- optionally two coffee-specific profiles

UI example:

Compare

Profile A:
Burundi Mubuga Fruity v4

Profile B:
Burundi Mubuga Fruity v3

Display:

1. Overlay graph
   - pressure
   - flow
   - temperature where applicable
   - phase boundaries

2. Parameter comparison table

Include useful metrics that can be reliably derived, such as:

- dose
- target yield
- ratio
- temperature
- total target duration
- preinfusion duration
- bloom duration
- peak pressure
- average or peak flow if meaningful
- stop weight
- scale support
- safety timeout

3. Phase-level diff

Example:

Saturation
v3: 2.5 bar / 8 s
v4: 2.3 bar / 8 s

Finish
v3: 2.1 ml/s
v4: 1.8 ml/s

Transition (if `transition.target` differs between versions)
v3: time-based ramp
v4: volumetric-based ramp

4. Human-readable summary

Example:

"v4 reduces finish flow and stops the pump earlier."

Only generate such summaries from actual detected differences.
Do not infer taste impact as fact.

Requirements:

- reuse the Phase 4 profile parser
- mobile-compatible comparison
- clear legend
- identical units
- highlight meaningful differences
- support shareable compare URLs if practical

Deliver:
- implementation
- changed files
- comparison logic description
```

---

# Phase 8 – Version history and changelog integration

## Goal

Turn multiple profile versions into a coherent history instead of exposing them as
unrelated files.

## Prompt

```text
Implement structured profile version history.

For each coffee, detect or define profile versions and variants.

Example:

Burundi Mubuga

Current: v4

v4 — Current
- lower finish flow
- earlier scale stop

v3
- higher temperature test

v2
- first Bluetooth-scale version

Requirements:

- derive version ordering from structured metadata where possible
- do not rely only on filename lexical sorting
- identify the recommended/current profile explicitly
- preserve older JSON downloads
- allow:
  [View]
  [Download]
  [Compare with current]

Integrate existing changelog.md content.

If the changelog format is currently too free-form for reliable parsing:
- keep rendering the Markdown
- introduce optional structured version metadata
- do not destroy existing changelog content

The user should understand which profile to brew without reading filenames.

Deliver:
- implementation
- metadata additions
- changed files
- migration of existing versions where practical
```

---

# Phase 9 – Taste feedback and dial-in assistant

## Goal

Add local taste logging and rule-based recommendations.

## Prompt

```text
Implement a first version of a Taste Feedback / Dial-in Assistant.

This phase must remain deterministic and explainable.
Do not add a generic AI chatbot.

After a shot, allow local feedback:

Acidity:
- too sour
- bright
- balanced
- muted

Bitterness:
- low
- balanced
- high

Sweetness:
- low
- medium
- high

Body:
- tea-like
- medium
- syrupy

Dryness / astringency:
- none
- slight
- high

Dominant flavor tags:
- fruit
- floral
- citrus
- berry
- chocolate
- nutty
- spice
- roast

Optional shot observations:
- channeling
- spraying
- unstable stream
- early flow
- slow start

Then provide a conservative suggested next adjustment.

Possible adjustable variables:
- grind
- yield
- temperature
- dose
- peak pressure
- flow
- preinfusion
- bloom

Important rules:

- Prefer one or at most two changes per recommendation.
- Distinguish strong evidence from heuristic suggestions.
- Never claim a taste result is guaranteed.
- Explain why each adjustment is proposed.
- Do not automatically modify the production JSON profile.
- Offer suggested settings separately.

Example:

Observed:
Slightly sour + thin

Suggested next test:
Yield: 42.5 g → 44.0 g

Reason:
A slightly longer ratio may increase extraction without changing puck preparation.

Keep all tasting history in browser-local storage for this phase.

Create the dial-in logic as a reusable module so it can later be replaced or
enhanced by the project's profile-engine / Barista Optimizer logic.

Deliver:
- UI
- rule engine
- explanation of the rules
- local persistence
- changed files
```

---

# Phase 10 – Shot history

## Goal

Build a useful local history of real brews.

## Prompt

```text
Implement local Shot History.

A shot belongs to a coffee and profile version.

Record:

- date/time
- coffee
- profile
- profile version
- dose
- yield
- ratio
- temperature
- grinder setting
- RPM
- shot duration
- optional pump-stop weight
- optional final cup weight
- taste feedback
- rating
- notes

Allow:

- add shot
- edit shot
- delete shot
- mark best shot
- duplicate settings for next shot

Coffee page should show:

Recent shots

#14
18.5 → 43.0 g
38.2 s
93 °C
★★★★☆

Best shot

#13
Grind 7.8
18.5 → 43 g
39 s

Requirements:

- browser-local storage only in this phase
- export history to JSON
- import exported history
- no account required
- no external service
- clearly indicate data is stored on this browser/device
- schema must include a version number for future migration

If later GLP/GaggiMate shot-log integration is possible, design the local data model
so imported machine logs can coexist with manually entered shots.

Deliver:
- implementation
- storage schema
- export/import
- changed files
```

---

# Phase 11 – Profile Finder

## Goal

Help select a reasonable starting profile for an unknown coffee.

## Prompt

```text
Implement a Profile Finder wizard.

This is not yet a full profile generator.
It should recommend a suitable existing profile archetype or existing coffee
profile as a starting point.

Inputs:

Roast
- Light
- Medium-light
- Medium
- Medium-dark
- Dark

Process
- Washed
- Natural
- Honey
- Anaerobic
- Other

Bean age
- very fresh
- rested
- older

Desired cup style
- Fruity / clarity
- Balanced
- Sweet
- Body
- Traditional espresso

Optional:
- origin
- altitude
- varietal

Output:

Recommended profile

Adaptive Bloom

Recommended starting recipe:
18.5 g → 44 g
93 °C
1:2.38

Why:
- suitable for light roast
- longer ratio favors clarity
- bloom phase supports even extraction

Alternative:
Classic 9-bar

Requirements:

- use explicit deterministic rules
- show reasoning
- do not present a percentage confidence unless there is a real scoring algorithm
- separate profile recommendation from actual coffee-specific dial-in
- do not pretend the recommendation is validated if it is heuristic

Where suitable, reuse logic from the existing profile-engine instead of creating
competing rules.

Deliver:
- wizard UI
- recommendation engine
- rule documentation
- changed files
```

---

# Phase 12 – Knowledge Base

## Goal

Turn existing documentation into a coherent in-site knowledge section.

## Prompt

```text
Build a Coffee Knowledge section from the project's existing Markdown documentation.

Do not rewrite valid technical content unnecessarily.

Information architecture:

Coffee
- Origins
- Processing
- Roast levels
- Flavor

Espresso
- Dose
- Ratio
- Grind
- Temperature
- Pressure
- Flow
- Preinfusion
- Bloom

GaggiMate
- Profile concepts
- Profile phases
- Bluetooth scale
- Brew-by-weight
- Profile import
- Troubleshooting

Equipment
- Gaggia Classic Pro / GaggiMate setup
- grinder
- basket
- puck screen
- scale

Requirements:

- Markdown-driven content
- consistent navigation
- table of contents
- readable typography
- internal linking
- mobile-friendly
- retain original technical depth
- do not duplicate the same guide into multiple files
- provide contextual links from profile pages to relevant knowledge articles

Examples:

"Why use bloom?"
"How does temperature affect a light roast?"
"How does Bluetooth scale stop work?"

Implement search within Knowledge if it can share the Phase 2 search infrastructure.

Deliver:
- implementation
- documentation structure
- changed files
```

---

# Phase 13 – PWA / offline support

## Goal

Make the site app-like on a phone beside the coffee machine.

## Prompt

```text
Turn GaggiMate Coffee Profiles into an installable Progressive Web App while
preserving normal GitHub Pages behavior.

Implement:

- web app manifest
- appropriate app name
- icons
- standalone display mode
- theme/background metadata
- service worker
- offline shell
- caching of recently viewed coffee/profile pages
- caching of recipe metadata
- caching of selected profile JSON files

Offline expectations:

Users should be able to reopen recently viewed:
- coffee pages
- recipes
- Brew Mode
- profile graphs

Do not cache aggressively in a way that prevents profile updates from appearing.

Use a sensible cache versioning strategy.

Clearly handle:
- first visit while offline
- updated profile available
- stale cache
- service worker update

Do not make local-network GaggiMate upload appear available when offline or when the
device cannot be reached.

Deliver:
- PWA implementation
- cache strategy
- update strategy
- changed files
```

---

# Phase 14 – Visual polish and accessibility pass

## Goal

Finish the UI coherently after functionality is stable.

## Prompt

```text
Perform a complete visual consistency and accessibility pass on the GaggiMate Coffee
Profiles application.

Do not redesign core workflows again.

Review:

Typography
- clear hierarchy
- readable mobile sizes
- consistent numeric presentation

Spacing
- consistent spacing scale
- cards
- sections
- dialogs

Components
- buttons
- chips
- filters
- badges
- tables
- inputs
- navigation
- chart controls

Status indicators
- current
- dialed in
- experimental
- scale-enabled
- archived

Dark mode
Implement a system-aware dark mode with an optional manual override.

Avoid a stereotypical brown coffee theme.

Prefer:
- neutral dark surfaces
- high contrast
- subtle warm accents
- technical instrument/dashboard character

Accessibility:

- WCAG-conscious contrast
- visible focus states
- keyboard navigation
- semantic labels
- touch target sizes
- reduced motion support
- proper dialog behavior
- form labels
- screen-reader-friendly chart fallback
- no information conveyed by color alone

Check common viewport widths:

360
390
430
768
1024
1440

Deliver:
- visual fixes
- accessibility fixes
- any remaining known issues
```

---

# Phase 15 – Performance, regression and release hardening

## Goal

Stabilize the application before treating the redesign as production-ready.

## Prompt

```text
Perform a release-hardening pass on GaggiMate Coffee Profiles.

Do not add new product features.

Audit:

1. Broken links
2. Missing JSON downloads
3. Missing images
4. Missing recipe/changelog files
5. Invalid metadata
6. Profile parsing failures
7. Mobile overflow
8. JavaScript console errors
9. Service-worker update issues
10. GitHub Pages path handling
11. Relative URLs when hosted below a repository path
12. Accessibility regressions
13. Performance regressions

Add automated validation where practical.

Useful checks could include:

- catalog references an existing coffee
- metadata references existing profile JSON
- every downloadable profile exists
- current/recommended version exists
- recipe links resolve
- changelog links resolve
- generated chart can parse each supported profile
- no duplicate coffee IDs
- no duplicate version identifiers within one coffee
- expected numeric fields are valid

Create or improve a build/check script that can run locally and in GitHub Actions.

A commit should fail when a critical catalog/profile reference is broken.

Also run a Lighthouse-oriented optimization pass:

- performance
- accessibility
- best practices
- PWA where relevant

Deliver:
- validation tooling
- CI integration
- fixes found during audit
- final known limitations
- release checklist
```

---

# Recommended implementation order

```text
Phase 0   Audit / architecture
Phase 1   Homepage redesign
Phase 2   Search / filters
Phase 3   Profile detail page
Phase 4   Interactive chart
Phase 8   Version history
Phase 7   Compare profiles
Phase 5   Send to GaggiMate
Phase 6   Brew Mode
Phase 9   Taste feedback
Phase 10  Shot history
Phase 11  Profile Finder
Phase 12  Knowledge Base
Phase 13  PWA
Phase 14  Visual/accessibility polish
Phase 15  Release hardening
```

This ordering intentionally moves **version history before compare mode**, because
comparison becomes cleaner once profile/version identity is structured.

---

# Recommended MVP cut

For the first major redesign release, stop after:

```text
Phase 0
Phase 1
Phase 2
Phase 3
Phase 4
Phase 8
Phase 5
Phase 6
```

That already creates a significantly better product:

**Coffee catalog → rich profile page → interactive profile → versioning → direct
GaggiMate workflow → Brew Mode**

Taste feedback, shot history and automatic profile recommendation can then be added
without forcing another architecture rewrite.

---

# Suggested product direction

The project should evolve from:

```text
Coffee → Files
```

toward:

```text
Coffee
   ↓
Recipe
   ↓
Profile
   ↓
Brew
   ↓
Taste
   ↓
Adjust
```

The JSON file remains technically important, but becomes an implementation detail
rather than the main user experience.
