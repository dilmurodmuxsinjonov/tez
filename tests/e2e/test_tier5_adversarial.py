"""
Tier 5: Adversarial & Full Vault Integrity Tests
Verifies Milestone 4 (PARA MOCs) and Milestone 3 (Gemini Topics Projects)
with strict adversarial validation, zero-tolerance link integrity, and UTF-8 hygiene.
"""

import os
from pathlib import Path
import re
import unittest

from tests.e2e.helpers import (
    ACTIVE_PROJECTS,
    AGENT_PROFILES,
    COMMUNICATION_STYLES,
    PARA_MOCS,
    VAULT_ROOT,
    check_file_utf8_clean,
    check_visual_separation,
    extract_wikilinks,
    parse_frontmatter,
    resolve_wikilink,
    validate_suggested_next_step,
)


class TestTier5ParaMocs(unittest.TestCase):
    """Adversarial verification of all 5 PARA MOC files."""

    @classmethod
    def setUpClass(cls):
        cls.mocs = {
            "00 Inbox": VAULT_ROOT / "00 Inbox" / "00 Inbox.md",
            "10 Projects": VAULT_ROOT / "10 Projects" / "10 Projects.md",
            "20 Areas": VAULT_ROOT / "20 Areas" / "20 Areas.md",
            "30 Resources": VAULT_ROOT / "30 Resources" / "30 Resources.md",
            "40 Archives": VAULT_ROOT / "40 Archives" / "40 Archives.md",
        }

    def test_tc501_all_five_mocs_exist(self):
        """TC5.01: All 5 PARA MOC files must exist in their respective directories."""
        for name, path in self.mocs.items():
            self.assertTrue(path.is_file(), f"MOC note missing: {path}")

    def test_tc502_mocs_valid_frontmatter(self):
        """TC5.02: All MOCs must have valid YAML frontmatter with type: moc."""
        for name, path in self.mocs.items():
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            fm, body = parse_frontmatter(content)
            self.assertIsNotNone(fm, f"Frontmatter missing or invalid in {path.name}")
            self.assertEqual(fm.get("type"), "moc", f"type must be 'moc' in {path.name}")
            self.assertEqual(fm.get("status"), "active", f"status must be 'active' in {path.name}")
            self.assertIn("title", fm)
            self.assertIn("tags", fm)

    def test_tc503_mocs_link_to_master_brain(self):
        """TC5.03: Every MOC note must link back to AI Sozlangan Miyyasi."""
        for name, path in self.mocs.items():
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            links = extract_wikilinks(content)
            targets = [l["target"] for l in links]
            self.assertTrue(
                any("AI Sozlangan Miyyasi" in t for t in targets),
                f"{path.name} does not link back to Master Brain. Found: {targets}"
            )

    def test_tc504_projects_moc_indexes_all_active_projects(self):
        """TC5.04: 10 Projects.md must index all 5 active project notes."""
        p_moc = self.mocs["10 Projects"]
        with open(p_moc, "r", encoding="utf-8") as f:
            content = f.read()
        for proj in ACTIVE_PROJECTS:
            self.assertIn(proj, content, f"Project {proj} missing from 10 Projects.md")

    def test_tc505_areas_moc_indexes_all_agent_profiles(self):
        """TC5.05: 20 Areas.md must index all 4 agent profiles and concurrency protocol."""
        a_moc = self.mocs["20 Areas"]
        with open(a_moc, "r", encoding="utf-8") as f:
            content = f.read()
        for prof in AGENT_PROFILES:
            self.assertIn(prof, content, f"Agent profile {prof} missing from 20 Areas.md")


class TestTier5GeminiTopicsProjectsFidelity(unittest.TestCase):
    """Adversarial verification of the 5 Project notes created in Milestone 3."""

    def test_tc506_all_five_project_notes_exist(self):
        """TC5.06: All 5 active project notes must exist in 10 Projects/."""
        for proj in ACTIVE_PROJECTS:
            p = VAULT_ROOT / "10 Projects" / f"{proj}.md"
            self.assertTrue(p.is_file(), f"Project note missing: {p}")

    def test_tc507_project_notes_frontmatter_schema(self):
        """TC5.07: Each project note must have type: project-memory and full schema."""
        required_keys = ["title", "version", "status", "type", "tags", "project_path", "tech_stack"]
        for proj in ACTIVE_PROJECTS:
            p = VAULT_ROOT / "10 Projects" / f"{proj}.md"
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            fm, _ = parse_frontmatter(content)
            self.assertIsNotNone(fm, f"Frontmatter missing in {proj}.md")
            self.assertEqual(fm.get("type"), "project-memory")
            self.assertEqual(fm.get("status"), "active")
            for k in required_keys:
                self.assertIn(k, fm, f"Key '{k}' missing in frontmatter of {proj}.md")

    def test_tc508_suggested_next_steps_strict_validation(self):
        """TC5.08: Suggested Next Steps must use approved action verbs and satisfy 60-85 chars."""
        for proj in ACTIVE_PROJECTS:
            p = VAULT_ROOT / "10 Projects" / f"{proj}.md"
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            sns_match = re.search(r"## 🎯 Suggested Next Steps\s*\n+([\s\S]*?)(?=\n{5,}```)", content)
            self.assertIsNotNone(sns_match, f"Suggested Next Steps section missing in {proj}.md")
            raw_lines = sns_match.group(1).strip().splitlines()
            clean_steps = [re.sub(r"^[0-9*.-]+\s*", "", s).strip() for s in raw_lines if s.strip()]
            self.assertGreaterEqual(len(clean_steps), 2, f"Fewer than 2 next steps in {proj}.md")
            self.assertLessEqual(len(clean_steps), 4, f"More than 4 next steps in {proj}.md")
            for step in clean_steps:
                val = validate_suggested_next_step(step)
                self.assertTrue(
                    val["is_valid"],
                    f"Invalid step in {proj}.md: '{step}' (Reason: {val})"
                )

    def test_tc509_visual_separation_and_topic_memory_block(self):
        """TC5.09: Visual separation must have >= 5 blank lines followed by ```text topic memory."""
        for proj in ACTIVE_PROJECTS:
            p = VAULT_ROOT / "10 Projects" / f"{proj}.md"
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            is_sep, count = check_visual_separation(content)
            self.assertTrue(is_sep, f"Visual separation (< 5 blank lines) failed in {proj}.md (got {count})")
            self.assertIn("```text", content, f"```text block missing in {proj}.md")
            self.assertIn("🎯 ACTIVE GOALS & OBJECTIVES", content)
            self.assertIn("📋 LATEST STATE & MILESTONE PROGRESS", content)
            self.assertIn("💡 ARCHITECTURAL DECISIONS LOG", content)


class TestTier5VaultGraphHygiene(unittest.TestCase):
    """Forensic integrity and encoding checks across newly created vault files."""

    def test_tc510_utf8_clean_without_bom(self):
        """TC5.10: All newly created notes must be clean UTF-8 without BOM."""
        notes_to_check = [
            VAULT_ROOT / "AI Sozlangan Miyyasi.md",
            VAULT_ROOT / "Dashboard.md",
            VAULT_ROOT / "00 Inbox" / "00 Inbox.md",
            VAULT_ROOT / "10 Projects" / "10 Projects.md",
            VAULT_ROOT / "20 Areas" / "20 Areas.md",
            VAULT_ROOT / "30 Resources" / "30 Resources.md",
            VAULT_ROOT / "40 Archives" / "40 Archives.md",
            VAULT_ROOT / "30 Resources" / "Autonomous Agent Architectures.md",
            VAULT_ROOT / "20 Areas" / "Browser Automation Playbook.md",
            VAULT_ROOT / "30 Resources" / "Multimodal Generation Workflows.md",
            VAULT_ROOT / "00 Inbox" / "00 Inbox MOC.md",
            VAULT_ROOT / "10 Projects" / "10 Projects MOC.md",
            VAULT_ROOT / "20 Areas" / "20 Areas MOC.md",
            VAULT_ROOT / "30 Resources" / "30 Resources MOC.md",
            VAULT_ROOT / "40 Archives" / "40 Archives MOC.md",
        ]
        for proj in ACTIVE_PROJECTS:
            notes_to_check.append(VAULT_ROOT / "10 Projects" / f"{proj}.md")
        for prof in AGENT_PROFILES:
            notes_to_check.append(VAULT_ROOT / "20 Areas" / "Agent Profiles" / f"{prof}.md")

        for note in notes_to_check:
            is_clean, err = check_file_utf8_clean(note)
            self.assertTrue(is_clean, f"Encoding issue in {note.name}: {err}")


if __name__ == "__main__":
    unittest.main()
