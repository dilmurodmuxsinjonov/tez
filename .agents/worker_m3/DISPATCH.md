# Task Assignment: Milestone 3 Implementation (Gemini Topics Memory Architecture & Active Projects)

## Working Directory
`D:\obsidian file\.agents\worker_m3`

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Objective
Implement Milestone 3 (Gemini Topics Memory Architecture & Active Projects) by creating all 5 active project memory files in `D:\obsidian file\10 Projects\`:
1. `MobCreatorWebApp.md` (Path: `C:\Users\dilmu\.gemini\antigravity\scratch\MobCreatorWebApp`, React 19, Three.js, R3F, procedural box modeler).
2. `NagoyaCastle.md` (Path: `C:\Users\dilmu\.gemini\antigravity\scratch\NagoyaCastle`, Minecraft Anvil chunks `region/*.mca`, `level.dat`, mediafire scraper).
3. `The_AI_Pipeline.md` (Path: `C:\Users\dilmu\.gemini\antigravity\scratch\The_AI_Pipeline`, 60 scripts UZ/EN, Gemini API, video automation, linked with `D:\youtube chennel 1\work_45min`).
4. `Orol Shahar Qirollik.md` (Path: `C:\Users\dilmu\OneDrive\Desktop\game23v1`, Express 5, Prisma 7, PostgreSQL, React 19, R3F, milestones V1-P1/P2 done, V1-P3 in progress).
5. `Doctor A Med Clinic.md` (Path: `C:\Users\dilmu\OneDrive\Desktop\DOCTOR A`, Next.js 16, Tailwind CSS v4, Prisma 5, SQLite, Material Clinical Precision theme, branch `feature/doctor-a-med-clinic-website`).

## Strict Requirements for Each File
Every single file must strictly include:
1. **YAML Frontmatter**: `title`, `version: 1.0.0`, `status: active`, `type: project-memory`, `tags: [project, active, gemini-topics]`, `project_path`, `tech_stack`.
2. **Backlinks**: Prominent reciprocal link to `[[AI Sozlangan Miyyasi]]`.
3. **📋 Latest State Summary**: 1–2 sentences (30–50 words) capturing exact current state, active branch, and immediate focus.
4. **💡 Goals & Decisions Log (ADR)**: Table or structured log with Context, Decision, Alternatives, Status, and Author Agent.
5. **💬 Interaction Dynamics (10 Communication Styles)**: Tailored greeting anchors for all 10 styles:
   - Thoughtful check-in
   - Progress celebration
   - Reflection prompt
   - Callback to detail
   - Invitation to continue
   - Anticipation builder
   - Gentle nudge
   - Curiosity spark
   - Empathetic acknowledgment
   - Low-pressure opener
6. **🎯 Suggested Next Steps**:
   - 2 to 4 curated options
   - Must start with an imperative action-verb (e.g. `Tekshirish`, `Ko'rib chiqish`, `Tahlil qilish`, `Qurish`, `Optimallashtirish`)
   - Strict ~75-character limit (each option between 60 and 85 characters)
   - Scope restricted to AI-actionable tasks
   - Temporally relevant to the project's current milestone
7. **Visual Separation**: Exactly 5 blank lines (`\n\n\n\n\n\n`) preceding the Topic Memory code block.
8. **Topic Memory Code Block**: Structured markdown code block with emoji-tagged sections:
   - `🎯 Active Goals`
   - `📋 Latest State`
   - `💡 Decisions Log`
   - `⚠️ Known Issues`
   - `💬 Relevant Conversations`
   - `🔗 Dependencies`
   Zero horizontal scrolling, zero information loss.

## Write Ownership
You exclusively own:
- `D:\obsidian file\10 Projects\MobCreatorWebApp.md`
- `D:\obsidian file\10 Projects\NagoyaCastle.md`
- `D:\obsidian file\10 Projects\The_AI_Pipeline.md`
- `D:\obsidian file\10 Projects\Orol Shahar Qirollik.md`
- `D:\obsidian file\10 Projects\Doctor A Med Clinic.md`

## Verification & Git Commit
- Run `python run_e2e_tests.py` (all tests must pass, especially `TC1.18–TC1.22`, `TC2.07–TC2.10`, `TC3.03`, `TC3.06`).
- Run `python .agents\explorer_survey_projects\validate_vault.py` (0 syntax errors; all 5 project links in `AI Sozlangan Miyyasi.md` lines 112–116 must now resolve cleanly).
- Commit changes per `RULE[user_global]` (`git add .`, `git commit -m "feat(m3): implement Gemini Topics Memory Architecture for all active projects"`).
- Write 5-component handoff report to `D:\obsidian file\.agents\worker_m3\handoff.md` and message Orchestrator.
