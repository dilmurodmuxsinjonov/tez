import os
import sys
import re
from pathlib import Path

VAULT_ROOT = Path(r"D:\obsidian file")

print("=== FORENSIC INTEGRITY AUDIT: MILESTONE 4 (GEN 2) - REFINED ===")

core_files = {
    "Autonomous Agent Architectures.md": VAULT_ROOT / "30 Resources" / "Autonomous Agent Architectures.md",
    "Browser Automation Playbook.md": VAULT_ROOT / "20 Areas" / "Browser Automation Playbook.md",
    "Multimodal Generation Workflows.md": VAULT_ROOT / "30 Resources" / "Multimodal Generation Workflows.md",
}

mocs = {
    "00 Inbox MOC.md": VAULT_ROOT / "00 Inbox" / "00 Inbox MOC.md",
    "10 Projects MOC.md": VAULT_ROOT / "10 Projects" / "10 Projects MOC.md",
    "20 Areas MOC.md": VAULT_ROOT / "20 Areas" / "20 Areas MOC.md",
    "30 Resources MOC.md": VAULT_ROOT / "30 Resources" / "30 Resources MOC.md",
    "40 Archives MOC.md": VAULT_ROOT / "40 Archives" / "40 Archives MOC.md",
}

all_m4_files = list(core_files.values()) + list(mocs.values())

# Indexed vault targets
ignored = {".agents", ".antigravity", ".git", ".obsidian"}
indexed_targets = set()
for root, dirs, files in os.walk(VAULT_ROOT):
    dirs[:] = [d for d in dirs if d not in ignored]
    for f in files:
        full = Path(root) / f
        rel = full.relative_to(VAULT_ROOT).as_posix()
        stem = full.stem
        rel_no_ext = os.path.splitext(rel)[0]
        indexed_targets.add(f.lower())
        indexed_targets.add(stem.lower())
        indexed_targets.add(rel.lower())
        indexed_targets.add(rel_no_ext.lower())

# Match wikilinks, handling escaped pipes in markdown tables and anchors
wikilink_regex = re.compile(r'!?\[\[([^\]|#\\]+)(?:#[^\]|\\]*)?(?:\\?\|[^\]]*)?\]\]')

broken = []
total_links = 0

for p in all_m4_files:
    content = p.read_text(encoding="utf-8")
    lines = content.splitlines()
    for l_idx, line in enumerate(lines, 1):
        # strip inline code spans `...` to avoid example syntax
        clean_line = re.sub(r"`[^`]+`", "", line)
        for m in wikilink_regex.finditer(clean_line):
            target = m.group(1).rstrip("\\").strip()
            if target == "..." or not target:
                continue
            total_links += 1
            norm = target.replace("\\", "/").rstrip("/").lower()
            if norm not in indexed_targets:
                broken.append((p.name, l_idx, target))
                print(f"[FAIL] Broken link in {p.name}:{l_idx} -> [[{target}]]")

if not broken:
    print(f"[PASS] All {total_links} wikilinks across all 8 M4 deliverables are 100% VALID and RESOLVED!")
else:
    print(f"[FAIL] Found {len(broken)} broken links!")
