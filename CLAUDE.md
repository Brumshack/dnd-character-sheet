# D&D Character Sheet — Project Briefing for Claude
*Read this at the start of every session before doing anything.*

---

## Who I'm Working With

**Andy** is a complete beginner to coding — this is his first project. He has no prior experience with HTML, CSS, JavaScript, Python, or any backend technologies. Explain concepts in plain English. Never assume he knows what a term means. Keep instructions simple and paste-ready. He learns best by seeing results in the browser.

---

## What We're Building

A fully interactive D&D 5e character sheet website — think D&D Beyond, but built for Andy's whole crew. The goal is a **blank, universal character sheet** that anyone in the group can open and fill in with their own character. It is NOT built around one specific character.

Any player should be able to:
- Open the sheet and enter their own character's info
- View and edit stats, spells, inventory, and features
- Track HP, spell slots, and limited-use abilities
- Eventually save and load their character data (backend, Phase 3)
- Access it from any device at the table

**Reference**: The D&D Beyond character sheet screenshot (`D&D Beyond Screenshot.png`) in this folder is the visual target.

**Andy's character** (used only as placeholder/test data during development): Raylock Flystone — Wood Elf Ranger, Level 15. Use this when you need realistic sample data to populate the sheet during development, but the sheet itself must work for any character, any class, any level.

---

## Current State of the Project (as of April 2026)

### What exists right now
- `index.html` — a single-file character sheet, no external dependencies except Google Fonts
- `modal_app.py` — a Modal backend stub (not deployed yet, not connected to the frontend)
- `.env.example` — template for environment variables

### What the frontend (`index.html`) currently has
- **Header**: character name, class, race, level, XP, and stat boxes (proficiency, initiative, AC, speed, HP, passive perception)
- **HP bar**: visual health tracker
- **Left column**: ability scores with modifiers and saving throw dots
- **Second column**: saving throws and full skills list with proficiency dots
- **Main tabbed area** (single box, tabs switch content):
  - **Actions** → sub-tabs: All, Attack, Action, Bonus Action, Reaction, Other, Limited Use
  - **Spells** → sub-tabs: All, Cantrips, 3rd Level, Ritual, Concentration + **live search bar**
  - **Inventory** → sub-tabs: All, Equipment, Backpack, Component Pouch, Attunement, Other Possessions + **live search bar**
  - **Features & Traits** → sub-tabs: All, Class Features, Species & Traits, Feats
  - **Background** → sub-tabs: Characteristics, Appearance
  - **Notes** → sub-tabs: All, Organizations, Allies, Enemies, Backstory, Other
  - **Extras** → Special senses, resistances
- **Right sidebar**: Conditions, Proficiencies & Training, Senses, Death Saves
- **Visual style**: white/light background, red (#C53131) accent color from D&D Beyond's actual CSS, Roboto Condensed font, all cards have a subtle red artistic border with corner accent marks

### What still needs work on the frontend
- **All data is still hardcoded** for a placeholder Warlock character — needs to become a blank/editable sheet
- HP, spell slots, and limited-use pips are not yet interactive/clickable (just visual)
- No way to edit any values yet — everything needs to be click-to-edit or have an edit mode
- Death save pips are not clickable
- Mobile layout could use more polish
- Conditions section is empty — no way to add/remove conditions yet
- Character name, class, race, level, XP, ability scores, etc. all need to be user-editable fields

### Frontend stack
- Pure HTML + CSS + vanilla JavaScript (no frameworks, no build tools)
- Everything in one `index.html` file
- Google Fonts (Roboto + Roboto Condensed) via CDN

---

## The Roadmap (What Comes Next)

### Phase 1 — Polish the frontend + make it editable (current phase)
Continue iterating on `index.html`. Andy will share browser screenshots; refine the design based on feedback. Key things still to improve:
- **Transition to a blank character sheet** — replace all hardcoded Raylock data with empty/placeholder fields
- Make HP, spell slots, death saves, and limited-use pips **clickable and interactive** (JavaScript)
- Add **click-to-edit** for all character values (name, scores, HP, etc.) — click a field, type a new value, click away to save
- Improve **mobile responsiveness**
- Add **conditions tracker** (click to add/remove conditions like Poisoned, Stunned, etc.)
- General visual polish to get closer to D&D Beyond

### Phase 2 — Multiple characters + JSON data
- Move character data out of hardcoded HTML into a JavaScript object or JSON file
- Build a character selector so Andy can switch between characters
- This is the bridge between Phase 1 and Phase 3

### Phase 3 — Backend (Modal + database)
- Build Modal API endpoints to save/load character data
- Use a simple database (likely SQLite or a hosted option like Supabase)
- Connect the frontend to the backend via fetch() calls
- Add authentication so only Andy can edit his characters
- `modal_app.py` is the starting point — it already has the auth token pattern

### Phase 4 — GitHub + hosting
- Push the project to a GitHub repository (Andy has a GitHub account but is new to git)
- Host the frontend on GitHub Pages (free, instant, no server needed)
- Eventually point a custom domain at it

---

## GitHub — What Andy Needs to Know

Andy's GitHub username is **Brumshack**. He has an account but is new to git. When the time comes, explain it like this:

**GitHub** is like Google Drive for code. A **repository (repo)** is a folder that GitHub tracks — every change you make is saved with a description of what changed, so you can always go back. **Pushing** just means uploading your latest changes from your computer to GitHub.

**Steps when we're ready**:
1. Install Git: https://git-scm.com/download/win
2. In PowerShell: `git init` → `git add .` → `git commit -m "first commit"`
3. Create a new repo on github.com (no README, no .gitignore)
4. Follow GitHub's instructions to push: `git remote add origin <url>` → `git push -u origin main`
5. For hosting: go to repo Settings → Pages → Source: main branch → Save

Always walk Andy through each command one at a time. Don't give him a wall of commands to paste at once.

---

## How to Run the Project

Right now everything is just a file — no server needed:
- **Open the site**: Double-click `index.html` in File Explorer, or run `start index.html` in PowerShell
- **Edit the site**: Open `index.html` in VS Code (or any text editor), save, then refresh the browser

For the backend (when we get there):
- `modal deploy modal_app.py` — deploy to Modal
- `modal run modal_app.py` — test locally

---

## Modal / Backend Setup (Not Active Yet)

Modal secrets are already configured:
- `anthropic-api-key` → `ANTHROPIC_API_KEY`
- `api-auth-token` → `API_AUTH_TOKEN`

The `modal_app.py` file has a `character_stats` endpoint stub that calculates ability modifiers, saving throws, and skills from raw ability scores. It's not connected to the frontend yet.

---

## Session Workflow (How to Start Each Session)

1. Read this file
2. Read `index.html` to remind yourself of the current code state
3. Ask Andy: *"What would you like to work on today?"*
4. Build → show result → iterate based on his screenshot feedback
5. Update this CLAUDE.md if anything significant changes (new features added, phase completed, etc.)

---

## Design Rules (Don't Break These)

- **All cards** must have the red artistic border: `border: 1px solid rgba(197,49,49,0.45)` + corner accent pseudo-elements
- **Color**: `--red: #C53131` is the primary accent. Don't change it.
- **Font**: Roboto Condensed for labels/headings, Roboto for body text
- **Background**: white (`#FEFEFE`) main content, light grey (`#f4f5f5`) page background
- **No dark theme** — the target is D&D Beyond's light mode
- Keep everything in a single `index.html` until Phase 2 when we split into data + template
