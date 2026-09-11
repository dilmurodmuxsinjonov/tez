#!/usr/bin/env python3
"""
Universal AI Second Brain - Milestone 5 Adversarial Coverage Hardening Suite
Author: Milestone 5 Adversarial Challenger (Generation 2)
Location: D:\\obsidian file\\.agents\\challenger_m5_gen2\\adversarial_m5_hardening.py

Stress-tests:
1. Full vault graph bidirectional connectivity (zero orphan notes across all 65+ files).
2. Case-sensitivity, alias piping, and heading anchor formatting of wikilinks.
3. Concurrency lock collision simulation, TTL stale lock recovery, and multi-thread contention.
4. Comprehensive UTF-8 verification without BOM on all markdown and metadata files.
5. Boundary tests for Gemini Topics next steps and Latest State word bounds.
"""

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time
import unittest
from typing import Any, Dict, List, Optional, Set, Tuple

VAULT_ROOT = Path(r"D:\obsidian file")
sys.path.insert(0, str(VAULT_ROOT))

try:
    from tests.e2e.concurrency_sim import ConcurrencyProtocolManager, LockResult
    from tests.e2e.helpers import (
        ACTIVE_PROJECTS,
        AGENT_PROFILES,
        APPROVED_ACTION_VERBS,
        COMMUNICATION_STYLES,
        PARA_MOCS,
        check_file_utf8_clean,
        check_visual_separation,
        extract_wikilinks,
        parse_frontmatter,
        resolve_wikilink,
        validate_suggested_next_step,
    )
except ImportError:
    # Fallback if running outside root
    pass


def get_all_vault_markdown_files(vault_path: Path, ignored_dirs: Optional[Set[str]] = None) -> List[Tuple[Path, str]]:
    """Discovers all markdown files in vault excluding agent metadata and git dirs."""
    if ignored_dirs is None:
        ignored_dirs = {".agents", ".antigravity", ".git", ".obsidian"}
    md_files = []
    for root, dirs, files in os.walk(vault_path):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for f in files:
            if f.endswith(".md"):
                full_p = Path(root) / f
                rel_p = full_p.relative_to(vault_path).as_posix()
                md_files.append((full_p, rel_p))
    return sorted(md_files, key=lambda x: x[1])


def build_vault_graph(vault_path: Path, md_files: List[Tuple[Path, str]]) -> Dict[str, Any]:
    """Builds bidirectional graph of all markdown files and tracks broken links and case mismatches."""
    files_exact = {}
    files_lower = {}
    
    # Index all vault files (including non-md)
    ignored_dirs = {".agents", ".antigravity", ".git", ".obsidian"}
    for root, dirs, files in os.walk(vault_path):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for f in files:
            full_path = Path(root) / f
            rel_path = full_path.relative_to(vault_path).as_posix()
            base_name = full_path.stem
            
            files_exact[rel_path] = full_path
            files_exact[base_name] = full_path
            files_exact[f] = full_path
            
            files_lower[rel_path.lower()] = (rel_path, full_path)
            files_lower[base_name.lower()] = (rel_path, full_path)
            files_lower[f.lower()] = (rel_path, full_path)

    wikilink_regex = re.compile(r"(!?)\[\[([^\]\r\n]+)\]\]")
    
    in_links = {rel: [] for _, rel in md_files}
    out_links = {rel: [] for _, rel in md_files}
    broken_links = []
    case_mismatches = []
    anchor_failures = []
    all_links = []

    for full_path, rel_path in md_files:
        try:
            content = full_path.read_text(encoding="utf-8")
        except Exception:
            content = full_path.read_text(encoding="utf-8", errors="replace")

        # Strip code blocks and inline code spans so didactic/example links in backticks are not treated as active wikilinks
        content_clean = re.sub(r"```[\s\S]*?```", "", content)
        content_clean = re.sub(r"`[^`\r\n]*`", "", content_clean)

        for m in wikilink_regex.finditer(content_clean):
            inner = m.group(2).strip()
            # Alias pipe
            if "|" in inner:
                target_part = re.split(r"\\?\|", inner, maxsplit=1)[0].rstrip("\\").strip()
            else:
                target_part = inner.rstrip("\\").strip()

            # Heading anchor
            anchor = None
            if "#" in target_part:
                parts = target_part.split("#", 1)
                target = parts[0].rstrip("\\").strip()
                anchor = parts[1].rstrip("\\").strip()
            else:
                target = target_part

            if not target or target == "...":
                continue

            all_links.append((rel_path, target))
            norm_target = target.replace("\\", "/").rstrip("/")

            resolved_exact = None
            resolved_lower = None

            # 1. Exact match
            for candidate in [norm_target, f"{norm_target}.md", Path(norm_target).name, f"{Path(norm_target).name}.md"]:
                if candidate in files_exact:
                    resolved_exact = files_exact[candidate]
                    break

            # 2. Case-insensitive match
            for candidate in [norm_target.lower(), f"{norm_target.lower()}.md", Path(norm_target).name.lower(), f"{Path(norm_target).name.lower()}.md"]:
                if candidate in files_lower:
                    resolved_lower = files_lower[candidate]
                    break

            # 3. Folder MOC convention
            folder_moc = f"{norm_target}/{Path(norm_target).name}"
            if folder_moc in files_exact or f"{folder_moc}.md" in files_exact:
                resolved_exact = files_exact.get(folder_moc) or files_exact.get(f"{folder_moc}.md")
            elif folder_moc.lower() in files_lower or f"{folder_moc.lower()}.md" in files_lower:
                resolved_lower = files_lower.get(folder_moc.lower()) or files_lower.get(f"{folder_moc.lower()}.md")

            if resolved_exact:
                target_rel = resolved_exact.relative_to(vault_path).as_posix()
                out_links[rel_path].append((target_rel, target))
                if target_rel in in_links:
                    in_links[target_rel].append((rel_path, target))

                # Check anchor
                if anchor and resolved_exact.suffix == ".md":
                    t_content = resolved_exact.read_text(encoding="utf-8", errors="replace")
                    t_headings = {h.strip() for h in re.findall(r"^#{1,6}\s+(.+)$", t_content, flags=re.MULTILINE)}
                    t_clean = {re.sub(r"[*_`]", "", h).strip() for h in t_headings}
                    if anchor not in t_headings and anchor not in t_clean:
                        anchor_failures.append((rel_path, target, anchor))

            elif resolved_lower:
                target_rel, _ = resolved_lower
                case_mismatches.append((rel_path, target, target_rel))
                out_links[rel_path].append((target_rel, target))
                if target_rel in in_links:
                    in_links[target_rel].append((rel_path, target))
            else:
                broken_links.append((rel_path, target))

    orphans_in = [rel for rel, links in in_links.items() if len(links) == 0]
    orphans_out = [rel for rel, links in out_links.items() if len(links) == 0]
    pure_islands = [rel for rel in orphans_in if rel in orphans_out]

    return {
        "in_links": in_links,
        "out_links": out_links,
        "broken_links": broken_links,
        "case_mismatches": case_mismatches,
        "anchor_failures": anchor_failures,
        "orphans_in": orphans_in,
        "orphans_out": orphans_out,
        "pure_islands": pure_islands,
        "total_links": len(all_links),
    }


class TestAdversarialVaultGraphConnectivity(unittest.TestCase):
    """Stress-test: Vault Graph Bidirectional Connectivity & Zero Orphan Notes across all 65+ files."""

    @classmethod
    def setUpClass(cls):
        cls.md_files = get_all_vault_markdown_files(VAULT_ROOT)
        cls.graph = build_vault_graph(VAULT_ROOT, cls.md_files)

    def test_adv101_vault_contains_at_least_65_markdown_files(self):
        """ADV1.01: Vault must contain >= 65 active markdown files across all PARA folders."""
        self.assertGreaterEqual(
            len(self.md_files),
            65,
            f"Expected at least 65 markdown files, found {len(self.md_files)}"
        )

    def test_adv102_zero_broken_wikilinks_in_active_project_and_profile_notes(self):
        """ADV1.02: Core active project notes and agent profiles must have ZERO broken wikilinks."""
        core_dirs = ("10 Projects/", "20 Areas/Agent Profiles/", "AI Sozlangan Miyyasi.md", "Dashboard.md")
        core_broken = [
            (src, tgt) for src, tgt in self.graph["broken_links"]
            if any(src.startswith(prefix) or src == prefix for prefix in core_dirs)
        ]
        self.assertEqual(
            len(core_broken),
            0,
            f"Core notes contain broken wikilinks: {core_broken}"
        )

    def test_adv103_vault_wide_broken_wikilink_audit(self):
        """ADV1.03: Vault-wide broken link audit. Discovers any invalid wikilink across all 65 files."""
        broken = self.graph["broken_links"]
        # Adversarial check: Detect any broken links in the vault
        self.assertEqual(
            len(broken),
            0,
            f"Vault contains {len(broken)} broken wikilinks: {broken}"
        )

    def test_adv104_zero_orphan_incoming_links_core_notes(self):
        """ADV1.04: All core project notes, agent profiles, and PARA MOCs must have incoming links."""
        core_notes = [
            "AI Sozlangan Miyyasi.md",
            "Dashboard.md",
            "00 Inbox/00 Inbox.md",
            "10 Projects/10 Projects.md",
            "20 Areas/20 Areas.md",
            "30 Resources/30 Resources.md",
            "40 Archives/40 Archives.md",
        ]
        for proj in ["MobCreatorWebApp", "NagoyaCastle", "The_AI_Pipeline", "Orol Shahar Qirollik", "Doctor A Med Clinic"]:
            core_notes.append(f"10 Projects/{proj}.md")
        for prof in ["Antigravity 1", "Antigravity 2", "Codex LLM Assistant", "Concurrency & Sync Protocol"]:
            core_notes.append(f"20 Areas/Agent Profiles/{prof}.md")

        for note in core_notes:
            inbound = self.graph["in_links"].get(note, [])
            self.assertGreater(
                len(inbound),
                0,
                f"Core note {note} is orphaned (in-degree = 0, no notes link to it)."
            )

    def test_adv105_zero_orphan_incoming_links_vault_wide(self):
        """ADV1.05: Vault-wide orphan check. Every markdown file in vault must have >= 1 incoming link."""
        orphans = self.graph["orphans_in"]
        self.assertEqual(
            len(orphans),
            0,
            f"Found {len(orphans)} orphan markdown files with no inbound links: {orphans}"
        )

    def test_adv106_zero_pure_island_nodes_vault_wide(self):
        """ADV1.06: No file in the vault should be a pure isolated island (in-degree=0 AND out-degree=0)."""
        islands = self.graph["pure_islands"]
        self.assertEqual(
            len(islands),
            0,
            f"Found pure island notes completely disconnected from vault graph: {islands}"
        )

    def test_adv107_core_notes_bidirectional_connectivity(self):
        """ADV1.07: Every core note must have BOTH inbound (>= 1) and outbound (>= 1) links."""
        core_notes = [
            "AI Sozlangan Miyyasi.md",
            "Dashboard.md",
            "00 Inbox/00 Inbox.md",
            "10 Projects/10 Projects.md",
            "20 Areas/20 Areas.md",
            "30 Resources/30 Resources.md",
            "40 Archives/40 Archives.md",
            "10 Projects/MobCreatorWebApp.md",
            "10 Projects/NagoyaCastle.md",
            "10 Projects/The_AI_Pipeline.md",
            "10 Projects/Orol Shahar Qirollik.md",
            "10 Projects/Doctor A Med Clinic.md",
            "20 Areas/Agent Profiles/Antigravity 1.md",
            "20 Areas/Agent Profiles/Antigravity 2.md",
            "20 Areas/Agent Profiles/Codex LLM Assistant.md",
            "20 Areas/Agent Profiles/Concurrency & Sync Protocol.md",
        ]
        for note in core_notes:
            in_count = len(self.graph["in_links"].get(note, []))
            out_count = len(self.graph["out_links"].get(note, []))
            self.assertGreater(in_count, 0, f"{note} lacks inbound links (in-degree={in_count})")
            self.assertGreater(out_count, 0, f"{note} lacks outbound links (out-degree={out_count})")


class TestAdversarialWikilinkCaseAndAliasFormatting(unittest.TestCase):
    """Stress-test: Case-Sensitivity, Alias Piping, and Heading Anchor Formatting."""

    @classmethod
    def setUpClass(cls):
        cls.md_files = get_all_vault_markdown_files(VAULT_ROOT)
        cls.graph = build_vault_graph(VAULT_ROOT, cls.md_files)

    def test_adv201_wikilink_case_sensitivity_alignment(self):
        """ADV2.01: All wikilinks in the vault must match the exact disk case of their target files."""
        mismatches = self.graph["case_mismatches"]
        self.assertEqual(
            len(mismatches),
            0,
            f"Found wikilinks with case mismatches (cross-platform risk on Linux/Git): {mismatches}"
        )

    def test_adv202_wikilink_heading_anchors_exist_in_target(self):
        """ADV2.02: All heading anchors ([[Target#Heading]]) must correspond to actual headings."""
        failures = self.graph["anchor_failures"]
        self.assertEqual(
            len(failures),
            0,
            f"Found wikilinks pointing to non-existent headings: {failures}"
        )

    def test_adv203_wikilink_alias_syntax_robustness(self):
        """ADV2.03: Stress-test alias parsing against standard and escaped pipes."""
        synthetic_cases = [
            ("[[AI Sozlangan Miyyasi|Boshqaruv]]", "AI Sozlangan Miyyasi", "Boshqaruv"),
            (r"[[AI Sozlangan Miyyasi\|Boshqaruv Markazi]]", "AI Sozlangan Miyyasi", "Boshqaruv Markazi"),
            ("[[10 Projects/10 Projects|Projects MOC]]", "10 Projects/10 Projects", "Projects MOC"),
            (r"[[20 Areas/Agent Profiles/Antigravity 1\|AG-1]]", "20 Areas/Agent Profiles/Antigravity 1", "AG-1"),
        ]
        for text, expected_target, expected_alias in synthetic_cases:
            links = extract_wikilinks(text)
            self.assertEqual(len(links), 1)
            self.assertEqual(links[0]["target"], expected_target)
            self.assertEqual(links[0]["alias"], expected_alias)

    def test_adv204_wikilink_no_raw_windows_backslashes(self):
        """ADV2.04: Wikilinks across all markdown files must NOT use Windows backslashes in paths."""
        backslash_links = []
        for full_p, rel_p in self.md_files:
            content = full_p.read_text(encoding="utf-8", errors="replace")
            links = extract_wikilinks(content)
            for link in links:
                if "\\" in link["target"]:
                    backslash_links.append((rel_p, link["target"]))
        self.assertEqual(
            len(backslash_links),
            0,
            f"Found wikilinks containing unnormalized backslashes: {backslash_links}"
        )

    def test_adv205_wikilink_bracket_balance_and_cleanliness(self):
        """ADV2.05: Verify no malformed double brackets across all vault markdown notes."""
        malformed = []
        for full_p, rel_p in self.md_files:
            content = full_p.read_text(encoding="utf-8", errors="replace")
            # Look for [[[ or ]]] or unclosed [[
            open_count = content.count("[[")
            close_count = content.count("]]")
            if open_count != close_count:
                malformed.append((rel_p, f"Bracket mismatch: {open_count} '[[' vs {close_count} ']]'"))
            if "[[[" in content or "]]]" in content:
                malformed.append((rel_p, "Triple brackets detected"))
        self.assertEqual(len(malformed), 0, f"Found malformed wikilink brackets: {malformed}")


class TestAdversarialConcurrencyAndStaleLockRecovery(unittest.TestCase):
    """Stress-test: Concurrency Lock Collision, Stale Lock Recovery, and Multi-thread Contention."""

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_root = Path(self.temp_dir.name)
        self.locks_dir = self.test_root / ".agents" / "locks"
        self.mgr = ConcurrencyProtocolManager(self.test_root, self.locks_dir)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_adv301_collision_rejection_and_data_preservation(self):
        """ADV3.01: Active lock completely blocks second agent and preserves original lock metadata."""
        target = "10 Projects/MobCreatorWebApp.md"
        # Agent 1 locks
        res1 = self.mgr.acquire_lock(target, "Antigravity_1", "conv-001", "refactoring", ttl_seconds=300)
        self.assertTrue(res1.success)
        self.assertFalse(res1.was_stale_recovered)

        # Agent 2 attempts acquisition
        res2 = self.mgr.acquire_lock(target, "Codex_Assistant", "conv-002", "compilation", ttl_seconds=300)
        self.assertFalse(res2.success)
        self.assertIn("Collision", res2.error)
        self.assertIn("Antigravity_1", res2.error)

        # Verify lockfile still belongs to Agent 1
        with open(res1.lock_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data["locked_by"], "Antigravity_1")
        self.assertEqual(data["agent_conv_id"], "conv-001")

    def test_adv302_stale_lock_boundary_conditions(self):
        """ADV3.02: Stale lock threshold: age < TTL is blocked; age >= TTL is broken and recovered."""
        target = "10 Projects/The_AI_Pipeline.md"
        now = time.time()

        # Step 1: Create lock with age = 299 seconds (TTL = 300) -> Still active
        res_init = self.mgr.acquire_lock(
            target, "Antigravity_1", "conv-001", "work", ttl_seconds=300, current_time=now - 299
        )
        self.assertTrue(res_init.success)

        res_boundary_fail = self.mgr.acquire_lock(
            target, "Antigravity_2", "conv-002", "recovery", ttl_seconds=300, current_time=now
        )
        self.assertFalse(res_boundary_fail.success, "Lock at 299s should NOT be stale yet")

        # Step 2: Set lock timestamp to now - 301 seconds -> Stale
        with open(res_init.lock_file, "w", encoding="utf-8") as f:
            json.dump({
                "target_file": target,
                "locked_by": "Antigravity_1",
                "acquired_timestamp": now - 301,
                "ttl_seconds": 300,
            }, f)

        res_stale_success = self.mgr.acquire_lock(
            target, "Antigravity_2", "conv-002", "recovery", ttl_seconds=300, current_time=now
        )
        self.assertTrue(res_stale_success.success, "Stale lock (301s old) must be broken")
        self.assertTrue(res_stale_success.was_stale_recovered)

        # Verify audit log contains STALE_LOCK_BROKEN
        audit_content = self.mgr.audit_log.read_text(encoding="utf-8")
        self.assertIn("STALE_LOCK_BROKEN", audit_content)
        self.assertIn("Antigravity_2", audit_content)

    def test_adv303_corrupt_lockfile_adversarial_recovery(self):
        """ADV3.03: Handles completely corrupt, empty, or partial lockfiles gracefully."""
        target = "10 Projects/Doctor A Med Clinic.md"
        lock_file = self.mgr.get_lock_path(target)

        corrupt_contents = [
            "",  # Empty file
            "{ invalid json ...",  # Malformed JSON
            '{"target_file": "Doctor A Med Clinic.md"}',  # Missing acquired_timestamp
            "\x00\x00\x00\x00",  # Null bytes
        ]

        for idx, bad_content in enumerate(corrupt_contents):
            with open(lock_file, "w", encoding="utf-8") as f:
                f.write(bad_content)
            
            res = self.mgr.acquire_lock(
                target, f"Agent_Corrupt_Test_{idx}", f"conv-{idx}", "recovery", ttl_seconds=300
            )
            self.assertTrue(res.success, f"Failed to recover from corrupt content pattern {idx}")
            self.assertTrue(res.was_stale_recovered, f"Should report stale recovered on corrupt file {idx}")
            self.mgr.release_lock(target, f"Agent_Corrupt_Test_{idx}")

    def test_adv304_multi_threaded_lock_contention(self):
        """ADV3.04: 10 concurrent threads simultaneously race to acquire the exact same file lock."""
        target = "10 Projects/NagoyaCastle.md"
        results = []

        def worker(agent_idx: int):
            mgr = ConcurrencyProtocolManager(self.test_root, self.locks_dir)
            try:
                return mgr.acquire_lock(
                    target, f"Agent_{agent_idx}", f"conv-{agent_idx}", "stress_test", ttl_seconds=300
                )
            except PermissionError as pe:
                return LockResult(
                    success=False,
                    lock_file=mgr.get_lock_path(target),
                    error=f"Unhandled Windows NT PermissionError [WinError 5]: {pe}"
                )

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(worker, i) for i in range(10)]
            for fut in futures:
                results.append(fut.result())

        # Adversarial check: Windows file locking race condition bug
        unhandled_permission_errors = [r for r in results if r.error and "PermissionError" in r.error]
        self.assertEqual(
            len(unhandled_permission_errors),
            0,
            f"ConcurrencyProtocolManager failed under high thread contention with OS PermissionError: {unhandled_permission_errors}"
        )

    def test_adv305_atomic_write_rollback_integrity(self):
        """ADV3.05: Atomic write rollback leaves zero leftover temporary files on validation failure."""
        target_file = self.test_root / "test_doc.md"
        target_file.write_text("# Original Content\n", encoding="utf-8")

        def failing_validator(content: str) -> Tuple[bool, Optional[str]]:
            return False, "Synthetic security validation failure"

        success, err = self.mgr.atomic_write(
            target_file, "# Malicious Unvalidated Overwrite\n", "agent-malicious", validator=failing_validator
        )
        self.assertFalse(success)
        self.assertIn("Validation failed", err)

        # Original content must be strictly untouched
        self.assertEqual(target_file.read_text(encoding="utf-8"), "# Original Content\n")

        # Zero temporary files in folder
        temp_files = list(self.test_root.glob("*.tmp*"))
        self.assertEqual(len(temp_files), 0, f"Leftover temporary files found: {temp_files}")


class TestAdversarialVaultUtf8NoBomHygiene(unittest.TestCase):
    """Stress-test: Comprehensive UTF-8 Verification Without BOM across all markdown files."""

    @classmethod
    def setUpClass(cls):
        cls.md_files = get_all_vault_markdown_files(VAULT_ROOT)

    def test_adv401_all_vault_markdown_files_no_bom(self):
        """ADV4.01: Verifies that NO markdown file in the entire vault contains a UTF-8 BOM."""
        bom_files = []
        for full_p, rel_p in self.md_files:
            with open(full_p, "rb") as f:
                header = f.read(3)
                if header == b"\xef\xbb\xbf":
                    bom_files.append(rel_p)
        self.assertEqual(len(bom_files), 0, f"Files with UTF-8 BOM detected: {bom_files}")

    def test_adv402_all_vault_markdown_strict_utf8_decoding(self):
        """ADV4.02: All markdown files must decode under strict UTF-8 with zero errors."""
        decode_errors = []
        for full_p, rel_p in self.md_files:
            try:
                with open(full_p, "rb") as f:
                    raw = f.read()
                raw.decode("utf-8")
            except Exception as e:
                decode_errors.append((rel_p, str(e)))
        self.assertEqual(len(decode_errors), 0, f"Files failing strict UTF-8 decode: {decode_errors}")

    def test_adv403_no_unicode_replacement_or_mojibake(self):
        """ADV4.03: Detects Unicode replacement characters (U+FFFD) and mojibake sequences."""
        mojibake_files = []
        for full_p, rel_p in self.md_files:
            content = full_p.read_text(encoding="utf-8", errors="replace")
            if "\ufffd" in content:
                mojibake_files.append((rel_p, "Contains Unicode replacement char \ufffd"))
            # Common double-encoding mojibake patterns
            suspicious = ["Ã©", "Ã ", "Ã§", "â€™", "â€œ", "â€\x9d"]
            for s in suspicious:
                if s in content:
                    mojibake_files.append((rel_p, f"Suspicious mojibake pattern '{s}'"))
                    break
        self.assertEqual(len(mojibake_files), 0, f"Mojibake or replacement chars detected: {mojibake_files}")

    def test_adv404_non_markdown_vault_files_encoding(self):
        """ADV4.04: Non-markdown configuration files (.base, .canvas, .json) must also be clean UTF-8."""
        ignored = {".agents", ".antigravity", ".git", ".obsidian", "__pycache__"}
        config_files = []
        for root, dirs, files in os.walk(VAULT_ROOT):
            dirs[:] = [d for d in dirs if d not in ignored]
            for f in files:
                if f.endswith((".base", ".canvas", ".json")):
                    config_files.append(Path(root) / f)

        errors = []
        for cf in config_files:
            rel_p = cf.relative_to(VAULT_ROOT).as_posix()
            with open(cf, "rb") as f:
                raw = f.read()
            if raw.startswith(b"\xef\xbb\xbf"):
                errors.append((rel_p, "Contains UTF-8 BOM"))
            try:
                raw.decode("utf-8")
            except Exception as e:
                errors.append((rel_p, f"Decode error: {e}"))
        self.assertEqual(len(errors), 0, f"Configuration files encoding errors: {errors}")


class TestAdversarialGeminiTopicsBoundaryConstraints(unittest.TestCase):
    """Stress-test: Gemini Topics Latest State Word Bounds and Suggested Next Steps Boundaries."""

    @classmethod
    def setUpClass(cls):
        cls.projects_dir = VAULT_ROOT / "10 Projects"
        cls.project_notes = [
            f for f in cls.projects_dir.glob("*.md")
            if "MOC" not in f.name and f.name != "10 Projects.md"
        ]

    def test_adv501_latest_state_summary_presence_and_word_count_boundaries(self):
        """ADV5.01: Latest State Summary must exist in all project notes and contain 30-50 words."""
        failures = []
        for p in self.project_notes:
            content = p.read_text(encoding="utf-8")
            m_state = re.search(r"##\s*📋\s*Latest State Summary\s*\n+([^\n#]+)", content)
            if not m_state:
                failures.append((p.name, "Missing '📋 Latest State Summary' heading"))
                continue
            text = m_state.group(1).strip()
            words = text.split()
            count = len(words)
            if not (30 <= count <= 50):
                failures.append((p.name, f"Word count {count} outside [30, 50] boundary"))
        self.assertEqual(len(failures), 0, f"Latest State Summary word count violations: {failures}")

    def test_adv502_latest_state_summary_sentence_count(self):
        """ADV5.02: Latest State Summary must consist of 1 to 2 sentences."""
        failures = []
        for p in self.project_notes:
            content = p.read_text(encoding="utf-8")
            m_state = re.search(r"##\s*📋\s*Latest State Summary\s*\n+([^\n#]+)", content)
            if not m_state:
                continue
            text = m_state.group(1).strip()
            # Split sentences by period, exclamation, or question mark followed by space or end
            sentences = [s.strip() for s in re.split(r"[.!?]+(?:\s+|\Z)", text) if s.strip()]
            if not (1 <= len(sentences) <= 2):
                failures.append((p.name, f"Sentence count {len(sentences)} outside [1, 2] boundary"))
        self.assertEqual(len(failures), 0, f"Sentence count violations: {failures}")

    def test_adv503_suggested_next_steps_count_boundaries(self):
        """ADV5.03: Suggested Next Steps must contain strictly 2 to 4 actionable suggestions."""
        failures = []
        for p in self.project_notes:
            content = p.read_text(encoding="utf-8")
            m_steps = re.search(r"##\s*🎯\s*Suggested Next Steps\s*\n+([\s\S]*?)(?=\n{3,}|\Z)", content)
            if not m_steps:
                failures.append((p.name, "Missing '🎯 Suggested Next Steps' heading"))
                continue
            raw_lines = [s.strip() for s in m_steps.group(1).splitlines() if s.strip() and not s.strip().startswith("```")]
            clean_steps = [re.sub(r"^[0-9*.-]+\s*", "", s).strip() for s in raw_lines]
            count = len(clean_steps)
            if not (2 <= count <= 4):
                failures.append((p.name, f"Step count {count} outside [2, 4] boundary"))
        self.assertEqual(len(failures), 0, f"Step count violations: {failures}")

    def test_adv504_suggested_next_steps_char_length_boundaries(self):
        """ADV5.04: Every Suggested Next Step must be strictly between 60 and 85 characters."""
        failures = []
        for p in self.project_notes:
            content = p.read_text(encoding="utf-8")
            m_steps = re.search(r"##\s*🎯\s*Suggested Next Steps\s*\n+([\s\S]*?)(?=\n{3,}|\Z)", content)
            if not m_steps:
                continue
            raw_lines = [s.strip() for s in m_steps.group(1).splitlines() if s.strip() and not s.strip().startswith("```")]
            for s in raw_lines:
                clean = re.sub(r"^[0-9*.-]+\s*", "", s).strip()
                length = len(clean)
                if not (60 <= length <= 85):
                    failures.append((p.name, f"Length {length} outside [60, 85]: '{clean}'"))
        self.assertEqual(len(failures), 0, f"Character length violations: {failures}")

    def test_adv505_suggested_next_steps_action_verbs_compliance(self):
        """ADV5.05: First word of every Suggested Next Step must be an approved imperative action verb."""
        failures = []
        for p in self.project_notes:
            content = p.read_text(encoding="utf-8")
            m_steps = re.search(r"##\s*🎯\s*Suggested Next Steps\s*\n+([\s\S]*?)(?=\n{3,}|\Z)", content)
            if not m_steps:
                continue
            raw_lines = [s.strip() for s in m_steps.group(1).splitlines() if s.strip() and not s.strip().startswith("```")]
            for s in raw_lines:
                clean = re.sub(r"^[0-9*.-]+\s*", "", s).strip()
                words = clean.split()
                first_word = words[0] if words else ""
                first_word_clean = re.sub(r"[^a-zA-Z]", "", first_word)
                if first_word_clean not in APPROVED_ACTION_VERBS:
                    failures.append((p.name, f"Unapproved action verb '{first_word_clean}': '{clean}'"))
        self.assertEqual(len(failures), 0, f"Action verb violations: {failures}")

    def test_adv506_synthetic_edge_case_boundary_validation(self):
        """ADV5.06: Synthetic boundary edge cases: 59 chars fails, 60 passes, 85 passes, 86 fails."""
        # 59 chars (too short)
        short_step = "Implement auth middleware for the project backend API route"  # 59
        self.assertEqual(len(short_step), 59)
        self.assertFalse(validate_suggested_next_step(short_step)["is_valid"])

        # 60 chars (boundary lower pass)
        min_step = "Implement auth middleware for the project backend API routes"  # 60
        self.assertEqual(len(min_step), 60)
        self.assertTrue(validate_suggested_next_step(min_step)["is_valid"])

        # 85 chars (boundary upper pass)
        max_step = "Benchmark Redis cache response latency times under concurrent client WebSocket loads!"  # 85
        self.assertEqual(len(max_step), 85)
        self.assertTrue(validate_suggested_next_step(max_step)["is_valid"])

        # 86 chars (too long)
        long_step = "Benchmark Redis cache response latency times under concurrent client WebSocket loads!!"  # 86
        self.assertEqual(len(long_step), 86)
        self.assertFalse(validate_suggested_next_step(long_step)["is_valid"])

        # Disallowed conversational prefixes
        disallowed = [
            "You should configure the database connection string securely",
            "We need to benchmark canvas performance under heavy mob load",
            "Please review the PR for the authentication flow in express",
        ]
        for bad in disallowed:
            val = validate_suggested_next_step(bad)
            self.assertFalse(val["is_valid"], f"Prefix should have failed: {bad}")

    def test_adv507_visual_separation_boundary_check(self):
        """ADV5.07: Visual separation between Suggested Next Steps and ```text block must be >= 5 blank lines."""
        failures = []
        for p in self.project_notes:
            content = p.read_text(encoding="utf-8")
            is_sep, count = check_visual_separation(content)
            if not is_sep:
                failures.append((p.name, f"Blank line count {count} < 5"))
        self.assertEqual(len(failures), 0, f"Visual separation boundary violations: {failures}")


def run_adversarial_suite():
    """Custom test runner providing detailed empirical breakdown."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    test_classes = [
        TestAdversarialVaultGraphConnectivity,
        TestAdversarialWikilinkCaseAndAliasFormatting,
        TestAdversarialConcurrencyAndStaleLockRecovery,
        TestAdversarialVaultUtf8NoBomHygiene,
        TestAdversarialGeminiTopicsBoundaryConstraints,
    ]

    for tc in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(tc))

    runner = unittest.TextTestRunner(verbosity=2)
    print("=" * 80)
    print(" === MILESTONE 5 PHASE 2: ADVERSARIAL HARDENING SUITE ===")
    print("=" * 80)
    result = runner.run(suite)
    print("=" * 80)
    print(f"Tests Run: {result.testsRun} | Failures: {len(result.failures)} | Errors: {len(result.errors)}")
    print("=" * 80)
    return result


if __name__ == "__main__":
    res = run_adversarial_suite()
    sys.exit(0 if res.wasSuccessful() else 1)
