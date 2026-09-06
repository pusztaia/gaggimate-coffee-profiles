# Gaggimate Barista

AI espresso coach powered by [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and [Gaggimate](https://gaggimate.com/) hardware integration.

<img width="2816" height="1536" alt="Gemini_Generated_Image_p2rojwp2rojwp2ro" src="https://github.com/user-attachments/assets/ae48eed2-c88a-49ae-8580-a8bf3fa2e148" />


## What It Does

- **Researches new coffees** — identifies origin, variety, processing, and roast characteristics to recommend starting extraction parameters
- **Creates extraction profiles** — designs pressure/flow curves tailored to each bean and uploads them directly to your machine
- **Analyzes shot telemetry** — correlates pressure, flow, and temperature data with your taste feedback to diagnose issues
- **Learns from your results** — maintains a grind map and per-coffee tasting journal that improve recommendations over time

## How It Works

Gaggimate Barista is a Claude Code project — not a standalone app, but a structured set of instructions, knowledge files, and skills that turn Claude into a specialized espresso dialing assistant.

- **Claude Code** is the agent runtime. It reads the project's `CLAUDE.md` for its instructions, uses skills for specialized workflows, and calls tools to interact with your machine.
- **Knowledge files** provide espresso expertise — extraction science, pressure theory, tasting diagnosis, profile design — organized in hot/cold storage so the agent loads only what's needed.
- **MCP tools** (included in `mcp/`, based on [gaggimate-mcp](https://github.com/julianleopold/gaggimate-mcp) by Julian Leopold) give Claude direct access to your Gaggimate hardware: uploading profiles, pulling shot telemetry, and reading extraction data.
- **Dynamic data files** evolve with use: `grind-map.md` tracks successful settings, `coffees/` stores per-bean research and tasting notes, and `user-setup.md` holds your equipment and preferences.

## Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) (requires Anthropic API key or Claude Pro/Max subscription)
- A [Gaggimate](https://gaggimate.com/)-equipped espresso machine (Gaggia Classic Pro, Gaggia Classic Evo, or Rancilio Silvia)
- [`uv`](https://docs.astral.sh/uv/) (Python package manager, for the MCP server)

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/gaggimate-barista.git
cd gaggimate-barista
```

### 2. Set up personal data

Your equipment profile, grind map, and coffee notes live outside this repo. Choose one path:

**Without a private repo** (quickest start, data stays local):
```bash
cp user-setup.example.md user-setup.md
mkdir -p coffees
cp grind-map.example.md grind-map.md
```
Then edit `user-setup.md` with your equipment details. Note: data files (`coffees/`, `grind-map.md`, `user-setup.md`) are stored locally and won't carry over to a new machine. Use the private repo path if you want persistence across machines.

**With a private repo** (recommended — data syncs across machines, history is preserved):
```bash
bin/setup-data-repo.sh /absolute/path/to/gaggimate-barista-data
```
The script creates symlinks for `coffees/`, `grind-map.md`, and `user-setup.md`, and configures `GAGGIMATE_STORAGE_PATH` in `mcp/.env` to point to your private repo's `mcp-data/` directory. If `GAGGIMATE_STORAGE_PATH` is misconfigured, shot ratings and profile data are silently lost — the setup script handles this automatically. See [Data Architecture](#data-architecture) for details.

### 3. Install the MCP server

```bash
uv sync --directory mcp
```

### 4. Configure the MCP server

Create `.mcp.json` in the project root (gitignored). Replace the two paths with your actual locations (`which uv` and `pwd`):

```json
{
  "mcpServers": {
    "gaggimate": {
      "type": "stdio",
      "command": "/absolute/path/to/uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/gaggimate-barista/mcp",
        "mcp",
        "run",
        "src/gaggimate_mcp/server.py"
      ]
    }
  }
}
```

### 5. Configure Claude Code permissions

Create `.claude/settings.local.json` (gitignored):

```json
{
  "permissions": {
    "allow": [
      "mcp__gaggimate__list_recent_shots",
      "mcp__gaggimate__analyze_shot",
      "mcp__gaggimate__manage_profile"
    ]
  },
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": [
    "gaggimate"
  ]
}
```

This pre-approves the Gaggimate MCP tools so Claude can read shots and manage profiles without prompting each time.

### 6. Start dialing

```bash
claude
```

Tell the agent about your coffee, or use `/new-coffee` to start the research workflow.

## Project Structure

```
gaggimate-barista/
├── CLAUDE.md                  # Agent instructions and workflow definitions
├── user-setup.md              # → symlink to private repo (your equipment + active coffee)
├── user-setup.example.md      # Example template for new users
├── grind-map.md               # → symlink to private repo (successful grind settings)
├── grind-map.example.md       # Example template for new users
├── bin/
│   └── setup-data-repo.sh     # Wires private data repo via symlinks
│
├── mcp/                       # Gaggimate MCP server (Python)
│   ├── src/gaggimate_mcp/     # Server source code
│   └── tests/                 # Test suite
│
├── coffees/                   # → symlink to private repo (per-coffee data)
│   └── roaster-coffee-name/
│       ├── README.md          # Bean research, profiles table, tasting journal
│       └── *.json             # Extraction profiles for this coffee
│
├── knowledge/                 # Espresso expertise (hot storage)
│   ├── ESPRESSO_BREWING_BASICS.md
│   ├── PRESSURE_GUIDE.md
│   ├── EXTRACTION_SCIENCE.md
│   ├── ESPRESSO_TASTING_GUIDE.md
│   ├── GAGGIMATE_PROFILE_CREATION_GUIDE.md
│   ├── PROFILE_LIBRARY.md
│   ├── BEAN_FRESHNESS_AND_STORAGE.md
│   ├── SPECIAL_CATEGORIES.md
│   ├── MILK_AND_DRINKS.md
│   ├── BASKETS.md
│   ├── grinders/              # Grinder-specific guides
│   │   └── SETTE_270.md
│   ├── automatic-pro/         # Gaggimate Automatic Pro firmware profiles
│   └── reference/             # Deep reference files (cold storage)
│       ├── EXTRACTION_SCIENCE_REFERENCE.md
│       ├── PROFILE_CREATION_REFERENCE.md
│       ├── PRESSURE_REFERENCE.md
│       └── ...                # 11 deep-dive reference files
│
└── .claude/
    └── skills/                # Slash command workflows
        ├── new-coffee/        # /new-coffee — research and starting parameters
        ├── gaggimate-profiles/# /gaggimate-profiles — profile design and upload
        └── diagnose/          # /diagnose — shot telemetry analysis
```

## Workflows

### `/new-coffee` — Research a new bag

Share a photo of your bag or describe the coffee. The agent researches origin, variety, processing, and roast level, then recommends starting grind, temperature, ratio, and profile. Creates a coffee directory with research notes and uploads a profile to your machine.

### `/gaggimate-profiles` — Design extraction profiles

Build custom pressure/flow profiles for your coffee. The agent walks through pre-infusion style, pressure targets, transitions, and stop conditions, then generates valid JSON and uploads it to your Gaggimate.

### `/diagnose` — Analyze shot telemetry

After a shot, the agent pulls telemetry data from your machine and correlates pressure curves, flow rates, and temperature stability with your taste feedback to pinpoint extraction issues.

### The core loop

Pull a shot, tell the agent how it tasted (rating, balance, observations), and get specific adjustments for the next shot. The agent records everything — successful settings go to `grind-map.md`, all shots go to the coffee's tasting journal.

## Data Architecture

Personal data (`coffees/`, `grind-map.md`, `user-setup.md`) is stored in a separate private repo and linked into this repo via symlinks. This keeps the public repo free of personal data while allowing it to function as a reusable template.

The MCP server's storage path (`GAGGIMATE_STORAGE_PATH` in `mcp/.env`) points to `{private-repo}/mcp-data/` for shot ratings and profile persistence. `bin/setup-data-repo.sh` configures everything automatically.

### Keeping up with upstream

If you set up this project from the template, you can pull in future improvements:

```bash
git remote add upstream https://github.com/charlie-hall/gaggimate-barista.git
git fetch upstream
git merge upstream/main
```

## Customization

This project is designed to be used as a template (click "Use this template" on GitHub) and adapted:

- **Different grinder** — Replace `knowledge/grinders/SETTE_270.md` with a guide for your grinder. Update `user-setup.md` with your model.
- **Different basket size** — Update `user-setup.md`. Profile volumetric targets auto-scale based on your dose.
- **Different machine** — The knowledge base is machine-agnostic. The MCP server handles hardware specifics. Any Gaggimate-equipped machine works.
- **Different preferences** — Edit `user-setup.md` with your drink preferences, flavor interests, and roast tendencies. The agent adapts its recommendations accordingly.
- **Add knowledge** — Drop new `.md` files into `knowledge/` for topics the agent should know about. Reference them in `CLAUDE.md`.

## Knowledge Architecture

Knowledge files use a **hot/cold storage** pattern:

- **Hot storage** (`knowledge/*.md`) — Concise quick-reference files loaded during active dialing. Contain the tables, decision trees, and parameters the agent needs for routine recommendations.
- **Cold storage** (`knowledge/reference/*.md`) — Deep-dive reference files loaded on demand. Cover theory, science, edge cases, and detailed explanations for when you want to go deeper.

This keeps the agent's context window focused on what matters for the current task while preserving access to comprehensive reference material.
