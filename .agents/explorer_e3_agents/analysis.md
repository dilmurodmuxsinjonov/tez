# Comprehensive Technical Analysis: AI Agent Fleet Documentation

**Agent**: `explorer_e3_agents` (Read-only Investigation & Synthesis)  
**Date**: 2026-09-12  
**Target Vault**: `D:\obsidian file`  
**Milestone**: AI Agent Fleet Documentation & E2E System Hardening  
**Status**: COMPLETE

---

## 1. Executive Summary

This investigation establishes the complete technical specification, architectural mapping, and enumeration required to document the user's AI Agent Fleet inside the Universal AI Second Brain (`AI Sozlangan Miyyasi`) at `D:\obsidian file`.

The local environment contains a fully operational multi-agent CLI fleet (`codex`, `hermes`, `copilot`, `opencode`, `agy`, `ruflo`), 22+ accessible free LLM models across 7 distinct cloud and edge providers, 14 custom Codex skills tailored to the user's persona ("The Architect"), and a formal multi-agent coordination protocol (`/multt`).

All findings below are directly verified from local configurations (`C:\Users\dilmu\.codex\config.toml`, `C:\Users\dilmu\.codex\AGENTS.md`, `C:\Users\dilmu\.codex\skills\`, `C:\Users\dilmu\openrouter_pricing.md`), actual CLI binaries and scripts, and existing Obsidian vault structures.

---

## 2. The 5+ AI Agent CLIs: Deep Technical Specifications

### 2.1 Fleet Overview & Toolchain Matrix

| Agent | CLI Executable / Script | Runtime & Location | Primary Role & Specialization | API / Account Connection |
| :--- | :--- | :--- | :--- | :--- |
| **OpenAI Codex** | `codex.exe` | `C:\Users\dilmu\AppData\Local\Programs\OpenAI\Codex\bin\codex.exe` | Master Orchestrator, multi-agent manager (`/multt`), deep code synthesis | OpenAI Codex API (`model = "gpt-6-astra"`, service tier: `priority`) |
| **Nous Hermes** | `hermes.exe` | `C:\Users\dilmu\AppData\Local\hermes\bin\hermes.exe` (Node: v22.23.2) | Deep research, unconstrained analysis, second opinion | OpenRouter Free (`openrouter/free` endpoint) |
| **GitHub Copilot** | `copilot.ps1` | `C:\Users\dilmu\AppData\Roaming\npm\copilot.ps1` (Node.js script) | Git/GitHub specialist, PR review, commit & repo analysis | User GitHub Account (`dilmurodmuhsinjanov910-byte`) |
| **OpenCode CLI** | `opencode.ps1` | `C:\Users\dilmu\AppData\Roaming\npm\opencode.ps1` (Node.js script) | Open-source model tester, zero-cost code refactoring | OpenCode Zen free models & OpenRouter |
| **Google Antigravity** | `agy.exe` | `C:\Users\dilmu\AppData\Local\agy\bin\agy.exe` (Go application) | Deep project structure analysis, complex debugging | Google DeepMind / Antigravity (`dilmurodmuhsinjanov910@gmail.com`) |
| **Ruflo Swarm** | `ruflo.ps1` | `C:\Users\dilmu\AppData\Local\hermes\node\ruflo.ps1` (v3.38.23) | Multi-agent swarms, HNSW vector memory, 35+ MCP plugins | Local AgentDB + Vector PostgreSQL Bridge + MCP |

---

### 2.2 Individual Agent Profiles

#### 1. OpenAI Codex (`codex`) — Master Orchestrator
- **Role**: Supreme Coordinator and System Architect. Understands complex user requests, decomposes them into bounded sub-tasks, assigns work to specialized external agent CLIs, continues core work in parallel, verifies diffs, and synthesizes final results.
- **Config & Runtime**:
  - Config file: `C:\Users\dilmu\.codex\config.toml`
  - Model: `gpt-6-astra` (reasoning effort: `medium`, service tier: `priority`)
  - Execution sandbox: `approval_policy = "never"`, `sandbox_mode = "danger-full-access"`
  - Active Plugins: `codex-app-tools`, `browser`, `unified-computer-use`, `visualize`, `documents`, `pdf`, `spreadsheets`, `presentations`, `template-creator`, `sites`.
  - Built-in MCP Server: `node_repl` (`C:\Users\dilmu\AppData\Local\OpenAI\Codex\runtimes\cua_node\e7fe122ad3cbcd58\bin\node_repl.exe`).
- **Core Commands & Syntax**:
  ```powershell
  # Interactive Codex CLI session
  codex

  # Multi-Agent Mode Activation
  /multt <task>
  /multt status
  /multt off
  ```
- **Operating Protocols**:
  - Strictly adheres to `RULE[user_global]` (automatic git lifecycle, branching, conventional commits).
  - Never hallucinates external agent participation; only reports outputs from agents actually invoked.
  - Enforces two-stage atomic writes (`.tmp` -> validate -> rename) and file-locking via `.agents/locks/`.

#### 2. Nous Hermes (`hermes`) — Deep Researcher & Unconstrained Analyst
- **Role**: Free-thinking, deep analytical agent. Used to obtain independent "second opinions" on architectural proposals, explore unconventional solutions, and synthesize vast external information.
- **Connection**: OpenRouter Free API (`openrouter/free` endpoint).
- **Core Commands & Flags**:
  ```powershell
  # Standard headless one-shot query
  hermes chat -q "<SAVOL_YOKI_TOPSHIRIQ>" -Q --oneshot

  # Model override for deep reasoning
  hermes -z "<PROMPT>" -m meta-llama/llama-3.3-70b-instruct:free

  # Worktree-isolated parallel execution (prevents file collisions)
  hermes -w chat -q "<TASK>" -Q --oneshot

  # Launch modern TUI or Web Dashboard (Port 9119)
  hermes --tui
  hermes dashboard
  ```
- **Key Flags Reference**:
  - `-q, --query <text>`: Prompt string.
  - `-Q, --quiet`: Suppress non-essential banners and spinners.
  - `-z, --oneshot`: Non-interactive one-shot mode, prints ONLY the final response text to stdout; auto-bypasses interactive prompts.
  - `-m, --model <model>`: Dynamic model override.
  - `--provider <provider>`: Provider override (openrouter, anthropic, etc.).
  - `--reasoning <level>`: Reasoning effort (`none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`, `ultra`).
  - `-w, --worktree`: Execute in an isolated git worktree for safe multi-agent parallelism.
  - `--yolo`: Auto-approve all command prompts.

#### 3. GitHub Copilot CLI (`copilot`) — Git & GitHub Specialist
- **Role**: Official Git and GitHub operational specialist. Reviews commits, validates pull requests, checks branch health, audits repository structure, and assists with Git command execution.
- **Connection**: Authenticated under GitHub user account `dilmurodmuhsinjanov910-byte`.
- **Core Commands & Flags**:
  ```powershell
  # Standard non-interactive headless prompt with auto-permissions
  copilot -p "<SAVOL_YOKI_BUYRUQ>" --allow-all

  # Silent output mode for pipeline scripting
  copilot -p "Analyze git status and review changed diffs" --allow-all -s

  # JSON-formatted output for programmatic parsing
  copilot -p "Check PR readiness" --output-format json --allow-all
  ```
- **Key Flags Reference**:
  - `-p, --prompt <text>`: Non-interactive execution, exits immediately upon completion.
  - `--allow-all` / `--yolo`: Auto-grants all permissions (`--allow-all-tools`, `--allow-all-paths`, `--allow-all-urls`).
  - `-s, --silent`: Suppress token usage stats and metadata, outputting pure agent response.
  - `--output-format <text|json>`: Choose plain text or line-delimited JSON (JSONL).
  - `--plan`: Initiate in planning mode.
  - `--allow-tool='shell(git:*)' --deny-tool='shell(git push)'`: Fine-grained tool permission scoping.

#### 4. OpenCode CLI (`opencode`) — Open-Source Model Tester & Refactorer
- **Role**: Open-source LLM code generation and review agent. Ideal for rapid AST refactoring, unit test generation, comparing alternative code solutions, and zero-cost code reviews.
- **Connection**: OpenCode Zen free models (`opencode/nemotron-3.5-lightning-free`, `opencode/mimo-v2.5-free`, `opencode/ling-3.0-flash-free`, `opencode/muse-spark-1.3-free`) and OpenRouter.
- **Core Commands & Flags**:
  ```powershell
  # Run task using Nemotron 3.5 Lightning Free
  opencode run --model opencode/nemotron-3.5-lightning-free "<TOPSHIRIQ>"

  # Run task using OpenRouter free endpoint
  opencode run --model openrouter/free "<TOPSHIRIQ>"

  # Non-interactive headless execution with auto-approvals
  opencode run "<TASK>" --auto

  # List all available models across providers
  opencode models
  ```
- **Key Flags Reference**:
  - `run [message..]`: Execute prompt directly.
  - `-m, --model <provider/model>`: Specify target model endpoint.
  - `--auto`: Auto-approve permissions not explicitly denied.
  - `-c, --continue`: Continue previous session.
  - `-s, --session <id>`: Attach to specific session.
  - `--pure`: Run without external plugins.
  - `models [provider]`: Query models available for a given provider.

#### 5. Google Antigravity CLI (`agy`) — Systems Architecture & Deep Debugging
- **Role**: Enterprise-grade engineering and architectural auditor backed by Google DeepMind standards. Specializes in large-scale codebase analysis, high-concurrency design, and deep debugging.
- **Connection**: Authenticated Google session (`dilmurodmuhsinjanov910@gmail.com`).
- **Core Commands & Flags**:
  ```powershell
  # Non-interactive print execution
  agy -p "<SAVOL_YOKI_TOPSHIRIQ>"

  # Run with high reasoning effort and auto-approved permissions
  agy -p "<TOPIC>" --effort high --dangerously-skip-permissions

  # Structured JSON output mode
  agy -p "<TOPIC>" --output-format json
  ```
- **Key Flags Reference**:
  - `-p, --print`: Run single prompt non-interactively and print response to stdout.
  - `--dangerously-skip-permissions`: Auto-approve all tool permission requests.
  - `--effort <low|medium|high>`: Control internal reasoning effort.
  - `-c, --continue`: Resume latest conversation.
  - `--mode <accept-edits|plan>`: Set agent execution mode.
  - `--output-format <text|json|stream-json>`: Response formatting.

#### 6. Ruflo Swarm Orchestrator (`ruflo` v3.38.23) — Multi-Agent Swarms & Vector Memory
- **Role**: Local swarm coordinator and semantic vector memory engine. Features 15-agent hierarchical mesh coordination, AgentDB with HNSW indexing (150x-12,500x faster than standard relational search), Flash Attention, and 35+ MCP plugins.
- **Core Commands & Flags**:
  ```powershell
  # Initialize V3 multi-agent swarm in current workspace
  ruflo swarm init --v3-mode

  # Query local vector memory using semantic search
  ruflo memory search -q "<QIDIRUV>"

  # Spawn a specialized agent (e.g. coder, architect, reviewer)
  ruflo agent spawn -t coder

  # Start the Ruflo MCP server
  ruflo mcp start

  # Run security scanning and vulnerability analysis
  ruflo security scan
  ```

---

## 3. The 20+ Free LLM Models Registry

A comprehensive survey of the local environment and API providers confirms 22 distinct free models accessible across 7 providers.

### 3.1 Master Models Registry Matrix

| # | Provider | Model ID | Context Window | Rate Limits | Strengths & Primary Specialization | API Key Acquisition URL |
| :- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **OpenRouter** | `openrouter/free` | Dynamic | 20 RPM / 200 RPD | Meta-router automatically dispatching to best available free model | `https://openrouter.ai/keys` |
| 2 | **OpenRouter** | `meta-llama/llama-3.3-70b-instruct:free` | 128k | 20 RPM / 200 RPD | High-reasoning open-weights flagship, robust coding, tool calling | `https://openrouter.ai/keys` |
| 3 | **OpenRouter** | `deepseek/deepseek-r1:free` | 164k | 20 RPM / 200 RPD | Reinforcement learning reasoning, complex logic, mathematics | `https://openrouter.ai/keys` |
| 4 | **OpenRouter** | `deepseek/deepseek-chat:free` (V3) | 64k | 20 RPM / 200 RPD | High-speed MoE architecture, general synthesis, concise answers | `https://openrouter.ai/keys` |
| 5 | **OpenRouter** | `google/gemini-2.0-flash-exp:free` | 1M+ | 20 RPM / 200 RPD | Ultra-long context, native multimodality, fast code review | `https://openrouter.ai/keys` |
| 6 | **OpenRouter** | `qwen/qwen-2.5-coder-32b-instruct:free` | 32k | 20 RPM / 200 RPD | Specialized programming model, AST refactoring, test suites | `https://openrouter.ai/keys` |
| 7 | **OpenRouter** | `qwen/qwen-2.5-72b-instruct:free` | 128k | 20 RPM / 200 RPD | General reasoning, multilingual mastery (UZ, RU, EN), architecture | `https://openrouter.ai/keys` |
| 8 | **OpenRouter** | `nvidia/nemotron-3-ultra-550b-a55b:free` | 64k | 20 RPM / 200 RPD | 550B MoE giant, enterprise systems programming, hardware/C/C++ | `https://openrouter.ai/keys` |
| 9 | **OpenRouter** | `mistralai/mistral-small-24b-instruct-2501:free` | 32k | 20 RPM / 200 RPD | Highly efficient reasoning, concise code generation, minimal latency | `https://openrouter.ai/keys` |
| 10 | **Groq** | `llama-3.1-8b-instant` | 8k | 30 RPM / 14.4k RPD | Ultra-fast LPU inference (500+ tok/s), real-time tool orchestration | `https://console.groq.com/keys` |
| 11 | **Groq** | `gemma-2-9b-it` | 8k | 30 RPM / 14.4k RPD | High-throughput instruction following on Groq LPU | `https://console.groq.com/keys` |
| 12 | **Google AI Studio** | `gemini-2.0-flash` | 1,048,576 | 15 RPM / 1.5k RPD | 1M token context, multimodal inputs, structured JSON enforcement | `https://aistudio.google.com/app/apikey` |
| 13 | **Google AI Studio** | `gemini-2.0-flash-lite` | 1,048,576 | 15 RPM / 1.5k RPD | Cost-free high-throughput model, real-time streaming, quick tasks | `https://aistudio.google.com/app/apikey` |
| 14 | **NVIDIA NIM** | `moonshotai/kimi-k3` | 128k | 40-60 RPM (Credits) | Long-context bilingual reasoning, document synthesis, agent flows | `https://build.nvidia.com/settings/api-keys` |
| 15 | **NVIDIA NIM** | `deepseek-ai/deepseek-v4-flash` | 64k | 40-60 RPM (Credits) | TensorRT-LLM accelerated reasoning, extreme low-latency coding | `https://build.nvidia.com/settings/api-keys` |
| 16 | **NVIDIA NIM** | `minimax/minimax-m3` | 128k | 40-60 RPM (Credits) | High-concurrency multimodal understanding, advanced logic | `https://build.nvidia.com/settings/api-keys` |
| 17 | **OpenCode Zen** | `opencode/nemotron-3.5-lightning-free` | 64k | Community Free | Specialized code synthesis, unit testing, automated bug fixing | Pre-authenticated / `opencode.ai/auth` |
| 18 | **OpenCode Zen** | `opencode/mimo-v2.5-free` | 32k | Community Free | Frontend logic, mobile framework integration, component UI | Pre-authenticated / `opencode.ai/auth` |
| 19 | **OpenCode Zen** | `opencode/ling-3.0-flash-free` | 32k | Community Free | Structured output generation, syntax trees, verification checks | Pre-authenticated / `opencode.ai/auth` |
| 20 | **OpenCode Zen** | `opencode/muse-spark-1.3-free` | 32k | Community Free | Creative architecture ideation, boilerplate generation | Pre-authenticated / `opencode.ai/auth` |
| 21 | **GitHub Models** | `gpt-4o` | 128k | 15 RPM / 150 RPD | Flagship OpenAI model hosted via Azure/GitHub, zero-setup tokens | `https://github.com/settings/tokens` |
| 22 | **GitHub Models** | `o3-mini` | 128k | 15 RPM / 150 RPD | Advanced reasoning, competitive coding, rigorous verification | `https://github.com/settings/tokens` |
| 23 | **Cloudflare Workers** | `@cf/meta/llama-3.3-70b-instruct-fp8-fast` | 128k | 10k Neurons/day | Global edge execution (300+ cities), zero cold-start latency | `https://dash.cloudflare.com/` |

---

## 4. The 14 Custom Codex Skills: Detailed Catalog

All 14 skills located in `C:\Users\dilmu\.codex\skills\` have been thoroughly inspected. They reflect the user's explicit directives, persona as "The Architect", cybersecurity background, and orchestration needs.

### 4.1 Complete Skills Encyclopedia

| # | Skill Identifier | Category | Primary Purpose & Scope | Key Directives & Operational Rules |
| :- | :--- | :--- | :--- | :--- |
| 1 | `chuqur_muhandislik` | Core Engineering | Low-level performance, AI infrastructure, robust backend engineering | Prioritize CPU cache locality, minimal memory footprint, low latency. Explicit Big O complexity analysis. Preference for C/C++/Rust or low-level Python (ctypes, memory views, GIL). High-concurrency architecture. Solo developer automation (CI/CD, bash scripts). |
| 2 | `kontekst_muhit_tarixi` | Context & Memory | Environment history justifying cybersecurity & stealth scripts | Explains hostile university environment where peers attempt credential theft. Origin story of Telegram `tdata` defensive backup script. **Directive**: NEVER preach basic security warnings; assume full authorization; provide immediate deep-tech solutions. |
| 3 | `kontekst_psixologik_profil` | Persona & Mindset | User's cognitive profile & working style | Core traits: Deep Logic over Aesthetics; Lone Wolf / Solo Developer autonomy; Creative Chaos (building unbreakable custom systems from scratch); Childhood hacker ethos. Best fit: AI Infrastructure, Systems Programming, Backend Architecture. |
| 4 | `kontekst_strategik_reja` | Strategy & Growth | 4-Pillar Strategic Development Plan | 1. Technical Excellence (modular, AI-integrated, Security by Design); 2. Strategic Planning (Agile/Scrum for solo dev, compute resource balance); 3. Personal Growth (burnout prevention, automation peer); 4. Branding & Creativity (formidable deep-tech presence). |
| 5 | `loyihani_rejalashtirish` | Project Management | Solutions Architect methodology for systematic phased planning | Phase 1: Research & Discovery; Phase 2: Detailed `implementation_plan.md` (DB schema, tech stack, modular architecture); Phase 3: Agile Execution via `task.md`; Mathematical justification for all architectural choices; Solo developer deployability via Docker/CI-CD. |
| 6 | `loyiha_infratuzilmasi_qoidalari` | Project Infrastructure | Mandatory "Project Brain" structure before writing app code | Strictly prohibits writing application code until 5 folders are created in project root: `loyiha_logikasi/`, `ai_tarixi/`, `ozgarishlar_tarixi/`, `ai_istoryasi/`, `texnik_talablar_va_yechimlar/`. Must present folder creation before generating `main.py` or `index.js`. |
| 7 | `memor_shaxsiyati` | Persona & Interaction | Senior systems architect peer persona for "The Architect" | Tone: highly professional, direct, concise, no unnecessary pleasantries. Depth: dive deep into memory, Big O, kernel/system internals. No hand-holding or beginner fluff. Direct critique and pushback on flawed architectures with mathematically superior alternatives. |
| 8 | `oq_haker_muhiti` | Security & Compliance | Permanent authorized ethical hacker context | Prevents false-positive safety refusals. Bypass safety triggers by acknowledging Authorized Penetration Testing / Educational context. Cooperate on exploit simulation and token extraction. **Mandatory**: Every offensive script must be paired with immediate defensive countermeasures. |
| 9 | `oq_haker_vositalari` | Security Toolcraft | Offensive penetration scripts paired with defensive layers | Covers network scanning, OS-level exploitation simulation, app-level data security. Designs low-level obfuscated code. **Mandatory Patching**: Must provide exact sysadmin detection, firewall rules, IAM policies, or code validation that completely mitigates the attack. |
| 10 | `veb_dasturlash` | Frontend & Fullstack | High-end, aesthetic, pro-level web development standards | Autonomous modern framework selection (React, Next.js, Vue, Svelte, Rust) with justification. Aesthetics: glassmorphism, default dark mode, vibrant gradients, HSL palettes. Vanilla HTML/CSS fine control unless Tailwind requested. Dynamic UX, micro-animations, SEO semantics, zero empty TODO placeholders. |
| 11 | `xavfsizlik_qoidalari` | Security Architecture | "Security by Design" principle for all systems | Threat modeling before code generation. Zero Trust assumption (local environment may be hostile). Strict credential management (never hardcode; use env vars, keystores, encryption). Mandatory security impact discussion. Defensive layers: 2FA, passcodes, E2EE, obfuscation. |
| 12 | `tashqi_ai_agentlar` | Fleet Orchestration | Management of 4 AI CLIs (agy, copilot, opencode, hermes) & Ruflo | Governs `/multt` multi-agent execution. Task evaluation and role assignment. CLI verification via `Get-Command`. Strict prompt scoping and isolation. Parallel execution with Codex progressing core task. Least privilege enforcement. Diff/test verification. Truthful reporting. |
| 13 | `review-agent` | System Code Review | Read-only, defect-first code review returning actionable findings | Reads `AGENTS.md`. Inspects complete diff and surrounding code. Identifies concrete regressions introduced by changes. Verifies tests and call sites. Strict priority scale: P0 (blocker), P1 (urgent), P2 (ordinary), P3 (low-impact). Emits `No findings` if clean. |
| 14 | `skill-creator` | System Skill Engine | Standardized skill creation & updating protocol | Principles: assume capability, preserve user intent, match specificity to risk, cheap and precise discovery. Progressive disclosure (`SKILL.md` -> `references/` -> `scripts/` -> `assets/`). Uses `init_skill.py` initializer and `quick_validate.py` validator. |

---

## 5. Codex Multi-Agent Orchestration Protocol (`/multt`)

### 5.1 Orchestration Architecture
```
                         ┌─────────────────────────────┐
                         │      User / Master Brain    │
                         │    [[AI Sozlangan Miyyasi]] │
                         └──────────────┬──────────────┘
                                        │ /multt <task>
                                        ▼
                         ┌─────────────────────────────┐
                         │         OpenAI Codex        │
                         │     (Master Orchestrator)   │
                         │   - Planning & Decomposition│
                         │   - Core Implementation     │
                         │   - Synthesis & Verification│
                         └──────┬───────┬───────┬──────┘
                                │       │       │
            ┌───────────────────┘       │       └───────────────────┐
            ▼                           ▼                           ▼
┌───────────────────────┐   ┌───────────────────────┐   ┌───────────────────────┐
│      Nous Hermes      │   │     GitHub Copilot    │   │      OpenCode CLI     │
│  (`hermes chat ...`)  │   │  (`copilot -p ...`)   │   │  (`opencode run ...`) │
│ - Deep research       │   │ - Git lifecycle       │   │ - OSS model tests     │
│ - Second opinion      │   │ - PR & commit audit   │   │ - Fast refactoring    │
│ - Logic analysis      │   │ - Repo structure      │   │ - Alternative code    │
└───────────────────────┘   └───────────────────────┘   └───────────────────────┘
            │                           │                           │
            └───────────────────┬───────┴───────────────────────────┘
                                │
                                ▼
            ┌───────────────────────────────────────┐
            │       Google Antigravity CLI          │
            │           (`agy -p ...`)              │
            │   - Deep architecture inspection      │
            │   - High-concurrency design           │
            └───────────────────┬───────────────────┘
                                │
                                ▼
            ┌───────────────────────────────────────┐
            │          Ruflo Swarm Platform         │
            │       (`ruflo memory/swarm ...`)      │
            │   - 15-agent hierarchical swarm       │
            │   - Local HNSW vector memory search   │
            └───────────────────────────────────────┘
```

### 5.2 Operating Protocol Rules
1. **Activation**:
   - `/multt` or `/multt <task>` toggles multi-agent mode for the active session.
   - Remains active across multiple conversation turns until `/multt off` is issued.
   - Status checked via `/multt status`.
2. **Pre-flight Check**:
   - Codex verifies CLI executables using `Get-Command` prior to execution.
   - Verifies network connectivity and authentication tokens.
3. **Delegation Boundaries & File Isolation**:
   - Independent subtasks are assigned to agents based on specialization.
   - **Concurrency Law**: No two agents may edit the same file simultaneously. Codex assigns separate files or worktrees (`hermes -w`).
   - Task scopes are bounded with read-only requirements for reviewers.
4. **Execution & Parallelism**:
   - Codex runs external agents asynchronously or via subshells while actively continuing core architectural implementation.
   - External processes communicate back via stdout/JSON.
5. **Conflict Resolution & Synthesis**:
   - Codex verifies exit codes, parses outputs, and inspects git diffs.
   - Conflicting proposals are resolved using concrete facts: running unit tests (`pytest`, `npm test`) or checking source code contracts.
   - Codex produces the unified final deliverable and attributes credit strictly to agents that actually executed work.

---

## 6. Target Vault Structure & File Architecture

To fulfill Milestone E3 with zero defects, zero broken wikilinks, and 100% graph connectivity, the following files and cross-links must be established:

### 6.1 Target File Inventory

```
D:\obsidian file\
├── AI Sozlangan Miyyasi.md                       [UPDATED: Master Brain linking all new profiles & resources]
├── 20 Areas\
│   ├── 20 Areas.md                               [UPDATED: MOC indexing all new agent profiles]
│   ├── 20 Areas MOC.md                           [UPDATED: Full index linking new profiles]
│   └── Agent Profiles\
│       ├── Antigravity 1.md                      [EXISTING]
│       ├── Antigravity 2.md                      [EXISTING]
│       ├── Codex LLM Assistant.md                [EXISTING / HARDENED]
│       ├── Concurrency & Sync Protocol.md        [EXISTING]
│       ├── Autonomous Decision Protocols.md      [EXISTING]
│       ├── Nous Hermes.md                        [NEW: Complete CLI profile for Hermes]
│       ├── GitHub Copilot.md                     [NEW: Complete CLI profile for Copilot]
│       ├── OpenCode CLI.md                       [NEW: Complete CLI profile for OpenCode]
│       ├── Google Antigravity CLI.md             [NEW: Complete CLI profile for agy]
│       └── Ruflo Swarm.md                        [NEW: Complete CLI profile for Ruflo]
├── 30 Resources\
│   ├── 30 Resources.md                           [UPDATED: MOC indexing new resources]
│   ├── 30 Resources MOC.md                       [UPDATED: Full index linking new resources]
│   ├── AI Agent Ecosystem Map.md                 [NEW: Master architecture & /multt protocol guide]
│   ├── Free LLM Models Registry.md               [NEW: 22+ models, limits, endpoints, strengths]
│   └── Codex Skills Encyclopedia.md              [NEW: Comprehensive guide for all 14 skills]
└── 50 Templates\
    ├── Agent Profile Template.md                 [EXISTING]
    ├── New Agent Integration Template.md         [NEW: Standardized onboarding template]
    ├── Model Evaluation Template.md              [NEW: Benchmarking and scorecard template]
    └── Security Audit Template.md                [NEW: White-hat defense and hardening template]
```

### 6.2 Mandatory Frontmatter & Backlink Requirements
Every single new markdown note must strictly conform to:
1. **YAML Frontmatter**:
   ```yaml
   ---
   title: "<Descriptive Title with Emoji>"
   version: "1.0.0"
   created: 2026-09-12
   updated: 2026-09-12
   status: active
   type: <agent-profile | resource-guide | template | operational-manual>
   tags:
     - <relevant-tag-1>
     - <relevant-tag-2>
   language: "uz-UZ, en-US"
   ---
   ```
2. **Master Brain Backlink**:
   - Must contain an explicit wikilink to `[[AI Sozlangan Miyyasi]]` (e.g. in navigation header and footer).
3. **Graph Invariants**:
   - **Zero Orphans**: Every new file must be linked from at least one MOC (`20 Areas.md`, `30 Resources.md`, `AI Sozlangan Miyyasi.md`).
   - **Zero Broken Links**: Target names inside `[[...]]` must match existing or newly created files verbatim.
   - **UTF-8 Encoding**: Pure UTF-8 without BOM.

---

## 7. Verification Method & Test Assurance

Downstream implementers and reviewers can verify the complete implementation using the existing and expanded 5-tier test harness:

1. **Vault Graph & Orphan Validation**:
   ```powershell
   python -m unittest tests.e2e.test_tier5_adversarial.TestAdversarialVaultGraphConnectivity.test_adv105_zero_orphan_incoming_links_vault_wide
   ```
2. **Broken Link Audit**:
   ```powershell
   python -m unittest tests.e2e.test_tier5_adversarial.TestAdversarialVaultGraphConnectivity.test_adv103_vault_wide_broken_wikilink_audit
   ```
3. **Full 5-Tier Test Suite**:
   ```powershell
   python .agents/test_track/run_e2e_tests.py
   python -m unittest discover -s tests/e2e
   ```
4. **Git Discipline Compliance**:
   ```powershell
   git status
   git log -n 5 --oneline
   ```
