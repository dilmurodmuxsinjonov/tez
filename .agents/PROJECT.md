# Project: Universal AI Second Brain ("AI Sozlangan Miyyasi")

## Architecture
The Universal AI Second Brain unifies all AI assistants (Antigravity 1, Antigravity 2, Codex/LLM, Hermes, Copilot, OpenCode, Ruflo Swarm) into a single, cohesive, fault-tolerant knowledge and operational base inside the Obsidian vault at `D:\obsidian file`.

```
                        [Master Brain Entrypoint]
                       (AI Sozlangan Miyyasi.md)
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
   [20 Areas]                [10 Projects]             [30 Resources]
 Agent Profiles           Active Project Memory         Agent Skills Hub
 • Antigravity 1          • MobCreatorWebApp           • AI Ecosystem Map
 • Antigravity 2          • NagoyaCastle               • Free LLM Models Registry
 • Codex LLM Assistant    • The_AI_Pipeline            • Codex Skills Encyclopedia
 • Nous Hermes            • Orol Shahar Qirollik       • Skills Dashboard
 • GitHub Copilot         • Doctor A Med Clinic        • git-workflow.md
 • OpenCode CLI                    │
 • Ruflo Swarm          [50 Templates & MOCs]
 • Concurrency & Sync   Daily, Project, Resource, Agent, Model, Security
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
| 9 | Gemini Topics 10 Communication Styles | Formal engine specification & contextual greetings for all 10 styles | M3 | Survey (Spec Miner) |
| 10 | Suggested Next Steps Engine | Action-verb requirement, ~75 character limit (60-85 chars), 2-4 curated options | M3 | Survey (Spec Miner) |
| 11 | Emoji-tagged Topic Memory Blocks | 5 blank lines visual separation preceding markdown code block with emoji-tagged sections | M3 | Survey (Spec Miner) |
| 12 | Goals & Decisions Log (ADR) | Append-only architectural decision records | M3 | Survey (Spec Miner) |
| 13 | MobCreatorWebApp Profile | Project note in `10 Projects/MobCreatorWebApp.md` | M3 | Survey (Projects Explorer) |
| 14 | NagoyaCastle / Osaka Castle Profile | Project note in `10 Projects/NagoyaCastle.md` | M3 | Survey (Projects Explorer) |
| 15 | The_AI_Pipeline Profile | Project note in `10 Projects/The_AI_Pipeline.md` | M3 | Survey (Projects Explorer) |
| 16 | Orol Shahar Profile | Project note in `10 Projects/Orol Shahar Qirollik.md` | M3 | Survey (Projects Explorer) |
| 17 | Doctor A Med Clinic Profile | Project note in `10 Projects/Doctor A Med Clinic.md` | M3 | Survey (Projects Explorer) |
| 18 | PARA Maps of Content (MOCs) | Create MOC notes for `00`, `10`, `20`, `30`, `40` (dual-MOC convention) | M4 | Survey (Vault, Projects) |
| 19 | Agent Skills Hub Integration | Connect `30 Resources/Agent Skills/` to Master Brain | M4 | Survey (Vault Explorer) |
| 20 | Template Infrastructure Integration | Cross-link existing templates with Master Brain and MOCs | M4 | Survey (Vault Explorer) |
| 21 | E2E Testing Suite (Tiers 1-4) | Comprehensive test suite covering features, boundaries, combinations, workflows | M5 | Test Track |
| 22 | Wikilink & Markdown Syntax Validation | Programmatic validation confirming 0 broken wikilinks across vault | M5 | Projects Explorer |
| 23 | Adversarial Coverage Hardening (Tier 5) | White-box adversarial probing (Windows lock collision, escaped tutorial links) | M5 | Hardening Track |
| 24 | Forensic Integrity Audit | Mandatory independent audit verifying genuine implementation | M5 | Audit Enforcement |
| 25 | Nous Hermes Agent Profile | Dedicated profile in `20 Areas/Agent Profiles/Nous Hermes.md` (`hermes chat -q ...`, OpenRouter free models, deep researcher) | E1 | Survey (E3 Agents) |
| 26 | GitHub Copilot Agent Profile | Dedicated profile in `20 Areas/Agent Profiles/GitHub Copilot.md` (`copilot -p ...`, git/github automation, multi-agent bridge) | E1 | Survey (E3 Agents) |
| 27 | OpenCode CLI Agent Profile | Dedicated profile in `20 Areas/Agent Profiles/OpenCode CLI.md` (`opencode run ...`, open-source model tester, Nemotron/MiMo/Qwen) | E1 | Survey (E3 Agents) |
| 28 | Google Antigravity CLI Profile | Dedicated profile in `20 Areas/Agent Profiles/Google Antigravity CLI.md` (`agy -p ...`, architecture engineer, clean-room execution) | E1 | Survey (E3 Agents) |
| 29 | Ruflo Swarm Agent Profile | Dedicated profile in `20 Areas/Agent Profiles/Ruflo Swarm.md` (`ruflo swarm init`, `ruflo memory search ...`, vector memory) | E1 | Survey (E3 Agents) |
| 30 | 20 Areas Dual-MOC Sync | Update `20 Areas/20 Areas.md` & `20 Areas/20 Areas MOC.md` with new agent profiles | E1 | Survey (E3 Vault) |
| 31 | AI Agent Ecosystem Map | Master resource note in `30 Resources/AI Agent Ecosystem Map.md` with `/multt` protocol and interconnection diagram | E2 | Survey (E3 Agents) |
| 32 | Free LLM Models Registry | Master resource note in `30 Resources/Free LLM Models Registry.md` cataloging 23 free models across 7 providers with keys/limits | E2 | Survey (E3 Agents) |
| 33 | Codex Skills Encyclopedia | Master resource note in `30 Resources/Codex Skills Encyclopedia.md` documenting 14 custom & system skills | E2 | Survey (E3 Agents) |
| 34 | New Agent Integration Template | Template in `50 Templates/New Agent Integration Template.md` | E2 | Survey (E3 Vault) |
| 35 | Model Evaluation Template | Template in `50 Templates/Model Evaluation Template.md` | E2 | Survey (E3 Vault) |
| 36 | Security Audit Template | Template in `50 Templates/Security Audit Template.md` | E2 | Survey (E3 Vault) |
| 37 | Master Brain & Dashboard Expansion | Update `AI Sozlangan Miyyasi.md` and `Dashboard.md` with escaped table pipes `[[target\|alias]]` referencing all new content | E2 | Survey (E3 Vault) |
| 38 | 30 Resources & 00 Inbox Dual-MOC Sync | Update `30 Resources.md`, `30 Resources MOC.md`, `00 Inbox.md`, `00 Inbox MOC.md` | E2 | Survey (E3 Vault) |
| 39 | E2E Test Suite Extension (21+ tests) | Extend `tests/e2e/` with tests for new agents, registry, encyclopedia, templates, zero orphans, and quality | E3 | Survey (E3 Tests) |
| 40 | Runner Registration & Test Scale | Update `tests/e2e/runner.py` TIER_MAP; verify discover (139 tests) and tier runner (115 tests) total 254 tests | E3 | Survey (E3 Tests) |
| 41 | Git Discipline & Atomic Commits | Execute 4 atomic Conventional Commits on `feature/universal-ai-second-brain` | E1-E4 | Survey (E3 Tests) |
| 42 | Final Adversarial Gate & Audit | Reviewers APPROVE, Challengers APPROVE, Forensic Auditor CLEAN | E4 | Project Protocol |

## Milestones

| # | Name | Scope | Dependencies | Status |
|---|---|---|---|---|
| M1 | Master Brain Core & Rules Engine | `AI Sozlangan Miyyasi.md`, `Dashboard.md`, Verbatim `RULE[user_global]`, Toolchain matrix | Initial Survey | DONE |
| M2 | Universal AI Agent Profiles & Concurrency | `20 Areas/Agent Profiles/` (Antigravity 1, Antigravity 2, Codex, Concurrency & Sync Protocol) | M1 | DONE |
| M3 | Gemini Topics Memory & Active Projects | `10 Projects/` (5 project profiles with Topic Memory Blocks, 10 communication styles, ~75-char action-verb next steps, ADR logs) | M1, M2 | DONE |
| M4 | Obsidian PARA MOCs & Skills Hub Integration | MOCs for 00, 10, 20, 30, 40; cross-linking `30 Resources/Agent Skills` and `50 Templates` | M1, M2, M3 | DONE |
| M5 | E2E Verification & Adversarial Hardening | Phase 1: Pass 100% of E2E test suite (Tiers 1-4) & 0 broken wikilinks. Phase 2: Adversarial Tier 5 hardening. Forensic Integrity Audit. | M1, M2, M3, M4 | DONE |
| E1 | AI Agent Fleet Profiles & MOC Sync | 5 CLI Agent Profiles (`Nous Hermes`, `GitHub Copilot`, `OpenCode CLI`, `Google Antigravity CLI`, `Ruflo Swarm`), update `20 Areas` dual MOCs, Git commit 1 (`b35e0e0`) | M5 | DONE |
| E2 | Master Resource Guides, Templates & Brain Sync | 3 Resource notes (`AI Agent Ecosystem Map`, `Free LLM Models Registry`, `Codex Skills Encyclopedia`), 3 Templates, Master Brain & Dashboard update, dual-MOC sync, Git commit 2 (`724dbc1`) | E1 | DONE |
| E3 | E2E Test Suite Extension & Zero-Orphan Hardening | 21+ new test cases across Tiers 1-5, update `runner.py` TIER_MAP, scale test suite to 254 tests, verify 0 orphans, Git commit 3 (`1287586`) | E2 | DONE |
| E4 | Final Adversarial Review & Forensic Integrity Gate | Dual Reviewers APPROVE, Dual Challengers APPROVE, Forensic Auditor CLEAN, Remediation commit 4 (`0e783d0`) | E3 | DONE |

## Interface Contracts

### Master Brain ↔ Agent Profiles (`AI Sozlangan Miyyasi.md` ↔ `20 Areas/Agent Profiles/`)
- Master brain indexes agent profiles table: `[[Antigravity 1]]`, `[[Antigravity 2]]`, `[[Codex LLM Assistant]]`, `[[Nous Hermes]]`, `[[GitHub Copilot]]`, `[[OpenCode CLI]]`, `[[Google Antigravity CLI]]`, `[[Ruflo Swarm]]`, `[[Concurrency & Sync Protocol]]`.
- Agent profiles cite exact binary paths, role descriptions, lockfile paths (`.agents/locks/<hash>.lock`), atomic write rules, and backlink to `[[AI Sozlangan Miyyasi]]`.

### Master Brain ↔ Resource Encyclopedias (`AI Sozlangan Miyyasi.md` ↔ `30 Resources/`)
- Master brain indexes: `[[AI Agent Ecosystem Map]]`, `[[Free LLM Models Registry]]`, `[[Codex Skills Encyclopedia]]`.
- All table links use escaped pipes `[[Target\|Alias]]` to prevent markdown column breakdown.

### MOCs ↔ Vault Graph (`PARA MOCs` ↔ Sub-notes)
- Every folder note (`Folder/Folder.md`) and companion MOC (`Folder/Folder MOC.md`) must be kept in sync.
- Every note has YAML frontmatter: `tags`, `type`, `date`, `updated`, `status`.
- Zero inbound orphans across the entire vault.
