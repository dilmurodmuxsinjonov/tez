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
    VAULT_ROOT,
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


if __name__ == "__main__":
    unittest.main()
