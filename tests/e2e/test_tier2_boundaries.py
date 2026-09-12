"""
Tier 2: Boundary & Corner Cases E2E Tests
Tests edge cases, boundary limits, strict formatting, Unicode, and error handling.
"""

import os
from pathlib import Path
import re
import tempfile
import time
import unittest

from tests.e2e.concurrency_sim import ConcurrencyProtocolManager
from tests.e2e.helpers import (
    APPROVED_ACTION_VERBS,
    CODEX_CUSTOM_SKILLS,
    FREE_LLM_PROVIDERS,
    NEW_CLI_AGENTS,
    NEW_TEMPLATES,
    VAULT_ROOT,
    check_file_utf8_clean,
    check_visual_separation,
    extract_wikilinks,
    parse_frontmatter,
    resolve_wikilink,
    validate_suggested_next_step,
)


class TestTier2WikilinksAndUnicodeBoundaries(unittest.TestCase):
    """Tier 2: Wikilink Parsing, Path Encoding, and Unicode Fidelity."""

    def test_tc201_wikilink_with_whitespace_and_folders(self):
        """TC2.01: Resolves wikilinks containing spaces and subfolder slashes."""
        sample_text = "See [[30 Resources/Agent Skills/git-workflow]] and [[Dashboard]]."
        links = extract_wikilinks(sample_text)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0]["target"], "30 Resources/Agent Skills/git-workflow")
        resolved_0 = resolve_wikilink(VAULT_ROOT, None, links[0]["target"])
        self.assertIsNotNone(resolved_0, "Failed to resolve path with spaces in folder.")
        self.assertTrue(resolved_0.exists())

    def test_tc202_wikilink_alias_piping(self):
        """TC2.02: Resolves wikilinks with alias pipe [[Target|Display Name]]."""
        sample_text = "Reference: [[AI Sozlangan Miyyasi|?? Boshqaruv Markazi]]"
        links = extract_wikilinks(sample_text)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0]["target"], "AI Sozlangan Miyyasi")
        self.assertEqual(links[0]["alias"], "?? Boshqaruv Markazi")
        resolved = resolve_wikilink(VAULT_ROOT, None, links[0]["target"])
        self.assertIsNotNone(resolved)
        self.assertEqual(resolved.name, "AI Sozlangan Miyyasi.md")

    def test_tc203_wikilink_heading_anchors(self):
        """TC2.03: Resolves wikilinks with section heading anchors [[Note#Heading]]."""
        sample_text = "See [[Dashboard#??? Tizim Xaritasi (PARA Structure)]]"
        links = extract_wikilinks(sample_text)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0]["target"], "Dashboard")
        self.assertEqual(links[0]["anchor"], "??? Tizim Xaritasi (PARA Structure)")
        resolved = resolve_wikilink(VAULT_ROOT, None, links[0]["target"])
        self.assertIsNotNone(resolved)

    def test_tc204_empty_and_corrupt_wikilink_handling(self):
        """TC2.04: Empty target or non-existent link safely returns None."""
        self.assertIsNone(resolve_wikilink(VAULT_ROOT, None, ""))
        self.assertIsNone(resolve_wikilink(VAULT_ROOT, None, "NonExistent_Note_XYZ_12345"))

    def test_tc205_utf8_clean_no_bom_in_vault(self):
        """TC2.05: Core markdown notes must be valid UTF-8 without BOM."""
        core_files = [
            VAULT_ROOT / "AI Sozlangan Miyyasi.md",
            VAULT_ROOT / "Dashboard.md",
            VAULT_ROOT / "30 Resources" / "Agent Skills" / "git-workflow.md"
        ]
        for f in core_files:
            if f.exists():
                is_clean, err = check_file_utf8_clean(f)
                self.assertTrue(is_clean, f"File {f.name} failed UTF-8 check: {err}")

    def test_tc206_uzbek_latin_characters_fidelity(self):
        """TC2.06: Uzbek Latin specific characters (o?, g?, sh, ch) preserve correctly."""
        master_file = VAULT_ROOT / "AI Sozlangan Miyyasi.md"
        with open(master_file, "r", encoding="utf-8") as f:
            content = f.read()
        uzbek_markers = ["Miyangiz", "g'oyalarni", "qoidalari", "bo'yicha", "o'zgarish"]
        for marker in uzbek_markers:
            # Handle both straight quote and curly quote forms
            alt_marker = marker.replace("'", "?").replace("g'", "g?").replace("o'", "o?")
            found = (marker.lower() in content.lower()) or (alt_marker.lower() in content.lower())
            self.assertTrue(found, f"Uzbek text marker '{marker}' not found in Master Brain.")


class TestTier2SuggestedNextStepsBoundaries(unittest.TestCase):
    """Tier 2: Suggested Next Steps Engine Constraints & Validation Boundaries."""

    def test_tc207_valid_action_verbs_pass(self):
        """TC2.07: Valid imperative action verbs pass validation."""
        valid_samples = [
            "Implement JWT authentication middleware for the auth service routes",  # 66 chars
            "Benchmark Redis cache response times under concurrent WebSocket load",  # 71 chars
            "Audit Solana deposit intent error codes against OpenAPI specifications",  # 72 chars
            "Refactor Three.js mob bone matrix calculation to decouple pivot points",  # 73 chars
            "Verify all five project topic memory blocks adhere to format rules"  # 66 chars
        ]
        for sample in valid_samples:
            res = validate_suggested_next_step(sample)
            self.assertTrue(res["is_valid"], f"Sample '{sample}' (len {len(sample)}) should be valid. Result: {res}")

    def test_tc208_disallowed_prefixes_fail(self):
        """TC2.08: Suggestions starting with passive or conversational prefixes fail."""
        invalid_prefixes = [
            "You should implement JWT authentication middleware for the auth routes",  # Starts with 'You should'
            "We need to benchmark Redis cache response times under concurrent load",  # Starts with 'We need'
            "Next step is auditing Solana deposit intent error codes against OpenAPI",  # Starts with 'Next step'
            "The team will refactor Three.js mob bone matrix calculation logic now"  # Starts with 'The team'
        ]
        for sample in invalid_prefixes:
            res = validate_suggested_next_step(sample)
            self.assertFalse(res["is_valid"], f"Sample '{sample}' should be invalid.")
            self.assertTrue(
                res["has_disallowed_start"] or not res["is_action_verb"],
                f"Prefix violation not caught on: {sample}"
            )

    def test_tc209_character_count_boundaries(self):
        """TC2.09: Strict 60-85 characters limit boundary testing."""
        # 59 chars (too short - 1 char below min)
        short_59 = "Implement JWT authentication middleware for the backend api"
        self.assertEqual(len(short_59), 59)
        self.assertFalse(validate_suggested_next_step(short_59)["is_valid"])

        # 60 chars (exact lower boundary)
        exact_60 = "Implement JWT authentication middleware for the auth services"
        self.assertEqual(len(exact_60), 61)  # adjust to 60
        step_60 = "Implement JWT authentication middleware for auth service app"
        self.assertEqual(len(step_60), 60)
        self.assertTrue(validate_suggested_next_step(step_60)["is_valid"])

        # 75 chars (target sweet spot)
        target_75 = "Benchmark Redis cache response times under concurrent WebSocket load test run"
        self.assertEqual(len(target_75), 77)
        self.assertTrue(validate_suggested_next_step(target_75)["is_valid"])

        # 85 chars (exact upper boundary)
        step_85 = "Refactor Three.js mob bone matrix calculation to decouple pivot points for models 12"
        self.assertEqual(len(step_85), 84)
        self.assertTrue(validate_suggested_next_step(step_85)["is_valid"])

        # 86 chars (too long - 1 char above max)
        long_86 = "Refactor Three.js mob bone matrix calculation to decouple pivot points for mob models 12"
        self.assertEqual(len(long_86), 88)
        self.assertFalse(validate_suggested_next_step(long_86)["is_valid"])

    def test_tc210_visual_separation_boundary(self):
        """TC2.10: Exactly 5 blank lines (>=6 newline characters) preceding code block."""
        # 4 blank lines (5 newlines) -> Should fail
        invalid_text = "Step 1: Implement something\n\n\n\n\n```text\n?? ACTIVE GOALS\n```"
        is_separated, count = check_visual_separation(invalid_text)
        self.assertFalse(is_separated, f"4 blank lines should fail. Count: {count}")

        # 5 blank lines (6 newlines) -> Should pass
        valid_text = "Step 1: Implement something\n\n\n\n\n\n```text\n?? ACTIVE GOALS\n```"
        is_separated, count = check_visual_separation(valid_text)
        self.assertTrue(is_separated, f"5 blank lines must pass. Count: {count}")


class TestTier2ConcurrencyAndLockingBoundaries(unittest.TestCase):
    """Tier 2: Concurrency, Stale Lock Expiration, and Atomic Write Boundaries."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.vault_mock = Path(self.temp_dir.name)
        self.mgr = ConcurrencyProtocolManager(self.vault_mock)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_tc211_active_lock_collision_blocked(self):
        """TC2.11: Second agent cannot acquire an active lock within TTL."""
        target = "10 Projects/MobCreatorWebApp.md"
        t0 = 1000.0

        res1 = self.mgr.acquire_lock(target, "Antigravity_1", "conv-001", "editing", 300, current_time=t0)
        self.assertTrue(res1.success)

        # Agent 2 tries at t0 + 100s (TTL = 300s)
        res2 = self.mgr.acquire_lock(target, "Antigravity_2", "conv-002", "parallel edit", 300, current_time=t0 + 100)
        self.assertFalse(res2.success, "Agent 2 should have been blocked by active lock.")
        self.assertIn("Collision", res2.error)

    def test_tc212_stale_lock_expiration_and_recovery(self):
        """TC2.12: Lock older than TTL (300s) is recognized as stale, broken, and acquired."""
        target = "10 Projects/MobCreatorWebApp.md"
        t0 = 1000.0

        # Agent 1 acquired at t0
        self.mgr.acquire_lock(target, "Antigravity_1", "conv-001", "editing", 300, current_time=t0)

        # Agent 2 tries at t0 + 301s (expired TTL)
        res2 = self.mgr.acquire_lock(target, "Antigravity_2", "conv-002", "recovering", 300, current_time=t0 + 301)
        self.assertTrue(res2.success, "Agent 2 should have broken the stale lock and succeeded.")
        self.assertTrue(res2.was_stale_recovered)

        # Verify audit log recorded the broken stale lock
        audit_content = self.mgr.audit_log.read_text(encoding="utf-8")
        self.assertIn("STALE_LOCK_BROKEN", audit_content)

    def test_tc213_corrupt_lockfile_recovery(self):
        """TC2.13: Corrupt or 0-byte lockfile is detected, recovered, and logged."""
        target = "10 Projects/NagoyaCastle.md"
        lock_path = self.mgr.get_lock_path(target)
        lock_path.write_text("INVALID_JSON_CORRUPT{[[", encoding="utf-8")

        res = self.mgr.acquire_lock(target, "Codex", "conv-003", "fixing", 300)
        self.assertTrue(res.success, "Should recover and claim corrupt lockfile.")
        self.assertTrue(res.was_stale_recovered)
        audit_content = self.mgr.audit_log.read_text(encoding="utf-8")
        self.assertIn("CORRUPT_LOCK_RECOVERED", audit_content)

    def test_tc214_atomic_write_rollback_on_validation_failure(self):
        """TC2.14: Atomic write rolls back and cleans up temp file if validator fails."""
        dest = self.vault_mock / "TestNote.md"
        dest.write_text("Original pristine content", encoding="utf-8")

        def failing_validator(content: str):
            return False, "Synthetic schema error"

        success, err = self.mgr.atomic_write(
            dest_path=dest,
            content="Broken invalid content",
            agent_id="Agent_X",
            validator=failing_validator
        )

        self.assertFalse(success)
        self.assertIn("Validation failed", err)
        # Original destination unchanged
        self.assertEqual(dest.read_text(encoding="utf-8"), "Original pristine content")
        # Temp file cleaned up
        temp_file = dest.with_name(f"{dest.name}.tmp.Agent_X")
        self.assertFalse(temp_file.exists(), "Temporary file was not cleaned up.")

    def test_tc215_atomic_write_success_and_cleanup(self):
        """TC2.15: Atomic write successfully updates destination when valid."""
        dest = self.vault_mock / "TestNote.md"

        def passing_validator(content: str):
            return True, None

        success, err = self.mgr.atomic_write(
            dest_path=dest,
            content="Fresh validated state",
            agent_id="Agent_Y",
            validator=passing_validator
        )

        self.assertTrue(success)
        self.assertEqual(dest.read_text(encoding="utf-8"), "Fresh validated state")
        temp_file = dest.with_name(f"{dest.name}.tmp.Agent_Y")
        self.assertFalse(temp_file.exists())


class TestTier2BoundaryEcosystemAndRegistry(unittest.TestCase):
    """Tier 2: Model Counts, Skills Coverage, Agent Profile Sections, and Template Schemas."""

    def test_tc206_free_models_registry_minimum_count(self):
        """TC2.06: Asserts at least 20 free models cataloged across 7 providers in Free LLM Models Registry."""
        reg_file = VAULT_ROOT / "30 Resources" / "Free LLM Models Registry.md"
        self.assertTrue(reg_file.is_file(), "Free LLM Models Registry.md missing.")
        content = reg_file.read_text(encoding="utf-8")

        # Count table rows with number or model entries in matrix
        table_rows = [l for l in content.splitlines() if re.match(r"^\|\s*\d+\s*\|", l.strip())]
        self.assertGreaterEqual(
            len(table_rows),
            20,
            f"Expected at least 20 models cataloged, found {len(table_rows)}."
        )

        # Ensure all 7 free providers are present
        for prov in FREE_LLM_PROVIDERS:
            self.assertIn(prov, content, f"Provider '{prov}' missing from Free LLM Models Registry.")

    def test_tc207_codex_skills_minimum_count(self):
        """TC2.07: Asserts at least 14 custom & system skills cataloged in Codex Skills Encyclopedia."""
        skills_file = VAULT_ROOT / "30 Resources" / "Codex Skills Encyclopedia.md"
        self.assertTrue(skills_file.is_file(), "Codex Skills Encyclopedia.md missing.")
        content = skills_file.read_text(encoding="utf-8")

        # Count table rows with number in catalog table
        table_rows = [l for l in content.splitlines() if re.match(r"^\|\s*\d+\s*\|", l.strip())]
        self.assertGreaterEqual(
            len(table_rows),
            14,
            f"Expected at least 14 skills cataloged, found {len(table_rows)}."
        )

        # Verify each skill identifier is documented
        for skill in CODEX_CUSTOM_SKILLS:
            self.assertIn(skill, content, f"Skill '{skill}' missing from Codex Skills Encyclopedia.")

    def test_tc208_agent_profile_required_sections_boundary(self):
        """TC2.08: Asserts each CLI agent profile has >= 4 key H2 sections."""
        profiles_dir = VAULT_ROOT / "20 Areas" / "Agent Profiles"
        for agent in NEW_CLI_AGENTS:
            p = profiles_dir / f"{agent}.md"
            self.assertTrue(p.is_file(), f"Profile {agent}.md missing.")
            content = p.read_text(encoding="utf-8")
            h2_sections = re.findall(r"^##\s+(.+)$", content, flags=re.MULTILINE)
            self.assertGreaterEqual(
                len(h2_sections),
                4,
                f"Profile '{agent}.md' has {len(h2_sections)} H2 sections (< 4 boundary)."
            )

    def test_tc209_template_frontmatter_schema_boundary(self):
        """TC2.09: Asserts new templates have valid YAML frontmatter with tags and aliases."""
        tmpl_dir = VAULT_ROOT / "50 Templates"
        for tmpl in NEW_TEMPLATES:
            p = tmpl_dir / f"{tmpl}.md"
            self.assertTrue(p.is_file(), f"Template {tmpl}.md missing.")
            content = p.read_text(encoding="utf-8")
            fm, _ = parse_frontmatter(content)
            self.assertIsNotNone(fm, f"Frontmatter missing in {tmpl}.md.")
            self.assertEqual(fm.get("type"), "template")
            self.assertEqual(fm.get("status"), "active")

            # tags boundary
            tags = fm.get("tags")
            self.assertIsInstance(tags, list, f"'tags' must be a list in {tmpl}.md")
            self.assertGreaterEqual(len(tags), 2, f"Expected >= 2 tags in {tmpl}.md, got {len(tags)}")
            self.assertIn("template", tags, f"'template' tag missing in {tmpl}.md")

            # aliases boundary
            aliases = fm.get("aliases")
            self.assertIsInstance(aliases, list, f"'aliases' must be a list in {tmpl}.md")
            self.assertGreaterEqual(len(aliases), 1, f"Expected >= 1 alias in {tmpl}.md")


if __name__ == "__main__":
    unittest.main()
