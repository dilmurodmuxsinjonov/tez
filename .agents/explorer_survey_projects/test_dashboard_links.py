import os
import re

vault_root = r"D:\obsidian file"
ignored_dirs = {".agents", ".antigravity", ".git", ".obsidian"}

# Index all valid vault files
vault_targets = set()
for root, dirs, files in os.walk(vault_root):
    dirs[:] = [d for d in dirs if d not in ignored_dirs]
    for file in files:
        rel_path = os.path.relpath(os.path.join(root, file), vault_root).replace("\\", "/")
        name_no_ext = os.path.splitext(file)[0]
        rel_no_ext = os.path.splitext(rel_path)[0]
        
        vault_targets.add(file.lower())
        vault_targets.add(name_no_ext.lower())
        vault_targets.add(rel_path.lower())
        vault_targets.add(rel_no_ext.lower())

print(f"Indexed vault targets: {len(vault_targets)}")

# Scan Dashboard.md
with open(os.path.join(vault_root, "Dashboard.md"), "r", encoding="utf-8") as f:
    content = f.read()

wikilink_regex = re.compile(r'!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')
for m in wikilink_regex.finditer(content):
    target = m.group(1).strip()
    target_norm = target.replace("\\", "/").rstrip("/").lower()
    found = target_norm in vault_targets
    print(f"Target: '{target}' -> Normalized: '{target_norm}' -> Found: {found}")
