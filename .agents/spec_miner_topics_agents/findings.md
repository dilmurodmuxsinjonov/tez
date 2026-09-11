# Specification Report: Gemini Topics Architecture, Universal AI Profiles & Master Brain Entrypoint

**Miner**: Topics Architecture Spec Miner (`spec_miner_topics_agents`)  
**Timestamp**: 2026-09-11T18:35:00Z  
**Scope**: Specifications for Gemini Topics Architecture (10 communication styles, Latest State, Goals & Decisions Log, Topic Memory Blocks, action-verb ~75-char next steps), Universal AI Agent Profiles (Antigravity 1, Antigravity 2, Codex/LLM, concurrency/locking), and Master Brain Entrypoint (`AI Sozlangan Miyyasi.md`).  
**Authoritative Sources**:
1. `D:\obsidian file\.agents\ORIGINAL_REQUEST.md` — Authoritative User Project Requirements
2. `C:\Users\dilmu\.gemini\antigravity\brain\f625b60a-9da9-4106-85ed-2ca60c1d2209\gemini_topics_analysis.md` — Gemini "Topics" System Prompt Architecture & Prompt Breakdown (Google Gemini Internal Spec)
3. `C:\Users\dilmu\.gemini\config\AGENTS.md` & `config.json` — User Global Rules (`RULE[user_global]`), Toolchain Configurations, and Active Agent Profiles
4. `D:\obsidian file\Antigravity Chat History.md` & `Dashboard.md` — Historical Vault Interaction Dynamics & Existing Conventions
5. Local Toolchain Binaries: `C:\Users\dilmu\AppData\Roaming\npm\opencode.ps1`, `C:\Users\dilmu\AppData\Local\Programs\OpenAI\Codex\bin\codex.exe`, `node.exe` (v22), `python.exe` (3.12), `git.exe`

---

## Executive Summary

This report establishes the authoritative, end-to-end technical specifications for three foundational pillars of the **Universal AI Second Brain ("AI Sozlangan Miyyasi")**:
1. **Gemini Topics Architecture & State Tracking**: Full implementation rules for state summaries, architectural decisions logs, the 10 defined interaction communication styles, low-pressure next steps with strict action-verb constraints and ~75 character limits, and structured topic memory blocks.
2. **Universal AI Agent Profiles & Concurrency Protocols**: Operational role definitions for Antigravity 1 (Primary Google account session), Antigravity 2 (Secondary isolated Google account session), and Codex / LLM Assistants (`codex.exe`, `opencode.ps1`), backed by atomic file-locking, branch partitioning, and collision avoidance rules.
3. **Master Brain Entrypoint (`AI Sozlangan Miyyasi.md`)**: Complete architectural design, YAML metadata schemas, navigation graphs, and startup contracts unifying all agents and active projects.

---

## Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Gemini Topics | Latest State Summary | 1-2 sentence dense operational executive summary capturing milestones, stopping points, and active blockers. | Recent git commits, open task logs, session status. | Validated 1-2 sentence Markdown paragraph (30-50 words). | Reject speculative or unverified claims; fallback to last git commit state. | `gemini_topics_analysis.md` §2.A, `ORIGINAL_REQUEST.md` R2 |
| 2 | Gemini Topics | Goals & Decisions Log (ADR) | Append-only architectural decisions log recording rationale, alternatives considered, and rejected paths. | Decision title, context, chosen approach, rejected options, author agent. | Structured Markdown table/entry with timestamp, status, and rationale. | Prohibit modifications without formal ADR entry; prevent circular regressions. | `gemini_topics_analysis.md` §2.A, `ORIGINAL_REQUEST.md` R2 |
| 3 | Interaction Dynamics | Style 1: Thoughtful Check-in | Contextual greeting for ongoing work with steady progress and no monumental breakthrough. | Active topic state showing continuous development. | `# Header` greeting emphasizing steady rhythm and checking readiness. | Avoid false urgency or unwarranted celebration. | `gemini_topics_analysis.md` §2.B.a |
| 4 | Interaction Dynamics | Style 2: Progress Celebration | Contextual greeting when a major milestone, release, or key test suite succeeds. | Milestone completed event, major git merge, successful deployment. | `# Header` greeting acknowledging milestone and reinforcing momentum. | Suppress celebration if milestone has unresolved critical regressions. | `gemini_topics_analysis.md` §2.B.b |
| 5 | Interaction Dynamics | Style 3: Reflection Prompt | Contextual greeting for long-term project transitions, encouraging high-level evaluation. | End of major project phase, multi-week sprint boundary. | `# Header` greeting proposing a step back to review architecture or trajectory. | Do not trigger mid-debugging or during active uncommitted code sprints. | `gemini_topics_analysis.md` §2.B.c |
| 6 | Interaction Dynamics | Style 4: Callback to Detail | Contextual greeting anchoring on a memorable nuance, user preference, or unique constraint. | Specific user preference (e.g. offline-only models, zero-dependency). | `# Header` greeting recalling the exact prior preference in current context. | Verify factual existence of detail; never fabricate prior user preferences. | `gemini_topics_analysis.md` §2.B.d |
| 7 | Interaction Dynamics | Style 5: Invitation to Continue | Contextual greeting when a prior session ended abruptly or mid-task with clear pending work. | Uncommitted working tree, open PR, WIP branch, active task log. | `# Header` greeting offering immediate zero-friction resumption at the exact line. | Verify branch state; do not offer if files were modified externally. | `gemini_topics_analysis.md` §2.B.e |
| 8 | Interaction Dynamics | Style 6: Anticipation Builder | Contextual greeting when approaching an upcoming critical milestone, release, or live demo. | Proximity to target release date, 1-2 final tasks remaining in milestone. | `# Header` greeting energizing the agent and user toward the final milestone push. | Do not trigger if blocking prerequisites are incomplete. | `gemini_topics_analysis.md` §2.B.f |
| 9 | Interaction Dynamics | Style 7: Gentle Nudge | Contextual greeting when an active domain has been dormant (>7-14 days) with unfinished work. | Project inactivity timestamp > 7 days, unfinished tasks in backlog. | `# Header` greeting non-intrusively re-opening the door without pressure or guilt. | Prohibit guilt-tripping or nagging language; maintain respectful low pressure. | `gemini_topics_analysis.md` §2.B.g |
| 10 | Interaction Dynamics | Style 8: Curiosity Spark | Contextual greeting proposing a novel optimization, alternative pattern, or creative angle. | Newly available library, pattern optimization, or architectural alternative. | `# Header` greeting presenting an intriguing technical angle or performance idea. | Ensure proposed idea is technically sound and relevant to project scope. | `gemini_topics_analysis.md` §2.B.h |
| 11 | Interaction Dynamics | Style 9: Empathetic Acknowledgment | Contextual greeting when navigating heavy debugging, deep regressions, or high cognitive load. | Failing test suites, repeated crash logs, complex async debugging. | `# Header` greeting validating the difficulty and offering methodical step-by-step parsing. | Avoid patronizing remarks; maintain calm, grounded technical solidarity. | `gemini_topics_analysis.md` §2.B.i |
| 12 | Interaction Dynamics | Style 10: Low-Pressure Opener | Contextual greeting for casual entry, general browsing, or routine check-in without set agenda. | General session startup, clean workspace, no pending critical alerts. | `# Header` greeting completely open-ended, inviting user direction with zero demands. | Never force a task; present available domains casually. | `gemini_topics_analysis.md` §2.B.j |
| 13 | Interaction Dynamics | Greeting Header Formatting Standard | Standardized visual and linguistic rules for all greeting anchors. | Selected greeting style (1-10), topic context. | Single `# <Greeting Text>` Markdown header with emotional core, no canned repetition. | Disallow duplicate phrases across consecutive sessions; ban raw timestamp dumps in title. | `gemini_topics_analysis.md` §2.B |
| 14 | Gemini Topics | Suggested Next Steps Engine | Generates 2 to 4 actionable, low-pressure next steps strictly conforming to length and verb rules. | Current state, pending tasks, AI capabilities. | List of 2-4 items, each starting with an active verb, length 60-85 chars (~75 chars). | Enforce length and verb validation; reject passive voice and non-AI-actionable tasks. | `gemini_topics_analysis.md` §2.D, `ORIGINAL_REQUEST.md` R2 |
| 15 | Gemini Topics | Visual Separation Standard | Formatting protocol separating conversational guidance from structured memory blocks. | Rendered suggestions block. | Exactly 5 blank lines (`\n\n\n\n\n`) preceding the topic memory code block. | Format linter enforces exactly 5 newline characters before memory block. | `gemini_topics_analysis.md` §3 |
| 16 | Gemini Topics | Topic Memory Code Block | Dense, human-readable structured context block containing all state, goals, and history without loss. | Full topic state, ADRs, blockers, conversations. | Markdown code block (` ```text ` or ` ```yaml `) with emoji-tagged sections and word-wrapped lines. | Prohibit horizontal scrolling; enforce zero information omission. | `gemini_topics_analysis.md` §4 |
| 17 | Gemini Topics | Multi-Turn Dynamic Resumption | Protocol for ongoing dialogue after initial greeting and topic presentation. | User reply / follow-up input. | Natural, unstructured conversational turn; scope re-generation only upon confirmed topic shift. | Prevent repeated injection of full greeting and state headers on subsequent turns. | `gemini_topics_analysis.md` §5 |
| 18 | Gemini Topics | Welcome Persona System | 5 distinct persona lenses for contextual orientation across user domains. | Domain type (Productivity, Creative, Governance, Multi-source, Explorer). | Selected persona (Productivity Partner, Creative Muse, Trustworthy Guide, Synthesizer, Showcase). | Maintain strict domain alignment; adhere to transparency and user control guidelines. | `gemini_topics_analysis.md` §Welcome Personas |
| 19 | Gemini Topics | Privacy & Non-Invasive Boundaries | Strict safety rules preventing inappropriate exposure of sensitive private data or 3rd party names. | User session context, local files. | Filtered output strictly preserving privacy, user control, and benefit. | Redact unsolicited private medical/personal data; disallow unconsented naming. | `gemini_topics_analysis.md` §Muhim Xavfsizlik Qoidalari |
| 20 | Universal Agent | Antigravity 1 Profile | Primary Google account session (`dilmurodmuhsinjanov910@gmail.com`), Chief Vault Architect & user liaison. | User prompts, IDE commands, vault files. | High-level planning, vault curation, interactive UI responses, task orchestration. | Must acquire file locks before vault writes; respect user Git guidelines. | `ORIGINAL_REQUEST.md` R3, `AGENTS.md` |
| 21 | Universal Agent | Antigravity 2 Profile | Secondary isolated Google account session, parallel researcher and sandbox builder. | Background task delegations, research prompts. | Isolated builds, benchmark reports, research summaries, test executions. | Restricted from direct master vault writes; operates on dedicated branches and outputs PRs. | `ORIGINAL_REQUEST.md` R3 |
| 22 | Universal Agent | Codex / LLM Assistants Profile | Autonomous code synthesis engine (`codex.exe`, `opencode.ps1`) for precision refactoring & CLI tasks. | Structured technical specs, OpenAPI schemas, file paths. | Executable code, unit tests, bug fixes, automated commits on feature branches. | Must conform strictly to schema contracts; defers vault note updates to Antigravity 1. | `ORIGINAL_REQUEST.md` R3, `opencode.ps1`, `codex.exe` |
| 23 | Concurrency | Multi-Agent File-Locking Protocol | Distributed lockfile system preventing race conditions and lost updates across concurrent agents. | Target file path, agent ID, operation type. | JSON lockfile in `.agents/locks/<hash>.lock` with timestamp and 300s TTL. | Block competing writes if lock active; allow read operations concurrently. | `ORIGINAL_REQUEST.md` R3 |
| 24 | Concurrency | Stale Lock Expiration & Recovery | Automatic detection and breaking of abandoned locks left by crashed or terminated agents. | Active lockfile inspect command, current system time. | Lock release and warning log if `acquired_at + 300s < now()`. | Audit log event written to `.agents/locks/lock_audit.log` before breaking lock. | System integrity protocol |
| 25 | Concurrency | Atomic Write & Temp-Rename Pattern | Two-stage write protocol ensuring zero file corruption or partial reads during updates. | New file content, destination path. | Write to `<dest>.tmp.<agent_id>`, validate syntax, atomic replace to `<dest>`. | If write fails or syntax invalid, delete temp file and abort without touching destination. | System reliability protocol |
| 26 | Concurrency | Git Branch Partitioning | Multi-agent collaboration pattern isolating work into agent-specific Git branches. | Feature scope, active agent profile. | Feature branch (`feature/<agent>-<feature_name>`) with descriptive incremental commits. | Disallow direct pushes to `main`; require review or programmatic validation before merge. | `ORIGINAL_REQUEST.md` R3, `RULE[user_global]` |
| 27 | Master Brain | Entrypoint Specification (`AI Sozlangan Miyyasi.md`) | Root navigation and operational directive note serving as universal startup anchor. | Startup hook of any AI instance. | Standardized master markdown file at `D:\obsidian file\AI Sozlangan Miyyasi.md`. | Error if file missing, malformed frontmatter, or containing broken internal links. | `ORIGINAL_REQUEST.md` R1 |
| 28 | Master Brain | YAML Frontmatter Standard | Machine-readable metadata block defining document identity, roles, version, and tags. | System metadata parameters. | Valid YAML frontmatter block with `tags`, `type`, `version`, `updated`, and `language`. | Validate with YAML parser; fail build if syntax errors or missing mandatory tags. | `ORIGINAL_REQUEST.md` R1 |
| 29 | Master Brain | User Identity & Operational Preferences | Canonical profile anchoring user accounts, communication channels, and language policy. | User configurations (`dilmurodmuhsinjanov910-byte`, etc.). | Standardized profile block: Uzbek for conversational interaction, English for technical artifacts. | Prevent language confusion; maintain consistent bilingual distinction. | `Antigravity Chat History.md`, `config.json` |
| 30 | Master Brain | Inviolable Git Rule Enforcement (`RULE[user_global]`) | Verbatim preservation and enforcement of the user's mandatory automatic Git workflow. | Any project or vault modification command. | Automatic `git init`, `git status`, `git add .`, descriptive `git commit`, `git pull/push`, branching. | Prohibit any manual prompt asking user to run git commands; execute automatically. | `ORIGINAL_REQUEST.md` R4, Acceptance Criteria |
| 31 | Master Brain | Local Toolchain Inventory Specification | Authoritative directory of verified local software binaries, paths, and versions. | Environment PATH and filesystem locations. | Validated toolchain table: Node v22, Python 3.12, PowerShell, Git, Codex, Electron. | Warn if expected binary missing or version mismatch; provide fallback path. | `ORIGINAL_REQUEST.md` R4, system inspection |
| 32 | Master Brain | Active Projects & Gemini Topic Hub | Central index routing all agents to active project topic memory notes. | Active user projects (MobCreatorWebApp, NagoyaCastle, The_AI_Pipeline, Orol Shahar, Medical Clinic). | Table of active projects with wikilinks, local repository paths, active branch, and Latest State. | Zero broken links; verify all target topic memory notes exist. | `ORIGINAL_REQUEST.md` R4, `inspect_projects.ps1` |
| 33 | Master Brain | Vault Navigation Architecture (PARA + Skills) | Complete structural index linking all vault folders, templates, and agent skills. | Vault directories: `00 Inbox`, `10 Projects`, `20 Areas`, `30 Resources`, `40 Archives`, `50 Templates`. | Navigational dashboard table with bidirectional wikilinks to key hubs. | Block orphaned core folders; ensure seamless Obsidian graph view connectivity. | `ORIGINAL_REQUEST.md` R4, `Dashboard.md` |
| 34 | Master Brain | Startup & Write-Back Protocol Specification | Explicit step-by-step algorithms detailing how any AI initializes and saves state. | AI startup event, session termination event. | Documented procedure: 5 startup steps (read, lock check, topic load, greeting select, next steps) & 4 shutdown steps. | Prevent silent state loss; enforce memory update at session completion. | `ORIGINAL_REQUEST.md` R1 & Acceptance Criteria |
| 35 | Knowledge Graph | Bidirectional Wikilink Validation Standard | Strict validation rules ensuring 100% clean graph without broken links or orphaned concepts. | All newly generated `.md` and `.base` files. | Zero broken `[[...]]` links; valid relative/vault paths; correct title aliases. | Automated test script (`validate_vault.py`) must pass with 0 errors before release. | `ORIGINAL_REQUEST.md` R5, Acceptance Criteria |

---

## Detailed Specifications

### 1. Gemini Topics Architecture & State Tracking

#### 1.1 Latest State Summary Specification
- **Length**: Strictly 1 to 2 sentences (between 25 and 60 words).
- **Core Elements**:
  1. *Current Milestone*: Active sprint, release version, or phase.
  2. *Exact Stopping Point*: The precise file, function, route, or test where active work concluded.
  3. *Active Blockers / Dependencies*: Immediate blockers requiring resolution before progress can continue (or explicit declaration that no blockers exist).
  4. *Active Git Branch*: Current working branch name and short commit hash.
- **Tone**: Dense, objective, factual, zero conversational fluff.
- **Example**:
  > "Sprint V2-P1 is currently active on branch `feature/wallet-deposit` (commit `a8c90f1`), where the Solana Phantom wallet connect flow is fully integrated and tested. Next immediate focus is resolving the deposit intent expiry verification before merging into main."

#### 1.2 Goals & Decisions Log Specification (Architectural Decision Record - ADR)
- **Structure**: Markdown table or chronological sub-sections.
- **Mandatory Schema**:
  ```markdown
  ### 💡 Goals & Decisions Log

  | Date | ADR ID | Decision & Scope | Rationale & Trade-offs | Alternatives Rejected | Status | Author |
  | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
  | 2026-09-11 | ADR-001 | Adopt Prisma ORM for Orol Shahar | Type-safe schema generation and seamless SQLite/Postgres migration | TypeORM (too heavy), Raw SQL (lack of schema sync) | Active | Antigravity 1 |
  | 2026-09-11 | ADR-002 | Use Edge-TTS with uz-UZ-MadinaNeural | High naturalness and 0 API cost for local voice synthesis | pyttsx3 (robotic voice), Cloud ElevenLabs (expensive) | Active | Antigravity 1 |
  ```
- **Rules**:
  - Append-only: historical entries must never be deleted; if superseded, add a new entry referencing the old one and mark the old status as `Superseded by ADR-xxx`.
  - Every non-trivial architectural choice (framework, database, state manager, auth provider) MUST have a corresponding entry.

#### 1.3 Interaction Dynamics & The 10 Defined Communication Styles
The AI assistant must select the single most contextually appropriate greeting style from the 10 defined archetypes:

| Style # | Style Name | Trigger Condition | Linguistic Tone | Anchor Template / Example |
|---|---|---|---|---|
| **1** | **Thoughtful check-in** | Ongoing, steady development; no major release or critical blocker; normal working rhythm. | Calm, supportive, collaborative. | `# Ready to continue shaping the backend service routes?` |
| **2** | **Progress celebration** | Immediate completion of a major milestone, successful green build after red, or major release. | High-energy, appreciative, validating. | `# Milestone reached: Solana Wallet deposit flow is fully verified!` |
| **3** | **Reflection prompt** | Milestone transition point, multi-week sprint boundary, or before scaling architecture. | Contemplative, strategic, big-picture. | `# Taking a step back: how is the modular architecture feeling so far?` |
| **4** | **Callback to detail** | Resuming a task that hinges on a unique user preference or memorable design nuance. | Attentive, context-aware, personalized. | `# Keeping things 100% local: ready to tune the offline voice pipeline?` |
| **5** | **Invitation to continue** | Prior session interrupted mid-task with open uncommitted edits or active WIP branch. | Frictionless, immediate, action-ready. | `# Picking up right where we left off on the Shipyard upgrade logic.` |
| **6** | **Anticipation builder** | One or two final steps remain before a major public demo, production deployment, or launch. | Energizing, forward-looking, focused. | `# Just one step away from our first end-to-end multiplayer live test.` |
| **7** | **Gentle nudge** | Project or domain untouched for >7 days with pending open tasks. | Warm, non-judgmental, pressure-free. | `# Checking in on Nagoya Castle assets whenever you feel like diving back in.` |
| **8** | **Curiosity spark** | Discovery of an innovative pattern, performance optimization, or elegant refactoring idea. | Inquisitive, intellectually engaging. | `# Stumbled upon an instanced mesh trick that could double our FPS—interested?` |
| **9** | **Empathetic acknowledgment** | Following complex, frustrating debugging sessions, elusive race conditions, or repeated crashes. | Grounded, patient, methodical. | `# That was a thorny async race condition. Let's inspect the traces calmly.` |
| **10** | **Low-pressure opener** | Casual drop-in, general vault maintenance, or session start without predefined agenda. | Relaxed, open-ended, zero expectations. | `# Everything in the vault is clean and organized. What's on your mind today?` |

**Mandatory Linguistic Rules for Greetings**:
- Always format as a top-level Markdown header (`# <Greeting>`).
- Speak to the emotional and cognitive core of the task, not a mechanical readout of dates or commit hashes.
- Never reuse verbatim identical greetings across consecutive sessions on the same topic.
- Grounded strictly in recorded facts: zero hallucination of unperformed milestones.

#### 1.4 Suggested Next Steps Engine Specification
- **Quantity**: Exactly 2 to 4 suggested options per topic.
- **Action-Verb Rule**: The first word of every suggestion MUST be an imperative action verb.
  - *Allowed verbs*: `Review`, `Inspect`, `Refactor`, `Draft`, `Implement`, `Audit`, `Benchmark`, `Verify`, `Integrate`, `Configure`, `Test`, `Document`, `Extract`.
  - *Disallowed formats*: "You should...", "We need to...", "Next step is...", "The codebase requires...".
- **Character Limit**: Target **~75 characters** (Strict bounds: minimum 55 characters, maximum 85 characters).
- **AI-Actionable Scope**: Suggestions must represent tasks that the AI model can directly perform or collaboratively execute with the user in the workspace.
- **Temporal Relevance**: Suggestions must be currently unfulfilled, forward-looking, and directly unblocked by current dependencies.
- **Validation Examples**:
  - ✅ `Implement JWT verification middleware for the auth service routes` (66 chars)
  - ✅ `Benchmark Redis cache response times under concurrent WebSocket load` (71 chars)
  - ✅ `Audit Solana deposit intent error codes against OpenAPI specifications` (72 chars)
  - ❌ `Go to the store and buy a new graphics card for AI model training` (Invalid: Non-AI actionable)
  - ❌ `You should probably consider looking into whether or not we might want to refactor the database` (98 chars, starts with "You should")

#### 1.5 Visual Separation & Topic Memory Code Block Specification
Following the suggestions, there must be **exactly 5 blank lines** (`\n\n\n\n\n`) before the Topic Memory Block.
The Topic Memory Block is wrapped inside a code block (` ```text ` or ` ```markdown `) containing:
```text
🎯 ACTIVE GOALS & OBJECTIVES
- Objective 1: Implement full Web3 Solana wallet transaction cycle
- Objective 2: Complete automated integration test suite with 100% pass rate

📋 LATEST STATE & MILESTONE PROGRESS
- Current Phase: Sprint V2-P1 (Wallet Integration)
- Active Branch: feature/wallet-deposit (HEAD: 8d2e1a9)
- Stopping Point: frontend/src/features/Wallet.tsx line 142

💡 ARCHITECTURAL DECISIONS LOG
- 2026-09-11: Adopted Phantom Wallet standard signMessage for challenge verification
- 2026-09-11: Chose bs58 dynamic import in frontend to preserve lightweight bundle

⚠️ KNOWN ISSUES & ACTIVE BLOCKERS
- Blocker: Devnet faucet rate limit encountered during automated E2E batch test
- Workaround: Use persistent devnet test wallet pre-funded with 5 SOL

💬 RELEVANT CONVERSATIONS & GIT COMMITS
- Commit 8d2e1a9: "feat(wallet): implement challenge signature verification"
- Discussion: Antigravity Session 2026-09-11 on Treasury Ledger architecture

🔗 CROSS-DOMAIN DEPENDENCIES
- Depends on: [[10 Projects/Orol Shahar/Treasury Ledger Spec]]
- Blocks: [[10 Projects/Orol Shahar/NFT Marketplace]]
```
- **Formatting Constraint**: Formatted cleanly with line wraps to prevent horizontal scrolling in standard Obsidian viewing widths.

---

### 2. Universal AI Agent Profiles & Sync Protocols

#### 2.1 Antigravity 1 Profile (Primary Google Account & Chief Architect)
- **Account Identity**: Primary user Google account (`dilmurodmuhsinjanov910@gmail.com`).
- **Runtime Environment**: Primary Antigravity IDE workspace, default browser user data directory (`C:\Users\dilmu\.gemini\antigravity-browser-profile`).
- **Core Responsibilities**:
  - Serves as the primary user-facing conversational liaison and system architect.
  - Maintains the single source of truth inside `D:\obsidian file\AI Sozlangan Miyyasi.md`.
  - Manages active project topic memory states and greeting interaction dynamics.
  - Coordinates high-level planning, delegates subtasks, and reviews work produced by other agents.
- **Read/Write Authority**: Full read/write authority across the entire vault and workspace projects. Must acquire file locks when updating shared central files.

#### 2.2 Antigravity 2 Profile (Secondary Isolated Session & Sandbox Worker)
- **Account Identity**: Secondary isolated Google account session.
- **Runtime Environment**: Secondary browser profile / sandbox environment without shared session storage, cookies, or authorization tokens with Antigravity 1.
- **Core Responsibilities**:
  - Handles parallel compute-intensive research, clean-room testing, and large-scale document synthesis.
  - Executes isolated benchmark runs and exploratory spikes without polluting Antigravity 1's memory context.
  - Validates code changes through clean independent test passes.
- **Read/Write Authority**: Read access to the vault; writes only to isolated output directories, temporary research notes (`20 Areas/Research/...`), or dedicated Git feature branches (`feature/antigravity2-...`). Prohibited from modifying `AI Sozlangan Miyyasi.md` directly.

#### 2.3 Codex / LLM Assistants Profile (Precision Code Generation & Headless Engine)
- **Tool Binaries**:
  - `codex.exe`: `C:\Users\dilmu\AppData\Local\Programs\OpenAI\Codex\bin\codex.exe`
  - `opencode.ps1`: `C:\Users\dilmu\AppData\Roaming\npm\opencode.ps1`
- **Core Responsibilities**:
  - Autonomous code synthesis, precision refactoring, bug fixes, and unit test generation.
  - Headless task execution invoked via command line:
    ```powershell
    opencode run "Implement OpenAPI endpoints for Treasury in backend/src/modules/treasury" --auto
    ```
  - Direct execution of build and test toolchains (npm, pytest, cargo, prisma).
- **Execution & Code Synthesis Protocol**:
  - Strictly follows interface contracts (`openapi.json`, TypeScript definitions, Prisma schemas).
  - Automatically executes `RULE[user_global]` Git commands (`git status`, `git add`, `git commit -m "..."`).
  - Writes code directly into project codebases; logs task traces into `.data/agents/<task-id>/`.
  - Never edits Obsidian vault notes directly; emits completion summaries for ingestion by Antigravity 1.

#### 2.4 Concurrency, File Locking & Conflict Avoidance Protocol
- **Lock Directory**: `D:\obsidian file\.agents\locks\`
- **Lock Mechanism**:
  - When an agent intends to update a critical shared file (e.g. `AI Sozlangan Miyyasi.md` or a Topic Memory file), it generates a SHA-256 hash of the target relative path.
  - Writes lock file: `.agents/locks/<file_hash>.lock`.
  - Schema:
    ```json
    {
      "target_file": "AI Sozlangan Miyyasi.md",
      "locked_by": "Antigravity_1",
      "agent_conv_id": "2069dec9-a876-4118-a7b4-e9c8f138064b",
      "acquired_at": "2026-09-11T18:35:00Z",
      "ttl_seconds": 300,
      "purpose": "Updating active project latest state summary"
    }
    ```
- **Lock Acquisition Logic**:
  1. Inspect if `.agents/locks/<file_hash>.lock` exists.
  2. If present, read timestamp. If `acquired_at + ttl_seconds > current_time`: Lock is active. Yield and retry after 2000ms.
  3. If present but `acquired_at + ttl_seconds <= current_time`: Lock is stale (agent crashed). Break lock, log warning to `.agents/locks/audit.log`, and claim lock.
  4. Write own lock file atomically.
- **Two-Stage Atomic Write Protocol**:
  1. Write updated content to a temporary sibling file: `<target_file>.tmp.<agent_id>`.
  2. Perform syntax and integrity validation on the temporary file (confirm valid YAML frontmatter, valid Markdown, and no broken wikilinks).
  3. Perform atomic filesystem rename/replace from temporary file to target file.
  4. Delete the lock file immediately.
- **Git Branch Partitioning**:
  - To prevent repository git merge collisions, agents NEVER commit directly to `main` simultaneously.
  - Antigravity 1 works on `feature/arch-...` or orchestrates merges.
  - Antigravity 2 works on `feature/research-...`.
  - Codex works on `feature/codex-...`.
  - All branches are merged into `main` only after passing the automated verification test suite.

---

### 3. Master Brain Entrypoint (`AI Sozlangan Miyyasi.md`) Design Specification

#### 3.1 Document Header & Frontmatter Schema
```yaml
---
title: "🧠 AI Sozlangan Miyyasi — Universal AI Second Brain"
version: "1.0.0"
created: 2026-09-11
updated: 2026-09-11
status: active
type: master-brain-entrypoint
author: "Dilmurod Muhsinjanov & AI Fleet"
tags:
  - second-brain
  - master-entrypoint
  - gemini-topics
  - antigravity
  - codex
  - system-protocol
language: "uz-UZ, en-US"
---
```

#### 3.2 Required Document Sections & Content Architecture

```markdown
# 🧠 AI Sozlangan Miyyasi — Universal AI Second Brain

> "Miyangiz g'oyalarni saqlash uchun emas, ularni yaratish uchun xizmat qiladi." — David Allen

---

## ⚡ Universal AI Startup Directive (Read-First Protocol)
[Mandatory operational directive instructing any incoming AI agent to read this document, identify active priorities, verify file locks, and initialize state.]

## 👤 Foydalanuvchi Profili va Shaxsiyati (User Identity Anchor)
- **Foydalanuvchi**: Dilmurod Muhsinjanov
- **Email / Google Account**: `dilmurodmuhsinjanov910@gmail.com`
- **GitHub**: `dilmurodmuhsinjanov910-byte`
- **Muloqot tili (Interaction)**: O'zbek tili (Lotin yozuvi)
- **Texnik hujjatlar va kod (Technical artifacts)**: English (US)

## ⚖️ Majburiy Global Qoidalar (Mandatory Git Workflow: RULE[user_global])
[Verbatim preservation and enforcement of the user's custom Git rules:
- Default to Git
- Automatic lifecycle operations (init, status, add, commit, pull, push)
- Automatic branching for major modifications (feature/... or fix/...)]

## 🛠️ Mahalliy Dasturiy Vositalar (Local Toolchain Specification)
| Asbob | Versiya / Manzil | Asosiy Vazifasi |
| :--- | :--- | :--- |
| **Node.js** | v22 (`C:\Users\dilmu\AppData\Local\hermes\node\node.exe`) | Frontend va backend JavaScript/TypeScript runtime |
| **Python** | 3.12 (`C:\Users\dilmu\AppData\Local\Programs\Python\Python312\python.exe`) | AI skriptlari, tahlil va avtomatlashtirish |
| **Git** | 2.x (`C:\Program Files\Git\cmd\git.exe`) | Versiyalar nazorati va GitHub sinxronizatsiyasi |
| **PowerShell**| Windows PowerShell 5.1 / 7.x | Tizim buyruqlari va muhit boshqaruvi |
| **Codex CLI** | `codex.exe` & `opencode.ps1` (`C:\Users\dilmu\AppData\Roaming\npm\opencode.ps1`) | Avtonom kod yozish va testlarni bajarish |

## 🤖 Ulangan AI Agentlar Floti (Connected AI Agent Profiles)
- [[20 Areas/Agent Profiles/Antigravity 1 Profile|Antigravity 1]]: Bosh arxitektor va interaktiv yordamchi (Google Primary)
- [[20 Areas/Agent Profiles/Antigravity 2 Profile|Antigravity 2]]: Izolyatsiyalangan tadqiqotchi va sandbox sinovchi (Google Secondary)
- [[20 Areas/Agent Profiles/Codex Assistant Profile|Codex / opencode]]: Avtonom kod generatsiyasi va refaktoring dvigateli
- [[20 Areas/Agent Profiles/Concurrency & Lock Protocol|Konkurentlik va Blokirovka Protokoli]]: Fayllarni bir vaqtda xavfsiz tahrirlash qoidalari

## 🗂️ Faol Loyihalar va Gemini Topic Memory Markazi (Active Projects Hub)
| Loyiha | Soha | Joriy Holat (Latest State) | Faol Shox | Mavzu Xotirasi (Topic Memory) |
| :--- | :--- | :--- | :--- | :--- |
| **MobCreatorWebApp** | Web App / Tool | Modellar generatori UI va eksport funksiyalari faol | `main` | [[10 Projects/MobCreatorWebApp/Topic Memory - MobCreatorWebApp\|Xotira Bloki]] |
| **Nagoya & Osaka Castle** | 3D / Creative | 3D aktivlar va sahna optimizatsiyasi davom etmoqda | `main` | [[10 Projects/NagoyaOsakaCastle/Topic Memory - Nagoya Osaka Castle\|Xotira Bloki]] |
| **The_AI_Pipeline** | Pipeline / MLOps | Avtomatlashtirilgan AI quvurlari va skriptlari | `main` | [[10 Projects/The_AI_Pipeline/Topic Memory - The_AI_Pipeline\|Xotira Bloki]] |
| **Orol Shahar** | Web3 / Game | V2-P1 G'azna (Wallet & Treasury) integratsiyasi faol | `feature/wallet` | [[10 Projects/Orol Shahar/Topic Memory - Orol Shahar\|Xotira Bloki]] |
| **Medical Clinic** | Web App / Med | Doctor A tibbiyot markazi portali sahifalari va shakllari | `feature/doctor-a` | [[10 Projects/Medical Clinic/Topic Memory - Medical Clinic\|Xotira Bloki]] |

## 🗺️ Tizim Xaritasi (PARA Structure & Resources)
- [[00 Inbox/|00 Inbox]]: Yangi g'oyalar va qayta ishlanmagan xabarlar
- [[10 Projects/|10 Projects]]: Aniq maqsad va muddatga ega faol loyihalar
- [[20 Areas/|20 Areas]]: Doimiy javobgarlik sohalari va agent profillari
- [[30 Resources/|30 Resources]]: Foydali manbalar va [[30 Resources/Agent Skills/Skills Dashboard|Agent Ko'nikmalari Boshqaruv Paneli]]
- [[40 Archives/|40 Archives]]: Yakunlangan loyihalar arxivi
- [[50 Templates/|50 Templates]]: Kunlik, loyiha va resurs shablonlari

## 🔄 Sessiya Boshlash va Yakunlash Protokoli (Session Lifecycle)
[Clear 5-step startup algorithm and 4-step shutdown algorithm ensuring 100% memory persistence without state loss.]
```

#### 3.3 Startup & Write-back Protocol Details
1. **Startup Protocol (When an AI begins a session)**:
   - Step 1: Read `D:\obsidian file\AI Sozlangan Miyyasi.md`.
   - Step 2: Check `.agents/locks/` to confirm no active locks on target files.
   - Step 3: Read the target project's `Topic Memory` note in `10 Projects/...`.
   - Step 4: Evaluate recent context and select 1 of the 10 Greeting Styles for the greeting anchor.
   - Step 5: Formulate the 1-2 sentence Latest State Summary and 2-4 Action-Verb Next Steps (~75 chars).
2. **Write-Back Protocol (When an AI concludes a session)**:
   - Step 1: Acquire lock on the target topic memory note.
   - Step 2: Update the `📋 LATEST STATE & MILESTONE PROGRESS` section with verified progress, active commit hash, and current stopping point.
   - Step 3: Append any new architectural decisions to `💡 ARCHITECTURAL DECISIONS LOG`.
   - Step 4: Update the 2-4 Suggested Next Steps adhering strictly to the action-verb and ~75 character limit.
   - Step 5: Save via the atomic two-stage write protocol and release the lock.
   - Step 6: Automatically commit and push changes according to `RULE[user_global]`.

---

## Edge Cases & Error Handling Specifications

| # | Edge Case / Condition | Trigger Input | System Specification & Expected Handling |
|---|----------------------|---------------|------------------------------------------|
| 1 | Suggested Next Step exceeds character limit | Step text length > 85 characters. | Linter / generator truncates or rephrases text to 60-85 chars (~75 chars), preserving the leading active verb. |
| 2 | Suggested Next Step lacks leading action verb | Step starts with noun/pronoun ("The team should...", "Reviewing...", "JWT auth..."). | Validator rejects suggestion; replaces with active imperative verb (`Implement JWT authentication middleware for auth service routes`). |
| 3 | Suggested Next Step describes impossible external task | Step suggests real-world physical action ("Buy new RAM", "Fly to Nagoya"). | Generator rejects suggestion; reformulates into AI-collaborative action (`Draft specifications for system hardware memory requirements`). |
| 4 | Simultaneous write attempt on same note | Two agents (e.g. Antigravity 1 and Codex) attempt to write to `AI Sozlangan Miyyasi.md` simultaneously. | First agent acquires lockfile; second agent detects active lock, yields for 2000ms, and retries up to 3 times before deferring. |
| 5 | Stale lockfile from crashed agent | Lockfile exists with `acquired_at + ttl_seconds < now()` (> 300 seconds old). | Inspecting agent detects expired TTL, logs warning to `.agents/locks/audit.log`, breaks stale lock, and acquires fresh lock. |
| 6 | Space character in vault directory path | Path contains space (`D:\obsidian file`). | All scripts, CLI commands, and links must wrap filesystem paths in quotes (`"D:\obsidian file"`) or use URL encoding where appropriate. |
| 7 | Non-ASCII Uzbek characters | Uzbek text with modifier letters (`o‘`, `g‘`, `sh`, `ch`, Cyrillic). | Enforce UTF-8 encoding across all files; forbid ANSI or UTF-8 with BOM to prevent corrupted rendering in Obsidian. |
| 8 | Vault uninitialized in Git | Workspace or project folder lacks `.git` repository. | Automatically invoke `git init`, set branch to `main`, and commit initial files per `RULE[user_global]`. |
| 9 | Direct commit to `main` for non-trivial change | Agent prepares major architectural update or refactor. | Intercept and automatically create a descriptive branch (`git checkout -b feature/<desc>`) per `RULE[user_global]`. |
| 10 | Broken wikilink in newly created note | Wikilink target note does not exist in vault (`[[NonExistentNote]]`). | Automated validator script (`validate_vault.py`) flags missing target file; build gate blocks completion until resolved. |
| 11 | Ambiguous wikilink between same-name notes | Multiple notes with identical names in different folders (e.g. `2026-07-01.md`). | Require explicit folder path in wikilink (`[[DILMUROD/2026-07-01]]` vs `[[00 Inbox/2026-07-01]]`). |
| 12 | User requests topic scope change mid-session | User says "Let's work on something completely different today". | Follow Multi-Turn Dynamic rule: confirm change of focus first, then regenerate greeting and state for the new topic. |

---

## Verification & Validation Criteria

To verify that implementations conform to this specification:
1. **Wikilink Integrity Check**:
   - Run Python validation script across all `.md` files in `D:\obsidian file`.
   - Result must show 0 broken wikilinks, 100% resolution against physical vault paths.
2. **Next Steps Format Validation**:
   - Run regex validation on all suggested next steps:
     `^[A-Z][a-z]+ .+$` with length `60 <= len(step) <= 85`.
   - Verify leading word is an active imperative verb.
3. **Visual Separation Check**:
   - Verify that 5 blank newline characters (`\n\n\n\n\n`) exist between the suggested next steps list and the topic memory code block.
4. **Agent Profile & Concurrency Check**:
   - Verify `.agents/locks/` directory exists and lock acquisition / release tests succeed without deadlock.
5. **Git Workflow Compliance**:
   - Verify `git status` in `D:\obsidian file` reflects clean working tree with descriptive commit history.
