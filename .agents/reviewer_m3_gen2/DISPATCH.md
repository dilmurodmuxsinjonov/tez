## 2026-09-11T21:12:51Z

You are the Milestone 3 Reviewer (Generation 2) for the Universal AI Second Brain project in D:\obsidian file.
Your working directory is D:\obsidian file\.agents\reviewer_m3_gen2.
Your parent orchestrator conversation ID is f06f5f60-bc02-4012-b059-403c1e143ff2.

MANDATORY FIRST STEP:
Read D:\obsidian file\.agents\ORIGINAL_REQUEST.md, D:\obsidian file\.agents\PROJECT.md, D:\obsidian file\.agents\spec_miner_topics_agents\findings.md, and D:\obsidian file\.agents\worker_m3_gen2\handoff.md.

OBJECTIVE:
Independently review the 5 active project notes in D:\obsidian file\10 Projects\:
1. MobCreatorWebApp.md
2. NagoyaCastle.md
3. The_AI_Pipeline.md
4. Orol Shahar Qirollik.md
5. Doctor A Med Clinic.md

REVIEW CHECKLIST:
- YAML frontmatter completeness and validity.
- Reciprocal link to [[AI Sozlangan Miyyasi]].
- Latest State Summary (1-2 sentences, strictly between 30-50 words).
- Goals & Decisions Log (ADR) table structure (Sana, ADR ID, Decision & Scope, Rationale, Alternatives, Holat, Muallif).
- Interaction Dynamics matching all 10 defined communication styles with contextual # <Greeting Text> anchors.
- Suggested Next Steps (2-4 items, action-verb first, length strictly 60-85 characters).
- Exactly 5 blank lines visual separation before markdown code block.
- Emoji-tagged Topic Memory Code Block with all 6 required sections and zero horizontal scrolling (lines <= 80 chars).

VERIFICATION COMMANDS TO RUN:
1. python "D:\obsidian file\.agents\worker_m3\test_projects.py"
2. python "D:\obsidian file\.agents\explorer_survey_projects\validate_vault.py"
3. python "D:\obsidian file\run_e2e_tests.py"

OUTPUT:
Write your handoff report to D:\obsidian file\.agents\reviewer_m3_gen2\handoff.md following the Handoff Protocol.
Include an explicit verdict: APPROVE or REQUEST_CHANGES.
Send a completion message to your parent orchestrator with your verdict and findings.
