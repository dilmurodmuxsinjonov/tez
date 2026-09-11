# Original User Request

## Initial Request — 2026-09-11T18:29:55Z

Build a complete, modular, and fault-tolerant Universal AI Second Brain ("AI Sozlangan Miyyasi") inside the user's Obsidian vault (`D:\obsidian file`). This central brain will unify and serve as the single source of truth for all user AI assistants (Antigravity 1, Antigravity 2, OpenAI Codex, and others), incorporating structured topic memory from the Gemini Topics system architecture, complete user rules, coding practices, environment configurations, and active project states.

Working directory: D:\obsidian file
Integrity mode: development

## Requirements

### R1. Master Brain Entrypoint (`AI Sozlangan Miyyasi.md`)
Create a master navigation and operational protocol note at the root of the Obsidian vault (`D:\obsidian file\AI Sozlangan Miyyasi.md`). It must serve as the primary directive and indexing center that any AI (Antigravity 1, Antigravity 2, Codex) reads on startup to instantly understand the user's identity, active priorities, global coding rules, and shared operational workflows.

### R2. Gemini Topics Memory Architecture & State Tracking
Implement a structured memory engine inspired by the Gemini Topics architecture. For each core domain and active project, record:
- **Latest State Summary**: Current milestones, progress, and where work left off.
- **Goals & Decisions Log**: Major architectural and design decisions already made.
- **Interaction Dynamics**: Contextual greeting anchors and low-pressure next steps matching the 10 defined communication styles without hallucinating or assuming unverified state.
- **Topic Memory Blocks**: Organized, human-readable structured context blocks with emoji-tagged sections.

### R3. Universal AI Agent Profiles & Sync Protocols
Define clear operation protocols for all connected AI instances:
- **Antigravity 1**: Primary Google account session and environment role.
- **Antigravity 2**: Secondary isolated Google account session and environment role.
- **Codex / LLM Assistants**: Role, tool execution, and code synthesis protocols.
- **Concurrency & Conflict Avoidance**: Clear file-locking and atomic updating guidelines so multiple agents working on the vault do not overwrite each other's updates.

### R4. Complete Context & Knowledge Migration
Migrate and systematically index all existing capabilities, user rules, and active workspace projects:
- User-specific Git workflow: Automatic `git init`, `git status`, incremental descriptive commits, and automatic branching (`feature/...` or `fix/...`) for non-trivial modifications.
- Local software toolchain: Node.js (v22), PowerShell, Python, Electron development, Git.
- Active project profiles: MobCreatorWebApp, NagoyaCastle/Osaka Castle, The_AI_Pipeline (scripts & architecture), Orol Shahar, and Medical Clinic projects.
- Existing Obsidian infrastructure: Connect with `10 Projects`, `20 Areas`, `30 Resources\Agent Skills`, and `50 Templates`.

### R5. Interconnected Wikilink Knowledge Graph
Ensure that every sub-note, project memory, and rule is cross-linked using bidirectional Obsidian wikilinks (`[[...]]`) with valid paths and relevant YAML frontmatter tags, ensuring a 100% clean graph without broken links or orphaned critical concepts.

## Acceptance Criteria

### Master Brain & Architecture
- [ ] `D:\obsidian file\AI Sozlangan Miyyasi.md` exists, contains valid YAML frontmatter, and provides an end-to-end index for all AI assistants.
- [ ] Operating protocols for Antigravity 1, Antigravity 2, and Codex are explicitly defined with instructions on reading and writing back to memory.

### Gemini Topics Memory Fidelity
- [ ] Structured topic memory sections exist for all primary active user domains with Latest State, Goals, Decisions, and Suggested Next Steps.
- [ ] All suggestions follow the strict action-verb requirement, ~75 character limit, and temporal relevance criteria.

### Knowledge & System Integrity
- [ ] User's global Git workflow rules (`RULE[user_global]`) are verbatim documented and enforced as a mandatory guideline for all AIs.
- [ ] Active local projects and agent skills (`30 Resources\Agent Skills`) are fully referenced and cross-linked.
- [ ] Programmatic validation confirms zero broken wikilinks in newly created files and 100% valid Markdown syntax.
