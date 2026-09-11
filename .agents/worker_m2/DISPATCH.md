# Task Assignment: Milestone 2 Implementation (Universal AI Agent Profiles & Concurrency)

## Working Directory
`D:\obsidian file\.agents\worker_m2`

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Objective
Implement Milestone 2 (Universal AI Agent Profiles & Concurrency) in `D:\obsidian file\20 Areas\Agent Profiles\`:
1. **`Antigravity 1.md`**:
   - YAML frontmatter (`tags: [agent-profile, antigravity, primary]`, `type: agent-profile`, `role: chief-architect`, `status: active`).
   - Role & Account: Primary Google account session (`dilmurodmuhsinjanov910@gmail.com`), default USERPROFILE (`C:\Users\dilmu`), master vault architect, interactive planner, memory maintainer.
   - Startup & memory write-back protocol reference.
   - Concurrency locking rules and link to `[[Concurrency & Sync Protocol]]`.
   - Link to `[[AI Sozlangan Miyyasi]]` and `[[RULE[user_global]]]`.
2. **`Antigravity 2.md`**:
   - YAML frontmatter (`tags: [agent-profile, antigravity, secondary, sandbox]`, `type: agent-profile`, `role: sandbox-tester`, `status: active`).
   - Role & Account: Secondary isolated Google account session (`C:\Users\dilmu\AntigravityProfile2`, launched via VBS), sandbox tester, clean-room parallel builder.
   - Operates on dedicated isolated git branches (`feature/antigravity2-...`).
   - Concurrency locking rules and link to `[[Concurrency & Sync Protocol]]`.
   - Link to `[[AI Sozlangan Miyyasi]]` and `[[RULE[user_global]]]`.
3. **`Codex LLM Assistant.md`**:
   - YAML frontmatter (`tags: [agent-profile, codex, autonomous, cli]`, `type: agent-profile`, `role: code-synthesis`, `status: active`).
   - Role & Toolchain: CLI autonomous execution via `opencode.ps1` (`opencode run ... --auto`) and `codex.exe`, test runner, bound by interface contracts.
   - Logs execution outputs to `.data/agents/<task>/`.
   - Concurrency locking rules and link to `[[Concurrency & Sync Protocol]]`.
   - Link to `[[AI Sozlangan Miyyasi]]` and `[[RULE[user_global]]]`.
4. **`Concurrency & Sync Protocol.md`**:
   - YAML frontmatter (`tags: [protocol, concurrency, file-locking, synchronization]`, `type: protocol`, `status: active`).
   - Directory initialization: ensure `.agents/locks/` exists.
   - Lockfile schema: `.agents/locks/<hash>.lock` where `<hash>` is SHA-256 of target relative path (e.g. `10 Projects/MobCreatorWebApp.md`).
   - Lockfile contents: JSON with `agent_id`, `pid`, `timestamp`, `expires_at` (300s TTL), `target_path`.
   - Stale lock expiration (>300s) and recovery protocol with logging to `.agents/audit.log`.
   - Two-stage atomic write pattern: `<file>.tmp.<agent_id>` -> syntax validation -> atomic rename/replace.
   - Windows retry loop: 3 attempts with 50-100ms jitter to handle transient `PermissionError` (WinError 32) from indexing/antivirus.
   - Git branch partitioning: automatic branching per `RULE[user_global]`.
   - Link back to `[[AI Sozlangan Miyyasi]]`.

## Write Ownership
You exclusively own:
- `D:\obsidian file\20 Areas\Agent Profiles\Antigravity 1.md`
- `D:\obsidian file\20 Areas\Agent Profiles\Antigravity 2.md`
- `D:\obsidian file\20 Areas\Agent Profiles\Codex LLM Assistant.md`
- `D:\obsidian file\20 Areas\Agent Profiles\Concurrency & Sync Protocol.md`
- Directory `.agents\locks\` (create if not exists)

## Verification & Git Commit
- Run `python run_e2e_tests.py` (must pass 100%).
- Run `python .agents\explorer_survey_projects\validate_vault.py` (0 syntax errors, wikilinks to M2 profiles now resolve cleanly).
- Commit changes per `RULE[user_global]` (`git add .`, `git commit -m "feat(m2): implement Universal AI Agent Profiles and Concurrency Protocol"`).
## 2026-09-11T18:55:13Z
You are the Milestone 2 Worker (Universal AI Agent Profiles & Concurrency).
Your working directory is: D:\obsidian file\.agents\worker_m2
Read DISPATCH.md in your working directory.
Read D:\obsidian file\.agents\ORIGINAL_REQUEST.md, PROJECT.md, and spec_miner_topics_agents\findings.md.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Implement:
1. D:\obsidian file\20 Areas\Agent Profiles\Antigravity 1.md
2. D:\obsidian file\20 Areas\Agent Profiles\Antigravity 2.md
3. D:\obsidian file\20 Areas\Agent Profiles\Codex LLM Assistant.md
4. D:\obsidian file\20 Areas\Agent Profiles\Concurrency & Sync Protocol.md
Ensure directory .agents\locks exists.
Run tests and validators, commit changes with descriptive git message per RULE[user_global].
Write handoff report to handoff.md and send message to Orchestrator.
