import os
import re

vault_root = r"D:\obsidian file"
ignored_dirs = {".agents", ".antigravity", ".git", ".obsidian"}

all_files = {}
for root, dirs, files in os.walk(vault_root):
    dirs[:] = [d for d in dirs if d not in ignored_dirs]
    for file in files:
        rel_path = os.path.relpath(os.path.join(root, file), vault_root)
        name_no_ext = os.path.splitext(file)[0]
        all_files[file] = rel_path
        all_files[name_no_ext] = rel_path
        all_files[rel_path] = rel_path

print(f"Total indexed vault files/names: {len(all_files)}")

wikilink_regex = re.compile(r'!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')

broken_links = []
total_links = 0

for root, dirs, files in os.walk(vault_root):
    dirs[:] = [d for d in dirs if d not in ignored_dirs]
    for file in files:
        if not file.endswith(".md"):
            continue
        filepath = os.path.join(root, file)
        rel_path = os.path.relpath(filepath, vault_root)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        for i, line in enumerate(lines, 1):
            matches = wikilink_regex.findall(line)
            for m in matches:
                target = m.strip()
                total_links += 1
                # check if target exists
                if target in all_files or f"{target}.md" in all_files:
                    pass
                else:
                    broken_links.append((rel_path, i, target))

print(f"Total wikilinks scanned in existing vault: {total_links}")
print(f"Broken links found: {len(broken_links)}")
for b in broken_links[:10]:
    print(f"  {b[0]}:{b[1]} -> [[{b[2]}]] NOT FOUND")
