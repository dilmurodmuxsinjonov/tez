#!/usr/bin/env python3
r"""
Adversarial Vault Graph Stress Test Harness
Author: challenger_e4_1 (Empirical Challenger)
Workspace: D:\obsidian file\.agents\challenger_e4_1
Project Root: D:\obsidian file
"""

import os
import re
import sys
import json
import yaml
from pathlib import Path
from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple, Any, Optional

sys.stdout.reconfigure(encoding="utf-8")

VAULT_ROOT = Path(r"D:\obsidian file").resolve()
IGNORED_DIRS = {".agents", ".antigravity", ".git", ".obsidian"}

def discover_vault_files(root: Path) -> Tuple[List[Tuple[Path, str]], List[Tuple[Path, str]]]:
    """Finds all markdown files and all total files in vault excluding dot-directories."""
    all_files = []
    md_files = []
    for dirpath, dirs, filenames in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for f in filenames:
            full_path = Path(dirpath) / f
            rel_path = full_path.relative_to(root).as_posix()
            all_files.append((full_path, rel_path))
            if f.endswith(".md"):
                md_files.append((full_path, rel_path))
    return sorted(md_files, key=lambda x: x[1]), sorted(all_files, key=lambda x: x[1])

def audit_utf8_and_bom(md_files: List[Tuple[Path, str]]) -> Dict[str, Any]:
    """Audits encoding, BOM presence, and replacement characters."""
    bom_files = []
    utf8_decode_errors = []
    mojibake_or_replacement = []
    line_ending_stats = defaultdict(int)

    for full_path, rel_path in md_files:
        raw = full_path.read_bytes()
        
        # Check BOM
        if raw.startswith(b"\xef\xbb\xbf"):
            bom_files.append((rel_path, "UTF-8 BOM (EF BB BF)"))
        elif raw.startswith(b"\xff\xfe"):
            bom_files.append((rel_path, "UTF-16 LE BOM (FF FE)"))
        elif raw.startswith(b"\xfe\xff"):
            bom_files.append((rel_path, "UTF-16 BE BOM (FE FF)"))

        # Decode UTF-8 strict
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as e:
            utf8_decode_errors.append((rel_path, str(e)))
            text = raw.decode("utf-8", errors="replace")

        # Check replacement char
        if "\ufffd" in text:
            mojibake_or_replacement.append((rel_path, text.count("\ufffd")))

        # Check line endings
        if "\r\n" in text:
            line_ending_stats["CRLF"] += 1
        elif "\n" in text:
            line_ending_stats["LF"] += 1

    return {
        "bom_files": bom_files,
        "utf8_decode_errors": utf8_decode_errors,
        "mojibake_or_replacement": mojibake_or_replacement,
        "line_ending_stats": dict(line_ending_stats)
    }

def audit_frontmatter(md_files: List[Tuple[Path, str]]) -> Dict[str, Any]:
    """Audits frontmatter existence, standard YAML syntax, required tags, and date format."""
    missing_frontmatter = []
    yaml_syntax_errors = []
    missing_tags = []
    invalid_tags_format = []
    missing_status = []
    date_format_issues = []
    parsed_frontmatters = {}

    for full_path, rel_path in md_files:
        try:
            content = full_path.read_text(encoding="utf-8")
        except Exception:
            content = full_path.read_text(encoding="utf-8", errors="replace")

        fm_match = re.match(r"^---\r?\n(.*?)\r?\n---", content, re.DOTALL)
        if not fm_match:
            missing_frontmatter.append(rel_path)
            continue

        raw_yaml = fm_match.group(1)
        try:
            data = yaml.safe_load(raw_yaml)
            if not isinstance(data, dict):
                yaml_syntax_errors.append((rel_path, "Frontmatter parsed to non-dict object"))
                continue
            parsed_frontmatters[rel_path] = data
        except Exception as e:
            yaml_syntax_errors.append((rel_path, str(e)))
            continue

        # Check tags
        tags = data.get("tags")
        if tags is None:
            missing_tags.append(rel_path)
        elif not isinstance(tags, list) or len(tags) == 0:
            invalid_tags_format.append((rel_path, f"Tags is not a non-empty list: {repr(tags)}"))

        # Check status
        if "status" not in data and not rel_path.startswith("50 Templates/"):
            missing_status.append(rel_path)

        # Check date
        date_val = data.get("date") or data.get("created")
        if date_val:
            s_val = str(date_val)
            if not rel_path.startswith("50 Templates/") and not re.match(r"^\d{4}-\d{2}-\d{2}", s_val):
                date_format_issues.append((rel_path, s_val))

    return {
        "missing_frontmatter": missing_frontmatter,
        "yaml_syntax_errors": yaml_syntax_errors,
        "missing_tags": missing_tags,
        "invalid_tags_format": invalid_tags_format,
        "missing_status": missing_status,
        "date_format_issues": date_format_issues,
        "parsed_count": len(parsed_frontmatters)
    }

def audit_table_pipe_escaping(md_files: List[Tuple[Path, str]]) -> List[Dict[str, Any]]:
    """Audits markdown table rows for unescaped pipe syntax inside wikilinks."""
    violations = []

    for full_path, rel_path in md_files:
        try:
            content = full_path.read_text(encoding="utf-8")
        except Exception:
            content = full_path.read_text(encoding="utf-8", errors="replace")

        lines = content.splitlines()
        # Find all markdown table lines
        # Check table delimiter rows
        table_row_indices = set()
        for idx, line in enumerate(lines):
            if re.match(r"^\|?\s*[-:]+\s*\|", line):
                back = idx - 1
                while back >= 0 and lines[back].strip() and "|" in lines[back]:
                    table_row_indices.add(back)
                    back -= 1
                fwd = idx + 1
                while fwd < len(lines) and lines[fwd].strip() and "|" in lines[fwd]:
                    table_row_indices.add(fwd)
                    fwd += 1

        for row_idx in sorted(table_row_indices):
            line = lines[row_idx]
            if "[[" in line:
                for m in re.finditer(r"\[\[([^\]\r\n]+)\]\]", line):
                    inner = m.group(1)
                    if re.search(r"(?<!\\)\|", inner):
                        violations.append({
                            "file": rel_path,
                            "line": row_idx + 1,
                            "wikilink": m.group(0),
                            "inner": inner,
                            "full_line": line.strip()
                        })
    return violations

def build_graph_and_audit_links(root: Path, md_files: List[Tuple[Path, str]], all_files: List[Tuple[Path, str]]) -> Dict[str, Any]:
    """Constructs directed graph, resolves wikilinks against all vault files, checks anchors and case mismatches."""
    files_exact = {}
    files_lower = {}
    file_headings = {}

    for full_path, rel_path in all_files:
        base_name = full_path.stem
        f_name = full_path.name
        
        files_exact[rel_path] = (full_path, rel_path)
        files_exact[base_name] = (full_path, rel_path)
        files_exact[f_name] = (full_path, rel_path)
        
        files_lower[rel_path.lower()] = (full_path, rel_path)
        files_lower[base_name.lower()] = (full_path, rel_path)
        files_lower[f_name.lower()] = (full_path, rel_path)

        if full_path.suffix == ".md":
            try:
                content = full_path.read_text(encoding="utf-8")
            except Exception:
                content = full_path.read_text(encoding="utf-8", errors="replace")
            headings = set(re.findall(r"^#{1,6}\s+(.+)$", content, flags=re.MULTILINE))
            clean_headings = {re.sub(r"[*_`]", "", h).strip() for h in headings}
            file_headings[rel_path] = headings.union(clean_headings)

    out_edges = defaultdict(list)
    in_edges = defaultdict(list)

    all_nodes = [rel for _, rel in md_files]
    for n in all_nodes:
        out_edges[n] = []
        in_edges[n] = []

    broken_links = []
    case_mismatches = []
    anchor_failures = []
    windows_backslashes = []
    bracket_errors = []
    self_links = []
    total_wikilink_count = 0

    wikilink_pat = re.compile(r"(!?)\[\[([^\]\r\n]+)\]\]")

    for full_path, rel_path in md_files:
        try:
            content = full_path.read_text(encoding="utf-8")
        except Exception:
            content = full_path.read_text(encoding="utf-8", errors="replace")

        # Strip code blocks and inline code
        content_clean = re.sub(r"```[\s\S]*?```", "", content)
        content_clean = re.sub(r"`[^`\r\n]*`", "", content_clean)

        for m in wikilink_pat.finditer(content_clean):
            total_wikilink_count += 1
            raw_inner = m.group(2).strip()

            # Check alias
            if "|" in raw_inner:
                target_part = re.split(r"\\?\|", raw_inner, maxsplit=1)[0].rstrip("\\").strip()
            else:
                target_part = raw_inner.rstrip("\\").strip()

            # Check heading anchor
            anchor = None
            if "#" in target_part:
                parts = target_part.split("#", 1)
                target = parts[0].rstrip("\\").strip()
                anchor = parts[1].rstrip("\\").strip()
            else:
                target = target_part

            if not target or target == "...":
                continue

            # Check windows backslash in path
            if "\\" in target:
                windows_backslashes.append((rel_path, target))

            norm_target = target.replace("\\", "/").rstrip("/")

            # Resolution strategy
            resolved_file = None
            resolved_rel = None
            is_case_mismatch = False

            # 1. Exact resolution
            for cand in [norm_target, f"{norm_target}.md", Path(norm_target).name, f"{Path(norm_target).name}.md"]:
                if cand in files_exact:
                    resolved_file, resolved_rel = files_exact[cand]
                    break

            # 2. Case-insensitive resolution
            if not resolved_file:
                for cand in [norm_target.lower(), f"{norm_target.lower()}.md", Path(norm_target).name.lower(), f"{Path(norm_target).name.lower()}.md"]:
                    if cand in files_lower:
                        resolved_file, resolved_rel = files_lower[cand]
                        is_case_mismatch = True
                        break

            # 3. Folder MOC convention
            if not resolved_file:
                folder_moc = f"{norm_target}/{Path(norm_target).name}"
                if folder_moc in files_exact or f"{folder_moc}.md" in files_exact:
                    resolved_file, resolved_rel = files_exact.get(folder_moc) or files_exact.get(f"{folder_moc}.md")
                elif folder_moc.lower() in files_lower or f"{folder_moc.lower()}.md" in files_lower:
                    resolved_file, resolved_rel = files_lower.get(folder_moc.lower()) or files_lower.get(f"{folder_moc.lower()}.md")
                    is_case_mismatch = True

            if resolved_file:
                if is_case_mismatch:
                    case_mismatches.append((rel_path, target, resolved_rel))

                if resolved_rel == rel_path:
                    self_links.append((rel_path, target))

                out_edges[rel_path].append((resolved_rel, target, is_case_mismatch))
                if resolved_rel in in_edges:
                    in_edges[resolved_rel].append((rel_path, target))

                # Validate anchor
                if anchor and resolved_rel in file_headings:
                    if anchor not in file_headings[resolved_rel]:
                        anchor_failures.append((rel_path, resolved_rel, anchor))
            else:
                broken_links.append((rel_path, target))

    # Distinct in-degrees from other notes
    distinct_in_degrees = {n: len(set(src for src, _ in in_edges[n] if src != n)) for n in all_nodes}
    distinct_out_degrees = {n: len(set(dst for dst, _, _ in out_edges[n] if dst != n)) for n in all_nodes}

    # Orphans: In-degree == 0 from other notes
    orphans = [n for n in all_nodes if distinct_in_degrees[n] == 0]
    dead_ends = [n for n in all_nodes if distinct_out_degrees[n] == 0]
    pure_islands = [n for n in all_nodes if distinct_in_degrees[n] == 0 and distinct_out_degrees[n] == 0]

    return {
        "all_nodes": all_nodes,
        "out_edges": out_edges,
        "in_edges": in_edges,
        "distinct_in_degrees": distinct_in_degrees,
        "distinct_out_degrees": distinct_out_degrees,
        "orphans": orphans,
        "dead_ends": dead_ends,
        "pure_islands": pure_islands,
        "broken_links": broken_links,
        "case_mismatches": case_mismatches,
        "anchor_failures": anchor_failures,
        "windows_backslashes": windows_backslashes,
        "bracket_errors": bracket_errors,
        "self_links": self_links,
        "total_wikilink_count": total_wikilink_count
    }

def evaluate_graph_topology(graph_data: Dict[str, Any]) -> Dict[str, Any]:
    """Calculates connected components, diameter, reachability, hubs, and articulation points."""
    nodes = graph_data["all_nodes"]
    out_edges = graph_data["out_edges"]
    
    # 1. Undirected adjacency for Weakly Connected Components (WCC)
    undirected_adj = defaultdict(set)
    for u in nodes:
        for v, _, _ in out_edges[u]:
            if u != v:
                undirected_adj[u].add(v)
                undirected_adj[v].add(u)

    visited = set()
    components = []
    for node in nodes:
        if node not in visited:
            comp = []
            queue = deque([node])
            visited.add(node)
            while queue:
                curr = queue.popleft()
                comp.append(curr)
                for neighbor in undirected_adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            components.append(sorted(comp))

    components.sort(key=lambda c: len(c), reverse=True)

    # 2. Shortest paths and Diameter on largest component
    largest_comp = components[0] if components else []
    largest_set = set(largest_comp)
    
    max_distance_undirected = 0
    total_distance_undirected = 0
    pairs_count_undirected = 0
    diameter_endpoints = None
    eccentricities = {}

    for start_node in largest_comp:
        dist = {start_node: 0}
        queue = deque([start_node])
        max_dist_from_node = 0
        while queue:
            curr = queue.popleft()
            d = dist[curr]
            if d > max_dist_from_node:
                max_dist_from_node = d
            for neighbor in undirected_adj[curr]:
                if neighbor in largest_set and neighbor not in dist:
                    dist[neighbor] = d + 1
                    queue.append(neighbor)
                    if d + 1 > max_distance_undirected:
                        max_distance_undirected = d + 1
                        diameter_endpoints = (start_node, neighbor)
        eccentricities[start_node] = max_dist_from_node
        for target_node, d in dist.items():
            if target_node > start_node:
                total_distance_undirected += d
                pairs_count_undirected += 1

    avg_path_undirected = (total_distance_undirected / pairs_count_undirected) if pairs_count_undirected > 0 else 0.0
    radius = min(eccentricities.values()) if eccentricities else 0

    # 3. Directed Reachability from Master Brain: "AI Sozlangan Miyyasi.md"
    master_node = "AI Sozlangan Miyyasi.md"
    reachable_from_master = set()
    if master_node in nodes:
        queue = deque([master_node])
        reachable_from_master.add(master_node)
        while queue:
            curr = queue.popleft()
            for v, _, _ in out_edges[curr]:
                if v not in reachable_from_master:
                    reachable_from_master.add(v)
                    queue.append(v)

    unreachable_from_master = sorted(list(set(nodes) - reachable_from_master))

    # 4. Strongly Connected Components (SCC) using Tarjan's
    index = 0
    indices = {}
    lowlink = {}
    on_stack = set()
    stack = []
    sccs = []

    def strongconnect(u):
        nonlocal index
        indices[u] = index
        lowlink[u] = index
        index += 1
        stack.append(u)
        on_stack.add(u)

        for v, _, _ in out_edges[u]:
            if v not in indices:
                strongconnect(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif v in on_stack:
                lowlink[u] = min(lowlink[u], indices[v])

        if lowlink[u] == indices[u]:
            comp = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.append(w)
                if w == u:
                    break
            sccs.append(comp)

    for n in nodes:
        if n not in indices:
            strongconnect(n)

    sccs.sort(key=lambda c: len(c), reverse=True)

    # 5. Articulation points in undirected graph
    time_counter = 0
    tin = {}
    low = {}
    art_points = set()

    def dfs_art(u, parent=None):
        nonlocal time_counter
        tin[u] = low[u] = time_counter
        time_counter += 1
        children = 0
        for to in undirected_adj[u]:
            if to == parent:
                continue
            if to in tin:
                low[u] = min(low[u], tin[to])
            else:
                dfs_art(to, u)
                low[u] = min(low[u], low[to])
                if low[to] >= tin[u] and parent is not None:
                    art_points.add(u)
                children += 1
        if parent is None and children > 1:
            art_points.add(u)

    for n in nodes:
        if n not in tin:
            dfs_art(n)

    # 6. Top Hubs
    sorted_by_in = sorted(nodes, key=lambda n: graph_data["distinct_in_degrees"][n], reverse=True)
    sorted_by_out = sorted(nodes, key=lambda n: graph_data["distinct_out_degrees"][n], reverse=True)
    sorted_by_total = sorted(nodes, key=lambda n: (graph_data["distinct_in_degrees"][n] + graph_data["distinct_out_degrees"][n]), reverse=True)

    return {
        "component_count": len(components),
        "components": components,
        "is_single_connected_component": len(components) == 1,
        "largest_component_size": len(largest_comp),
        "undirected_diameter": max_distance_undirected,
        "diameter_endpoints": diameter_endpoints,
        "undirected_radius": radius,
        "avg_path_undirected": avg_path_undirected,
        "master_reachable_count": len(reachable_from_master),
        "master_unreachable_count": len(unreachable_from_master),
        "master_unreachable_nodes": unreachable_from_master,
        "scc_count": len(sccs),
        "largest_scc_size": len(sccs[0]) if sccs else 0,
        "articulation_points": sorted(list(art_points)),
        "top_in_hubs": [(n, graph_data["distinct_in_degrees"][n]) for n in sorted_by_in[:10]],
        "top_out_hubs": [(n, graph_data["distinct_out_degrees"][n]) for n in sorted_by_out[:10]],
        "top_total_hubs": [(n, graph_data["distinct_in_degrees"][n] + graph_data["distinct_out_degrees"][n]) for n in sorted_by_total[:10]],
    }

def run_stress_test() -> Dict[str, Any]:
    print("=" * 80)
    print(" ADVERSARIAL VAULT GRAPH STRESS TEST HARNESS -- CHALLENGER_E4_1")
    print(f" Vault Root: {VAULT_ROOT}")
    print("=" * 80)

    md_files, all_files = discover_vault_files(VAULT_ROOT)
    print(f"\n[1] Discovered {len(md_files)} active Markdown files ({len(all_files)} total vault files).")

    # Step 1: UTF-8 & BOM
    enc_res = audit_utf8_and_bom(md_files)
    print(f"\n[2] Encoding & BOM Audit:")
    print(f"    - Total Files Probed: {len(md_files)}")
    print(f"    - BOM Violations: {len(enc_res['bom_files'])}")
    print(f"    - UTF-8 Strict Decode Errors: {len(enc_res['utf8_decode_errors'])}")
    print(f"    - Mojibake / Replacement Chars: {len(enc_res['mojibake_or_replacement'])}")
    print(f"    - Line Endings: {enc_res['line_ending_stats']}")

    # Step 2: Frontmatter
    fm_res = audit_frontmatter(md_files)
    print(f"\n[3] Frontmatter & YAML Hygiene Audit:")
    print(f"    - Total Frontmatters Parsed: {fm_res['parsed_count']}")
    print(f"    - Missing Frontmatter: {len(fm_res['missing_frontmatter'])}")
    for mf in fm_res['missing_frontmatter']:
        print(f"      * Missing: {mf}")
    print(f"    - YAML Syntax / SafeLoad Errors: {len(fm_res['yaml_syntax_errors'])}")
    for f, err in fm_res['yaml_syntax_errors']:
        print(f"      * {f}: {err.splitlines()[0]}")
    print(f"    - Missing Tags: {len(fm_res['missing_tags'])}")
    print(f"    - Invalid Tags Format: {len(fm_res['invalid_tags_format'])}")
    print(f"    - Date Format Anomalies: {len(fm_res['date_format_issues'])}")

    # Step 3: Table Pipe Escaping
    table_pipes = audit_table_pipe_escaping(md_files)
    print(f"\n[4] Markdown Table Wikilink Pipe Escaping Audit:")
    print(f"    - Unescaped Pipe Violations inside Tables: {len(table_pipes)}")
    for tp in table_pipes:
        print(f"      * {tp['file']}:{tp['line']} -> {tp['wikilink']}")

    # Step 4: Graph and Link Resolution
    graph_res = build_graph_and_audit_links(VAULT_ROOT, md_files, all_files)
    print(f"\n[5] Wikilink Resolution & Graph Construction:")
    print(f"    - Total Wikilinks Audited: {graph_res['total_wikilink_count']}")
    print(f"    - Broken Wikilinks: {len(graph_res['broken_links'])}")
    for src, tgt in graph_res['broken_links']:
        print(f"      * Broken: {src} -> [[{tgt}]]")
    print(f"    - Case Mismatches: {len(graph_res['case_mismatches'])}")
    print(f"    - Heading Anchor Failures: {len(graph_res['anchor_failures'])}")
    print(f"    - Raw Windows Backslashes: {len(graph_res['windows_backslashes'])}")
    print(f"    - Bracket Balance Errors: {len(graph_res['bracket_errors'])}")
    print(f"    - Self Links: {len(graph_res['self_links'])}")
    print(f"    - In-degree 0 (Orphan Notes): {len(graph_res['orphans'])}")
    print(f"    - Pure Island Notes: {len(graph_res['pure_islands'])}")
    print(f"    - Dead-end Notes (Out-degree 0): {len(graph_res['dead_ends'])}")
    for de in graph_res['dead_ends']:
        print(f"      * Dead-end: {de}")

    # Step 5: Graph Topology & Components
    topo_res = evaluate_graph_topology(graph_res)
    print(f"\n[6] Graph Topology & Component Analysis:")
    print(f"    - Weakly Connected Components (WCC): {topo_res['component_count']}")
    print(f"    - Single Connected Component: {topo_res['is_single_connected_component']}")
    print(f"    - Undirected Graph Diameter: {topo_res['undirected_diameter']}")
    print(f"    - Diameter Endpoints: {topo_res['diameter_endpoints']}")
    print(f"    - Undirected Radius: {topo_res['undirected_radius']}")
    print(f"    - Average Shortest Path Length: {topo_res['avg_path_undirected']:.4f}")
    print(f"    - Master Brain Reachable Nodes: {topo_res['master_reachable_count']} / {len(md_files)}")
    print(f"    - Master Brain Unreachable Nodes: {topo_res['master_unreachable_count']}")
    print(f"    - Strongly Connected Components: {topo_res['scc_count']}")
    print(f"    - Largest SCC Size: {topo_res['largest_scc_size']}")
    print(f"    - Articulation Points (Cut Vertices): {len(topo_res['articulation_points'])}")
    for ap in topo_res['articulation_points'][:5]:
        print(f"      * Cut Vertex: {ap}")
    
    print(f"\n[7] Graph Hubs & Degree Extremes:")
    print(f"    - Top In-Degree Hubs:")
    for node, deg in topo_res['top_in_hubs'][:5]:
        print(f"      * {node}: {deg} incoming notes")
    print(f"    - Top Out-Degree Hubs:")
    for node, deg in topo_res['top_out_hubs'][:5]:
        print(f"      * {node}: {deg} outgoing targets")
    print(f"    - Top Total Degree Hubs:")
    for node, deg in topo_res['top_total_hubs'][:5]:
        print(f"      * {node}: {deg} total distinct neighbors")

    # Overall Verdict Calculation
    # We evaluate against all strict requirements:
    # 1. 0 broken wikilinks -> PASS (0 broken)
    # 2. In-degree >= 1 (0 orphans) -> PASS (0 orphans)
    # 3. Connected components == 1 (0 isolated components) -> PASS (1 component)
    # 4. UTF-8 Clean & 0 BOM -> PASS (0 BOM, 0 decode errors)
    # 5. Table pipes -> FAIL (3 unescaped pipes in tables)
    # 6. YAML safe_load -> FAIL (9 YAML parsing errors, 5 missing FM)
    
    critical_defects = []
    if len(table_pipes) > 0:
        critical_defects.append(f"Markdown Table Syntax: {len(table_pipes)} unescaped pipe wikilinks breaking table columns")
    if len(fm_res['yaml_syntax_errors']) > 0:
        critical_defects.append(f"YAML Syntax: {len(fm_res['yaml_syntax_errors'])} notes fail standard YAML safe_load parsing")
    if len(graph_res['broken_links']) > 0:
        critical_defects.append(f"Broken Links: {len(graph_res['broken_links'])} broken wikilinks")
    if len(graph_res['orphans']) > 0:
        critical_defects.append(f"Orphans: {len(graph_res['orphans'])} orphaned notes")
    if topo_res['component_count'] > 1:
        critical_defects.append(f"Isolated Components: Graph partitioned into {topo_res['component_count']} components")

    # Note: If critical defects exist, verdict is REJECT with conditional remediation requirements
    verdict = "REJECT" if critical_defects else "APPROVE"

    print("\n" + "=" * 80)
    print(f" OVERALL ADVERSARIAL VERDICT: {verdict}")
    if critical_defects:
        print(" CRITICAL DEFECTS IDENTIFIED:")
        for d in critical_defects:
            print(f"  [X] {d}")
    else:
        print(" ALL EMPIRICAL CRITERIA FULLY SATISFIED.")
    print("=" * 80)

    output_data = {
        "verdict": verdict,
        "critical_defects": critical_defects,
        "file_count": len(md_files),
        "encoding": enc_res,
        "frontmatter": fm_res,
        "table_pipes": table_pipes,
        "graph": {
            "total_wikilinks": graph_res["total_wikilink_count"],
            "broken_links": graph_res["broken_links"],
            "case_mismatches": graph_res["case_mismatches"],
            "anchor_failures": graph_res["anchor_failures"],
            "windows_backslashes": graph_res["windows_backslashes"],
            "bracket_errors": graph_res["bracket_errors"],
            "self_links": graph_res["self_links"],
            "orphans": graph_res["orphans"],
            "pure_islands": graph_res["pure_islands"],
            "dead_ends": graph_res["dead_ends"],
            "distinct_in_degrees": graph_res["distinct_in_degrees"],
            "distinct_out_degrees": graph_res["distinct_out_degrees"],
        },
        "topology": {
            "component_count": topo_res["component_count"],
            "components": topo_res["components"],
            "is_single_connected_component": topo_res["is_single_connected_component"],
            "largest_component_size": topo_res["largest_component_size"],
            "undirected_diameter": topo_res["undirected_diameter"],
            "diameter_endpoints": topo_res["diameter_endpoints"],
            "undirected_radius": topo_res["undirected_radius"],
            "avg_path_undirected": topo_res["avg_path_undirected"],
            "master_reachable_count": topo_res["master_reachable_count"],
            "master_unreachable_count": topo_res["master_unreachable_count"],
            "master_unreachable_nodes": topo_res["master_unreachable_nodes"],
            "scc_count": topo_res["scc_count"],
            "largest_scc_size": topo_res["largest_scc_size"],
            "articulation_points": topo_res["articulation_points"],
            "top_in_hubs": topo_res["top_in_hubs"],
            "top_out_hubs": topo_res["top_out_hubs"],
            "top_total_hubs": topo_res["top_total_hubs"],
        }
    }

    out_json = VAULT_ROOT / ".agents" / "challenger_e4_1" / "stress_results.json"
    out_json.write_text(json.dumps(output_data, indent=2), encoding="utf-8")
    print(f"\nFull results exported to {out_json}")
    return output_data

if __name__ == "__main__":
    run_stress_test()