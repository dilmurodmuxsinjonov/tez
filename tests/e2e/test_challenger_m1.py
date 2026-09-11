"""
Milestone 1 Challenger 1 — Empirical Verification Test Suite
Covers:
1. YAML Frontmatter Parsing & Strict Schema Validation
2. Section Completeness, Heading Hierarchy & Content Non-emptiness
3. Character Encoding (UTF-8, No BOM, No Mojibake, Uzbek Orthography, Emoji Codepoints)
4. Markdown Syntax, AST Parsing, Code Fences, Wikilinks, Anchors & Table Pipes
5. Verbatim RULE[user_global] Matching
"""

import codecs
import json
import os
from pathlib import Path
import re
import sys
import unittest

import markdown_it
import yaml

VAULT_ROOT = Path(r"D:\obsidian file")
MASTER_BRAIN_PATH = VAULT_ROOT / "AI Sozlangan Miyyasi.md"
DASHBOARD_PATH = VAULT_ROOT / "Dashboard.md"


class TestYAMLFrontmatter(unittest.TestCase):
    """EMPIRICAL TEST CATEGORY 1: YAML Frontmatter Parsing & Schema."""

    def test_master_brain_yaml_delimiters(self):
        """Verify AI Sozlangan Miyyasi starts with --- and has closing ---."""
        content = MASTER_BRAIN_PATH.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\n") or content.startswith("---\r\n"),
                        "Master brain note does not start with --- delimiter.")
        parts = content.split("---", 2)
        self.assertGreaterEqual(len(parts), 3, "Master brain note missing closing --- delimiter.")

    def test_master_brain_yaml_parse_pyyaml(self):
        """Verify AI Sozlangan Miyyasi frontmatter parses cleanly with PyYAML safe_load."""
        content = MASTER_BRAIN_PATH.read_text(encoding="utf-8")
        yaml_text = content.split("---", 2)[1]
        data = yaml.safe_load(yaml_text)
        self.assertIsInstance(data, dict, "Frontmatter did not parse into a dictionary.")

        # Required fields
        expected_keys = ["title", "version", "created", "updated", "status", "type", "author", "tags", "language"]
        for key in expected_keys:
            self.assertIn(key, data, f"Required frontmatter key '{key}' is missing.")

        self.assertEqual(data["status"], "active")
        self.assertEqual(data["type"], "master-brain")
        self.assertIn("Dilmurod Muhsinjanov", data["author"])
        self.assertIsInstance(data["tags"], list)
        self.assertIn("second-brain", data["tags"])
        self.assertIn("master-entrypoint", data["tags"])
        self.assertIn("uz-UZ", data["language"])

    def test_dashboard_yaml_delimiters(self):
        """Verify Dashboard.md starts with --- and has closing ---."""
        content = DASHBOARD_PATH.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("---\n") or content.startswith("---\r\n"),
                        "Dashboard note does not start with --- delimiter.")
        parts = content.split("---", 2)
        self.assertGreaterEqual(len(parts), 3, "Dashboard note missing closing --- delimiter.")

    def test_dashboard_yaml_parse_pyyaml(self):
        """Verify Dashboard.md frontmatter parses cleanly with PyYAML safe_load."""
        content = DASHBOARD_PATH.read_text(encoding="utf-8")
        yaml_text = content.split("---", 2)[1]
        data = yaml.safe_load(yaml_text)
        self.assertIsInstance(data, dict, "Dashboard frontmatter did not parse into a dictionary.")

        expected_keys = ["title", "updated", "status", "type", "tags"]
        for key in expected_keys:
            self.assertIn(key, data, f"Required Dashboard frontmatter key '{key}' is missing.")

        self.assertEqual(data["status"], "active")
        self.assertEqual(data["type"], "dashboard")
        self.assertIsInstance(data["tags"], list)
        self.assertIn("dashboard", data["tags"])
        self.assertIn("second-brain", data["tags"])

    def test_yaml_roundtrip_fidelity(self):
        """Verify YAML round-trip dump and reload preserves all data structures."""
        for path in [MASTER_BRAIN_PATH, DASHBOARD_PATH]:
            content = path.read_text(encoding="utf-8")
            yaml_text = content.split("---", 2)[1]
            original = yaml.safe_load(yaml_text)
            dumped = yaml.dump(original, allow_unicode=True)
            reloaded = yaml.safe_load(dumped)
            self.assertEqual(original, reloaded, f"Round-trip failed for {path.name}")


class TestSectionCompleteness(unittest.TestCase):
    """EMPIRICAL TEST CATEGORY 2: Section Completeness & Non-emptiness."""

    @classmethod
    def setUpClass(cls):
        cls.mb_content = MASTER_BRAIN_PATH.read_text(encoding="utf-8")
        cls.mb_body = cls.mb_content.split("---", 2)[2]
        cls.db_content = DASHBOARD_PATH.read_text(encoding="utf-8")
        cls.db_body = cls.db_content.split("---", 2)[2]

    def _parse_markdown_headings(self, text):
        """Parse headings while ignoring code blocks."""
        lines = text.splitlines()
        headings = []
        in_code_block = False
        current_heading = None
        current_lines = []

        for line in lines:
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
                current_lines.append(line)
                continue

            if in_code_block:
                current_lines.append(line)
                continue

            m = re.match(r"^(#{1,6})\s+(.*)$", line)
            if m:
                if current_heading is not None:
                    headings.append({
                        "title": current_heading["title"],
                        "level": current_heading["level"],
                        "body": "\n".join(current_lines).strip()
                    })
                current_heading = {
                    "title": m.group(2).strip(),
                    "level": len(m.group(1))
                }
                current_lines = []
            else:
                current_lines.append(line)

        if current_heading is not None:
            headings.append({
                "title": current_heading["title"],
                "level": current_heading["level"],
                "body": "\n".join(current_lines).strip()
            })
        return headings

    def test_master_brain_h1(self):
        """Verify exactly one H1 in Master Brain."""
        headings = self._parse_markdown_headings(self.mb_body)
        h1s = [h for h in headings if h["level"] == 1]
        self.assertEqual(len(h1s), 1, f"Expected 1 H1 heading, found {len(h1s)}")
        self.assertIn("AI Sozlangan Miyyasi", h1s[0]["title"])

    def test_master_brain_required_h2_sections(self):
        """Verify all 8 mandatory H2 sections exist in Master Brain."""
        headings = self._parse_markdown_headings(self.mb_body)
        titles = [h["title"] for h in headings if h["level"] == 2]

        required_h2 = [
            "Universal AI Startup Directive (Read-First Protocol)",
            "Foydalanuvchi Profili va Shaxsiyati (User Identity & Persona)",
            "Majburiy Global Git Qoidalari (Inviolable Git Workflow: RULE[user_global])",
            "Mahalliy Dasturiy Vositalar (Local Software Toolchain Directory)",
            "AI Agentlar Floti Indeksi (AI Agent Fleet Index)",
            "Faol Loyihalar Markazi (Active Projects Hub)",
            "Obsidian PARA & Skills Navigatsiya Xaritasi (PARA Structure & Skills Navigation)",
            "Sessiya Boshlash va Yakunlash Protokollari (Session Lifecycle Protocols)"
        ]

        for req in required_h2:
            self.assertTrue(
                any(req in t for t in titles),
                f"Missing mandatory H2 section: '{req}'. Found: {titles}"
            )

    def test_master_brain_required_h3_subsections(self):
        """Verify required H3 subsections exist under Lifecycle Protocols."""
        headings = self._parse_markdown_headings(self.mb_body)
        titles = [h["title"] for h in headings if h["level"] == 3]

        required_h3 = [
            "1. Ish Boshlash Protokoli (5-Step Startup Protocol)",
            "2. Yozib Qoldirish Protokoli (4-Step Write-Back Protocol)"
        ]

        for req in required_h3:
            self.assertTrue(
                any(req in t for t in titles),
                f"Missing mandatory H3 subsection: '{req}'. Found: {titles}"
            )

    def test_master_brain_sections_non_empty(self):
        """Verify every heading in Master Brain contains substantial content."""
        headings = self._parse_markdown_headings(self.mb_body)
        for h in headings:
            # Lifecycle parent heading contains subheadings, so its own body can be brief or empty
            if "Sessiya Boshlash va Yakunlash Protokollari" in h["title"]:
                continue
            self.assertGreater(
                len(h["body"]), 50,
                f"Section '{h['title']}' is unexpectedly empty or too short ({len(h['body'])} chars)."
            )

    def test_dashboard_headings_and_non_emptiness(self):
        """Verify Dashboard.md headings and non-emptiness."""
        headings = self._parse_markdown_headings(self.db_body)
        h1s = [h for h in headings if h["level"] == 1]
        self.assertEqual(len(h1s), 1, "Expected 1 H1 heading in Dashboard.md")

        h2_titles = [h["title"] for h in headings if h["level"] == 2]
        expected_h2 = [
            "Tizim Xaritasi (PARA Structure)",
            "Kunlik Rejalar & Aloqa",
            "Faol Loyihalar va Agentlar Markazi",
            "So'nggi Yozuvlar (Quick Links)"
        ]
        for exp in expected_h2:
            self.assertTrue(any(exp in t for t in h2_titles), f"Missing H2 in Dashboard: {exp}")

        for h in headings:
            self.assertGreater(len(h["body"]), 20, f"Dashboard section '{h['title']}' is too short.")

    def test_master_brain_callouts(self):
        """Verify presence of Obsidian callouts in Master Brain."""
        self.assertIn("> [!important]", self.mb_body, "Missing [!important] callout.")
        self.assertIn("> [!warning]", self.mb_body, "Missing [!warning] callout.")
        self.assertIn("> [!tip]", self.mb_body, "Missing [!tip] callout.")

    def test_dashboard_master_brain_callout(self):
        """Verify Master Brain entrypoint callout in Dashboard.md."""
        self.assertIn("> [!important]", self.db_body)
        self.assertIn("[[AI Sozlangan Miyyasi", self.db_body)

    def test_verbatim_git_rules_block(self):
        """Verify RULE[user_global] block matches character-by-character."""
        m = re.search(r"<RULE\[user_global\]>(.*?)</RULE\[user_global\]>", self.mb_body, re.DOTALL)
        self.assertIsNotNone(m, "RULE[user_global] tags missing in Master Brain.")
        block = m.group(1).strip()

        required_clauses = [
            "# Custom Agent Rules",
            "## Git and GitHub Workflow",
            "- **Default to Git**: Always use Git and GitHub when working on any project.",
            "- **Automatic Lifecycle Operations**: Perform Git commands automatically during development without requiring the user to type them:",
            "- **Initialization**: Run `git init` automatically if the folder is not already a Git repository.",
            "- **Status & Tracking**: Run `git status` to inspect changed files, and `git add .` to stage them.",
            "- **Commits**: Make incremental commits with descriptive messages using `git commit -m \"Descriptive commit message\"`.",
            "- **Syncing**: Run `git pull` to fetch latest changes before editing, and `git push` to upload completed work to GitHub.",
            "- **Automatic Branching for Major Changes**: When implementing significant features, bug fixes, refactoring, or any major changes, automatically create a new Git branch with a descriptive name (e.g., `feature/description` or `fix/description`) instead of working directly on `main` or `master`."
        ]
        for clause in required_clauses:
            self.assertIn(clause, block, f"Missing verbatim clause in RULE[user_global]: {clause}")


class TestCharacterEncodingAndUTF8Integrity(unittest.TestCase):
    """EMPIRICAL TEST CATEGORY 3: Character Encoding & UTF-8 Integrity."""

    def test_no_utf8_bom(self):
        """Verify neither file contains a UTF-8 Byte Order Mark (BOM)."""
        for p in [MASTER_BRAIN_PATH, DASHBOARD_PATH]:
            raw = p.read_bytes()
            self.assertFalse(raw.startswith(b"\xef\xbb\xbf"), f"{p.name} contains UTF-8 BOM.")

    def test_strict_utf8_decodable(self):
        """Verify byte stream strictly decodes as valid UTF-8 without replacement/errors."""
        for p in [MASTER_BRAIN_PATH, DASHBOARD_PATH]:
            raw = p.read_bytes()
            try:
                decoded = raw.decode("utf-8", errors="strict")
                self.assertGreater(len(decoded), 0)
            except UnicodeDecodeError as e:
                self.fail(f"{p.name} failed strict UTF-8 decode: {e}")

    def test_no_mojibake_or_double_encoding(self):
        """Verify absence of common UTF-8 mojibake / double-encoding corruption artifacts."""
        mojibake_tokens = [
            "Ã©", "Ã¢", "Â", "â€™", "Ã¼", "Ã¶", "â€”", "ï¿½", "\ufffd", "Ã ", "â€“", "Ã¡", "Ã­"
        ]
        for p in [MASTER_BRAIN_PATH, DASHBOARD_PATH]:
            text = p.read_text(encoding="utf-8")
            for token in mojibake_tokens:
                self.assertNotIn(token, text, f"Mojibake artifact '{token}' found in {p.name}")

    def test_uzbek_latin_orthography(self):
        """Verify Uzbek Latin characters (o', g', apostrophes) are cleanly preserved."""
        text = MASTER_BRAIN_PATH.read_text(encoding="utf-8")
        expected_uzbek_words = [
            "g'oyalarni", "yo'riqnoma", "boshlang'ich", "o'zgarish", "to'xtash", "bo'lim"
        ]
        for word in expected_uzbek_words:
            self.assertTrue(
                word in text.lower(),
                f"Expected Uzbek word '{word}' not found or corrupted in Master Brain."
            )

    def test_emoji_unicode_validity(self):
        """Verify all emojis decode and encode back to UTF-8 without dangling surrogates."""
        for p in [MASTER_BRAIN_PATH, DASHBOARD_PATH]:
            text = p.read_text(encoding="utf-8")
            emojis = re.findall(r"[\U00010000-\U0010ffff]|[\u2600-\u27bf]|[\u2300-\u23ff]", text)
            self.assertGreater(len(emojis), 5, f"Expected emojis in {p.name}")
            for em in emojis:
                try:
                    em_bytes = em.encode("utf-8")
                    self.assertEqual(em_bytes.decode("utf-8"), em)
                except Exception as e:
                    self.fail(f"Invalid emoji sequence '{em}' in {p.name}: {e}")

    def test_line_ending_consistency(self):
        """Verify uniform line endings within each file (no mixed CRLF/LF)."""
        for p in [MASTER_BRAIN_PATH, DASHBOARD_PATH]:
            raw = p.read_bytes()
            crlf = raw.count(b"\r\n")
            isolated_lf = raw.count(b"\n") - crlf
            isolated_cr = raw.count(b"\r") - crlf
            # File should be either 100% CRLF or 100% LF
            is_consistent = (crlf == 0 and isolated_lf > 0 and isolated_cr == 0) or \
                            (isolated_lf == 0 and crlf > 0 and isolated_cr == 0)
            self.assertTrue(
                is_consistent,
                f"Mixed line endings in {p.name}: CRLF={crlf}, LF={isolated_lf}, CR={isolated_cr}"
            )


class TestMarkdownSyntaxAndAstIntegrity(unittest.TestCase):
    """EMPIRICAL TEST CATEGORY 4: Markdown Syntax, AST & Link Integrity."""

    def test_code_fences_balanced(self):
        """Verify opening ``` fences match closing ``` fences."""
        for p in [MASTER_BRAIN_PATH, DASHBOARD_PATH]:
            lines = p.read_text(encoding="utf-8").splitlines()
            fence_lines = [i + 1 for i, l in enumerate(lines) if l.strip().startswith("```")]
            self.assertEqual(
                len(fence_lines) % 2, 0,
                f"Unbalanced code fences in {p.name}. Found fences at lines: {fence_lines}"
            )

    def test_wikilink_brackets_balanced(self):
        """Verify every [[ has a corresponding ]]."""
        for p in [MASTER_BRAIN_PATH, DASHBOARD_PATH]:
            text = p.read_text(encoding="utf-8")
            open_count = text.count("[[")
            close_count = text.count("]]")
            self.assertEqual(
                open_count, close_count,
                f"Unbalanced wikilink brackets in {p.name}: {open_count} '[[' vs {close_count} ']]'"
            )

    def test_commonmark_ast_clean_parsing(self):
        """Verify markdown-it-py parses both documents into full CommonMark AST without exceptions."""
        parser = markdown_it.MarkdownIt()
        for p in [MASTER_BRAIN_PATH, DASHBOARD_PATH]:
            content = p.read_text(encoding="utf-8")
            try:
                tokens = parser.parse(content)
                self.assertGreater(len(tokens), 20, f"Too few tokens parsed in {p.name}")
            except Exception as e:
                self.fail(f"markdown-it parse error in {p.name}: {e}")

    def test_dashboard_internal_anchors_exist_in_master_brain(self):
        """Verify internal section anchors in Dashboard.md target exact headings in Master Brain."""
        dash_text = DASHBOARD_PATH.read_text(encoding="utf-8")
        anchors = re.findall(r"\[\[AI Sozlangan Miyyasi#([^\]|\\]+)(?:\\?\|[^\]]+)?\]\]", dash_text)
        self.assertGreater(len(anchors), 0, "No internal section anchors found in Dashboard.md")

        mb_text = MASTER_BRAIN_PATH.read_text(encoding="utf-8")
        mb_headings = [l.lstrip("#").strip() for l in mb_text.splitlines() if l.startswith("#")]

        mismatches = []
        for anchor in anchors:
            clean_anchor = anchor.strip()
            if clean_anchor not in mb_headings:
                # Search for closest matching heading
                closest = [h for h in mb_headings if clean_anchor in h]
                mismatches.append(f"Anchor '#{clean_anchor}' -> Heading in Master Brain is actually '{closest[0] if closest else 'UNKNOWN'}'")

        self.assertEqual(
            len(mismatches), 0,
            f"Dashboard.md contains {len(mismatches)} broken internal heading anchor(s):\n" + "\n".join(f"  - {m}" for m in mismatches)
        )


class TestTablePipeDelimitersAdversarial(unittest.TestCase):
    """
    EMPIRICAL TEST CATEGORY 5 (ADVERSARIAL STRESS TEST):
    Table Pipe Delimiters vs CommonMark / GFM Parsing
    Examines whether wikilink aliases containing '|' inside table cells
    cause column count mismatches (MD056) or cell splitting under CommonMark.
    """

    def test_table_column_counts_under_commonmark(self):
        """
        Adversarial probe:
        Checks tables in both files for unescaped '|' inside [[target|alias]]
        and documents the column count behavior under CommonMark / GFM.
        """
        for p in [MASTER_BRAIN_PATH, DASHBOARD_PATH]:
            lines = p.read_text(encoding="utf-8").splitlines()
            in_table = False
            expected_cols = 0

            for line_idx, line in enumerate(lines, 1):
                stripped = line.strip()
                if not stripped.startswith("|") or not stripped.endswith("|"):
                    in_table = False
                    continue

                cells = [c.strip() for c in re.split(r"(?<!\\)\|", stripped)[1:-1]]

                # Header row
                if not in_table and all(c != "---" and not c.startswith(":") for c in cells):
                    in_table = True
                    expected_cols = len(cells)
                    continue

                # Separator row
                if in_table and all(re.match(r"^:?-+:?$", c) for c in cells):
                    continue

                # Data row in table
                if in_table:
                    actual_cols = len(cells)
                    has_aliased_wikilink = bool(re.search(r"\[\[[^\]|\\]+\|[^\]]+\]\]", line))
                    if actual_cols != expected_cols and has_aliased_wikilink:
                        # Unescaped pipe inside [[target|alias]] caused an extra cell in CommonMark
                        print(f"\n[ADVERSARIAL OBSERVATION] {p.name}:{line_idx} - CommonMark split row into {actual_cols} cols (expected {expected_cols}) due to unescaped pipe in wikilink alias.")


if __name__ == "__main__":
    unittest.main()
