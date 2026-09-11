# -*- coding: utf-8 -*-
"""
Adversarial Verification Suite - Milestone 4 (Generation 2)
Universal AI Second Brain Project - D:\obsidian file
"""

import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

VAULT_DIR = Path(r"D:\obsidian file")

# The 8 newly created notes in Milestone 4 Gen 2
M4_NEW_NOTES = [
    "30 Resources/Autonomous Agent Architectures.md",
    "20 Areas/Browser Automation Playbook.md",
    "30 Resources/Multimodal Generation Workflows.md",
    "00 Inbox/00 Inbox MOC.md",
    "10 Projects/10 Projects MOC.md",
    "20 Areas/20 Areas MOC.md",
    "30 Resources/30 Resources MOC.md",
    "40 Archives/40 Archives MOC.md",
]

# Core updated notes in Milestone 4 Gen 2
M4_UPDATED_NOTES = [
    "AI Sozlangan Miyyasi.md",
    "Dashboard.md",
    "00 Inbox/00 Inbox.md",
    "10 Projects/10 Projects.md",
    "20 Areas/20 Areas.md",
    "30 Resources/30 Resources.md",
    "40 Archives/40 Archives.md",
]

ALL_M4_EVALUATED_NOTES = M4_NEW_NOTES + M4_UPDATED_NOTES

PARA_MOC_FILES = [
    "00 Inbox/00 Inbox MOC.md",
    "10 Projects/10 Projects MOC.md",
    "20 Areas/20 Areas MOC.md",
    "30 Resources/30 Resources MOC.md",
    "40 Archives/40 Archives MOC.md",
]

PARA_PARENT_MOC_FILES = [
    "00 Inbox/00 Inbox.md",
    "10 Projects/10 Projects.md",
    "20 Areas/20 Areas.md",
    "30 Resources/30 Resources.md",
    "40 Archives/40 Archives.md",
]


class TestMilestone4Adversarial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Index all files in vault (excluding .git and .agents)
        cls.vault_files_by_relpath = {}
        cls.vault_files_by_stem = {}
        cls.vault_files_by_name = {}

        for root, dirs, files in os.walk(VAULT_DIR):
            rel_root = os.path.relpath(root, VAULT_DIR)
            parts = rel_root.split(os.sep)
            if ".git" in parts or ".agents" in parts:
                continue
            for f in files:
                full_path = Path(root) / f
                rel_path = full_path.relative_to(VAULT_DIR).as_posix()
                stem = full_path.stem
                
                cls.vault_files_by_relpath[rel_path.lower()] = full_path
                cls.vault_files_by_name[f.lower()] = full_path
                if stem.lower() not in cls.vault_files_by_stem:
                    cls.vault_files_by_stem[stem.lower()] = full_path

    def _read_bytes_and_text(self, rel_path):
        path = VAULT_DIR / rel_path
        self.assertTrue(path.exists(), f"File does not exist: {path}")
        raw_bytes = path.read_bytes()
        text = raw_bytes.decode("utf-8")
        return path, raw_bytes, text

    # =========================================================================
    # 1. ENCODING & BOM ADVERSARIAL STRESS TEST
    # =========================================================================
    def test_utf8_without_bom_all_new_and_updated_notes(self):
        """Verify clean UTF-8 encoding without BOM across all 8 new notes and updated notes."""
        for rel_path in ALL_M4_EVALUATED_NOTES:
            with self.subTest(file=rel_path):
                path, raw_bytes, text = self._read_bytes_and_text(rel_path)
                
                # Check UTF-8 BOM
                self.assertFalse(
                    raw_bytes.startswith(b"\xef\xbb\xbf"),
                    f"{rel_path} contains a UTF-8 Byte Order Mark (BOM)!"
                )
                # Check UTF-16 BOM (LE / BE)
                self.assertFalse(
                    raw_bytes.startswith(b"\xff\xfe") or raw_bytes.startswith(b"\xfe\xff"),
                    f"{rel_path} contains a UTF-16 BOM!"
                )
                # Check UTF-32 BOM
                self.assertFalse(
                    raw_bytes.startswith(b"\x00\x00\xfe\xff") or raw_bytes.startswith(b"\xff\xfe\x00\x00"),
                    f"{rel_path} contains a UTF-32 BOM!"
                )
                # Check replacement character
                self.assertNotIn(
                    "\ufffd", text,
                    f"{rel_path} contains Unicode replacement character U+FFFD (corrupt encoding)!"
                )
                # Check substantive content length
                self.assertGreater(len(text), 100, f"{rel_path} is suspiciously short!")

    # =========================================================================
    # 2. WIKILINK EXTRACTION & PHYSICAL RESOLUTION
    # =========================================================================
    def _extract_wikilinks(self, text):
        """
        Robustly extracts genuine navigable wikilinks:
        - Excludes markdown code blocks (```...```)
        - Excludes inline code spans (`...`)
        - Handles escaped table pipes ([[target\\|alias]])
        - Handles anchors ([[target#heading|alias]])
        """
        # Strip multiline code blocks
        clean_text = re.sub(r"```[\s\S]*?```", "", text)
        # Strip inline code spans
        clean_text = re.sub(r"`[^`\n]+`", "", clean_text)

        links = []
        pattern = r"\[\[(.*?)\]\]"
        matches = re.findall(pattern, clean_text)
        for m in matches:
            raw = m.strip()
            # Normalize escaped pipe in table
            normalized = raw.replace(r"\|", "|")
            # Split by | for alias
            if "|" in normalized:
                target_part = normalized.split("|")[0].strip()
                alias_part = normalized.split("|")[1].strip()
            else:
                target_part = normalized
                alias_part = None
            
            # Split by # for anchor
            if "#" in target_part:
                target_file = target_part.split("#")[0].strip()
                anchor = target_part.split("#")[1].strip()
            else:
                target_file = target_part
                anchor = None
            
            # Skip obvious template placeholder indicators if any
            if target_file == "...":
                continue

            links.append({
                "raw": raw,
                "target_file": target_file,
                "anchor": anchor,
                "alias": alias_part,
            })
        return links

    def _resolve_wikilink_target(self, target_file, source_file_path):
        """
        Resolves a wikilink target to a physical path in the vault.
        Returns (resolved_path, reason).
        """
        if not target_file:
            # Self-reference anchor like [[#heading]]
            return source_file_path, "self-reference"

        clean = target_file.strip().rstrip("/")
        if clean in [".", "..", "..."]:
            return None, "invalid_relative_placeholder"

        candidates = [
            clean,
            clean + ".md",
            clean + ".base",
            clean + ".canvas",
            clean + ".png",
        ]

        # 1. Check direct relative path from vault root
        for c in candidates:
            p = VAULT_DIR / c
            if p.is_file():
                return p, "direct_relpath"

        # 2. Check case-insensitive relative path from vault root
        for c in candidates:
            c_lower = c.lower().replace("\\", "/")
            if c_lower in self.vault_files_by_relpath:
                return self.vault_files_by_relpath[c_lower], "case_insensitive_relpath"

        # 3. Check by filename / basename in vault
        target_name = Path(clean).name
        candidates_name = [
            target_name,
            target_name + ".md",
            target_name + ".base",
            target_name + ".canvas",
        ]
        for cn in candidates_name:
            cn_lower = cn.lower()
            if cn_lower in self.vault_files_by_name:
                return self.vault_files_by_name[cn_lower], "by_name"
            if cn_lower in self.vault_files_by_stem:
                return self.vault_files_by_stem[cn_lower], "by_stem"

        # 4. Check relative to source file directory
        source_dir = source_file_path.parent
        for c in candidates:
            p = source_dir / c
            if p.is_file():
                return p, "relative_to_source"

        return None, "unresolved"

    def test_wikilinks_100_percent_resolution_in_all_8_new_notes(self):
        """Verify 100% resolution of all wikilinks originating from the 8 newly created notes."""
        total_links = 0
        unresolved_links = []

        for rel_path in M4_NEW_NOTES:
            path, raw_bytes, text = self._read_bytes_and_text(rel_path)
            links = self._extract_wikilinks(text)
            self.assertGreater(len(links), 0, f"No wikilinks found in {rel_path}!")

            for link in links:
                total_links += 1
                target = link["target_file"]
                resolved_path, reason = self._resolve_wikilink_target(target, path)
                if resolved_path is None:
                    unresolved_links.append(f"In {rel_path}: [[{link['raw']}]] -> target '{target}' could not be resolved!")

        self.assertEqual(
            len(unresolved_links), 0,
            f"Found {len(unresolved_links)} broken wikilinks out of {total_links} links in 8 new notes:\n" +
            "\n".join(f"  - {u}" for u in unresolved_links)
        )

    def test_wikilinks_100_percent_resolution_in_all_updated_notes(self):
        """Verify 100% resolution of all wikilinks in updated master notes and folder MOCs."""
        total_links = 0
        unresolved_links = []

        for rel_path in M4_UPDATED_NOTES:
            path, raw_bytes, text = self._read_bytes_and_text(rel_path)
            links = self._extract_wikilinks(text)
            self.assertGreater(len(links), 0, f"No wikilinks found in {rel_path}!")

            for link in links:
                total_links += 1
                target = link["target_file"]
                resolved_path, reason = self._resolve_wikilink_target(target, path)
                if resolved_path is None:
                    unresolved_links.append(f"In {rel_path}: [[{link['raw']}]] -> target '{target}' could not be resolved!")

        self.assertEqual(
            len(unresolved_links), 0,
            f"Found {len(unresolved_links)} broken wikilinks out of {total_links} links in updated notes:\n" +
            "\n".join(f"  - {u}" for u in unresolved_links)
        )

    # =========================================================================
    # 3. INTERNAL HEADING ANCHORS VERIFICATION
    # =========================================================================
    def test_master_brain_and_dashboard_internal_heading_anchors(self):
        """Verify internal heading anchors in Dashboard.md target exact headings in AI Sozlangan Miyyasi.md."""
        dash_path, _, dash_text = self._read_bytes_and_text("Dashboard.md")
        mb_path, _, mb_text = self._read_bytes_and_text("AI Sozlangan Miyyasi.md")

        # Collect all headings in AI Sozlangan Miyyasi.md
        mb_headings = set()
        for line in mb_text.splitlines():
            if line.startswith("#"):
                heading = line.lstrip("#").strip()
                mb_headings.add(heading)

        # Extract all wikilinks with anchors to AI Sozlangan Miyyasi in Dashboard.md
        dash_links = self._extract_wikilinks(dash_text)
        anchors_checked = 0
        broken_anchors = []

        for link in dash_links:
            target = link["target_file"]
            anchor = link["anchor"]
            if anchor and ("AI Sozlangan Miyyasi" in target or target == ""):
                anchors_checked += 1
                clean_anchor = anchor.strip()
                if clean_anchor not in mb_headings:
                    closest = [h for h in mb_headings if clean_anchor in h or h in clean_anchor]
                    broken_anchors.append(
                        f"Anchor '#{clean_anchor}' not found in Master Brain! Closest: {closest}"
                    )

        self.assertGreater(anchors_checked, 0, "No internal heading anchors tested in Dashboard.md!")
        self.assertEqual(
            len(broken_anchors), 0,
            f"Broken heading anchors found in Dashboard.md:\n" + "\n".join(f"  - {b}" for b in broken_anchors)
        )

    def test_all_notes_internal_heading_anchors_valid(self):
        """Verify all wikilinks with #anchors across all evaluated M4 notes resolve to valid headings."""
        broken_anchors = []
        total_anchors = 0

        for rel_path in ALL_M4_EVALUATED_NOTES:
            path, _, text = self._read_bytes_and_text(rel_path)
            links = self._extract_wikilinks(text)

            for link in links:
                anchor = link["anchor"]
                if not anchor:
                    continue

                total_anchors += 1
                target = link["target_file"]
                resolved_file, _ = self._resolve_wikilink_target(target, path)
                
                if resolved_file and resolved_file.suffix.lower() == ".md":
                    target_text = resolved_file.read_text(encoding="utf-8")
                    target_headings = set(
                        l.lstrip("#").strip() for l in target_text.splitlines() if l.startswith("#")
                    )
                    clean_anchor = anchor.strip()
                    if clean_anchor not in target_headings:
                        broken_anchors.append(
                            f"In {rel_path}: [[{link['raw']}]] -> anchor '#{clean_anchor}' not found in {resolved_file.name}!"
                        )

        self.assertEqual(
            len(broken_anchors), 0,
            f"Found {len(broken_anchors)} broken heading anchors across evaluated notes:\n" +
            "\n".join(f"  - {b}" for b in broken_anchors)
        )

    # =========================================================================
    # 4. PARA MOC LINKAGE: SKILLS DASHBOARD & 50 TEMPLATES
    # =========================================================================
    def test_para_mocs_link_to_skills_dashboard_and_50_templates(self):
        """Verify that every PARA MOC note links to Skills Dashboard and 50 Templates/."""
        all_para_moc_files = PARA_MOC_FILES + PARA_PARENT_MOC_FILES

        for rel_path in all_para_moc_files:
            with self.subTest(file=rel_path):
                path, _, text = self._read_bytes_and_text(rel_path)
                links = self._extract_wikilinks(text)

                # Check for Skills Dashboard link
                has_skills_dashboard = any(
                    "Skills Dashboard" in l["target_file"] or "Skills Dashboard" in (l["raw"] or "")
                    for l in links
                )
                self.assertTrue(
                    has_skills_dashboard,
                    f"{rel_path} does NOT contain a wikilink to Skills Dashboard!"
                )

                # Check for 50 Templates link
                has_templates = any(
                    "50 Templates" in l["target_file"] or "50 Templates" in (l["raw"] or "")
                    for l in links
                )
                self.assertTrue(
                    has_templates,
                    f"{rel_path} does NOT contain a wikilink to 50 Templates/!"
                )

    # =========================================================================
    # 5. BIDIRECTIONAL CONNECTIVITY: MASTER BRAIN & DASHBOARD
    # =========================================================================
    def test_bidirectional_linkage_with_master_brain_and_dashboard(self):
        """Verify every new M4 note links to Master Brain and Dashboard, and vice-versa."""
        mb_path, _, mb_text = self._read_bytes_and_text("AI Sozlangan Miyyasi.md")
        dash_path, _, dash_text = self._read_bytes_and_text("Dashboard.md")

        mb_links = self._extract_wikilinks(mb_text)
        dash_links = self._extract_wikilinks(dash_text)

        for rel_path in M4_NEW_NOTES:
            with self.subTest(new_note=rel_path):
                path, _, text = self._read_bytes_and_text(rel_path)
                note_links = self._extract_wikilinks(text)

                # Check that note links back to AI Sozlangan Miyyasi
                has_mb_backlink = any(
                    "AI Sozlangan Miyyasi" in l["target_file"] for l in note_links
                )
                self.assertTrue(
                    has_mb_backlink,
                    f"{rel_path} does NOT backlink to AI Sozlangan Miyyasi!"
                )

                # Check that note links back to Dashboard
                has_dash_backlink = any(
                    "Dashboard" in l["target_file"] for l in note_links
                )
                self.assertTrue(
                    has_dash_backlink,
                    f"{rel_path} does NOT backlink to Dashboard!"
                )

                # Check that Master Brain links to this new note
                stem = path.stem
                has_link_from_mb = any(
                    stem in l["target_file"] or rel_path.replace(".md", "") in l["target_file"]
                    for l in mb_links
                )
                self.assertTrue(
                    has_link_from_mb,
                    f"AI Sozlangan Miyyasi.md does NOT index {rel_path}!"
                )

                # Check that Dashboard links to this new note
                has_link_from_dash = any(
                    stem in l["target_file"] or rel_path.replace(".md", "") in l["target_file"]
                    for l in dash_links
                )
                self.assertTrue(
                    has_link_from_dash,
                    f"Dashboard.md does NOT index {rel_path}!"
                )

    # =========================================================================
    # 6. SUBSTANTIVE DEPTH & ANTI-FACADE ADVERSARIAL CHECKS
    # =========================================================================
    def test_frontier_dossiers_depth_and_zero_placeholders(self):
        """Verify that research dossiers have substantial depth and zero placeholder tokens."""
        dossiers = [
            ("30 Resources/Autonomous Agent Architectures.md", 800, 100),
            ("20 Areas/Browser Automation Playbook.md", 800, 100),
            ("30 Resources/Multimodal Generation Workflows.md", 800, 100),
        ]

        forbidden_patterns = [
            r"\bTODO\b",
            r"\bTBD\b",
            r"\bLOREM IPSUM\b",
            r"\bPLACEHOLDER\b",
            r"\bFIXME\b",
            r"\bXXX\b",
        ]

        for rel_path, min_words, min_lines in dossiers:
            with self.subTest(dossier=rel_path):
                path, _, text = self._read_bytes_and_text(rel_path)
                lines = text.splitlines()
                words = text.split()

                self.assertGreaterEqual(
                    len(words), min_words,
                    f"{rel_path} has only {len(words)} words, expected at least {min_words}!"
                )
                self.assertGreaterEqual(
                    len(lines), min_lines,
                    f"{rel_path} has only {len(lines)} lines, expected at least {min_lines}!"
                )

                for pat in forbidden_patterns:
                    match = re.search(pat, text, re.IGNORECASE)
                    self.assertIsNone(
                        match,
                        f"{rel_path} contains forbidden placeholder pattern: {pat}"
                    )

    # =========================================================================
    # 7. YAML FRONTMATTER SCHEMA AUDIT
    # =========================================================================
    def test_yaml_frontmatter_schema_compliance(self):
        """Verify strict YAML frontmatter structure across all 8 new notes."""
        for rel_path in M4_NEW_NOTES:
            with self.subTest(file=rel_path):
                path, _, text = self._read_bytes_and_text(rel_path)
                self.assertTrue(
                    text.startswith("---\n") or text.startswith("---\r\n"),
                    f"{rel_path} does not start with YAML frontmatter delimiter '---'!"
                )
                parts = text.split("---", 2)
                self.assertGreaterEqual(len(parts), 3, f"{rel_path} has malformed frontmatter delimiters!")
                frontmatter = parts[1]

                # Check required keys
                for key in ["title:", "status:", "type:", "tags:"]:
                    self.assertIn(
                        key, frontmatter,
                        f"{rel_path} frontmatter is missing required key '{key}'!"
                    )

    # =========================================================================
    # 8. GIT STATUS & BRANCH CONFIRMATION
    # =========================================================================
    def test_git_branch_status(self):
        """Verify current git branch is feature/universal-ai-second-brain."""
        res = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=str(VAULT_DIR),
            capture_output=True,
            text=True,
            check=True
        )
        current_branch = res.stdout.strip()
        self.assertEqual(
            current_branch, "feature/universal-ai-second-brain",
            f"Expected branch 'feature/universal-ai-second-brain', got '{current_branch}'"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
