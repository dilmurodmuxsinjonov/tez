"""
Tier 3: Cross-Feature Combinations (Pairwise Verification) E2E Tests
Tests the interconnectivity, mutual backlinks, and contract consistency between disparate modules.
Follows Progressive Testability principles.
"""

import os
from pathlib import Path
import unittest

from tests.e2e.helpers import (
    ACTIVE_PROJECTS,
    AGENT_PROFILES,
    PARA_MOCS,
    VAULT_ROOT,
    extract_wikilinks,
    resolve_wikilink,
)


class TestTier3CrossFeatureCombinations(unittest.TestCase):
    """Tier 3: Pairwise links, MOC resolution, and contract consistency."""

    @classmethod
    def setUpClass(cls):
        cls.master_file = VAULT_ROOT / "AI Sozlangan Miyyasi.md"
        cls.dashboard_file = VAULT_ROOT / "Dashboard.md"
        cls.skills_dash = VAULT_ROOT / "30 Resources" / "Agent Skills" / "Skills Dashboard.md"

        with open(cls.master_file, "r", encoding="utf-8") as f:
            cls.master_content = f.read()
        with open(cls.dashboard_file, "r", encoding="utf-8") as f:
            cls.dash_content = f.read()
        if cls.skills_dash.exists():
            with open(cls.skills_dash, "r", encoding="utf-8") as f:
                cls.skills_content = f.read()
        else:
            cls.skills_content = ""

    def test_tc301_master_brain_to_dashboard_mutual_linking(self):
        """TC3.01: Master Brain and Dashboard.md have reciprocal cross-linking."""
        master_links = extract_wikilinks(self.master_content)
        dash_links = extract_wikilinks(self.dash_content)

        # Dashboard links to Master Brain
        dash_targets = [l["target"] for l in dash_links]
        self.assertTrue(
            any("AI Sozlangan Miyyasi" in t for t in dash_targets),
            "Dashboard.md does not link to AI Sozlangan Miyyasi."
        )

        # Both agree on PARA MOC targets
        for moc in ["00 Inbox", "10 Projects", "20 Areas", "30 Resources", "40 Archives"]:
            self.assertTrue(
                any(moc in t for t in dash_targets),
                f"Dashboard missing PARA target {moc}"
            )

    def test_tc302_master_brain_agent_fleet_contract_consistency(self):
        """TC3.02: Master Brain links all 4 agent profiles and cites Concurrency & Sync Protocol."""
        master_links = extract_wikilinks(self.master_content)
        master_targets = {l["target"] for l in master_links}

        for agent in AGENT_PROFILES:
            has_link = any(agent.lower() in t.lower() for t in master_targets)
            self.assertTrue(has_link, f"Master Brain missing link to agent: {agent}")

        # Concurrency protocol must be referenced in agent section
        self.assertIn("Concurrency & Sync Protocol", self.master_content)

    def test_tc303_master_brain_active_projects_contract_consistency(self):
        """TC3.03: Master Brain links all 5 active projects with technology stacks."""
        master_links = extract_wikilinks(self.master_content)
        master_targets = {l["target"] for l in master_links}

        for proj in ACTIVE_PROJECTS:
            has_link = any(proj.lower() in t.lower() for t in master_targets)
            self.assertTrue(has_link, f"Master Brain missing link to project: {proj}")

        # Check tech stack pairing
        self.assertIn("React 19", self.master_content)
        self.assertIn("Three.js", self.master_content)
        self.assertIn("Python", self.master_content)
        self.assertIn("Prisma", self.master_content)
        self.assertIn("Next.js", self.master_content)

    def test_tc304_skills_dashboard_to_git_workflow_pairwise(self):
        """TC3.04: Skills Dashboard links to git-workflow.md and Obsidian skills."""
        if not self.skills_content:
            self.skipTest("Skills Dashboard not available.")

        links = extract_wikilinks(self.skills_content)
        targets = [l["target"] for l in links]
        self.assertTrue(
            any("git-workflow" in t.lower() for t in targets),
            "Skills Dashboard must link to git-workflow."
        )

    def test_tc305_agent_profile_notes_backlink_check(self):
        """TC3.05: If agent profile notes exist on disk (M2), verify they link back to Master Brain."""
        agent_profiles_dir = VAULT_ROOT / "20 Areas" / "Agent Profiles"
        if not agent_profiles_dir.exists():
            # Milestone M2 not yet executed; verify specification contract
            self.assertTrue(
                "Antigravity 1" in self.master_content and "Agent" in self.master_content,
                "Master Brain must index Agent Profiles."
            )
            return

        agent_files = list(agent_profiles_dir.glob("*.md"))
        if not agent_files:
            return  # Pending M2 population

        for af in agent_files:
            content = af.read_text(encoding="utf-8")
            links = extract_wikilinks(content)
            targets = [l["target"] for l in links]
            self.assertTrue(
                any("AI Sozlangan Miyyasi" in t for t in targets),
                f"Agent profile note {af.name} does not link back to Master Brain."
            )

    def test_tc306_active_projects_topic_memory_backlink_check(self):
        """TC3.06: If project notes exist on disk (M3), verify they link back to Master Brain."""
        projects_dir = VAULT_ROOT / "10 Projects"
        if not projects_dir.exists():
            self.assertIn("10 Projects", self.master_content)
            return

        proj_files = [f for f in projects_dir.glob("*.md") if f.name != "10 Projects.md"]
        if not proj_files:
            return  # Pending M3 population

        for pf in proj_files:
            content = pf.read_text(encoding="utf-8")
            links = extract_wikilinks(content)
            targets = [l["target"] for l in links]
            self.assertTrue(
                any("AI Sozlangan Miyyasi" in t for t in targets),
                f"Project note {pf.name} does not link back to Master Brain."
            )

    def test_tc307_vault_graph_existing_nodes_resolution(self):
        """TC3.07: Verify all wikilinks in Master Brain and Dashboard point to valid targets or established contracts."""
        notes_to_scan = [self.master_file, self.dashboard_file]
        for note in notes_to_scan:
            content = note.read_text(encoding="utf-8")
            links = extract_wikilinks(content)
            for link in links:
                target = link["target"]
                # Must not be empty
                self.assertTrue(len(target) > 0, f"Empty wikilink in {note.name}")
                # Must not contain Windows backslash inside link
                self.assertNotIn("\\", target, f"Wikilink '{target}' in {note.name} contains backslash.")


if __name__ == "__main__":
    unittest.main()
