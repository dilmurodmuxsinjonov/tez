# -*- coding: utf-8 -*-
"""
Adversarial Verification Suite - Milestone 3 (Gen 2)
Universal AI Second Brain Project - D:\obsidian file
"""

import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

VAULT_DIR = Path(r"D:\obsidian file")
PROJECTS_DIR = VAULT_DIR / "10 Projects"
PROJECT_FILES = [
    "MobCreatorWebApp.md",
    "NagoyaCastle.md",
    "The_AI_Pipeline.md",
    "Orol Shahar Qirollik.md",
    "Doctor A Med Clinic.md",
]

APPROVED_IMPERATIVE_VERBS = {
    "Review", "Inspect", "Refactor", "Draft", "Implement",
    "Audit", "Benchmark", "Verify", "Integrate", "Configure",
    "Test", "Document", "Extract", "Build", "Validate",
}

DISALLOWED_PREFIXES = [
    "you should", "we need to", "next step is", "the codebase requires",
    "i will", "let's", "please", "to implement", "implementing",
]

ALL_10_STYLES = [
    "Thoughtful check-in",
    "Progress celebration",
    "Reflection prompt",
    "Callback to detail",
    "Invitation to continue",
    "Anticipation builder",
    "Gentle nudge",
    "Curiosity spark",
    "Empathetic acknowledgment",
    "Low-pressure opener",
]

REQUIRED_TOPIC_EMOJI_SECTIONS = [
    r"🎯 ACTIVE GOALS",
    r"📋 LATEST STATE",
    r"💡 ARCHITECTURAL DECISIONS",
    r"⚠️ KNOWN ISSUES",
    r"💬 RELEVANT CONVERSATIONS",
    r"🔗 CROSS-DOMAIN DEPENDENCIES",
]


class TestMilestone3Adversarial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault_files = {}
        for root, dirs, files in os.walk(VAULT_DIR):
            rel_root = os.path.relpath(root, VAULT_DIR)
            parts = rel_root.split(os.sep)
            if ".git" in parts or ".agents" in parts:
                continue
            for f in files:
                full_path = Path(root) / f
                rel_path = full_path.relative_to(VAULT_DIR).as_posix()
                stem = full_path.stem
                cls.vault_files[rel_path.lower()] = full_path
                if stem.lower() not in cls.vault_files:
                    cls.vault_files[stem.lower()] = full_path

    def _read_bytes_and_text(self, filename):
        path = PROJECTS_DIR / filename
        self.assertTrue(path.exists(), f"File does not exist: {path}")
        raw_bytes = path.read_bytes()
        text = raw_bytes.decode("utf-8")
        return path, raw_bytes, text

    # -------------------------------------------------------------------------
    # 1. ENCODING & BOM
    # -------------------------------------------------------------------------
    def test_utf8_without_bom(self):
        """Verify UTF-8 encoding without BOM across all 5 project notes."""
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                path, raw_bytes, text = self._read_bytes_and_text(filename)
                self.assertFalse(
                    raw_bytes.startswith(b"\xef\xbb\xbf"),
                    f"{filename} contains a UTF-8 Byte Order Mark (BOM)!"
                )
                self.assertFalse(
                    raw_bytes.startswith(b"\xff\xfe") or raw_bytes.startswith(b"\xfe\xff"),
                    f"{filename} contains a UTF-16 BOM!"
                )
                self.assertNotIn(
                    "\ufffd", text,
                    f"{filename} contains Unicode replacement character (U+FFFD), indicating corrupt encoding!"
                )
                self.assertEqual(
                    text.encode("utf-8"), raw_bytes,
                    f"{filename} round-trip UTF-8 encoding failed!"
                )

    # -------------------------------------------------------------------------
    # 2. SUGGESTED NEXT STEPS: REGEX BOUNDARIES & IMPERATIVE VERBS
    # -------------------------------------------------------------------------
    def test_suggested_next_steps_imperative_verbs_and_bounds(self):
        """Stress-test suggested next steps for imperative verbs, regex format, and count."""
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                _, _, text = self._read_bytes_and_text(filename)
                
                m = re.search(r"## 🎯 Suggested Next Steps\s*\n(.*?)(?=\n\n\n\n\n|\n```|\Z)", text, re.DOTALL)
                self.assertIsNotNone(m, f"{filename}: Could not find ## 🎯 Suggested Next Steps section")
                section_content = m.group(1).strip()
                
                lines = [line.strip() for line in section_content.splitlines() if line.strip()]
                
                self.assertGreaterEqual(
                    len(lines), 2,
                    f"{filename}: Less than 2 suggested next steps found ({len(lines)})"
                )
                self.assertLessEqual(
                    len(lines), 4,
                    f"{filename}: More than 4 suggested next steps found ({len(lines)})"
                )
                
                seen_steps = set()
                for line in lines:
                    self.assertTrue(
                        line.startswith("- "),
                        f"{filename}: Next step does not start with '- ': '{line}'"
                    )
                    step_text = line[2:].strip()
                    
                    self.assertNotIn(
                        step_text, seen_steps,
                        f"{filename}: Duplicate suggestion found: '{step_text}'"
                    )
                    seen_steps.add(step_text)
                    
                    regex_match = re.match(r"^[A-Z][a-z]+ .+$", step_text)
                    self.assertIsNotNone(
                        regex_match,
                        f"{filename}: Suggestion '{step_text}' failed regex '^[A-Z][a-z]+ .+$'"
                    )
                    
                    first_word = step_text.split()[0]
                    self.assertIn(
                        first_word, APPROVED_IMPERATIVE_VERBS,
                        f"{filename}: First word '{first_word}' in '{step_text}' is not an approved imperative verb!"
                    )
                    
                    step_lower = step_text.lower()
                    for dis in DISALLOWED_PREFIXES:
                        self.assertFalse(
                            step_lower.startswith(dis),
                            f"{filename}: Suggestion contains disallowed conversational prefix '{dis}': '{step_text}'"
                        )

    # -------------------------------------------------------------------------
    # 3. CHARACTER LENGTH COMPLIANCE (60 <= len <= 85)
    # -------------------------------------------------------------------------
    def test_suggested_next_steps_character_length(self):
        """Verify strict length bounds: 60 <= len <= 85 characters for all suggestions."""
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                _, _, text = self._read_bytes_and_text(filename)
                m = re.search(r"## 🎯 Suggested Next Steps\s*\n(.*?)(?=\n\n\n\n\n|\n```|\Z)", text, re.DOTALL)
                self.assertIsNotNone(m)
                lines = [line.strip() for line in m.group(1).splitlines() if line.strip()]
                for line in lines:
                    step_text = line[2:].strip()
                    char_len = len(step_text)
                    self.assertGreaterEqual(
                        char_len, 60,
                        f"{filename}: Suggestion length {char_len} < 60 chars: '{step_text}'"
                    )
                    self.assertLessEqual(
                        char_len, 85,
                        f"{filename}: Suggestion length {char_len} > 85 chars: '{step_text}'"
                    )
                    self.assertEqual(
                        len(step_text), len(step_text.encode("utf-8").decode("utf-8")),
                        f"{filename}: Code point discrepancy in length!"
                    )

    # -------------------------------------------------------------------------
    # 4. EXACT COUNT OF 5 BLANK LINES BEFORE CODE BLOCKS
    # -------------------------------------------------------------------------
    def test_exact_5_blank_lines_visual_separation(self):
        """Verify exact count of 5 blank lines (\n\n\n\n\n\n) before code blocks."""
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                _, _, text = self._read_bytes_and_text(filename)
                normalized_text = text.replace("\r\n", "\n")
                
                m = re.search(r"(## 🎯 Suggested Next Steps.*?)(```text)", normalized_text, re.DOTALL)
                self.assertIsNotNone(m, f"{filename}: Could not find region between Suggested Next Steps and ```text")
                
                section_text = m.group(1)
                last_step_end = len(section_text.rstrip())
                separation = section_text[last_step_end:]
                
                newline_count = separation.count("\n")
                blank_lines = newline_count - 1
                
                self.assertEqual(
                    newline_count, 6,
                    f"{filename}: Expected exactly 6 newline characters (\n\n\n\n\n\n) yielding 5 blank lines, got {newline_count} newlines ({blank_lines} blank lines)! Separation: {repr(separation)}"
                )
                
                stripped_separation = separation.replace("\n", "")
                self.assertEqual(
                    stripped_separation, "",
                    f"{filename}: Blank lines contain dirty whitespace characters: {repr(stripped_separation)}"
                )

    # -------------------------------------------------------------------------
    # 5. ZERO LINES EXCEEDING 80 CHARACTERS INSIDE CODE BLOCKS
    # -------------------------------------------------------------------------
    def test_code_block_line_lengths_under_80(self):
        """Verify that inside ```text ... ``` blocks, zero lines exceed 80 characters."""
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                _, _, text = self._read_bytes_and_text(filename)
                
                m = re.search(r"```text\s*\n(.*?)\n```", text, re.DOTALL)
                self.assertIsNotNone(m, f"{filename}: Could not find ```text code block")
                code_content = m.group(1)
                
                lines = code_content.splitlines()
                overlong_lines = []
                for idx, line in enumerate(lines, 1):
                    if len(line) > 80:
                        overlong_lines.append((idx, len(line), line))
                
                self.assertEqual(
                    overlong_lines, [],
                    f"{filename}: Found {len(overlong_lines)} lines exceeding 80 characters in code block:\n" +
                    "\n".join([f"  Line {idx} ({l} chars): '{content}'" for idx, l, content in overlong_lines])
                )
                
                max_len = max(len(line) for line in lines) if lines else 0
                self.assertLessEqual(
                    max_len, 80,
                    f"{filename}: Maximum line length {max_len} > 80!"
                )

    # -------------------------------------------------------------------------
    # 6. CLEAN WIKILINK RESOLUTION AGAINST PHYSICAL VAULT
    # -------------------------------------------------------------------------
    def test_clean_wikilink_resolution(self):
        """Verify 100% clean wikilink resolution against physical vault files."""
        wikilink_pattern = re.compile(r"\[\[(.*?)\]\]")
        
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                _, _, text = self._read_bytes_and_text(filename)
                
                matches = wikilink_pattern.findall(text)
                self.assertGreater(
                    len(matches), 0,
                    f"{filename}: No wikilinks found! Expected links to Master Brain and related notes."
                )
                
                unresolved = []
                for raw_target in matches:
                    target = raw_target.split("|")[0].strip()
                    if "#" in target:
                        target = target.split("#", 1)[0].strip()
                    
                    if not target:
                        continue
                    
                    target_norm = target.replace("\\", "/").lower()
                    if target_norm.endswith(".md"):
                        target_norm = target_norm[:-3]
                    
                    resolved = False
                    for ext in ["", ".md", ".canvas", ".base"]:
                        candidate = (target_norm + ext).lower()
                        if candidate in self.vault_files:
                            resolved = True
                            break
                    
                    if not resolved:
                        stem = Path(target_norm).stem.lower()
                        if stem in self.vault_files:
                            resolved = True
                    
                    if not resolved:
                        unresolved.append(raw_target)
                
                self.assertEqual(
                    unresolved, [],
                    f"{filename}: Found unresolved wikilinks: {unresolved}"
                )

    # -------------------------------------------------------------------------
    # 7. RECIPROCAL MASTER BRAIN LINKING
    # -------------------------------------------------------------------------
    def test_reciprocal_master_brain_linking(self):
        """Verify reciprocal link to [[AI Sozlangan Miyyasi]] exists in header and block."""
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                _, _, text = self._read_bytes_and_text(filename)
                self.assertIn(
                    "[[AI Sozlangan Miyyasi]]", text,
                    f"{filename}: Missing reciprocal link to [[AI Sozlangan Miyyasi]]!"
                )

    # -------------------------------------------------------------------------
    # 8. YAML FRONTMATTER INTEGRITY
    # -------------------------------------------------------------------------
    def test_yaml_frontmatter_schema(self):
        """Verify YAML frontmatter exists, contains required keys, and is valid."""
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                _, _, text = self._read_bytes_and_text(filename)
                self.assertTrue(text.startswith("---\n"), f"{filename}: Does not start with frontmatter '---'")
                end_fm = text.find("\n---\n", 4)
                self.assertGreater(end_fm, 0, f"{filename}: Frontmatter does not properly close with '---'")
                fm_text = text[4:end_fm]
                
                required_keys = ["title:", "version:", "status:", "type:", "tags:", "project_path:", "tech_stack:"]
                for k in required_keys:
                    self.assertIn(k, fm_text, f"{filename}: Missing YAML frontmatter key '{k}'")
                
                self.assertIn("version: 1.0.0", fm_text)
                self.assertIn("status: active", fm_text)
                self.assertIn("type: project-memory", fm_text)

    # -------------------------------------------------------------------------
    # 9. LATEST STATE SUMMARY WORD & SENTENCE BOUNDS
    # -------------------------------------------------------------------------
    def test_latest_state_summary_word_and_sentence_bounds(self):
        """Verify Latest State Summary is 1-2 sentences and 30-50 words."""
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                _, _, text = self._read_bytes_and_text(filename)
                m = re.search(r"## 📋 Latest State Summary\s*\n\s*(.*?)(?=\n---\n|\n## |\Z)", text, re.DOTALL)
                self.assertIsNotNone(m, f"{filename}: Could not find ## 📋 Latest State Summary section")
                summary = m.group(1).strip()
                
                words = summary.split()
                word_count = len(words)
                self.assertGreaterEqual(
                    word_count, 30,
                    f"{filename}: Latest State word count {word_count} < 30 words!"
                )
                self.assertLessEqual(
                    word_count, 50,
                    f"{filename}: Latest State word count {word_count} > 50 words!"
                )
                
                sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", summary) if s.strip()]
                self.assertGreaterEqual(
                    len(sentences), 1,
                    f"{filename}: Latest State has 0 sentences!"
                )
                self.assertLessEqual(
                    len(sentences), 2,
                    f"{filename}: Latest State has {len(sentences)} sentences (max 2 allowed)!"
                )

    # -------------------------------------------------------------------------
    # 10. GOALS & DECISIONS LOG (ADR) TABLE SCHEMA
    # -------------------------------------------------------------------------
    def test_adr_table_schema(self):
        """Verify ADR table contains exact 7 columns and at least 1 active decision."""
        expected_header = "| Sana | ADR ID | Decision & Scope | Rationale | Alternatives | Holat | Muallif |"
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                _, _, text = self._read_bytes_and_text(filename)
                self.assertIn(
                    expected_header, text,
                    f"{filename}: ADR table header does not match exact schema '{expected_header}'"
                )
                m = re.search(r"## 💡 Goals & Decisions Log \(ADR\)\s*\n\s*(.*?)(?=\n---\n|\n## |\Z)", text, re.DOTALL)
                self.assertIsNotNone(m)
                adr_content = m.group(1)
                rows = [line.strip() for line in adr_content.splitlines() if line.strip().startswith("|") and "---" not in line and "Sana" not in line]
                self.assertGreaterEqual(
                    len(rows), 1,
                    f"{filename}: ADR table contains no data rows!"
                )
                for row in rows:
                    cols = [c.strip() for c in row.split("|")[1:-1]]
                    self.assertEqual(
                        len(cols), 7,
                        f"{filename}: ADR row does not have 7 columns: '{row}'"
                    )

    # -------------------------------------------------------------------------
    # 11. ALL 10 COMMUNICATION STYLES PRESENT
    # -------------------------------------------------------------------------
    def test_all_10_communication_styles(self):
        """Verify all 10 communication styles are documented with contextual # headers."""
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                _, _, text = self._read_bytes_and_text(filename)
                m = re.search(r"## 💬 Interaction Dynamics.*?\(10 Communication Styles\)\s*\n\s*(.*?)(?=\n---\n|\n## |\Z)", text, re.DOTALL)
                self.assertIsNotNone(m, f"{filename}: Missing 10 Communication Styles section")
                styles_content = m.group(1)
                for style in ALL_10_STYLES:
                    self.assertIn(
                        style, styles_content,
                        f"{filename}: Missing communication style '{style}'!"
                    )
                headers = re.findall(r"`#\s+[^`]+`", styles_content)
                self.assertEqual(
                    len(headers), 10,
                    f"{filename}: Expected 10 `# <Greeting>` headers, found {len(headers)}"
                )

    # -------------------------------------------------------------------------
    # 12. EMOJI-TAGGED TOPIC MEMORY BLOCK SECTIONS
    # -------------------------------------------------------------------------
    def test_emoji_tagged_code_block_sections(self):
        """Verify all 6 required emoji sections exist inside the ```text code block."""
        for filename in PROJECT_FILES:
            with self.subTest(file=filename):
                _, _, text = self._read_bytes_and_text(filename)
                m = re.search(r"```text\s*\n(.*?)\n```", text, re.DOTALL)
                self.assertIsNotNone(m)
                code_content = m.group(1)
                for sec_pattern in REQUIRED_TOPIC_EMOJI_SECTIONS:
                    self.assertTrue(
                        re.search(sec_pattern, code_content),
                        f"{filename}: Missing required section pattern '{sec_pattern}' in code block!"
                    )

    # -------------------------------------------------------------------------
    # 13. GIT REPOSITORY STATUS & COMMITS
    # -------------------------------------------------------------------------
    def test_git_branch_and_status(self):
        """Verify working branch is feature/universal-ai-second-brain and 10 Projects has no uncommitted changes."""
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=str(VAULT_DIR), text=True).strip()
        self.assertEqual(
            branch, "feature/universal-ai-second-brain",
            f"Git branch is '{branch}', expected 'feature/universal-ai-second-brain'!"
        )
        
        status = subprocess.check_output(["git", "status", "--porcelain", "10 Projects"], cwd=str(VAULT_DIR), text=True).strip()
        self.assertEqual(
            status, "",
            f"Uncommitted changes detected in 10 Projects/:\n{status}"
        )
        
        log_out = subprocess.check_output(["git", "log", "-n", "5", "--oneline"], cwd=str(VAULT_DIR), text=True)
        self.assertIn(
            "feat(m3): verify and ensure 100% compliance for all 5 Gemini Topics active project notes",
            log_out,
            "Recent git log does not contain Milestone 3 Gen 2 commit!"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)