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
- **Visual style**: dark theme — dark charcoal page (`#1a1d24`), dark cards (`#24272e`), forest green (`#2d6a4f`) primary accent, Roboto Condensed font, all cards have a subtle green artistic border with corner accent marks
- **Everything is click-to-edit**: all stats, scores, names, descriptions, table cells, etc.
- **Add/delete on all lists**: spells, inventory items, attacks, features, limited-use abilities, spell slot levels, senses, weapons, proficiency tags, conditions
- **Interactive pips**: spell slots, limited-use, death saves all toggle on click; pip +/− controls on spell slots and limited-use rows
- **HP bar** changes color by health: green (≥66%), yellow (33–65%), red (<33%)
- **Conditions tracker**: type a condition and click Add; conditions appear as removable pills
- **Proficiencies & Training**: add new tags, remove existing ones with ×

### What still needs work on the frontend
- **All data is still hardcoded** for a placeholder Warlock character — needs to become a blank/editable sheet (Phase 2)
- Mobile layout could use more polish
- Changes are not persisted — refreshing the page resets everything (Phase 3 backend will fix this)

### Frontend stack
- Pure HTML + CSS + vanilla JavaScript (no frameworks, no build tools)
- Everything in one `index.html` file
- Google Fonts (Roboto + Roboto Condensed) via CDN

---

## The Roadmap (What Comes Next)

### Phase 1 — Polish the frontend + make it editable (mostly complete)
Core editing is done. Remaining Phase 1 items:
- **Transition to a blank character sheet** — replace all hardcoded Warlock placeholder data with empty fields
- Improve **mobile responsiveness**
- General visual polish as Andy gives feedback

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

## GitHub — Setup (Already Done)

Andy's GitHub username is **Brumshack**.

The repository is live at: **https://github.com/Brumshack/dnd-character-sheet**

GitHub Pages (public URL for the sheet): **https://brumshack.github.io/dnd-character-sheet**
(Enable in repo Settings → Pages → Branch: master, if not already on)

Git is configured globally on Andy's machine:
- `user.name` = Brumshack
- `user.email` = andybrumlow@gmail.com
- GitHub CLI (`gh`) is installed and authenticated

**Everything is set up — no further configuration needed.**

---

## Git Workflow

**Only commit and push when Andy explicitly asks.** Do NOT auto-commit or auto-push after edits — running git commands uses tokens each time, and Andy prefers to decide when changes go to GitHub.

When Andy asks to push (e.g., "push this", "commit and push", "save to GitHub"), run:

```bash
cd "/c/Users/abrum/OneDrive/Documents/D&D/Character Webiste Project"
git add .
git commit -m "descriptive message about what changed"
git push
```

**Rules for commit messages:**
- Be specific: `"Add clickable HP tracker"` not `"update"`
- Present tense: `"Add..."`, `"Fix..."`, `"Update..."`, `"Remove..."`
- Examples:
  - `"Add interactive spell slot pips"`
  - `"Fix skills list alignment"`
  - `"Update CLAUDE.md with Phase 2 roadmap"`
  - `"Convert sheet to blank editable character template"`

---

## How to Run the Project

Right now everything is just a file — no server needed:
- **Open the site**: Double-click `index.html` in File Explorer, or run `start index.html` in PowerShell
- **Edit the site**: Open `index.html` in VS Code (or any text editor), save, then refresh the browser

For the backend (when we get there):
- `modal deploy modal_app.py` — deploy to Modal
- `modal run modal_app.py` — test locally

---

## Screenshot & Refinement Loop (Puppeteer)

Claude can take screenshots of `index.html` automatically — no need for Andy to manually screenshot and paste. This enables a full self-directed edit → screenshot → review → fix loop.

### Setup (already done)
- Node.js is installed on Andy's machine
- Puppeteer is installed: `npm install puppeteer` (run once in the project folder)
- `screenshot.js` is in the project root (excluded from git via `.gitignore`)

### How to take a screenshot
```bash
cd "/c/Users/abrum/OneDrive/Documents/D&D/Character Webiste Project"
node screenshot.js
```
This saves `screenshot.png` in the project folder. Claude can then read it with the `Read` tool (it supports images).

### The refinement loop
When doing visual work on `index.html`:
1. Make a set of edits
2. Run `node screenshot.js`
3. Read `screenshot.png` and also read `D&D Beyond Screenshot.png` for comparison
4. Identify specific differences (spacing, font size, color, layout)
5. Fix them
6. Repeat from step 2
7. Only check in with Andy when the result looks good, or when a design decision needs his input

**Do at least 3 screenshot rounds per session before presenting results.** Don't stop after one pass.

### screenshot.js contents (for reference / recreation if needed)
```js
const puppeteer = require('puppeteer');
const path = require('path');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900 });
  const filePath = 'file:///' + path.resolve(__dirname, 'index.html').replace(/\\/g, '/');
  await page.goto(filePath, { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 1500));
  await page.screenshot({ path: 'screenshot.png', fullPage: true });
  await browser.close();
  console.log('Screenshot saved.');
})();
```

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
6. **Only commit and push when Andy explicitly asks** (see Git workflow above)

---

## Design Rules (Don't Break These)

- **All cards** must have the green artistic border: `border: 1px solid rgba(45,106,79,0.45)` + corner accent pseudo-elements
- **Color**: `--red: #2d6a4f` is the primary accent (forest green — the variable is named `--red` for historical reasons, don't rename it). `--neg: #e05252` is used for actual red things (damage dice, negative modifiers).
- **Font**: Roboto Condensed for labels/headings, Roboto for body text
- **Background**: dark theme — `--page: #1a1d24` (page), `--bg: #24272e` (cards)
- **Text**: `--g900: #e8ecf0` (primary), `--g600: #8d93a0` (secondary/muted)
- Keep everything in a single `index.html` until Phase 2 when we split into data + template
