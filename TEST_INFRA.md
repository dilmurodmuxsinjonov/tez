# Universal AI Second Brain ? E2E Test Infrastructure Specification

**Document Version**: 1.0.0  
**Test Track**: E2E Verification & System Integrity (Tiers 1?4)  
**Target Vault**: `D:\obsidian file`  
**Test Suite Directory**: `D:\obsidian file\tests\e2e`  
**Automated Runner**: `D:\obsidian file\run_e2e_tests.py` and `D:\obsidian file\.agents\test_track\run_e2e_tests.py`  

---

## 1. Test Architecture Overview

The Universal AI Second Brain test suite is designed as an **opaque-box, requirement-driven, multi-tier validation system**. It tests the system against the formal specifications documented in `ORIGINAL_REQUEST.md`, `PROJECT.md`, and `findings.md` from specification mining.

The test infrastructure is built purely on **Python 3.12 Standard Library** (`unittest`, `re`, `json`, `pathlib`, `hashlib`, `time`, `tempfile`, `dataclasses`, `typing`), guaranteeing zero external third-party dependencies and 100% deterministic cross-platform execution on Windows PowerShell and POSIX shells.

```
                  ???????????????????????????????????????????????????
                  ?            run_e2e_tests.py (CLI)               ?
                  ???????????????????????????????????????????????????
                                           ?
         ???????????????????????????????????????????????????????????????
         ?                   ?                     ?                   ?
   [Tier 1: Feature]  [Tier 2: Boundary]   [Tier 3: Pairwise]  [Tier 4: Workload]
   ? Master Brain     ? Wikilink paths     ? Master ? Agents   ? Assistant Boot
   ? Git & Toolchain  ? Unicode & UTF-8    ? Master ? Projects ? Topic State Load
   ? Agent Profiles   ? Action-verb syntax ? MOC ? Folders     ? Lock Acquisition
   ? Gemini Memory    ? ~75-char limit     ? Profiles ? Tools  ? Greeting Selection
   ? PARA & Skills    ? 5 blank lines      ? Vault Graph Scan  ? 2-Stage Atomic Write
                      ? Stale Lock Timeout ? ADR Author Link   ? Collision Backoff
```

---

## 2. Test Hierarchy (4-Tier Systematic Approach)

### Tier 1: Feature Coverage (Core Requirements)
Verifies the presence, schema compliance, and content integrity of all features from `PROJECT.md ? Feature Inventory`:
- **Category 1 (Master Brain Entrypoint)**:
  - Valid YAML frontmatter (`tags`, `type: master-brain`, `updated`, `status: active`).
  - Universal AI Startup Directive (5 startup steps, 4 write-back steps).
  - User identity anchor (`dilmurodmuxsinjonov`, Uzbek for interaction, English for code).
  - Agent Fleet table linking to all 4 agent notes.
  - Active Projects table linking to all 5 project notes.
- **Category 2 (Git Workflow & Toolchain)**:
  - Verbatim inclusion and enforcement of `RULE[user_global]`.
  - Documentation of verified binaries: Node.js (v22), Python (3.12), PowerShell (5.1), Git (2.54), Electron.
  - GitHub username and email matching user profile.
- **Category 3 (Universal AI Agent Profiles & Concurrency)**:
  - Dedicated profiles for Antigravity 1, Antigravity 2, Codex LLM Assistant.
  - Dedicated `Concurrency & Sync Protocol.md` with SHA-256 lockfile schema, 300s TTL, and atomic two-stage write-rename.
- **Category 4 (Gemini Topics Memory & Active Projects)**:
  - 5 project notes in `10 Projects/` (`MobCreatorWebApp.md`, `NagoyaCastle.md`, `The_AI_Pipeline.md`, `Orol Shahar Qirollik.md`, `Doctor A Med Clinic.md`).
  - Required sections: Latest State Summary, Goals & Decisions Log (ADR), Interaction Dynamics (10 styles), Suggested Next Steps, Topic Memory Code Block.
- **Category 5 (Obsidian PARA MOCs & Skills Hub)**:
  - MOC notes: `00 Inbox.md`, `10 Projects.md`, `20 Areas.md`, `30 Resources.md`, `40 Archives.md`.
  - Skills Hub integration: `30 Resources/Agent Skills/Skills Dashboard.md` linking to 6 skill guides and `git-workflow.md`.
  - Templates integration: `50 Templates/Daily Note Template.md`, `Project Template.md`, `Resource Template.md`.

### Tier 2: Boundary & Corner Cases
Probes edge cases, string limits, formatting delimiters, and timing boundaries:
- **Case-sensitivity and Whitespace in Wikilinks**: Verifies resolution with spaces (`[[10 Projects/10 Projects]]`), alias pipes (`[[Target|Display]]`), and subfolder paths.
- **Unicode & Encoding**: Confirms valid UTF-8 without BOM; correct handling of Uzbek Latin characters (`o?`, `g?`, `sh`, `ch`) and Cyrillic notes.
- **Suggested Next Steps Rules**:
  - Starts with an approved imperative action verb (`Review`, `Inspect`, `Refactor`, `Draft`, `Implement`, `Audit`, `Benchmark`, `Verify`, `Integrate`, `Configure`, `Test`, `Document`, `Extract`).
  - Length strictly constrained to 60?85 characters (target ~75 characters).
  - Rejection of passive voice and non-AI-actionable external tasks.
  - Quantity strictly 2 to 4 items.
- **Visual Separation**: Exactly 5 blank lines (`




`) separating conversational next steps from the Topic Memory Code Block.
- **Concurrency Edge Cases**:
  - Stale lock expiration recovery: locks older than 300 seconds are safely broken and audited.
  - Corrupt lockfile detection and recovery.
  - Atomic two-stage temporary file cleanup on failure.

### Tier 3: Cross-Feature Combinations (Pairwise Verification)
Tests the interconnectivity and contract consistency between disparate modules:
- **Master Brain ? Agent Profiles**: Reciprocal links and naming alignment.
- **Master Brain ? Active Projects**: Master indexes projects, projects link back to Master Brain.
- **MOCs ? Folder Hierarchy**: Folder links (`[[10 Projects/]]`, `[[00 Inbox/]]`) resolve to valid MOC notes.
- **Agent Profiles ? Concurrency & Toolchain**: Codex note cites `opencode.ps1` and `codex.exe`; all agents cite `.agents/locks/`.
- **Project Notes ? Agent Profiles**: ADR logs cite valid agent authors (`Antigravity 1`, `Antigravity 2`, `Codex`).
- **Vault Graph Integrity**: Full graph scan confirming 0 broken wikilinks in newly created files.

### Tier 4: Real-World Workload Scenarios
Simulates realistic end-to-end multi-agent operational workflows:
- **Scenario 1: AI Assistant Cold Startup & Persona Ingestion**:
  Reads `AI Sozlangan Miyyasi.md`, extracts user identity, enforces language separation, verifies toolchain, checks Git rules.
- **Scenario 2: Project Targeting & Context Resumption**:
  Selects active project, loads Latest State Summary, parses ADRs, matches current context to 1 of 10 Greeting Styles, evaluates Suggested Next Steps.
- **Scenario 3: Concurrency Locking & Atomic State Update**:
  Simulates Agent 1 acquiring lock (`.agents/locks/<hash>.lock`), performing atomic two-stage write (`.tmp` -> validate -> rename), and releasing lock.
- **Scenario 4: Multi-Agent Collision & Stale Lock Recovery**:
  Agent 1 holds lock; Agent 2 attempts write, detects collision, backs off. Agent 1 lock expires (>300s); Agent 2 breaks stale lock, logs audit event, claims lock, and finishes write.

---

## 3. Test Runner CLI & Execution

### Execution Commands
Run the complete test suite from PowerShell:

```powershell
# From project root
python run_e2e_tests.py

# Or directly from the test track directory
python ".agents/test_track/run_e2e_tests.py"

# Run a specific tier only
python run_e2e_tests.py --tier 1
python run_e2e_tests.py --tier 2
python run_e2e_tests.py --tier 3
python run_e2e_tests.py --tier 4

# Output JSON summary report
python run_e2e_tests.py --json test_report.json
```

### Exit Codes
- `0`: All executed tests PASSED.
- `1`: One or more tests FAILED or ERRORED.

---

## 4. Test Infrastructure Deliverables Table

| Deliverable | Path | Purpose |
| :--- | :--- | :--- |
| **Test Infrastructure Spec** | `TEST_INFRA.md` & `.agents/TEST_INFRA.md` | Authoritative definition of test architecture and contracts |
| **Automated Test Runner** | `run_e2e_tests.py` | Top-level CLI entrypoint for running test tiers |
| **Track Test Runner** | `.agents/test_track/run_e2e_tests.py` | Standalone runner entrypoint for the test_track agent |
| **Modular Test Suite** | `tests/e2e/` | Structured test modules covering Tiers 1 through 4 |
| **Concurrency Simulator** | `tests/e2e/concurrency_sim.py` | Standalone engine simulating multi-agent file locks and atomic writes |
| **Vault Graph Validator** | `tests/e2e/vault_validator.py` | Opaque-box parser verifying wikilinks, frontmatter, and formatting |
| **Test Readiness Report** | `TEST_READY.md` & `.agents/TEST_READY.md` | Published scorecard and readiness declaration |

---

## 🧭 Navigatsiya
- 🧠 **[[AI Sozlangan Miyyasi|AI Sozlangan Miyyasi — Universal AI Second Brain]]**
- 🗄️ **[[40 Archives/40 Archives MOC|40 Archives MOC]]**

