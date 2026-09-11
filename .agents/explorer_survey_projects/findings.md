# Environment, User Git Rules & Active Projects Survey Report

**Explorer Agent:** Environment & Projects Explorer  
**Date:** 2026-09-11  
**Working Directory:** `D:\obsidian file\.agents\explorer_survey_projects`  
**Reference Assignment:** `DISPATCH.md` & `ORIGINAL_REQUEST.md`

---

## 1. Executive Summary

This investigation conducted a comprehensive survey across the local system environment, user Git rules, 5 active project profiles, and Obsidian knowledge graph integrity validation mechanisms.

Key findings:
1. **Toolchain Ready**: Node.js is confirmed at **v22.23.2** (npm 10.9.8), Python at **v3.12.10**, Windows PowerShell at **v5.1.26100.9444**, and Git at **v2.54.0.windows.1**. Obsidian runs as an Electron desktop runtime installed at `D:\obsidian me\Obsidian.exe`.
2. **User Git Rule Enforcement**: `RULE[user_global]` is verbatim codified in `C:\Users\dilmu\.gemini\config\AGENTS.md` and `D:\obsidian file\30 Resources\Agent Skills\git-workflow.md`. User GitHub identity is configured as `dilmurodmuhsinjanov910-byte` (`dilmurodmuhsinjanov910@gmail.com`). Active repositories (e.g. `DOCTOR A`) strictly follow automated branching (`feature/doctor-a-med-clinic-website`) and descriptive commit conventions.
3. **All 5 Active Projects Located & Profiled**:
   - **MobCreatorWebApp**: React 19 + Three.js / React Three Fiber (`@react-three/fiber`) 3D Minecraft mob/skeleton segment builder in `C:\Users\dilmu\.gemini\antigravity\scratch\MobCreatorWebApp`.
   - **NagoyaCastle / Osaka Castle**: Minecraft Japanese Castle world save extraction pipeline and world map assets in `C:\Users\dilmu\.gemini\antigravity\scratch\NagoyaCastle` (`Osaka Castle` NBT/region chunks and Python scraper `download_osaka.py`).
   - **The_AI_Pipeline**: 30-day automated AI production engine comprising 60 video scripts (30 English, 30 Uzbek) in `C:\Users\dilmu\.gemini\antigravity\scratch\The_AI_Pipeline`, linked to YouTube rendering scripts in `D:\youtube chennel 1\work_45min`.
   - **Orol Shahar** (*Orol → Shahar → Qirollik*): Monorepo economic simulation and city-builder game (Express 5, Prisma 7, PostgreSQL, React 19, R3F, WebSocket, Redis) in `C:\Users\dilmu\OneDrive\Desktop\game23v1`. V1-P1 and V1-P2 verified, V1-P3 in progress.
   - **Medical Clinic** (*Doctor A Med Clinic*): Production healthcare web platform in `C:\Users\dilmu\OneDrive\Desktop\DOCTOR A` (Next.js 16, Tailwind CSS v4, Prisma 5, SQLite, Material "Clinical Precision" design system). Active git repository on GitHub.
4. **Programmatic Wikilink & Markdown Validation Engine**: Built and verified dual automated validators (Python `validate_vault.py` and Node.js v22 `validate_vault.mjs`) requiring zero external dependencies. Current vault baseline: 21 markdown files, 24 links, 15 broken links (mostly due to folder links like `[[10 Projects/]]` lacking index files), and 0 syntax errors.

---

## 2. Local Software Toolchain & Environment Matrix

### 2.1 Toolchain Inventory

| Tool / Runtime | Version | Executable / Installation Path | Notes & Configuration |
| :--- | :--- | :--- | :--- |
| **Node.js** | `v22.23.2` | `C:\Users\dilmu\AppData\Local\hermes\node\node.exe` | Exact match for required Node.js v22 target. |
| **NPM** | `10.9.8` | `C:\Users\dilmu\AppData\Local\hermes\node\npm.cmd` | Global root: `C:\Users\dilmu\AppData\Local\hermes\node`. Corepack `0.34.6` enabled. |
| **Global NPM Packages** | `omniroute@3.8.50`, `ruflo@3.38.23` | Global node_modules | Routing / automation utilities. |
| **PowerShell** | `5.1.26100.9444` | `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` | PSEdition: `Desktop`. PowerShell 7 (`pwsh`) is not on system PATH; scripts should be compatible with PS 5.1. |
| **Python** | `3.12.10` | `C:\Users\dilmu\AppData\Local\Programs\Python\Python312\python.exe` | Standard CPython 64-bit; includes `requests`, `beautifulsoup4`, `re`, `os`, `sys`. |
| **Electron** | Desktop App Runtime | `D:\obsidian me\Obsidian.exe` (`app.asar.unpacked`) | Obsidian runs as Electron client; Antigravity also incorporates an Electron framework (`D:\Antigravity\resources\app`). |
| **Git** | `2.54.0.windows.1` | `C:\Program Files\Git\cmd\git.exe` | Windows Git with cmd wrapper and bash utilities. |

### 2.2 Shell & Script Execution Considerations
- When invoking PowerShell commands with string arguments containing backslashes or double quotes, inner quotes must be handled carefully or scripts should be written as `.ps1` files to prevent parameter truncation.
- Python scripts run seamlessly via `python <script.py>`. Standard library modules should be preferred to avoid PyYAML or third-party dependency failures.
- Node.js ESM modules (`.mjs`) execute directly on Node v22 via `node <script.mjs>`.

---

## 3. User Global Git Workflow Rules (`RULE[user_global]`)

### 3.1 Verbatim Specification
The user's global custom agent rules are defined as follows:

```markdown
<RULE[user_global]>
# Custom Agent Rules

## Git and GitHub Workflow
- **Default to Git**: Always use Git and GitHub when working on any project.
- **Automatic Lifecycle Operations**: Perform Git commands automatically during development without requiring the user to type them:
  - **Initialization**: Run `git init` automatically if the folder is not already a Git repository.
  - **Status & Tracking**: Run `git status` to inspect changed files, and `git add .` to stage them.
  - **Commits**: Make incremental commits with descriptive messages using `git commit -m "Descriptive commit message"`.
  - **Syncing**: Run `git pull` to fetch latest changes before editing, and `git push` to upload completed work to GitHub.
- **Automatic Branching for Major Changes**: When implementing significant features, bug fixes, refactoring, or any major changes, automatically create a new Git branch with a descriptive name (e.g., `feature/description` or `fix/description`) instead of working directly on `main` or `master`.
</RULE[user_global]>
```

### 3.2 System Configuration & Provenance
- **Agent Config File**: `C:\Users\dilmu\.gemini\config\AGENTS.md` contains the verbatim rule text above.
- **Vault Reference Note**: `D:\obsidian file\30 Resources\Agent Skills\git-workflow.md` provides an Uzbek-language mirror for vault documentation.
- **User GitHub Identity**:
  - GitHub User: `dilmurodmuhsinjanov910-byte`
  - GitHub Email: `dilmurodmuhsinjanov910@gmail.com`
- **Obsidian Git Plugin Context**: Mentioned in `Antigravity Chat History.md` (lines 283–285) as an automated hourly/daily backup method for the vault.

### 3.3 Proven Implementation Evidence (Doctor A Project)
Inspection of `C:\Users\dilmu\OneDrive\Desktop\DOCTOR A` confirms strict compliance in practice:
- Remote: `origin https://github.com/dilmurodmuhsinjanov910-byte/doctoramedclinic..git`
- Current Branch: `feature/doctor-a-med-clinic-website`
- Commit Log Samples:
  - `fd0c6dc Design: Maximize glassmorphism styling across navbar, cards, table, and modal inputs`
  - `ba016d8 Design: Implement UI/UX maximalism with ambient blurs, stats strip, and glassmorphic glow-cards`
  - `929aa28 Feat: Refactor visual branding to premium theme and implement modal editing in Admin Console`

---

## 4. Comprehensive Active Project Profiles

### Profile 1: MobCreatorWebApp

| Field | Detail |
| :--- | :--- |
| **Project Name** | MobCreatorWebApp |
| **Absolute Path** | `C:\Users\dilmu\.gemini\antigravity\scratch\MobCreatorWebApp` |
| **Domain & Purpose** | Web-based 3D Minecraft Mob & Creature Generator / Modeler |
| **Tech Stack** | React 19 (`19.2.6`), Three.js (`^0.184.0`), React Three Fiber (`@react-three/fiber` `^9.6.1`), React Three Drei (`@react-three/drei` `^10.7.7`), Vite (`^8.0.12`), Lucide React (`^1.18.0`), ESLint 10 |
| **Architecture** | Component-based 3D viewport (`SkeletonViewer`, `Canvas`, `OrbitControls`, `Grid`, `Environment`). Implements parametric multi-segment geometry generator (`addSegment`, `addBox`) calculating hierarchical pivot points, body blocks, dorsal fins, lateral ridges, belly plates, and side nubs for aquatic/mythical mobs (e.g. Leviathan). |
| **Current State** | Functional 3D canvas viewer in `src/App.jsx`, standard Vite build pipeline, node_modules installed. |
| **Git Status** | No `.git` repository initialized. Candidate for `git init` per `RULE[user_global]`. |
| **Next Steps** | Add UI controls for customizing mob segment dimensions, color palettes, and exporting to Minecraft Bedrock/Java geometry JSON format. |

---

### Profile 2: NagoyaCastle / Osaka Castle

| Field | Detail |
| :--- | :--- |
| **Project Name** | NagoyaCastle / Osaka Castle |
| **Absolute Path** | `C:\Users\dilmu\.gemini\antigravity\scratch\NagoyaCastle` |
| **Related Assets** | `C:\Users\dilmu\.gemini\antigravity\scratch\download_osaka.py`<br>`C:\Users\dilmu\.gemini\antigravity\scratch\Osaka_Castle.rar`<br>`D:\.minecraft\xaero\world-map\orolcha` |
| **Domain & Purpose** | Minecraft Historical Japanese Architecture asset ingestion and world-mapping pipeline. |
| **Tech Stack** | Python 3 (BeautifulSoup4, Requests, Regex downloader), Minecraft World Engine (Anvil format, `level.dat`, `region/*.mca`, `DIM-1`, `DIM1`, `datapacks`, `playerdata`, `poi`, `stats`). |
| **Architecture** | Automated scraper/downloader script (`download_osaka.py`) extracts direct MediaFire download links, downloads archive (`Osaka_Castle.rar`), extracts complete Minecraft world directory (`Osaka Castle`). |
| **Current State** | Map successfully downloaded and unpacked. Full world directory verified with `level.dat` (4,280 bytes), chunk region files, and icon. |
| **Git Status** | No `.git` repository. Local scratch asset workspace. |
| **Next Steps** | Integration into Minecraft server or export of 3D schematic structures (litematica/schematic) into web/R3F viewers. |

---

### Profile 3: The_AI_Pipeline

| Field | Detail |
| :--- | :--- |
| **Project Name** | The_AI_Pipeline |
| **Absolute Path** | `C:\Users\dilmu\.gemini\antigravity\scratch\The_AI_Pipeline` |
| **Related Media Engine** | `D:\youtube chennel 1\work_45min` |
| **Domain & Purpose** | 30-Day Master Video Course & Automated AI Media Engineering Pipeline. |
| **Tech Stack** | Python 3, Markdown, FFmpeg / Media Automation scripts (`analyze.py`, `render.py`, `render_numbered.py`, `verify.py`), YouTube Data API workflows. |
| **Architecture** | 60 comprehensive video production scripts divided into two language tracks: <br>• **English Scripts (`English_Scripts/VID_001` to `VID_030`)**<br>• **Uzbek Scripts (`Uzbek_Scripts/VID_001` to `VID_030`)**<br>Topics: AI Workflow fundamentals, Make.com/n8n automation, Python + Gemini API, secure key management, steganography, rate limit fallbacks, JSON structured prompting, AI agents, OAuth vs Service Accounts, Computer Vision room scanning, NotebookLM automation, automated YouTube uploads, horizontal/vertical scaling, cloud pricing, cron deployment, and pipeline monetization. |
| **Production Execution** | Actively executed in `D:\youtube chennel 1\work_45min` with seamless 45-minute audio looping (`audio_loop.wav`), audio/video seam checks (`seam_check_*.log`), video rendering (`vidyo2_musik2_45min.mp4`, `vidyo3_musik3_45min.mp4`), and JSON validation logs. |
| **Git Status** | Unversioned scratch script repository. |
| **Next Steps** | Auto-publishing scripts via YouTube API and connecting scripts with Obsidian video production notes. |

---

### Profile 4: Orol Shahar ("Orol → Shahar → Qirollik")

| Field | Detail |
| :--- | :--- |
| **Project Name** | Orol Shahar (orol-game) |
| **Absolute Path** | `C:\Users\dilmu\OneDrive\Desktop\game23v1` |
| **Backup Copies** | `C:\Users\dilmu\OneDrive\Desktop\orol-shahar-qirollik-loyiha.zip`<br>`C:\Users\dilmu\Downloads\Telegram Desktop\Orol_Shahar_Qirollik...` |
| **Domain & Purpose** | Browser-based economic simulation and city-building strategy game ("Island → City → Kingdom"). |
| **Tech Stack** | Monorepo structure (`backend`, `frontend`, `packages/contracts`).<br>• **Backend**: Express 5.2.1, Prisma 7.10.0, PostgreSQL (with `@embedded-postgres/windows-x64` 17 for zero-install local database), Redis (`ioredis` 5.8.2), WebSocket (`ws` 8.21.3), Node-cron, Nodemailer, Zod, Ajv.<br>• **Frontend**: React 19.2.8, React Three Fiber (R3F), Tailwind CSS, Vite, Playwright (`@playwright/test` 1.56.1), Vitest 5.0.0.<br>• **Engine Constraint**: Node `>=24 <25`. |
| **Architecture** | Modular decoupled game architecture: <br>1. **Core Gameplay Loop**: 4 production branches (wheat, timber, stone, iron), gather, build, upgrade, workers, population food balance.<br>2. **State & Ledger Engine**: Integer resource math, atomic transactions, idempotency keys, outbox pattern, 24-hour offline cap.<br>3. **Marketplace Engine**: 8 initial resource prices, 15-second quote lifecycle, floor/ceiling bounds, atomic settlement, WebSocket price broadcast.<br>4. **Worker Subsystem**: Independent background minute-tick worker.<br>5. **Admin Subsystem**: Analytics dashboard, UTC DAU/D1/D7 retention calculation, settings GET/PATCH, feedback collector. |
| **Current Milestones** | • Documentation v0.3 finalized (26 design gap closures O01–O26 in `loyiha/`).<br>• V1-P1 (Core game loop, buildings, workers, auth, ticks) completed and verified.<br>• V1-P2 (Marketplace, dynamic pricing, atomic transactions, WS) completed and verified.<br>• V1-P3 (5-step contextual guide, admin analytics dashboard, settings, retry idempotency) implemented locally.<br>• Roadmap: V2 planned for Treasury, Solana/web3 chain, NFT, seasonal economy; V3 planned for Kingdom expansion. |
| **Git Status** | Initialized locally without remote; verified via automated test suites (`scripts/test.mjs`, Playwright e2e). Candidate for remote repository creation on GitHub. |

---

### Profile 5: Medical Clinic ("Doctor A Med Clinic")

| Field | Detail |
| :--- | :--- |
| **Project Name** | Doctor A Med Clinic (`doctor-a-med-clinic-app`) |
| **Absolute Path** | `C:\Users\dilmu\OneDrive\Desktop\DOCTOR A` |
| **Subdirectories** | `doctor-a-med-clinic-app` (Full-stack Next.js app)<br>`stitch_doctor_a_med_clinic_website` (UI design tokens and prototypes) |
| **Domain & Purpose** | Premium multidisciplinary healthcare clinic portal and patient appointment booking platform. |
| **Tech Stack** | Next.js 16 (`16.2.11`), React 19 (`19.2.4`), Tailwind CSS v4 (`^4`), Prisma 5 (`^5.22.0`), SQLite (`prisma/dev.db`), TypeScript 5, Lucide React (`^1.26.0`), ESLint 9. |
| **Architecture & Design** | • **Design System**: "Clinical Precision" Material/Stitch tokens (`surface: #f8f9ff`, `on-surface: #0b1c30`, `clinical-red: #FF0000`, `deep-navy: #121521`, Rubik typography).<br>• **UI Features**: Maximalist glassmorphism, ambient blurs, stats strip, interactive glow-cards, doctor roster, online appointment queue reservation, service directory.<br>• **Backend**: Prisma ORM over SQLite dev database with automated seed script (`prisma/seed.js`).<br>• **Localization**: Multilingual dictionary structure in `src/locales/`. |
| **Git Status** | **Fully active Git repository**: <br>• Remote: `https://github.com/dilmurodmuhsinjanov910-byte/doctoramedclinic..git`<br>• Active Branch: `feature/doctor-a-med-clinic-website`<br>• Working Tree: Clean, commits verified. |

---

## 5. Programmatic Validation of Obsidian Wikilinks & Markdown Syntax

### 5.1 Obsidian Wikilink Resolution Rules & Vault Quirks
Obsidian resolves wikilinks using specific internal logic:
1. **Shortest Path Matching**: `[[Note Name]]` resolves to any `Note Name.md` in the vault if unique. If ambiguous, relative path takes precedence.
2. **Path Links**: `[[Folder/Subfolder/Note Name]]` matches vault-relative paths. Forward slashes `/` are strictly required; Windows backslashes `\` cause broken links inside Obsidian.
3. **Heading Anchors**: `[[Note Name#Section Heading]]` or `[[#Internal Heading]]`.
4. **Block Anchors**: `[[Note Name#^block-id]]`.
5. **Aliases**: `[[Target Note|Display Label]]`.
6. **Embeds**: `![[Target Note]]` or `![[image.png]]`.
7. **Folder Links Quirk**: A link to a folder (such as `[[10 Projects/]]` or `[[00 Inbox/]]`) **does NOT resolve** to a clickable note in Obsidian unless an actual note with that name exists (e.g. `10 Projects/10 Projects.md` or `10 Projects/Projects.md`).

### 5.2 Standalone Automated Validators Created
To ensure 100% testable integrity, two zero-external-dependency validators were created in this directory:

1. **Python Validator (`validate_vault.py`)**:
   - Location: `D:\obsidian file\.agents\explorer_survey_projects\validate_vault.py`
   - Uses Python 3.12 standard library (`os`, `re`, `sys`).
   - Validates frontmatter syntax, code fence parity, and all `[[...]]` links.
   - Run command: `python "D:\obsidian file\.agents\explorer_survey_projects\validate_vault.py"`

2. **Node.js v22 ESM Validator (`validate_vault.mjs`)**:
   - Location: `D:\obsidian file\.agents\explorer_survey_projects\validate_vault.mjs`
   - Uses Node.js v22 standard library (`fs`, `path`).
   - Run command: `node "D:\obsidian file\.agents\explorer_survey_projects\validate_vault.mjs"`

### 5.3 Baseline Scan Findings of Current Vault
Running both validators on `D:\obsidian file` produced identical baseline results:
- **Total Markdown Files Scanned**: 21
- **Total Wikilinks Checked**: 24
- **Syntax Errors Found**: 0 (all code fences and YAML frontmatter blocks are syntactically valid)
- **Broken Wikilinks Found in Pre-existing Files**: 15
  - `Dashboard.md:11` -> `[[00 Inbox/]]` (folder without note)
  - `Dashboard.md:12` -> `[[10 Projects/]]` (folder without note)
  - `Dashboard.md:13` -> `[[20 Areas/]]` (folder without note)
  - `Dashboard.md:14` -> `[[30 Resources/]]` (folder without note)
  - `Dashboard.md:15` -> `[[40 Archives/]]` (folder without note)
  - `50 Templates/Project Template.md:6` -> `[[20 Areas/]]` (folder link)
  - `Antigravity Chat History.md:105, 111` -> `[[Linklar]]`, `[[Qayd nomi]]` (dialogue examples)
  - `30 Resources/Agent Skills/obsidian-bases.md:44` -> `[[Vazifalar.base]]` (sample reference)
  - `30 Resources/Agent Skills/obsidian-markdown.md:17, 18, 19, 34, 35` -> documentation examples
  - `DILMUROD/Welcome.md:3` -> `[[create a link]]` (intro tutorial link)

### 5.4 Implementation Guidance for Downstream Agents
1. When creating the Universal AI Second Brain (`AI Sozlangan Miyyasi.md`) and populating `10 Projects`, `20 Areas`, `30 Resources`, etc., every referenced wikilink must resolve to a valid `.md` file.
2. For folder categories, create Map of Content (MOC) index notes:
   - `00 Inbox/00 Inbox.md` (or `Inbox MOC.md`)
   - `10 Projects/10 Projects.md` (or `Projects MOC.md`)
   - `20 Areas/20 Areas.md` (or `Areas MOC.md`)
   - `30 Resources/30 Resources.md` (or `Resources MOC.md`)
   - `40 Archives/40 Archives.md` (or `Archives MOC.md`)
3. Prior to final sign-off, run `python "D:\obsidian file\.agents\explorer_survey_projects\validate_vault.py"` or `node "D:\obsidian file\.agents\explorer_survey_projects\validate_vault.mjs"` to guarantee zero broken links in newly generated files.
