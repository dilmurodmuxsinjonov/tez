#!/usr/bin/env python3
"""
Adversarial Audit & Stress-Test Script for Milestone 4 (Generation 2)
Author: reviewer_m4_gen2
"""

import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

try:
    import yaml
except ImportError:
    yaml = None

VAULT_ROOT = Path(r"D:\obsidian file")

DELIVERABLES = {
    "Autonomous Agent Architectures": VAULT_ROOT / "30 Resources" / "Autonomous Agent Architectures.md",
    "Browser Automation Playbook": VAULT_ROOT / "20 Areas" / "Browser Automation Playbook.md",
    "Multimodal Generation Workflows": VAULT_ROOT / "30 Resources" / "Multimodal Generation Workflows.md",
    "00 Inbox MOC": VAULT_ROOT / "00 Inbox" / "00 Inbox MOC.md",
    "10 Projects MOC": VAULT_ROOT / "10 Projects" / "10 Projects MOC.md",
    "20 Areas MOC": VAULT_ROOT / "20 Areas" / "20 Areas MOC.md",
    "30 Resources MOC": VAULT_ROOT / "30 Resources" / "30 Resources MOC.md",
    "40 Archives MOC": VAULT_ROOT / "40 Archives" / "40 Archives MOC.md",
}

ENTRYPOINTS = {
    "AI Sozlangan Miyyasi": VAULT_ROOT / "AI Sozlangan Miyyasi.md",
    "Dashboard": VAULT_ROOT / "Dashboard.md",
}

COMPANION_PARENTS = {
    "00 Inbox": VAULT_ROOT / "00 Inbox" / "00 Inbox.md",
    "10 Projects": VAULT_ROOT / "10 Projects" / "10 Projects.md",
    "20 Areas": VAULT_ROOT / "20 Areas" / "20 Areas.md",
    "30 Resources": VAULT_ROOT / "30 Resources" / "30 Resources.md",
    "40 Archives": VAULT_ROOT / "40 Archives" / "40 Archives.md",
}

WIKILINK_REGEX = re.compile(r'!?\[\[([^\]|#\\]+)(?:#[^\]|\\]*)?(?:\\?\|[^\]]*)?\]\]')

def check_bom(path):
    with open(path, "rb") as f:
        first3 = f.read(3)
        return first3 == b"\xef\xbb\xbf"

def resolve_target(target_str, current_file):
    target_clean = target_str.split("#")[0].strip()
    if not target_clean:
        return True # internal anchor
    
    # 1. Exact relative or absolute path from vault root
    cand1 = VAULT_ROOT / target_clean
    if cand1.is_file():
        return True
    cand1_md = VAULT_ROOT / f"{target_clean}.md"
    if cand1_md.is_file():
        return True
    
    # 2. Relative to current file's directory
    cand2 = current_file.parent / target_clean
    if cand2.is_file():
        return True
    cand2_md = current_file.parent / f"{target_clean}.md"
    if cand2_md.is_file():
        return True

    # 3. Vault-wide filename match
    fname = target_clean if target_clean.endswith(".md") else f"{target_clean}.md"
    matches = list(VAULT_ROOT.rglob(fname))
    # filter out .git and .agents
    valid_matches = [m for m in matches if ".git" not in m.parts and ".agents" not in m.parts]
    if valid_matches:
        return True

    # 4. Check if it matches a non-md file (like .base, .canvas, .png)
    matches_any = list(VAULT_ROOT.rglob(target_clean))
    valid_matches_any = [m for m in matches_any if ".git" not in m.parts and ".agents" not in m.parts]
    if valid_matches_any:
        return True

    return False

def run_audit():
    print("=== ADVERSARIAL AUDIT FOR MILESTONE 4 (GEN 2) ===")
    errors = []
    warnings = []
    
    # Check deliverables existence, BOM, sizes, and word count
    print("\n--- 1. Deliverable Metrics & Content Depth ---")
    for name, path in DELIVERABLES.items():
        if not path.is_file():
            errors.append(f"MISSING DELIVERABLE: {name} at {path}")
            continue
        
        has_bom = check_bom(path)
        if has_bom:
            errors.append(f"UTF-8 BOM DETECTED in {name}")
        
        size = path.stat().st_size
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # YAML check
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3 and yaml:
                try:
                    fm = yaml.safe_load(parts[1])
                    if not isinstance(fm, dict):
                        errors.append(f"YAML frontmatter in {name} is not a dictionary.")
                    else:
                        pass
                except yaml.YAMLError as e:
                    errors.append(f"YAML parse error in {name}: {e}")
            elif len(parts) < 3:
                errors.append(f"Unclosed frontmatter in {name}")
        else:
            errors.append(f"Missing frontmatter in {name}")

        words = len(content.split())
        lines = len(content.splitlines())
        
        print(f"  [{'PASS' if not has_bom else 'FAIL'}] {name}: {size} bytes, {lines} lines, {words} words (BOM: {has_bom})")
        
        if words < 150:
            errors.append(f"SHALLOW CONTENT: {name} has only {words} words (likely dummy/facade).")
        
        # Facade checks
        suspicious = ["lorem ipsum", "todo:", "tbd", "fixme", "placeholder", "dummy implementation"]
        for s in suspicious:
            if s in content.lower():
                warnings.append(f"Suspicious marker '{s}' found in {name}")

    # Check wikilinks in all deliverables
    print("\n--- 2. Comprehensive Wikilink Verification in Deliverables ---")
    total_links = 0
    broken_links = 0
    for name, path in DELIVERABLES.items():
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        for m in WIKILINK_REGEX.finditer(content):
            target = m.group(1).rstrip("\\").strip()
            if target == "..." or not target:
                continue
            total_links += 1
            if not resolve_target(target, path):
                errors.append(f"BROKEN WIKILINK in {name}: [[{target}]]")
                broken_links += 1
                print(f"  [BROKEN] {name} -> [[{target}]]")
            else:
                pass
    print(f"  Verified {total_links} wikilinks across all deliverables. Broken: {broken_links}")

    # Check Entrypoint Alignment
    print("\n--- 3. Central Entrypoint Alignments ---")
    for ep_name, ep_path in ENTRYPOINTS.items():
        if not ep_path.is_file():
            errors.append(f"ENTRYPOINT MISSING: {ep_name}")
            continue
        with open(ep_path, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"  Verifying {ep_name} ({len(content)} chars)...")
        for deliv_name in DELIVERABLES:
            # Check if name is linked in entrypoint
            # Deliverable name or filename
            fname = DELIVERABLES[deliv_name].name
            stem = DELIVERABLES[deliv_name].stem
            if stem not in content and fname not in content:
                errors.append(f"UNLINKED DELIVERABLE in {ep_name}: {deliv_name} ({stem})")
                print(f"  [FAIL] {ep_name} does NOT link {deliv_name}")
            else:
                print(f"  [PASS] {ep_name} indexes {deliv_name}")

    # Check Bidirectional Backlinks in Deliverables
    print("\n--- 4. Bidirectional Backlinks to Master Brain & Dashboard ---")
    for name, path in DELIVERABLES.items():
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        has_brain = "AI Sozlangan Miyyasi" in content
        has_dash = "Dashboard" in content
        if not has_brain:
            errors.append(f"{name} lacks backlink to AI Sozlangan Miyyasi")
        if not has_dash:
            errors.append(f"{name} lacks backlink to Dashboard")
        print(f"  {name}: Brain Backlink: {'PASS' if has_brain else 'FAIL'}, Dashboard Backlink: {'PASS' if has_dash else 'FAIL'}")

    # Check Skills Dashboard and Templates linking in MOCs
    print("\n--- 5. MOC Integration with Skills Dashboard & 50 Templates/ ---")
    moc_names = ["00 Inbox MOC", "10 Projects MOC", "20 Areas MOC", "30 Resources MOC", "40 Archives MOC"]
    for m_name in moc_names:
        path = DELIVERABLES[m_name]
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        has_skills = "Skills Dashboard" in content
        has_tmpl = "50 Templates" in content
        if not has_skills:
            errors.append(f"{m_name} does not link to Skills Dashboard")
        if not has_tmpl:
            errors.append(f"{m_name} does not link to 50 Templates/")
        print(f"  {m_name}: Skills Dashboard: {'PASS' if has_skills else 'FAIL'}, 50 Templates: {'PASS' if has_tmpl else 'FAIL'}")

    # Check Companion Parent Files cross-linking with MOCs
    print("\n--- 6. Companion Parent Notes Cross-linking ---")
    for parent_name, parent_path in COMPANION_PARENTS.items():
        with open(parent_path, "r", encoding="utf-8") as f:
            content = f.read()
        moc_target = f"{parent_name} MOC"
        has_moc_link = moc_target in content
        if not has_moc_link:
            errors.append(f"{parent_name}.md does not link to {moc_target}.md")
        print(f"  {parent_name}.md -> {moc_target}.md: {'PASS' if has_moc_link else 'FAIL'}")

    print("\n==============================================")
    print(f"AUDIT SUMMARY: {len(errors)} Errors, {len(warnings)} Warnings")
    if errors:
        print("[FAIL] Audit discovered critical issues:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("[SUCCESS] All adversarial stress-tests PASSED flawlessly!")
        return True

if __name__ == "__main__":
    success = run_audit()
    sys.exit(0 if success else 1)
