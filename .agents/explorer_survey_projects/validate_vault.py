"""
Obsidian Vault Wikilink & Markdown Integrity Validator
Scans the Obsidian vault, verifies all [[wikilinks]] against vault files,
checks YAML frontmatter and code blocks, and reports broken links or syntax errors.
"""

import os
import re
import os
import re
import sys

def validate_vault(vault_root, ignored_dirs=None):
    if ignored_dirs is None:
        ignored_dirs = {".agents", ".antigravity", ".git", ".obsidian"}

    # Phase 1: Build target index
    indexed_files = set()
    file_list = []
    
    for root, dirs, files in os.walk(vault_root):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for f in files:
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, vault_root).replace("\\", "/")
            base_name, _ = os.path.splitext(f)
            rel_no_ext, _ = os.path.splitext(rel_path)
            
            # Case-insensitive normalized targets
            indexed_files.add(f.lower())
            indexed_files.add(base_name.lower())
            indexed_files.add(rel_path.lower())
            indexed_files.add(rel_no_ext.lower())
            
            if f.endswith(".md"):
                file_list.append((full_path, rel_path))

    wikilink_regex = re.compile(r'!?\[\[([^\]|#\\]+)(?:#[^\]|\\]*)?(?:\\?\|[^\]]*)?\]\]')
    
    broken_links = []
    syntax_errors = []
    total_links = 0

    # Phase 2: Validate each markdown file
    for full_path, rel_path in file_list:
        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            lines = content.splitlines()

        # Frontmatter validation
        if content.startswith("---"):
            fm_parts = content.split("---", 2)
            if len(fm_parts) >= 3:
                fm_raw = fm_parts[1]
                f_lines = fm_raw.splitlines()
                for f_idx, f_line in enumerate(f_lines, 2):
                    stripped = f_line.strip()
                    if not stripped or stripped.startswith("#"):
                        continue
                    if not (":" in stripped or stripped.startswith("-") or stripped.startswith("[") or stripped.endswith("]")):
                        syntax_errors.append((rel_path, f_idx, f"Suspect YAML frontmatter line: '{stripped}'"))
            else:
                syntax_errors.append((rel_path, 1, "Unclosed YAML frontmatter"))

        # Code block fence balance check
        fence_count = sum(1 for line in lines if line.strip().startswith("```"))
        if fence_count % 2 != 0:
            syntax_errors.append((rel_path, len(lines), f"Unclosed code fence (odd number of ```: {fence_count})"))

        # Wikilink check
        in_code_block = False
        for line_idx, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue

            # Strip inline code spans so didactic/example wikilinks wrapped in backticks are not treated as active links
            clean_line = re.sub(r'`[^`\r\n]*`', '', line)
            for m in wikilink_regex.finditer(clean_line):
                target = m.group(1).rstrip("\\").strip()
                # Skip template placeholders like [[...]]
                if target == "..." or not target:
                    continue
                total_links += 1
                norm_target = target.replace("\\", "/").rstrip("/").lower()
                if norm_target not in indexed_files:
                    broken_links.append((rel_path, line_idx, target))

    return {
        "scanned_files": len(file_list),
        "indexed_targets": len(indexed_files),
        "total_links": total_links,
        "broken_links": broken_links,
        "syntax_errors": syntax_errors
    }

if __name__ == "__main__":
    vault_path = sys.argv[1] if len(sys.argv) > 1 else r"D:\obsidian file"
    print(f"Validating vault at: {vault_path}")
    result = validate_vault(vault_path)
    print(f"Scanned Markdown Files: {result['scanned_files']}")
    print(f"Total Wikilinks Checked: {result['total_links']}")
    print(f"Broken Links Found: {len(result['broken_links'])}")
    for rel_path, line_idx, target in result['broken_links']:
        print(f"  [BROKEN] {rel_path}:{line_idx} -> [[{target}]]")
    print(f"Syntax Errors Found: {len(result['syntax_errors'])}")
    for rel_path, line_idx, err in result['syntax_errors']:
        print(f"  [SYNTAX] {rel_path}:{line_idx} -> {err}")
