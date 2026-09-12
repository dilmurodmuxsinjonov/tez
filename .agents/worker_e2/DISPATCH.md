## 2026-09-12T12:41:46Z

You are worker_e2, an implementation worker.
Your working directory is: D:\obsidian file\.agents\worker_e2
The project root is: D:\obsidian file

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

You MUST read the following authoritative files first:
- D:\obsidian file\.agents\ORIGINAL_REQUEST.md (specifically ## Follow-up — 2026-09-12T12:30:39Z)
- D:\obsidian file\.agents\PROJECT.md
- D:\obsidian file\.agents\explorer_e3_agents\analysis.md
- D:\obsidian file\.agents\explorer_e3_vault\analysis.md
- D:\obsidian file\.agents\worker_e1\handoff.md

Your Mission (Milestone E2: Master Resource Guides, Templates & Brain Sync):
1. Create 3 Master Resource Guides in `D:\obsidian file\30 Resources\`:
   - `AI Agent Ecosystem Map.md`: Comprehensive guide and architecture diagram showing the entire multi-agent ecosystem (Codex master orchestrator, Antigravity 1 & 2, Nous Hermes, GitHub Copilot, OpenCode CLI, Ruflo Swarm), the `/multt` multi-agent coordination protocol from C:\Users\dilmu\.codex\AGENTS.md and tashqi_ai_agentlar skill, delegation matrix, role boundaries, failure handling, and backlink to `[[AI Sozlangan Miyyasi]]`.
   - `Free LLM Models Registry.md`: Catalog all 22 free LLM models across OpenRouter (8), Groq (2), Google AI Studio (2), NVIDIA NIM (3), OpenCode Zen (4), GitHub Models (2), Cloudflare Workers AI (1). Include Model IDs, provider, context window, rate limits, strengths, API key URLs, and backlink to `[[AI Sozlangan Miyyasi]]`.
   - `Codex Skills Encyclopedia.md`: Catalog all 14 custom & system skills from C:\Users\dilmu\.codex\skills/ (`chuqur_muhandislik`, `kontekst_muhit_tarixi`, `kontekst_psixologik_profil`, `kontekst_strategik_reja`, `loyihani_rejalashtirish`, `loyiha_infratuzilmasi_qoidalari`, `memor_shaxsiyati`, `oq_haker_muhiti`, `oq_haker_vositalari`, `veb_dasturlash`, `xavfsizlik_qoidalari`, `tashqi_ai_agentlar`, `review-agent`, `skill-creator`). Document their purposes, directives, execution rules, and backlink to `[[AI Sozlangan Miyyasi]]`.
   Each note MUST have valid YAML frontmatter, rich technical sections, and direct backlink to `[[AI Sozlangan Miyyasi]]`.

2. Create 3 Workflow Templates in `D:\obsidian file\50 Templates\`:
   - `New Agent Integration Template.md`: Aliases `["New Agent Integration", "New Agent Integration Template"]`, standardized schema for adding future AI agents (executable path, CLI commands, model bindings, rate limits, role, test verification), backlink `[[AI Sozlangan Miyyasi]]`.
   - `Model Evaluation Template.md`: Aliases `["Model Evaluation", "Model Evaluation Template"]`, standardized benchmark and evaluation schema for testing new LLMs (context length, reasoning score, code generation score, speed/latency, cost/free limits), backlink `[[AI Sozlangan Miyyasi]]`.
   - `Security Audit Template.md`: Aliases `["Security Audit", "Security Audit Template"]`, white-hat vulnerability checklist aligned with ethical hacking skills (credential leaks, permission checks, sandbox barriers, prompt injection, atomic file lock checks), backlink `[[AI Sozlangan Miyyasi]]`.
   Each template must follow existing template structure (`<Name> Template.md`) and have valid YAML frontmatter.

3. Update Master Brain `AI Sozlangan Miyyasi.md` & `Dashboard.md`:
   - In `AI Sozlangan Miyyasi.md`:
     - Update Agent Fleet table to index all CLI agents (`[[Nous Hermes]]`, `[[GitHub Copilot]]`, `[[OpenCode CLI]]`, `[[Google Antigravity CLI]]`, `[[Ruflo Swarm]]`).
     - Update Toolchains table with their exact paths/scripts.
     - Add Resource Guides entries: `[[30 Resources/AI Agent Ecosystem Map\|AI Agent Ecosystem Map]]`, `[[30 Resources/Free LLM Models Registry\|Free LLM Models Registry]]`, `[[30 Resources/Codex Skills Encyclopedia\|Codex Skills Encyclopedia]]` (use escaped pipes `\|` in markdown tables).
     - Add Templates entries: `[[50 Templates/New Agent Integration Template\|New Agent Integration]]`, `[[50 Templates/Model Evaluation Template\|Model Evaluation]]`, `[[50 Templates/Security Audit Template\|Security Audit]]` (use escaped pipes `\|`).
   - In `Dashboard.md`:
     - Add links to the new agents, resources, and templates.

4. Update Dual-MOCs:
   - `30 Resources/30 Resources.md` AND `30 Resources/30 Resources MOC.md`: Register all 3 new resource notes with wikilinks.
   - `00 Inbox/00 Inbox.md` AND `00 Inbox/00 Inbox MOC.md`: Ensure `2026-09-12.md` is linked to reinforce in-degree.
   - In `20 Areas/Agent Profiles/` notes created in E1, upgrade any inline code references to the 3 new resource guides to active wikilinks now that the notes exist.

5. Enforce Zero Broken Links & Zero Orphans:
   - Verify every new note has incoming links from Master Brain and its respective MOCs.
   - Run `python -m unittest discover -s tests/e2e` and `python run_e2e_tests.py` to ensure 100% PASS with zero broken links and zero orphans.

6. Perform Git atomic commit 2 following RULE[user_global]:
   - Stage created resources, templates, and updated MOCs / Master Brain / Dashboard:
     `git add "30 Resources/" "50 Templates/" "AI Sozlangan Miyyasi.md" "Dashboard.md" "00 Inbox/" "20 Areas/Agent Profiles/"`
   - Commit with message: `feat(resources-templates): add ecosystem map, model registry, skills encyclopedia, templates, and sync master brain`

7. Document your work in `D:\obsidian file\.agents\worker_e2\report.md` and write a structured `handoff.md`. When done, message parent.
