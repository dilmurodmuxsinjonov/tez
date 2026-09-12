"""
Independent Adversarial Certification Probe
Author: challenger_e4_certifier (Empirical Challenger)
Workspace: D:\\obsidian file\\.agents\\challenger_e4_certifier
Project Root: D:\\obsidian file
"""

import os
import re
import sys
import yaml
from pathlib import Path
from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple, Any

sys.stdout.reconfigure(encoding="utf-8")

VAULT_ROOT = Path(r"D:\obsidian file").resolve()
EXCLUDE_DIRS = {".agents", ".antigravity", ".git", ".obsidian"}

print("================================================================================")
print(" INDEPENDENT ADVERSARIAL CERTIFICATION PROBE -- CHALLENGER_E4_CERTIFIER")
print(f" Target Vault: {VAULT_ROOT}")
print("================================================================================")

# 1. Discover all vault files
all_vault_files = []
md_files = []
for root, dirs, files in os.walk(VAULT_ROOT):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    for f in files:
        full_p = Path(root) / f
        rel_posix = full_p.relative_to(VAULT_ROOT).as_posix()
        all_vault_files.append((full_p, rel_posix))
        if f.lower().endswith(".md"):
            md_files.append((full_p, rel_posix))

md_files.sort(key=lambda x: x[1])
all_vault_files.sort(key=lambda x: x[1])

print(f"\n[1] Discovered {len(md_files)} markdown files across vault ({len(all_vault_files)} total files).")

# 2. Encoding & BOM Audit
bom_violations = []
utf8_decode_errors = []
mojibake_chars = []

for full_p, rel in md_files:
    raw = full_p.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        bom_violations.append((rel, "UTF-8 BOM"))
    elif raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        bom_violations.append((rel, "UTF-16 BOM"))
    try:
        text = raw.decode("utf-8")
        if "\ufffd" in text:
            mojibake_chars.append((rel, "Contains replacement character \ufffd"))
    except UnicodeDecodeError as e:
        utf8_decode_errors.append((rel, str(e)))

print(f"\n[2] Encoding & Byte Integrity Audit:")
print(f"    - Total Markdown Files Checked: {len(md_files)}")
print(f"    - BOM Violations: {len(bom_violations)}")
print(f"    - Strict UTF-8 Decode Errors: {len(utf8_decode_errors)}")
print(f"    - Mojibake / Replacement Chars: {len(mojibake_chars)}")

# 3. YAML Frontmatter safe_load Audit
yaml_errors = []
parsed_fm_count = 0
missing_fm = []

for full_p, rel in md_files:
    content = full_p.read_text(encoding="utf-8")
    if content.startswith("---\n") or content.startswith("---\r\n"):
        parts = re.split(r"^---\s*$", content, flags=re.MULTILINE)
        if len(parts) >= 3:
            fm_text = parts[1]
            try:
                data = yaml.safe_load(fm_text)
                parsed_fm_count += 1
                if not isinstance(data, dict):
                    yaml_errors.append((rel, f"Parsed frontmatter is not a mapping: {type(data)}"))
            except yaml.YAMLError as exc:
                yaml_errors.append((rel, f"yaml.safe_load syntax error: {exc}"))
        else:
            yaml_errors.append((rel, "Unclosed frontmatter (missing closing ---)"))
    else:
        missing_fm.append(rel)

print(f"\n[3] Frontmatter & YAML safe_load Compliance:")
print(f"    - Frontmatters Successfully Parsed with yaml.safe_load: {parsed_fm_count}")
print(f"    - YAML safe_load Syntax Errors: {len(yaml_errors)}")
for rel, err in yaml_errors:
    print(f"      * ERROR in {rel}: {err}")
print(f"    - Notes without YAML Frontmatter: {len(missing_fm)}")
for mf in missing_fm:
    print(f"      * {mf}")

# 4. Markdown Table Wikilink Pipe Escaping Audit
table_pipe_violations = []
table_count = 0
total_table_rows = 0

for full_p, rel in md_files:
    content = full_p.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    # Identify table blocks by locating delimiter rows
    delimiter_indices = []
    for idx, line in enumerate(lines):
        if re.match(r"^\|?\s*[-:]+[-| :]*\s*\|?$", line) and "|" in line and "-" in line:
            # Verify it has at least one dash group between pipes
            if re.search(r"\|?\s*[-:]+\s*\|", line):
                delimiter_indices.append(idx)
    
    table_row_indices = set()
    for d_idx in delimiter_indices:
        table_count += 1
        # Walk backward to collect headers
        back = d_idx - 1
        while back >= 0 and lines[back].strip() and "|" in lines[back]:
            table_row_indices.add(back)
            back -= 1
        # Walk forward to collect data rows
        fwd = d_idx + 1
        while fwd < len(lines) and lines[fwd].strip() and "|" in lines[fwd]:
            table_row_indices.add(fwd)
            fwd += 1
            
    total_table_rows += len(table_row_indices)
    
    # Check all rows in tables for unescaped pipes in wikilinks
    for r_idx in sorted(table_row_indices):
        line = lines[r_idx]
        if "[[" in line:
            # find all wikilinks
            for m in re.finditer(r"\[\[([^\]\r\n]+)\]\]", line):
                inner = m.group(1)
                # Unescaped pipe is a pipe not preceded by backslash
                if re.search(r"(?<!\\)\|", inner):
                    table_pipe_violations.append({
                        "file": rel,
                        "line": r_idx + 1,
                        "wikilink": m.group(0),
                        "inner": inner,
                        "row_content": line.strip()
                    })

print(f"\n[4] Markdown Table Wikilink Pipe Escaping Audit:")
print(f"    - Total Tables Detected: {table_count}")
print(f"    - Total Table Rows Audited: {total_table_rows}")
print(f"    - Table Wikilink Unescaped Pipe Violations: {len(table_pipe_violations)}")
for v in table_pipe_violations:
    print(f"      * VIOLATION in {v['file']}:{v['line']} -> {v['wikilink']}")

# 5. Wikilink Resolution & Graph Verification
# Build lookup indexes
vault_path_by_lower = {rel.lower(): rel for _, rel in all_vault_files}
vault_stem_by_lower = {}
vault_name_by_lower = {}
for _, rel in all_vault_files:
    p = Path(rel)
    stem_l = p.stem.lower()
    if stem_l not in vault_stem_by_lower:
        vault_stem_by_lower[stem_l] = rel
    name_l = p.name.lower()
    if name_l not in vault_name_by_lower:
        vault_name_by_lower[name_l] = rel

# Pre-index headings
headings_by_file = defaultdict(set)
for full_p, rel in md_files:
    lines = full_p.read_text(encoding="utf-8").splitlines()
    for l in lines:
        if l.startswith("#"):
            h = l.lstrip("#").strip().lower()
            headings_by_file[rel].add(h)

broken_links = []
case_mismatches = []
anchor_failures = []
total_wikilinks = 0

# Graph: notes
outgoing_edges = defaultdict(set)
incoming_edges = defaultdict(set)
all_md_rel_set = {rel for _, rel in md_files}

for full_p, rel in md_files:
    content = full_p.read_text(encoding="utf-8")
    # Strip code
    stripped = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    stripped = re.sub(r"`.*?`", "", stripped)
    
    for m in re.finditer(r"\[\[([^\]\r\n]+)\]\]", stripped):
        total_wikilinks += 1
        inner = m.group(1).strip()
        
        # Split target from alias: alias can start with \| or |
        target_raw = re.split(r"\\?\|", inner)[0].strip()
        
        anchor = None
        if "#" in target_raw:
            parts = target_raw.split("#", 1)
            target_raw = parts[0].strip()
            anchor = parts[1].strip()
            
        if not target_raw:
            # Self-reference anchor like [[#Navigatsiya]]
            if anchor:
                if anchor.lower() not in headings_by_file[rel]:
                    anchor_failures.append((rel, f"[[#{anchor}]]", "Anchor not found in self"))
            continue
            
        # Normalize
        norm = target_raw.replace("\\", "/")
        norm_no_ext = norm[:-3] if norm.lower().endswith(".md") else norm
        
        # Resolution lookup
        resolved_rel = None
        if norm.lower() in vault_path_by_lower:
            resolved_rel = vault_path_by_lower[norm.lower()]
        elif (norm + ".md").lower() in vault_path_by_lower:
            resolved_rel = vault_path_by_lower[(norm + ".md").lower()]
        elif Path(norm_no_ext).name.lower() in vault_stem_by_lower:
            resolved_rel = vault_stem_by_lower[Path(norm_no_ext).name.lower()]
        elif Path(norm).name.lower() in vault_name_by_lower:
            resolved_rel = vault_name_by_lower[Path(norm).name.lower()]
            
        if not resolved_rel:
            broken_links.append((rel, inner, target_raw))
        else:
            # Check anchor if note is md
            if anchor and resolved_rel in headings_by_file:
                if anchor.lower() not in headings_by_file[resolved_rel]:
                    anchor_failures.append((rel, f"[[{inner}]]", f"Anchor '#{anchor}' not found in {resolved_rel}"))
            
            # Record graph edge for md notes
            if resolved_rel in all_md_rel_set and resolved_rel != rel:
                outgoing_edges[rel].add(resolved_rel)
                incoming_edges[resolved_rel].add(rel)

print(f"\n[5] Wikilink Resolution & Integrity Audit:")
print(f"    - Total Wikilinks Audited: {total_wikilinks}")
print(f"    - Broken Wikilinks: {len(broken_links)}")
for b in broken_links:
    print(f"      * BROKEN in {b[0]}: [[{b[1]}]] -> '{b[2]}'")
print(f"    - Anchor Failures: {len(anchor_failures)}")
for a in anchor_failures:
    print(f"      * ANCHOR FAIL in {a[0]}: {a[1]} -> {a[2]}")

# 6. In-Degree & Inbound Orphan Note Analysis
orphan_notes = [note for note in all_md_rel_set if len(incoming_edges[note]) == 0]
in_deg_stats = {note: len(incoming_edges[note]) for note in all_md_rel_set}
out_deg_stats = {note: len(outgoing_edges[note]) for note in all_md_rel_set}

print(f"\n[6] In-Degree & Orphan Analysis:")
print(f"    - Total Notes in Scope: {len(all_md_rel_set)}")
print(f"    - Notes with Distinct In-Degree == 0 (Orphans): {len(orphan_notes)}")
for o in orphan_notes:
    print(f"      * ORPHAN: {o}")
print(f"    - Minimum In-Degree across Vault: {min(in_deg_stats.values())}")
print(f"    - Maximum In-Degree across Vault: {max(in_deg_stats.values())} ({[n for n, d in in_deg_stats.items() if d == max(in_deg_stats.values())]})")
print(f"    - 100% In-Degree >= 1 Satisfied: {len(orphan_notes) == 0}")

# 7. Graph Topology & Connected Components Analysis
# Build undirected adjacency
undirected = defaultdict(set)
for u in all_md_rel_set:
    for v in outgoing_edges[u]:
        undirected[u].add(v)
        undirected[v].add(u)

visited_nodes = set()
components = []
for node in sorted(all_md_rel_set):
    if node not in visited_nodes:
        comp = []
        q = deque([node])
        visited_nodes.add(node)
        while q:
            curr = q.popleft()
            comp.append(curr)
            for neighbor in undirected[curr]:
                if neighbor not in visited_nodes:
                    visited_nodes.add(neighbor)
                    q.append(neighbor)
        components.append(comp)

print(f"\n[7] Graph Topology & Weakly Connected Components:")
print(f"    - Weakly Connected Components (WCC): {len(components)}")
for i, comp in enumerate(components, 1):
    print(f"      Component {i}: {len(comp)} nodes (Sample: {comp[:3]})")

# Directed reachability from Master Brain
mb_note = "AI Sozlangan Miyyasi.md"
mb_reachable = set()
if mb_note in all_md_rel_set:
    q = deque([mb_note])
    mb_reachable.add(mb_note)
    while q:
        curr = q.popleft()
        for target in outgoing_edges[curr]:
            if target not in mb_reachable:
                mb_reachable.add(target)
                q.append(target)

print(f"    - Master Brain ('{mb_note}') Reachability: {len(mb_reachable)} / {len(all_md_rel_set)} ({len(mb_reachable)/len(all_md_rel_set)*100:.1f}%)")

# 8. Specific Verification of Remediated Files
print(f"\n[8] Specific Verification of Remediated Files (Commit 0e783d0):")
remediated_files = [
    "10 Projects/AI Story & Media Engine.md",
    "10 Projects/Universal Multi-Agent Swarm Framework.md",
    "20 Areas/20 Areas MOC.md",
    "20 Areas/20 Areas.md",
    "30 Resources/AI Agent Ecosystem Map.md",
    "50 Templates/Agent Profile Template.md",
    "50 Templates/Area Template.md",
    "50 Templates/Daily Note Template.md",
    "50 Templates/Model Evaluation Template.md",
    "50 Templates/New Agent Integration Template.md",
    "50 Templates/Project Template.md",
    "50 Templates/Resource Template.md",
    "50 Templates/Security Audit Template.md",
]

for rf in remediated_files:
    p = VAULT_ROOT / rf
    if not p.exists():
        print(f"    * FAIL: Remediated file missing: {rf}")
        continue
    txt = p.read_text(encoding="utf-8")
    # Check yaml parse
    fm_status = "No FM"
    if txt.startswith("---"):
        parts = re.split(r"^---\s*$", txt, flags=re.MULTILINE)
        if len(parts) >= 3:
            try:
                y = yaml.safe_load(parts[1])
                fm_status = f"YAML OK (keys: {list(y.keys())[:3]}...)"
            except Exception as e:
                fm_status = f"YAML FAIL: {e}"
    # Check table pipe escaping if relevant
    has_esc_pipe = r"\|" in txt
    in_deg = len(incoming_edges[rf])
    print(f"    - {rf:52} | In-Deg: {in_deg:2} | {fm_status}")

# 9. Final Independent Verdict
all_criteria_passed = (
    len(bom_violations) == 0 and
    len(utf8_decode_errors) == 0 and
    len(yaml_errors) == 0 and
    len(table_pipe_violations) == 0 and
    len(broken_links) == 0 and
    len(anchor_failures) == 0 and
    len(orphan_notes) == 0 and
    len(components) == 1 and
    len(mb_reachable) == len(all_md_rel_set)
)

print("\n================================================================================")
if all_criteria_passed:
    print(" INDEPENDENT ADVERSARIAL VERDICT: APPROVE")
    print(" 100% OF EMPIRICAL ADVERSARIAL CHECKS PASSED.")
else:
    print(" INDEPENDENT ADVERSARIAL VERDICT: REJECT")
    print(" FAILURES DETECTED IN INDEPENDENT AUDIT.")
print("================================================================================")
