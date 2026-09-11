import os
import re
from pathlib import Path
from collections import defaultdict

vault_root = Path(r"D:\obsidian file")
ignored = {".agents", ".antigravity", ".git", ".obsidian"}

# Collect all files
files_exact = {}
files_lower = {}
all_md_files = []

for root, dirs, files in os.walk(vault_root):
    dirs[:] = [d for d in dirs if d not in ignored]
    for f in files:
        full_path = Path(root) / f
        rel_path = full_path.relative_to(vault_root).as_posix()
        base_name = full_path.stem
        
        files_exact[rel_path] = full_path
        files_exact[base_name] = full_path
        files_exact[f] = full_path
        
        files_lower[rel_path.lower()] = (rel_path, full_path)
        files_lower[base_name.lower()] = (rel_path, full_path)
        files_lower[f.lower()] = (rel_path, full_path)
        
        if f.endswith(".md"):
            all_md_files.append((full_path, rel_path))

wikilink_regex = re.compile(r"(!?)\[\[([^\]\r\n]+)\]\]")

in_degree = defaultdict(int)
out_degree = defaultdict(int)
in_links = defaultdict(list)
out_links = defaultdict(list)

broken_links = []
case_mismatches = []
anchor_failures = []
total_links = 0

for full_path, rel_path in all_md_files:
    content = full_path.read_text(encoding="utf-8", errors="replace")
    
    # Extract headings for anchor checking
    headings = set()
    for h in re.findall(r"^#{1,6}\s+(.+)$", content, flags=re.MULTILINE):
        headings.add(h.strip())
        # Also clean markdown formatting from heading
        clean_h = re.sub(r"[*_`]", "", h).strip()
        headings.add(clean_h)

    for m in wikilink_regex.finditer(content):
        inner = m.group(2).strip()
        # Handle alias
        if "|" in inner:
            target_part = re.split(r"\\?\|", inner, maxsplit=1)[0].rstrip("\\").strip()
        else:
            target_part = inner.rstrip("\\").strip()
            
        # Handle anchor
        anchor = None
        if "#" in target_part:
            parts = target_part.split("#", 1)
            target = parts[0].rstrip("\\").strip()
            anchor = parts[1].rstrip("\\").strip()
        else:
            target = target_part
            
        if not target or target == "...":
            continue
            
        total_links += 1
        out_degree[rel_path] += 1
        
        norm_target = target.replace("\\", "/").rstrip("/")
        
        # Check resolution
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
                
        # 3. Folder MOC check
        folder_moc = f"{norm_target}/{Path(norm_target).name}"
        if folder_moc in files_exact or f"{folder_moc}.md" in files_exact:
            resolved_exact = files_exact.get(folder_moc) or files_exact.get(f"{folder_moc}.md")
        elif folder_moc.lower() in files_lower or f"{folder_moc.lower()}.md" in files_lower:
            resolved_lower = files_lower.get(folder_moc.lower()) or files_lower.get(f"{folder_moc.lower()}.md")

        if resolved_exact:
            target_rel = resolved_exact.relative_to(vault_root).as_posix()
            in_degree[target_rel] += 1
            in_links[target_rel].append((rel_path, target))
            out_links[rel_path].append((target_rel, target))
            
            # Check anchor if present
            if anchor and resolved_exact.suffix == ".md":
                target_content = resolved_exact.read_text(encoding="utf-8", errors="replace")
                target_headings = {h.strip() for h in re.findall(r"^#{1,6}\s+(.+)$", target_content, flags=re.MULTILINE)}
                target_clean_headings = {re.sub(r"[*_`]", "", h).strip() for h in target_headings}
                if anchor not in target_headings and anchor not in target_clean_headings:
                    anchor_failures.append((rel_path, target, anchor))
                    
        elif resolved_lower:
            # Case mismatch!
            target_rel, target_full = resolved_lower
            case_mismatches.append((rel_path, target, target_rel))
            in_degree[target_rel] += 1
            in_links[target_rel].append((rel_path, target))
            out_links[rel_path].append((target_rel, target))
        else:
            broken_links.append((rel_path, target))

print(f"Total markdown files: {len(all_md_files)}")
print(f"Total wikilinks: {total_links}")
print(f"Broken links ({len(broken_links)}):")
for src, tgt in broken_links:
    print(f"  {src} -> [[{tgt}]]")

print(f"\nCase mismatches ({len(case_mismatches)}):")
for src, tgt, actual in case_mismatches:
    print(f"  {src} -> [[{tgt}]] (actual: {actual})")

print(f"\nAnchor failures ({len(anchor_failures)}):")
for src, tgt, anc in anchor_failures:
    print(f"  {src} -> [[{tgt}#{anc}]]")

orphans_no_in = [rel for _, rel in all_md_files if in_degree[rel] == 0]
orphans_no_out = [rel for _, rel in all_md_files if out_degree[rel] == 0]
pure_islands = [rel for _, rel in all_md_files if in_degree[rel] == 0 and out_degree[rel] == 0]

print(f"\nFiles with in-degree = 0 (No incoming links) ({len(orphans_no_in)}):")
for o in sorted(orphans_no_in):
    print(f"  {o}")

print(f"\nFiles with out-degree = 0 (No outgoing links) ({len(orphans_no_out)}):")
for o in sorted(orphans_no_out):
    print(f"  {o}")

print(f"\nPure island files (in-degree=0 AND out-degree=0) ({len(pure_islands)}):")
for o in sorted(pure_islands):
    print(f"  {o}")
