import os
import re
import subprocess
from pathlib import Path

VAULT_DIR = Path(r"D:\obsidian file")
PROJECTS_DIR = VAULT_DIR / "10 Projects"
FILES = [
    "MobCreatorWebApp.md",
    "NagoyaCastle.md",
    "The_AI_Pipeline.md",
    "Orol Shahar Qirollik.md",
    "Doctor A Med Clinic.md",
]

print("=" * 80)
print("MILENSTONE 3 EMPIRICAL MEASUREMENTS & DATA BREAKDOWN")
print("=" * 80)

for filename in FILES:
    filepath = PROJECTS_DIR / filename
    raw = filepath.read_bytes()
    text = raw.decode("utf-8")
    
    print(f"\n>>> FILE: {filename}")
    print(f"  File size: {len(raw)} bytes, text length: {len(text)} chars")
    print(f"  First 4 bytes (hex): {raw[:4].hex()} (BOM check: {'FAIL' if raw.startswith(b'\xef\xbb\xbf') else 'PASS - No BOM'})")
    
    # 1. Suggested Next Steps
    m_steps = re.search(r"## 🎯 Suggested Next Steps\s*\n(.*?)(?=\n\n\n\n\n|\n```|\Z)", text, re.DOTALL)
    if m_steps:
        lines = [l.strip() for l in m_steps.group(1).splitlines() if l.strip()]
        print(f"  Suggested Next Steps ({len(lines)} items):")
        for idx, line in enumerate(lines, 1):
            st = line[2:].strip() if line.startswith("- ") else line
            verb = st.split()[0]
            print(f"    [{idx}] len={len(st)} chars | verb='{verb}' | text='{st}'")
    
    # 2. Visual Separation
    normalized = text.replace("\r\n", "\n")
    m_sep = re.search(r"(## 🎯 Suggested Next Steps.*?)(```text)", normalized, re.DOTALL)
    if m_sep:
        sec = m_sep.group(1)
        last_non_ws = len(sec.rstrip())
        sep = sec[last_non_ws:]
        nl_count = sep.count("\n")
        blank_lines = nl_count - 1
        print(f"  Visual Separation before code block:")
        print(f"    Newline count: {nl_count} (blank lines: {blank_lines}), exact repr: {repr(sep)}")
    
    # 3. Code block line lengths
    m_code = re.search(r"```text\s*\n(.*?)\n```", text, re.DOTALL)
    if m_code:
        code_lines = m_code.group(1).splitlines()
        max_l = max(len(l) for l in code_lines)
        over_80 = [l for l in code_lines if len(l) > 80]
        print(f"  Code block: {len(code_lines)} lines, max line length = {max_l} chars, over 80 chars = {len(over_80)}")
    
    # 4. Latest State Summary
    m_state = re.search(r"## 📋 Latest State Summary\s*\n\s*(.*?)(?=\n---\n|\n## |\Z)", text, re.DOTALL)
    if m_state:
        state_text = m_state.group(1).strip()
        words = state_text.split()
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", state_text) if s.strip()]
        print(f"  Latest State Summary: {len(words)} words, {len(sentences)} sentences")
    
    # 5. Wikilinks
    links = re.findall(r"\[\[(.*?)\]\]", text)
    print(f"  Wikilinks ({len(links)} links): {links}")

print("\n" + "=" * 80)
print("GIT STATUS & REVISION")
print("=" * 80)
branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=str(VAULT_DIR), text=True).strip()
commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(VAULT_DIR), text=True).strip()
log = subprocess.check_output(["git", "log", "-n", "3", "--format=%h %an %ad %s"], cwd=str(VAULT_DIR), text=True).strip()
status = subprocess.check_output(["git", "status", "--porcelain"], cwd=str(VAULT_DIR), text=True).strip()

print(f"Branch: {branch}")
print(f"HEAD commit: {commit}")
print(f"Recent commits:\n{log}")
print(f"Git status porcelain:\n{status}")