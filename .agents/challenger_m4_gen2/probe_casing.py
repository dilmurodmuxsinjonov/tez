import os
import re
from pathlib import Path

vault = Path(r"D:\obsidian file")
all_fs_files = {}
for root, dirs, files in os.walk(vault):
    rel_root = os.path.relpath(root, vault)
    if ".git" in rel_root.split(os.sep) or ".agents" in rel_root.split(os.sep):
        continue
    for f in files:
        full = Path(root) / f
        rel = full.relative_to(vault).as_posix()
        all_fs_files[rel] = full

m4_notes = [
    "30 Resources/Autonomous Agent Architectures.md",
    "20 Areas/Browser Automation Playbook.md",
    "30 Resources/Multimodal Generation Workflows.md",
    "00 Inbox/00 Inbox MOC.md",
    "10 Projects/10 Projects MOC.md",
    "20 Areas/20 Areas MOC.md",
    "30 Resources/30 Resources MOC.md",
    "40 Archives/40 Archives MOC.md",
    "AI Sozlangan Miyyasi.md",
    "Dashboard.md",
    "00 Inbox/00 Inbox.md",
    "10 Projects/10 Projects.md",
    "20 Areas/20 Areas.md",
    "30 Resources/30 Resources.md",
    "40 Archives/40 Archives.md",
]

casing_mismatches = []
unresolved = []
total_links = 0

for n in m4_notes:
    text = (vault / n).read_text(encoding="utf-8")
    matches = re.findall(r"\[\[(.*?)\]\]", text)
    for m in matches:
        total_links += 1
        raw = m.replace(r"\|", "|").split("|")[0].strip()
        target = raw.split("#")[0].strip()
        if not target:
            continue
        
        target_candidates = [target, target + ".md", target + ".base", target + ".canvas"]
        matched = False
        exact_matched = False

        # 1. Check exact relative path
        for c in target_candidates:
            if c in all_fs_files:
                matched = True
                exact_matched = True
                break

        # 2. Check filename exact
        if not exact_matched:
            target_name = Path(target).name
            for c in [target_name, target_name + ".md", target_name + ".base"]:
                for fs_rel, fs_path in all_fs_files.items():
                    if fs_path.name == c:
                        matched = True
                        exact_matched = True
                        break
                if matched:
                    break

        # 3. Check case-insensitive
        if not exact_matched:
            for c in target_candidates:
                for fs_rel, fs_path in all_fs_files.items():
                    if fs_rel.lower() == c.lower() or fs_path.name.lower() == Path(c).name.lower():
                        matched = True
                        casing_mismatches.append(f"In {n}: link target '{target}' vs physical '{fs_path.name}'")
                        break
                if matched:
                    break

        if not matched:
            unresolved.append(f"In {n}: [[{m}]] -> target '{target}'")

print(f"Total links inspected across 15 notes: {total_links}")
print(f"Unresolved links: {len(unresolved)}")
for u in unresolved:
    print("  - UNRESOLVED:", u)
print(f"Casing mismatches: {len(casing_mismatches)}")
for cm in casing_mismatches:
    print("  - CASING:", cm)
