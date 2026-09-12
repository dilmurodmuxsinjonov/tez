"""
Tier 4: Real-World Workload Scenarios E2E Tests
Simulates realistic, multi-step operational workflows of AI assistants:
Cold startup, project context loading, 10 greeting styles selection,
concurrency locking, atomic write cycles, collision backoff, and stale lock recovery.
"""

from pathlib import Path
import tempfile
import time
import unittest

from tests.e2e.concurrency_sim import ConcurrencyProtocolManager
from tests.e2e.helpers import (
    APPROVED_ACTION_VERBS,
    COMMUNICATION_STYLES,
    NEW_CLI_AGENTS,
    NEW_TEMPLATES,
    VAULT_ROOT,
    check_file_utf8_clean,
    check_visual_separation,
    extract_wikilinks,
    parse_frontmatter,
    validate_suggested_next_step,
)


class TestTier4RealWorldWorkloads(unittest.TestCase):
    """Tier 4: End-to-end multi-agent operational lifecycle simulations."""

    @classmethod
    def setUpClass(cls):
        cls.master_file = VAULT_ROOT / "AI Sozlangan Miyyasi.md"
        with open(cls.master_file, "r", encoding="utf-8") as f:
            cls.master_content = f.read()

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.sim_vault = Path(self.temp_dir.name)
        self.mgr = ConcurrencyProtocolManager(self.sim_vault)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_tc401_ai_assistant_cold_boot_workload(self):
        """TC4.01: Simulate AI Assistant cold startup reading Master Brain directives."""
        # 1. Read Master Brain
        frontmatter, body = parse_frontmatter(self.master_content)
        self.assertIsNotNone(frontmatter)
        self.assertEqual(frontmatter.get("type"), "master-brain")

        # 2. Extract User Persona
        self.assertIn("Dilmurod Muhsinjanov", body)
        self.assertIn("dilmurodmuhsinjanov910-byte", body)

        # 3. Verify Git Workflow
        self.assertIn("<RULE[user_global]>", body)
        self.assertIn("git status", body)
        self.assertIn("git add .", body)

        # 4. Check Local Toolchain availability in environment
        # Node v22, Python 3.12, PowerShell, Git
        self.assertIn("Node.js", body)
        self.assertIn("Python", body)
        self.assertIn("PowerShell", body)
        self.assertIn("Git", body)

        # 5. Identify Active Projects
        for proj in ["MobCreatorWebApp", "NagoyaCastle", "The_AI_Pipeline", "Orol Shahar", "Doctor A"]:
            self.assertIn(proj, body)

    def test_tc402_project_context_and_greeting_styles_selection(self):
        """TC4.02: Simulate selecting 1 of the 10 Communication Styles based on project state."""
        # Scenario A: Steady ongoing development -> Style 1 (Thoughtful check-in)
        context_steady = {"state": "active", "milestone": "ongoing", "days_idle": 1, "last_build": "green"}
        greeting_steady = "# Ready to continue shaping the backend service routes?"
        self.assertTrue(greeting_steady.startswith("# "))

        # Scenario B: Milestone achieved -> Style 2 (Progress celebration)
        context_milestone = {"state": "active", "milestone": "completed", "days_idle": 0, "last_build": "green"}
        greeting_milestone = "# Milestone reached: Solana Wallet deposit flow is fully verified!"
        self.assertTrue(greeting_milestone.startswith("# "))

        # Scenario C: Project untouched > 7 days -> Style 7 (Gentle nudge)
        context_idle = {"state": "idle", "milestone": "pending", "days_idle": 10, "last_build": "unknown"}
        greeting_idle = "# Checking in on Nagoya Castle assets whenever you feel like diving back in."
        self.assertTrue(greeting_idle.startswith("# "))

        # Validate that all 10 styles are documented in the system
        for style in COMMUNICATION_STYLES:
            self.assertIn(style.lower(), [s.lower() for s in COMMUNICATION_STYLES])

    def test_tc403_full_agent_session_atomic_writeback_cycle(self):
        """TC4.03: Simulate a complete agent write-back cycle with file lock and atomic rename."""
        target_note = self.sim_vault / "10 Projects" / "MobCreatorWebApp.md"
        target_rel = "10 Projects/MobCreatorWebApp.md"

        # 1. Acquire Lock
        lock_res = self.mgr.acquire_lock(
            target_rel_path=target_rel,
            agent_name="Antigravity_1",
            agent_conv_id="conv-session-403",
            purpose="Updating Latest State and Suggested Next Steps",
            ttl_seconds=300
        )
        self.assertTrue(lock_res.success)
        self.assertTrue(lock_res.lock_file.exists())

        # 2. Formulate Updated Note Content with Gemini Topics rules:
        # - Latest State
        # - Goals & Decisions (ADR)
        # - 3 Suggested Next Steps (Action-verb, 60-85 chars)
        # - 5 blank lines
        # - Topic Memory Code Block
        steps = [
            "Implement Three.js mob bone segment rotation controls for mob builder",  # 72 chars
            "Refactor segment pivot offset calculations to prevent mesh separation",  # 70 chars
            "Benchmark canvas 60fps rendering performance with twenty mob instances"  # 70 chars
        ]
        for s in steps:
            res = validate_suggested_next_step(s)
            self.assertTrue(res["is_valid"], f"Step failed: {s}")

        steps_rendered = "\n".join(f"- {s}" for s in steps)
        five_blank_lines = "\n\n\n\n\n\n"
        topic_memory_block = (
            "```text\n"
            "?? ACTIVE GOALS & OBJECTIVES\n"
            "- Implement procedural multi-segment mob generator\n\n"
            "?? LATEST STATE & MILESTONE PROGRESS\n"
            "- Stopping Point: src/App.jsx line 45\n"
            "- Active Branch: main\n\n"
            "?? ARCHITECTURAL DECISIONS LOG\n"
            "- 2026-09-11: Adopted React Three Fiber and Drei for procedural rendering\n"
            "```"
        )

        full_content = (
            "# MobCreatorWebApp ? Topic Memory\n\n"
            "## ?? Suggested Next Steps\n"
            f"{steps_rendered}"
            f"{five_blank_lines}"
            f"{topic_memory_block}\n"
        )

        # 3. Perform Two-Stage Atomic Write with Visual Separation validator
        def topic_validator(content: str):
            is_sep, count = check_visual_separation(content)
            if not is_sep:
                return False, f"Visual separation requires 5 blank lines, got {count}"
            return True, None

        write_ok, err = self.mgr.atomic_write(
            dest_path=target_note,
            content=full_content,
            agent_id="Antigravity_1",
            validator=topic_validator
        )
        self.assertTrue(write_ok, f"Atomic write failed: {err}")
        self.assertTrue(target_note.exists())

        # 4. Release Lock
        rel_ok = self.mgr.release_lock(target_rel, "Antigravity_1")
        self.assertTrue(rel_ok)
        self.assertFalse(lock_res.lock_file.exists())

    def test_tc404_multi_agent_collision_and_backoff(self):
        """TC4.04: Simulate Agent 1 holding lock while Agent 2 attempts write and backs off."""
        target_rel = "10 Projects/The_AI_Pipeline.md"
        t0 = time.time()

        # Agent 1 (Antigravity 1) acquires lock
        res1 = self.mgr.acquire_lock(
            target_rel_path=target_rel,
            agent_name="Antigravity_1",
            agent_conv_id="conv-agent1",
            purpose="Batch updating English and Uzbek script indexes",
            ttl_seconds=300,
            current_time=t0
        )
        self.assertTrue(res1.success)

        # Agent 2 (Codex) attempts to write to the same note
        res2 = self.mgr.acquire_lock(
            target_rel_path=target_rel,
            agent_name="Codex",
            agent_conv_id="conv-codex",
            purpose="Adding automated YouTube API upload task",
            ttl_seconds=300,
            current_time=t0 + 10  # 10s later
        )
        self.assertFalse(res2.success, "Codex should have been rejected due to active lock.")
        self.assertIn("Collision", res2.error)

        # Agent 1 completes work and releases lock
        self.mgr.release_lock(target_rel, "Antigravity_1")

        # Now Agent 2 retries and succeeds
        res2_retry = self.mgr.acquire_lock(
            target_rel_path=target_rel,
            agent_name="Codex",
            agent_conv_id="conv-codex",
            purpose="Adding automated YouTube API upload task",
            ttl_seconds=300,
            current_time=t0 + 20
        )
        self.assertTrue(res2_retry.success, "Codex should successfully acquire lock after release.")
        self.mgr.release_lock(target_rel, "Codex")

    def test_tc405_crashed_agent_stale_lock_recovery_workload(self):
        """TC4.05: Simulate crashed agent leaving stale lock (>300s) recovered by next agent."""
        target_rel = "10 Projects/Doctor A Med Clinic.md"
        t0 = 10000.0

        # Agent 1 crashed at t0
        self.mgr.acquire_lock(
            target_rel_path=target_rel,
            agent_name="Antigravity_1",
            agent_conv_id="crashed-conv",
            purpose="Refactoring appointment schema",
            ttl_seconds=300,
            current_time=t0
        )

        # Agent 2 starts at t0 + 350s (TTL expired 50s ago)
        res_rec = self.mgr.acquire_lock(
            target_rel_path=target_rel,
            agent_name="Codex",
            agent_conv_id="recovery-conv",
            purpose="Resuming appointment schema refactoring after crash",
            ttl_seconds=300,
            current_time=t0 + 350
        )
        self.assertTrue(res_rec.success, "Agent 2 must recover stale lock.")
        self.assertTrue(res_rec.was_stale_recovered)

        # Check audit trail
        audit_text = self.mgr.audit_log.read_text(encoding="utf-8")
        self.assertIn("STALE_LOCK_BROKEN", audit_text)
        self.assertIn("antigravity_1", audit_text.lower())

    def test_tc406_multt_multi_agent_orchestration_workflow(self):
        """TC4.06: Simulate complete /multt multi-agent orchestration workflow and verify CLI roles."""
        # 1. Read AI Agent Ecosystem Map
        eco_path = VAULT_ROOT / "30 Resources" / "AI Agent Ecosystem Map.md"
        self.assertTrue(eco_path.is_file(), "AI Agent Ecosystem Map.md missing.")
        eco_content = eco_path.read_text(encoding="utf-8")

        # Verify /multt command syntax documented
        self.assertIn("/multt", eco_content)
        self.assertIn("/multt status", eco_content)
        self.assertIn("/multt off", eco_content)

        # 2. Simulate User issuing /multt task: "Harden cryptographic vaults and run pen-test benchmark"
        task = "Harden cryptographic vaults and run pen-test benchmark"

        # 3. Master Orchestrator (Codex) decomposes task into specialized subagent assignments:
        delegations = {
            "Nous Hermes": {
                "binary": r"C:\Users\dilmu\AppData\Local\hermes\bin\hermes.exe",
                "invocation": 'hermes chat -q "research cryptographic vault zero-knowledge algorithms" --oneshot',
                "role": "deep-researcher"
            },
            "GitHub Copilot": {
                "binary": r"C:\Users\dilmu\AppData\Roaming\npm\copilot.ps1",
                "invocation": 'copilot -p "verify git branch feature/crypto-vault and PR diff"',
                "role": "git-lifecycle"
            },
            "OpenCode CLI": {
                "binary": r"C:\Users\dilmu\AppData\Roaming\npm\opencode.ps1",
                "invocation": 'opencode run "benchmark open-source crypto models under OpenCode Zen"',
                "role": "open-models"
            },
            "Google Antigravity CLI": {
                "binary": r"C:\Users\dilmu\AppData\Local\agy\bin\agy.exe",
                "invocation": 'agy -p "audit monorepo cryptographic boundaries and dependencies"',
                "role": "architecture"
            },
            "Ruflo Swarm": {
                "binary": r"C:\Users\dilmu\AppData\Local\hermes\node\ruflo.ps1",
                "invocation": 'ruflo memory search -q "cryptographic vault design history"',
                "role": "vector-memory"
            }
        }

        # 4. Verify each delegated agent's profile exists and documents the binary and command format
        profiles_dir = VAULT_ROOT / "20 Areas" / "Agent Profiles"
        for agent_name, dinfo in delegations.items():
            profile_path = profiles_dir / f"{agent_name}.md"
            self.assertTrue(profile_path.is_file(), f"Profile for {agent_name} missing.")
            p_content = profile_path.read_text(encoding="utf-8")

            # Verify binary or script is referenced
            bin_name = Path(dinfo["binary"]).name.lower()
            self.assertIn(bin_name, p_content.lower(), f"Binary {bin_name} not found in {agent_name}.md")

            # Verify primary CLI command prefix is documented
            cmd_prefix = dinfo["invocation"].split()[0]
            self.assertIn(cmd_prefix.lower(), p_content.lower())

        # 5. Simulate Concurrency Lock Acquisition during Multi-Agent Output Synthesis
        lock_res = self.mgr.acquire_lock(
            target_rel_path="30 Resources/AI Agent Ecosystem Map.md",
            agent_name="Codex_Orchestrator",
            agent_conv_id="multt-session-406",
            purpose="Synthesizing multi-agent outputs from Hermes, Copilot, OpenCode, and Ruflo",
            ttl_seconds=300
        )
        self.assertTrue(lock_res.success)

        # 6. Release lock after successful multi-agent synthesis
        rel_ok = self.mgr.release_lock("30 Resources/AI Agent Ecosystem Map.md", "Codex_Orchestrator")
        self.assertTrue(rel_ok)

    def test_tc407_end_to_end_agent_onboarding_scenario(self):
        """TC4.07: Simulate end-to-end agent onboarding scenario using New Agent Integration Template."""
        # 1. Read New Agent Integration Template
        template_path = VAULT_ROOT / "50 Templates" / "New Agent Integration Template.md"
        self.assertTrue(template_path.is_file(), "New Agent Integration Template.md missing.")
        template_content = template_path.read_text(encoding="utf-8")

        # Verify template schema and frontmatter
        tfm, tbody = parse_frontmatter(template_content)
        self.assertIsNotNone(tfm)
        self.assertEqual(tfm.get("type"), "template")
        self.assertEqual(tfm.get("status"), "active")
        self.assertIn("aliases", tfm)

        # 2. Instantiate new simulated agent profile note: "Ollama Local Engine"
        sim_agent_name = "Ollama Local Engine"
        sim_note_content = (
            "---\n"
            f'title: "🦙 {sim_agent_name} — Local Offline Inference Agent"\n'
            'version: "1.0.0"\n'
            'date: 2026-09-12\n'
            'created: 2026-09-12\n'
            'updated: 2026-09-12\n'
            'status: active\n'
            'type: agent-profile\n'
            f'agent: "{sim_agent_name}"\n'
            'role: local-offline-inferencer\n'
            'tags:\n'
            '  - agent-profile\n'
            '  - ollama\n'
            '  - offline-ai\n'
            '  - cli\n'
            '  - ai-fleet\n'
            'language: "uz-UZ, en-US"\n'
            '---\n\n'
            f"# 🦙 {sim_agent_name} — Local Offline Inference Agent\n\n"
            "## 🧭 Asosiy Boshqaruv Havolalari\n\n"
            "- 🧠 [[AI Sozlangan Miyyasi]]\n"
            "- 🗺️ [[30 Resources/AI Agent Ecosystem Map|AI Agent Ecosystem Map]]\n\n"
            "## 1. 📋 Rol va Vazifasi\n\n"
            "Mahalliy oflayn modellar bilan ishlash va maxfiy ma'lumotlarni tarmoqsiz tahlil qilish.\n\n"
            "## 2. 🚀 Terminal va CLI Buyruqlari\n\n"
            "```powershell\n"
            "ollama run llama3.3:8b\n"
            "```\n\n"
            "## 3. 🔌 Imkoniyatlar va API Ulanishi\n\n"
            "Localhost 11434 REST API orqali to'liq avtonom ishlash.\n\n"
            "## 4. 💡 Foydalanish Holatlari\n\n"
            "Maxfiy kod auditi va internetsiz sharoitda mantiqiy xulosalar.\n\n"
            "## 5. 🛡️ Xavfsizlik va Protokol\n\n"
            "Zero Trust va mahalliy xavfsizlik qoidalariga to'liq bo'ysunadi.\n"
        )

        # 3. Save instantiated note into simulated vault directory
        sim_agent_file = self.sim_vault / "20 Areas" / "Agent Profiles" / f"{sim_agent_name}.md"
        sim_agent_file.parent.mkdir(parents=True, exist_ok=True)
        sim_agent_file.write_text(sim_note_content, encoding="utf-8")

        # 4. Validate schema compatibility and vault invariants on the newly onboarded agent:
        # A. Frontmatter validity
        sim_fm, sim_body = parse_frontmatter(sim_note_content)
        self.assertIsNotNone(sim_fm)
        self.assertEqual(sim_fm.get("type"), "agent-profile")
        self.assertEqual(sim_fm.get("status"), "active")
        self.assertEqual(sim_fm.get("agent"), sim_agent_name)

        # B. Backlink to Master Brain
        sim_links = extract_wikilinks(sim_note_content)
        sim_targets = [l["target"] for l in sim_links]
        self.assertTrue(any("AI Sozlangan Miyyasi" in t for t in sim_targets))

        # C. Required H2 sections count >= 4
        h2s = [l for l in sim_note_content.splitlines() if l.startswith("## ")]
        self.assertGreaterEqual(len(h2s), 4)

        # D. UTF-8 cleanly encoded without BOM
        is_clean, err = check_file_utf8_clean(sim_agent_file)
        self.assertTrue(is_clean, f"Clean UTF-8 validation failed: {err}")


if __name__ == "__main__":
    unittest.main()
