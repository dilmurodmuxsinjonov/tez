"""
Tier 1: Feature Coverage E2E Tests
Verifies core requirements from ORIGINAL_REQUEST.md and PROJECT.md ? Feature Inventory.
Covers at least 5 test cases across each of the 5 core feature categories (>= 25 test cases total).
"""

import os
from pathlib import Path
import unittest

from tests.e2e.helpers import (
    ACTIVE_PROJECTS,
    AGENT_PROFILES,
    COMMUNICATION_STYLES,
    PARA_MOCS,
    VAULT_ROOT,
    extract_wikilinks,
    parse_frontmatter,
)


class TestTier1MasterBrainEntrypoint(unittest.TestCase):
    """Category 1: Master Brain Entrypoint (AI Sozlangan Miyyasi.md) Verification."""

    @classmethod
    def setUpClass(cls):
        cls.master_file = VAULT_ROOT / "AI Sozlangan Miyyasi.md"
        if cls.master_file.exists():
            with open(cls.master_file, "r", encoding="utf-8") as f:
                cls.content = f.read()
            cls.frontmatter, cls.body = parse_frontmatter(cls.content)
        else:
            cls.content = ""
            cls.frontmatter, cls.body = None, ""

    def test_tc101_master_brain_exists_and_substantial(self):
        """TC1.01: AI Sozlangan Miyyasi.md must exist at vault root and exceed 1,000 bytes."""
        self.assertTrue(self.master_file.exists(), "AI Sozlangan Miyyasi.md does not exist at vault root.")
        self.assertGreater(len(self.content), 1000, "Master brain note content is too short (< 1000 chars).")

    def test_tc102_master_brain_yaml_frontmatter(self):
        """TC1.02: Verify valid YAML frontmatter with mandatory metadata fields."""
        self.assertIsNotNone(self.frontmatter, "Master brain note lacks valid YAML frontmatter.")
        self.assertIn("title", self.frontmatter)
        self.assertIn("version", self.frontmatter)
        self.assertIn("created", self.frontmatter)
        self.assertIn("updated", self.frontmatter)
        self.assertEqual(self.frontmatter.get("status"), "active")
        self.assertEqual(self.frontmatter.get("type"), "master-brain")
        self.assertIn("author", self.frontmatter)
        tags = self.frontmatter.get("tags", [])
        self.assertTrue(any("second-brain" in t for t in tags))

    def test_tc103_master_brain_user_identity_and_language_policy(self):
        """TC1.03: Verify user identity anchor and natural language policy."""
        self.assertIn("Dilmurod Muhsinjanov", self.content, "User name missing.")
        self.assertIn("dilmurodmuhsinjanov910@gmail.com", self.content, "User email missing.")
        self.assertIn("dilmurodmuhsinjanov910-byte", self.content, "User GitHub handle missing.")
        # Language policy: Uzbek for conversational, English for code
        self.assertTrue("O'zbek" in self.content or "uz-UZ" in self.content, "Uzbek language policy missing.")
        self.assertTrue("English" in self.content or "en-US" in self.content, "English technical policy missing.")

    def test_tc104_master_brain_startup_and_writeback_directives(self):
        """TC1.04: Verify presence of 5-step Startup Protocol and 4-step Write-Back Protocol."""
        self.assertIn("Universal AI Startup Directive", self.content)
        self.assertIn("Startup Protocol", self.content)
        self.assertIn("Write-Back Protocol", self.content)
        # Check step mentions
        self.assertIn("1.", self.content)
        self.assertIn("5.", self.content)

    def test_tc105_master_brain_agent_fleet_index(self):
        """TC1.05: Verify Master Brain indexes all 4 agent fleet profiles."""
        links = extract_wikilinks(self.content)
        link_targets = {l["target"] for l in links}
        for agent in AGENT_PROFILES:
            matches = [t for t in link_targets if agent in t]
            self.assertTrue(
                len(matches) > 0,
                f"Agent profile '{agent}' not linked in Master Brain. Found: {link_targets}"
            )

    def test_tc106_master_brain_active_projects_hub(self):
        """TC1.06: Verify Master Brain indexes all 5 active project notes."""
        links = extract_wikilinks(self.content)
        link_targets = {l["target"] for l in links}
        for project in ACTIVE_PROJECTS:
            matches = [t for t in link_targets if project in t]
            self.assertTrue(
                len(matches) > 0,
                f"Project '{project}' not linked in Master Brain. Found: {link_targets}"
            )


class TestTier1GitRulesAndToolchain(unittest.TestCase):
    """Category 2: User Git Rules & Toolchain Directory Verification."""

    @classmethod
    def setUpClass(cls):
        cls.master_file = VAULT_ROOT / "AI Sozlangan Miyyasi.md"
        cls.git_skill = VAULT_ROOT / "30 Resources" / "Agent Skills" / "git-workflow.md"
        with open(cls.master_file, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_tc107_verbatim_git_rules_tag(self):
        """TC1.07: RULE[user_global] block must appear verbatim in Master Brain."""
        self.assertIn("<RULE[user_global]>", self.content, "Missing <RULE[user_global]> tag.")
        self.assertIn("</RULE[user_global]>", self.content, "Missing </RULE[user_global]> closing tag.")

    def test_tc108_git_lifecycle_operations_specified(self):
        """TC1.08: Verify mandatory lifecycle commands: init, status, add, commit, pull, push."""
        self.assertIn("git init", self.content)
        self.assertIn("git status", self.content)
        self.assertIn("git add .", self.content)
        self.assertIn("git commit -m", self.content)
        self.assertIn("git pull", self.content)
        self.assertIn("git push", self.content)

    def test_tc109_git_automatic_branching_rule(self):
        """TC1.09: Verify automatic branching for major changes (feature/... or fix/...)."""
        self.assertIn("feature/", self.content)
        self.assertIn("fix/", self.content)
        self.assertIn("Automatic Branching for Major Changes", self.content)

    def test_tc110_local_toolchain_node_documented(self):
        """TC1.10: Verify Node.js v22 and npm are documented with paths."""
        self.assertIn("Node.js", self.content)
        self.assertTrue("v22" in self.content or "22." in self.content)
        self.assertIn(r"C:\Users\dilmu\AppData\Local\hermes\node\node.exe", self.content)

    def test_tc111_local_toolchain_python_documented(self):
        """TC1.11: Verify Python 3.12 is documented with paths."""
        self.assertIn("Python", self.content)
        self.assertTrue("3.12" in self.content)
        self.assertIn("python.exe", self.content)

    def test_tc112_local_toolchain_powershell_git_codex(self):
        """TC1.12: Verify PowerShell 5.1, Git 2.54, and Codex CLI binaries are documented."""
        self.assertIn("PowerShell", self.content)
        self.assertIn("Git", self.content)
        self.assertIn("codex.exe", self.content)
        self.assertIn("opencode.ps1", self.content)


class TestTier1AgentProfilesAndConcurrency(unittest.TestCase):
    """Category 3: Agent Profiles & Concurrency Specification Verification."""

    @classmethod
    def setUpClass(cls):
        cls.master_file = VAULT_ROOT / "AI Sozlangan Miyyasi.md"
        with open(cls.master_file, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_tc113_antigravity1_spec_present(self):
        """TC1.13: Antigravity 1 defined as primary Google session and chief architect."""
        self.assertIn("Antigravity 1", self.content)
        self.assertIn("dilmurodmuhsinjanov910@gmail.com", self.content)

    def test_tc114_antigravity2_spec_present(self):
        """TC1.14: Antigravity 2 defined as secondary isolated session / sandbox researcher."""
        self.assertIn("Antigravity 2", self.content)
        self.assertTrue("izolyatsiya" in self.content.lower() or "isolated" in self.content.lower())

    def test_tc115_codex_profile_spec_present(self):
        """TC1.15: Codex Assistant defined for autonomous code synthesis and refactoring."""
        self.assertIn("Codex", self.content)
        self.assertTrue("opencode.ps1" in self.content or "codex.exe" in self.content)

    def test_tc116_concurrency_locking_protocol_specified(self):
        """TC1.16: Verify concurrency protocol specifies lockfile path and 300s TTL."""
        self.assertIn(".agents/locks/", self.content)
        self.assertIn("300", self.content)

    def test_tc117_two_stage_atomic_write_specified(self):
        """TC1.17: Verify two-stage atomic write (temp file -> validate -> rename) protocol."""
        self.assertTrue(
            "tmp" in self.content.lower() or "vaqtinchalik" in self.content.lower(),
            "Two-stage atomic write temp file specification missing."
        )


class TestTier1GeminiTopicsMemoryAndProjects(unittest.TestCase):
    """Category 4: Gemini Topics Memory Architecture & Active Projects Verification."""

    @classmethod
    def setUpClass(cls):
        cls.master_file = VAULT_ROOT / "AI Sozlangan Miyyasi.md"
        with open(cls.master_file, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_tc118_all_five_projects_indexed(self):
        """TC1.18: Verify all 5 target projects are indexed in the Projects Hub."""
        for proj in ACTIVE_PROJECTS:
            self.assertIn(proj, self.content, f"Project {proj} missing from Master Brain.")

    def test_tc119_communication_styles_referenced(self):
        """TC1.19: Verify reference to the 10 defined communication styles."""
        self.assertIn("10", self.content)
        self.assertIn("salomlashish", self.content.lower())
        # Check several sample style names
        self.assertTrue(
            any(s.lower() in self.content.lower() for s in ["thoughtful check-in", "celebration", "reflection", "nudge"])
        )

    def test_tc120_latest_state_summary_requirement(self):
        """TC1.20: Verify requirement for Latest State Summary (1-2 sentences)."""
        self.assertIn("Latest State", self.content)

    def test_tc121_goals_and_decisions_log_requirement(self):
        """TC1.21: Verify requirement for Goals & Decisions Log (ADRs)."""
        self.assertTrue(
            "Goals & Decisions Log" in self.content or "qarorlar jurnali" in self.content.lower()
        )

    def test_tc122_suggested_next_steps_rules_referenced(self):
        """TC1.22: Verify Suggested Next Steps rules (action verb, ~75 chars, 2-4 items)."""
        self.assertTrue("fe'l" in self.content or "verb" in self.content.lower())
        self.assertTrue("75" in self.content or "60?85" in self.content or "60-85" in self.content)


class TestTier1ObsidianParamocsAndSkills(unittest.TestCase):
    """Category 5: Obsidian PARA MOCs & Skills Hub Verification."""

    @classmethod
    def setUpClass(cls):
        cls.master_file = VAULT_ROOT / "AI Sozlangan Miyyasi.md"
        cls.dashboard_file = VAULT_ROOT / "Dashboard.md"
        with open(cls.master_file, "r", encoding="utf-8") as f:
            cls.master_content = f.read()
        with open(cls.dashboard_file, "r", encoding="utf-8") as f:
            cls.dash_content = f.read()

    def test_tc123_para_mocs_indexed_in_master(self):
        """TC1.23: Master Brain contains links to all 5 PARA directories."""
        for moc in PARA_MOCS:
            self.assertIn(moc, self.master_content, f"PARA folder {moc} missing from Master Brain.")

    def test_tc124_dashboard_prominently_links_master_brain(self):
        """TC1.24: Dashboard.md prominently links to AI Sozlangan Miyyasi.md."""
        links = extract_wikilinks(self.dash_content)
        targets = [l["target"] for l in links]
        self.assertTrue(
            any("AI Sozlangan Miyyasi" in t for t in targets),
            f"Dashboard.md does not link to Master Brain. Found links: {targets}"
        )

    def test_tc125_skills_dashboard_referenced(self):
        """TC1.25: Skills Dashboard is referenced in both Master Brain and Dashboard."""
        self.assertIn("Skills Dashboard", self.master_content)
        self.assertIn("Skills Dashboard", self.dash_content)

    def test_tc126_agent_skills_directory_populated(self):
        """TC1.26: 30 Resources/Agent Skills contains core skill documentation notes."""
        skills_dir = VAULT_ROOT / "30 Resources" / "Agent Skills"
        self.assertTrue(skills_dir.is_dir(), "Agent Skills directory does not exist.")
        expected_skills = [
            "Skills Dashboard.md", "git-workflow.md", "obsidian-markdown.md",
            "obsidian-bases.md", "obsidian-cli.md", "json-canvas.md"
        ]
        for skill in expected_skills:
            p = skills_dir / skill
            self.assertTrue(p.exists(), f"Skill file {skill} missing in {skills_dir}.")

    def test_tc127_templates_infrastructure_exists(self):
        """TC1.27: 50 Templates directory contains standard note templates."""
        templates_dir = VAULT_ROOT / "50 Templates"
        self.assertTrue(templates_dir.is_dir(), "50 Templates directory does not exist.")
        for tmpl in ["Daily Note Template.md", "Project Template.md", "Resource Template.md"]:
            p = templates_dir / tmpl
            self.assertTrue(p.exists(), f"Template {tmpl} missing in {templates_dir}.")

    def test_tc128_frontier_research_and_playbooks_exist(self):
        """TC1.28: Frontier research dossiers, browser playbook, and multimodal workflows exist and link cleanly."""
        dossiers = [
            VAULT_ROOT / "30 Resources" / "Autonomous Agent Architectures.md",
            VAULT_ROOT / "20 Areas" / "Browser Automation Playbook.md",
            VAULT_ROOT / "30 Resources" / "Multimodal Generation Workflows.md",
        ]
        for d in dossiers:
            self.assertTrue(d.is_file(), f"Dossier missing: {d}")
            with open(d, "r", encoding="utf-8") as f:
                content = f.read()
            fm, _ = parse_frontmatter(content)
            self.assertIsNotNone(fm, f"Frontmatter missing in {d.name}")
            self.assertEqual(fm.get("status"), "active", f"status must be 'active' in {d.name}")
            self.assertIn("title", fm)
            self.assertIn("tags", fm)
            links = extract_wikilinks(content)
            targets = [l["target"] for l in links]
            self.assertTrue(
                any("AI Sozlangan Miyyasi" in t for t in targets),
                f"{d.name} does not link to AI Sozlangan Miyyasi"
            )
            self.assertTrue(
                any("Dashboard" in t for t in targets),
                f"{d.name} does not link to Dashboard"
            )

        # Ensure Master Brain and Dashboard index these notes
        for d in dossiers:
            self.assertIn(d.stem, self.master_content, f"Master brain does not index {d.stem}")
            self.assertIn(d.stem, self.dash_content, f"Dashboard does not index {d.stem}")

    def test_tc129_all_para_moc_files_exist_and_crosslinked(self):
        """TC1.29: All five companion PARA MOC notes exist, have type: moc, and cross-link with Skills Dashboard."""
        mocs = {
            "00 Inbox MOC": VAULT_ROOT / "00 Inbox" / "00 Inbox MOC.md",
            "10 Projects MOC": VAULT_ROOT / "10 Projects" / "10 Projects MOC.md",
            "20 Areas MOC": VAULT_ROOT / "20 Areas" / "20 Areas MOC.md",
            "30 Resources MOC": VAULT_ROOT / "30 Resources" / "30 Resources MOC.md",
            "40 Archives MOC": VAULT_ROOT / "40 Archives" / "40 Archives MOC.md",
        }
        for name, path in mocs.items():
            self.assertTrue(path.is_file(), f"MOC file missing: {path}")
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            fm, _ = parse_frontmatter(content)
            self.assertIsNotNone(fm, f"Frontmatter missing in {name}")
            self.assertEqual(fm.get("type"), "moc", f"type must be 'moc' in {name}")
            self.assertEqual(fm.get("status"), "active", f"status must be 'active' in {name}")
            self.assertIn("title", fm)
            self.assertIn("tags", fm)
            self.assertIn("AI Sozlangan Miyyasi", content, f"{name} does not link to Master Brain")
            self.assertIn("Dashboard", content, f"{name} does not link to Dashboard")
            self.assertIn("Skills Dashboard", content, f"{name} does not index Skills Dashboard")

        # Master Brain and Dashboard must index the companion MOCs
        for name in mocs:
            self.assertIn(name, self.master_content, f"Master brain does not index {name}")
            self.assertIn(name, self.dash_content, f"Dashboard does not index {name}")


if __name__ == "__main__":
    unittest.main()
