# Task Assignment: E2E Testing Track Orchestration & Suite Creation

## Working Directory
`D:\obsidian file\.agents\test_track`

## Objective
Design and implement a comprehensive, opaque-box, requirement-driven E2E test suite for the Universal AI Second Brain (`AI Sozlangan Miyyasi`) at `D:\obsidian file`.
Publish `TEST_INFRA.md` at project root (`D:\obsidian file\TEST_INFRA.md` or `.agents/TEST_INFRA.md`) and when tests are ready, publish `TEST_READY.md`.

## Test Methodology & Requirements
Follow the 4-tier systematic approach:
1. **Tier 1 - Feature Coverage**:
   - Verify every feature from `ORIGINAL_REQUEST.md` and `PROJECT.md § Feature Inventory` (at least 5 test cases per core feature category).
   - Valid YAML frontmatter parsing, Master Brain entrypoint presence, toolchain documentation, Git rules presence.
2. **Tier 2 - Boundary & Corner Cases**:
   - Case-sensitivity of wikilinks, whitespace in wikilinks (`[[10 Projects/10 Projects]]`), empty/missing files, path resolution, unicode characters (Uzbek characters: o', g', sh, ch).
   - Strict action-verb verification in Suggested Next Steps.
   - Character count limits on suggestions (60-85 chars, target ~75 chars).
   - 5 blank lines visual separation preceding Topic Memory Code Blocks.
3. **Tier 3 - Cross-Feature Combinations (Pairwise)**:
   - Master Brain linking to Agent Profiles, Agent Profiles citing Concurrency Protocols.
   - Master Brain linking to Active Projects, Active Projects linking back to Master Brain.
   - MOC notes resolving folder links (`[[10 Projects/]]` -> `10 Projects.md`).
4. **Tier 4 - Real-World Workload Scenarios**:
   - Simulate an AI assistant startup: read `AI Sozlangan Miyyasi.md`, parse user persona, verify Git rules (`RULE[user_global]`), select active project (`MobCreatorWebApp`), parse Latest State, select Suggested Next Step, test concurrency lock acquisition/release simulation.

## Test Architecture & Deliverables
1. Automated Test Runner script: `D:\obsidian file\.agents\test_track\run_e2e_tests.py` (or Node.js script).
2. Produce test report and when suite is complete, write:
   `D:\obsidian file\TEST_READY.md` (and copy to `.agents/TEST_READY.md`).
3. Complete handoff report at `D:\obsidian file\.agents\test_track\handoff.md`.

## Input Files
- `D:\obsidian file\.agents\ORIGINAL_REQUEST.md`
- `D:\obsidian file\.agents\PROJECT.md`
- `D:\obsidian file\.agents\spec_miner_topics_agents\findings.md`
- `D:\obsidian file\.agents\explorer_survey_projects\findings.md`
- `D:\obsidian file\.agents\explorer_survey_vault\findings.md`

## 2026-09-11T18:36:37Z
You are the E2E Test Track Writer.
Your working directory is: D:\obsidian file\.agents\test_track
Read your task assignment in: D:\obsidian file\.agents\test_track\DISPATCH.md
Read the authoritative user request in: D:\obsidian file\.agents\ORIGINAL_REQUEST.md
Read the project architecture in: D:\obsidian file\.agents\PROJECT.md

Build the comprehensive, opaque-box E2E test suite (Tiers 1-4) for the Universal AI Second Brain.
Create TEST_INFRA.md, write the automated test runner (Python or Node.js), and when the suite is published and ready, output TEST_READY.md.
Write your handoff report to: D:\obsidian file\.agents\test_track\handoff.md
Send a completion message to the Orchestrator when done.

