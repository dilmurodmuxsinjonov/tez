import os
import re
from pathlib import Path

vault_root = Path(r"D:\obsidian file")

# Exclude .agents, .obsidian, .git, tests
excluded_dirs = {'.agents', '.obsidian', '.git', 'tests', '.trash', '.antigravity'}

# Collect all markdown files in the vault
all_md_files = []
for root, dirs, files in os.walk(vault_root):
    # filter out excluded dirs
    dirs[:] = [d for d in dirs if d not in excluded_dirs and not d.startswith('.')]
    rel_root = Path(root).relative_to(vault_root)
    if any(part in excluded_dirs for part in rel_root.parts):
        continue
    for f in files:
        if f.endswith('.md'):
            all_md_files.append(Path(root) / f)

print(f"Total vault markdown files: {len(all_md_files)}")

# Build file mapping by stem / name
file_by_name = {}
file_by_stem = {}
for p in all_md_files:
    file_by_name[p.name] = p
    file_by_stem[p.stem] = p

# Extract wikilinks from each file
# wikilinks can be [[Target]], [[Target|Alias]], [[Target#Heading]], [[Target#Heading|Alias]]
# Also check for table pipe escaping issues in tables
wikilink_pattern = re.compile(r'\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|([^\]]+))?\]\]')

incoming_links = {p: set() for p in all_md_files}
outgoing_links = {p: set() for p in all_md_files}
broken_links = []
pipe_escaping_violations = []

for p in all_md_files:
    content = p.read_text(encoding='utf-8')
    lines = content.splitlines()
    
    # Check table pipe escaping
    for line_idx, line in enumerate(lines, 1):
        if line.strip().startswith('|') and line.strip().endswith('|'):
            # In markdown tables, an unescaped pipe inside a wikilink [[Target|Alias]] breaks markdown table columns.
            # It should be escaped as [[Target\|Alias]].
            # Check for unescaped pipe in wikilinks in table lines:
            # Look for [[ ... | ... ]] where pipe is NOT preceded by \
            bad_pipes = re.findall(r'\[\[([^\]\|]+)\|([^\]]+)\]\]', line)
            # wait, if it has \|, re.findall(r'\[\[([^\]\|]+)\|...') won't match if we disallow \| before
            # let's explicitly search for unescaped pipes inside [[ ... ]]
            # A wikilink starts with [[ and ends with ]]
            # find all [[...]] in line
            raw_links = re.findall(r'\[\[(.*?)\]\]', line)
            for rl in raw_links:
                if '|' in rl:
                    # check if the pipe is preceded by backslash
                    # e.g. "Target\|Alias" has \|
                    parts = rl.split('|')
                    # if any part except the last doesn't end with backslash:
                    has_unescaped = False
                    for i in range(len(parts) - 1):
                        if not parts[i].endswith('\\'):
                            has_unescaped = True
                            break
                    if has_unescaped:
                        pipe_escaping_violations.append((p.relative_to(vault_root), line_idx, line.strip(), rl))

    # Parse wikilinks
    # First handle escaped pipes so regex can extract target properly
    clean_content = content.replace(r'\|', '|')
    matches = wikilink_pattern.findall(clean_content)
    for target, alias in matches:
        target = target.strip()
        if not target:
            continue
        # Check if target matches any vault note
        target_stem = Path(target).stem
        target_name = Path(target).name if target.endswith('.md') else target + '.md'
        
        resolved_file = None
        if target in file_by_stem:
            resolved_file = file_by_stem[target]
        elif target_name in file_by_name:
            resolved_file = file_by_name[target_name]
        elif target_stem in file_by_stem:
            resolved_file = file_by_stem[target_stem]
        
        if resolved_file:
            outgoing_links[p].add(resolved_file)
            incoming_links[resolved_file].add(p)
        else:
            broken_links.append((p.relative_to(vault_root), target))

print(f"\nGraph Connectivity & In-Degree Results:")
orphans = [p for p, callers in incoming_links.items() if len(callers) == 0]
print(f"  Total orphan notes (in-degree == 0): {len(orphans)}")
if orphans:
    for o in orphans:
        print(f"    ORPHAN: {o.relative_to(vault_root)}")
else:
    print("  ZERO ORPHAN INVARIANT PRESERVED! (All notes have in-degree >= 1)")

print(f"\nBroken Wikilinks:")
print(f"  Total broken wikilinks: {len(broken_links)}")
if broken_links:
    for src, tgt in broken_links[:20]:
        print(f"    From {src}: broken link to [[{tgt}]]")
else:
    print("  ZERO BROKEN WIKILINKS! (All wikilinks resolve to valid notes)")

print(f"\nTable Pipe Escaping Violations in MOCs and Master Brain:")
# filter for MOCs and Master Brain
moc_and_master_violations = [v for v in pipe_escaping_violations if "MOC" in str(v[0]) or "AI Sozlangan Miyyasi" in str(v[0])]
print(f"  Violations in MOCs & Master Brain: {len(moc_and_master_violations)}")
if moc_and_master_violations:
    for v in moc_and_master_violations:
        print(f"    File: {v[0]}, Line {v[1]}: link '{v[3]}'")

print(f"  Violations across ALL vault files: {len(pipe_escaping_violations)}")
if pipe_escaping_violations:
    for v in pipe_escaping_violations:
        print(f"    File: {v[0]}, Line {v[1]}: link '{v[3]}'")
else:
    print("  ZERO UNESCAPED TABLE PIPES VAULT-WIDE!")

