# Project: Universal AI Second Brain ("AI Sozlangan Miyyasi")

## Architecture
The Universal AI Second Brain unifies all AI assistants (Antigravity 1, Antigravity 2, Codex/LLM, and external agents) into a single, cohesive, fault-tolerant knowledge and operational base inside the Obsidian vault at `D:\obsidian file`.

```
                        [Master Brain Entrypoint]
                       (AI Sozlangan Miyyasi.md)
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
   [20 Areas]                [10 Projects]             [30 Resources]
 Agent Profiles           Active Project Memory         Agent Skills Hub
 • Antigravity 1          • MobCreatorWebApp           • git-workflow.md
 • Antigravity 2          • NagoyaCastle               • Skills Dashboard
 • Codex / LLM Assistant  • The_AI_Pipeline            • Obsidian Skills
 • Concurrency & Sync     • Orol Shahar Qirollik
                          • Doctor A Med Clinic
                                   │
                        [50 Templates & MOCs]
                 Daily, Project, Resource Templates
                   00 Inbox, 10, 20, 30, 40 MOCs
```

## Feature Inventory
Every feature from the Survey phase appears here with its assigned milestone. No feature is left unassigned.

| # | Feature | Description | Milestone | Source |
|---|---|---|---|---|
| 1 | Master Brain Entrypoint | `AI Sozlangan Miyyasi.md` at vault root with YAML frontmatter, universal startup directive, user persona, and PARA index | M1 | Survey (Vault, Spec Miner) |
| 2 | Verbatim Git Workflow Enforcer | Verbatim inclusion and enforcement of `RULE[user_global]` (`git init`, `git status`, `git add .`, incremental commits, `git pull`/`push`, feature branching) | M1 | Survey (Projects Explorer) |
| 3 | Local Software Toolchain Index | Exact documentation of local tool binaries (Node.js v22, Python 3.12, PowerShell 5.1, Git 2.54, Electron) | M1 | Survey (Projects Explorer) |
| 4 | Dashboard.md Alignment | Update and align `Dashboard.md` with master brain entrypoint and valid MOC links | M1 | Survey (Vault Explorer) |
| 5 | Antigravity 1 Agent Profile | Dedicated profile in `20 Areas/Agent Profiles/Antigravity 1.md` (Primary Google session, Chief Vault Architect, interactive planner) | M2 | Survey (Spec Miner, Vault) |
| 6 | Antigravity 2 Agent Profile | Dedicated profile in `20 Areas/Agent Profiles/Antigravity 2.md` (Secondary isolated session, sandbox tester, clean-room builder) | M2 | Survey (Spec Miner, Vault) |
| 7 | Codex / LLM Assistants Profile | Dedicated profile in `20 Areas/Agent Profiles/Codex LLM Assistant.md` (`opencode.ps1`, `codex.exe`, CLI automation, `.data/agents/` logs) | M2 | Survey (Spec Miner) |
| 8 | Concurrency & Conflict Protocol | Dedicated protocol in `20 Areas/Agent Profiles/Concurrency & Sync Protocol.md` (Lockfile `.agents/locks/<hash>.lock`, 300s TTL, atomic write-rename) | M2 | Survey (Spec Miner) |
| 9 | Gemini Topics 10 Communication Styles | Formal engine specification & contextual greetings for all 10 styles (Check-in, Celebration, Reflection, Callback, Continue, Anticipation, Nudge, Curiosity, Empathy, Low-pressure) | M3 | Survey (Spec Miner) |
| 10 | Suggested Next Steps Engine | Action-verb requirement, ~75 character limit (60-85 chars), 2-4 curated options, AI-actionable, temporal relevance | M3 | Survey (Spec Miner) |
| 11 | Emoji-tagged Topic Memory Blocks | 5 blank lines visual separation preceding markdown code block with emoji-tagged sections, zero horizontal scroll, zero information loss | M3 | Survey (Spec Miner) |
| 12 | Goals & Decisions Log (ADR) | Append-only architectural decision records (context, decision, alternatives, status, agent) | M3 | Survey (Spec Miner) |
| 13 | MobCreatorWebApp Profile | Project note in `10 Projects/MobCreatorWebApp.md` (React 19, Three.js, R3F, procedural box modeler, disk path, topic memory block) | M3 | Survey (Projects Explorer) |
| 14 | NagoyaCastle / Osaka Castle Profile | Project note in `10 Projects/NagoyaCastle.md` (Minecraft Anvil chunks, region/mca, Python mediafire pipeline, topic memory block) | M3 | Survey (Projects Explorer) |
| 15 | The_AI_Pipeline Profile | Project note in `10 Projects/The_AI_Pipeline.md` (60 scripts UZ/EN, Gemini API, YouTube audio/video rendering, topic memory block) | M3 | Survey (Projects Explorer) |
| 16 | Orol Shahar Profile | Project note in `10 Projects/Orol Shahar Qirollik.md` (Express 5, Prisma 7, PostgreSQL, React 19, R3F, milestones V1-P1/P2/P3, topic memory block) | M3 | Survey (Projects Explorer) |
| 17 | Doctor A Med Clinic Profile | Project note in `10 Projects/Doctor A Med Clinic.md` (Next.js 16, Tailwind CSS v4, Prisma 5, SQLite, Material Clinical Precision, topic memory block) | M3 | Survey (Projects Explorer) |
| 18 | PARA Maps of Content (MOCs) | Create MOC notes for `00 Inbox/00 Inbox.md`, `10 Projects/10 Projects.md`, `20 Areas/20 Areas.md`, `30 Resources/30 Resources.md`, `40 Archives/40 Archives.md` | M4 | Survey (Vault, Projects) |
| 19 | Agent Skills Hub Integration | Connect `30 Resources/Agent Skills/` (`Skills Dashboard.md`, `Skills Database.base`, 6 Obsidian skills, `git-workflow.md`) to Master Brain | M4 | Survey (Vault Explorer) |
| 20 | Template Infrastructure Integration | Cross-link `50 Templates/Daily Note Template.md`, `Project Template.md`, `Resource Template.md` with Master Brain and MOCs | M4 | Survey (Vault Explorer) |
| 21 | E2E Testing Suite (Tiers 1-4) | Comprehensive opaque-box test suite covering feature tests, boundary/corner tests, cross-feature combinations, and real-world workflows | M5 (Phase 1) | Test Track |
| 22 | Wikilink & Markdown Syntax Validation | Programmatic validation confirming 0 broken wikilinks and 100% valid Markdown syntax across the entire vault | M5 (Phase 1) | Survey (Projects Explorer) |
| 23 | Adversarial Coverage Hardening (Tier 5) | White-box adversarial probing by Challenger to detect edge cases, gaps, and race conditions | M5 (Phase 2) | Hardening Track |
| 24 | Forensic Integrity Audit | Mandatory independent audit verifying genuine implementation, zero dummy/facade data, zero hardcoded cheat results | M5 (Final) | Audit Enforcement |

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| M1 | Master Brain Core & Rules Engine | `AI Sozlangan Miyyasi.md`, `Dashboard.md`, Verbatim Git rules (`RULE[user_global]`), Toolchain matrix | Survey complete | DONE |
| M2 | Universal AI Agent Profiles & Concurrency | `20 Areas/Agent Profiles/` (`Antigravity 1.md`, `Antigravity 2.md`, `Codex LLM Assistant.md`, `Concurrency & Sync Protocol.md`) | M1 | DONE |
| M3 | Gemini Topics Memory & Active Projects | `10 Projects/` (5 project profiles with Topic Memory Blocks, 10 communication styles, ~75-char action-verb next steps, ADR logs) | M1, M2 | DONE |
| M4 | Obsidian PARA MOCs & Skills Hub Integration | MOCs for 00, 10, 20, 30, 40; cross-linking `30 Resources/Agent Skills` and `50 Templates` | M1, M2, M3 | DONE |
| M5 | E2E Verification & Adversarial Hardening | Phase 1: Pass 100% of E2E test suite (Tiers 1-4) & 0 broken wikilinks. Phase 2: Adversarial Tier 5 hardening. Forensic Integrity Audit. | M1, M2, M3, M4 | DONE |

## Interface Contracts

### Master Brain ↔ Agent Profiles (`AI Sozlangan Miyyasi.md` ↔ `20 Areas/Agent Profiles/`)
- Master brain indexes agent profiles table: `[[Antigravity 1]]`, `[[Antigravity 2]]`, `[[Codex LLM Assistant]]`, `[[Concurrency & Sync Protocol]]`.
- Agent profiles cite exact binary paths, role descriptions, lockfile paths (`.agents/locks/<hash>.lock`), and atomic write rules.

### Master Brain ↔ Active Projects (`AI Sozlangan Miyyasi.md` ↔ `10 Projects/`)
- Master brain indexes project portfolio: `[[MobCreatorWebApp]]`, `[[NagoyaCastle]]`, `[[The_AI_Pipeline]]`, `[[Orol Shahar Qirollik]]`, `[[Doctor A Med Clinic]]`.
- Each project note adheres strictly to the Gemini Topics architecture:
  1. `📋 Latest State Summary` (1-2 sentences, 30-50 words)
  2. `💡 Goals & Decisions Log (ADR)`
  3. `💬 Interaction Dynamics` (10 styles with contextual anchors)
  4. `🎯 Suggested Next Steps` (2-4 items, action-verb first, 60-85 chars)
  5. 5 blank lines
  6. Topic Memory Block (markdown code block with emoji tags)

### MOCs ↔ Vault Graph (`PARA MOCs` ↔ Sub-notes)
- Every folder link in existing notes (e.g. `[[10 Projects/]]`) must resolve to a valid MOC note `[[10 Projects/10 Projects|10 Projects]]` or folder MOC.
- Every note has YAML frontmatter: `tags`, `type`, `date`, `updated`, `status`.

## Code Layout
- Root:
  - `D:\obsidian file\AI Sozlangan Miyyasi.md` (Master Entrypoint)
  - `D:\obsidian file\Dashboard.md` (Updated Dashboard MOC)
- Folder 10 Projects:
  - `D:\obsidian file\10 Projects\10 Projects.md` (Projects MOC)
  - `D:\obsidian file\10 Projects\MobCreatorWebApp.md`
  - `D:\obsidian file\10 Projects\NagoyaCastle.md`
  - `D:\obsidian file\10 Projects\The_AI_Pipeline.md`
  - `D:\obsidian file\10 Projects\Orol Shahar Qirollik.md`
  - `D:\obsidian file\10 Projects\Doctor A Med Clinic.md`
- Folder 20 Areas:
  - `D:\obsidian file\20 Areas\20 Areas.md` (Areas MOC)
  - `D:\obsidian file\20 Areas\Agent Profiles\Antigravity 1.md`
  - `D:\obsidian file\20 Areas\Agent Profiles\Antigravity 2.md`
  - `D:\obsidian file\20 Areas\Agent Profiles\Codex LLM Assistant.md`
  - `D:\obsidian file\20 Areas\Agent Profiles\Concurrency & Sync Protocol.md`
- Folder 30 Resources:
  - `D:\obsidian file\30 Resources\30 Resources.md` (Resources MOC)
  - `D:\obsidian file\30 Resources\Agent Skills\Skills Dashboard.md`
- Folder 40 Archives:
  - `D:\obsidian file\40 Archives\40 Archives.md` (Archives MOC)
- Folder 00 Inbox:
  - `D:\obsidian file\00 Inbox\00 Inbox.md` (Inbox MOC)
- Testing & Audit Scripts:
  - `D:\obsidian file\.agents\explorer_survey_projects\validate_vault.py`
  - `D:\obsidian file\.agents\explorer_survey_projects\validate_vault.mjs`
  - `D:\obsidian file\.agents\test_track\e2e_runner.py`
