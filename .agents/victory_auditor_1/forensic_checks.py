import os
import re
import yaml
from pathlib import Path

vault_root = Path(r"D:\obsidian file")
ignored_dirs = {'.agents', '.antigravity', '.git', '.obsidian', 'tests', '.trash'}

print("=== FORENSIC ANTI-CHEAT & QUALITY INSPECTION ===")

all_md_files = []
for root, dirs, files in os.walk(vault_root):
    dirs[:] = [d for d in dirs if d not in ignored_dirs and not d.startswith('.')]
    rel_root = Path(root).relative_to(vault_root)
    if any(part in ignored_dirs for part in rel_root.parts):
        continue
    for f in files:
        if f.endswith('.md'):
            all_md_files.append(Path(root) / f)

print(f"1. YAML SAFE_LOAD CHECK ON ALL {len(all_md_files)} MARKDOWN FILES:")
yaml_failures = []
missing_frontmatter = []
for p in all_md_files:
    rel_path = p.relative_to(vault_root).as_posix()
    content = p.read_text(encoding='utf-8')
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_yaml = parts[1]
            try:
                parsed = yaml.safe_load(raw_yaml)
                if not isinstance(parsed, dict):
                    yaml_failures.append((rel_path, "Frontmatter does not evaluate to a dict"))
            except Exception as e:
                yaml_failures.append((rel_path, str(e)))
        else:
            yaml_failures.append((rel_path, "Unclosed frontmatter delimiter"))
    else:
        # Check if note is supposed to have frontmatter
        missing_frontmatter.append(rel_path)

print(f"   YAML Safe_load Failures: {len(yaml_failures)}")
for f, err in yaml_failures:
    print(f"     [FAIL] {f}: {err}")
print(f"   Notes without frontmatter: {len(missing_frontmatter)}")
for f in missing_frontmatter[:10]:
    print(f"     [INFO] No frontmatter: {f}")

print("\n2. CONTENT DEPTH & SUBSTANCE AUDIT (DETECT STUBS/FACADES):")
stub_threshold_words = 50
suspicious_stubs = []
for p in all_md_files:
    rel_path = p.relative_to(vault_root).as_posix()
    content = p.read_text(encoding='utf-8')
    words = content.split()
    word_count = len(words)
    byte_size = p.stat().st_size
    # Check for placeholder markers like TODO, TBD, LOREM IPSUM, coming soon
    has_lorem = "lorem ipsum" in content.lower()
    has_dummy = "dummy" in content.lower() and not "dummy" in rel_path.lower()
    # Check for empty body
    parts = content.split("---", 2)
    body = parts[2] if len(parts) >= 3 else content
    if len(body.strip()) < 100 or word_count < stub_threshold_words:
        suspicious_stubs.append((rel_path, word_count, byte_size))

print(f"   Suspiciously small files / potential stubs (<{stub_threshold_words} words): {len(suspicious_stubs)}")
for f, wc, sz in suspicious_stubs:
    print(f"     [WARN] {f}: {wc} words, {sz} bytes")

print("\n3. INSPECTING 5 NEW CLI AGENT PROFILES CONTENT SUBSTANCE:")
for a in ["Nous Hermes.md", "GitHub Copilot.md", "OpenCode CLI.md", "Google Antigravity CLI.md", "Ruflo Swarm.md"]:
    p = vault_root / "20 Areas" / "Agent Profiles" / a
    content = p.read_text(encoding='utf-8')
    wc = len(content.split())
    # Count sections
    sections = re.findall(r"^##+\s+(.*)$", content, flags=re.MULTILINE)
    # Count code blocks
    code_blocks = len(re.findall(r"`", content)) // 2
    print(f"   {a}: {wc} words, {len(sections)} sections, {code_blocks} code blocks, size={p.stat().st_size} bytes")

print("\n4. INSPECTING 3 MASTER RESOURCES CONTENT SUBSTANCE:")
for r in ["AI Agent Ecosystem Map.md", "Free LLM Models Registry.md", "Codex Skills Encyclopedia.md"]:
    p = vault_root / "30 Resources" / r
    content = p.read_text(encoding='utf-8')
    wc = len(content.split())
    sections = re.findall(r"^##+\s+(.*)$", content, flags=re.MULTILINE)
    code_blocks = len(re.findall(r"`", content)) // 2
    tables = content.count("|---")
    print(f"   {r}: {wc} words, {len(sections)} sections, {code_blocks} code blocks, {tables} tables, size={p.stat().st_size} bytes")

print("\n5. INSPECTING 3 NEW PRODUCTION TEMPLATES:")
for t in ["New Agent Integration Template.md", "Model Evaluation Template.md", "Security Audit Template.md"]:
    p = vault_root / "50 Templates" / t
    content = p.read_text(encoding='utf-8')
    wc = len(content.split())
    sections = re.findall(r"^##+\s+(.*)$", content, flags=re.MULTILINE)
    print(f"   {t}: {wc} words, {len(sections)} sections, size={p.stat().st_size} bytes")

