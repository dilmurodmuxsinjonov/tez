import os
import re
from pathlib import Path

vault_root = Path(r"D:\obsidian file")
projects_dir = vault_root / "10 Projects"

for p in sorted(projects_dir.glob("*.md")):
    if "MOC" in p.name or p.name == "10 Projects.md":
        continue
    content = p.read_text(encoding="utf-8")
    print(f"=== {p.name} ===")
    m_state = re.search(r"##\s*📋\s*Latest State Summary\s*\n+([^\n#]+)", content)
    if m_state:
        state_text = m_state.group(1).strip()
        words = state_text.split()
        print(f"Latest State words: {len(words)} ({state_text[:60]}...)")
    else:
        print("Latest State Summary NOT FOUND")
    m_steps = re.search(r"##\s*🎯\s*Suggested Next Steps\s*\n+([\s\S]*?)(?=\n{3,}|\Z)", content)
    if m_steps:
        raw_lines = [s.strip() for s in m_steps.group(1).splitlines() if s.strip() and not s.strip().startswith("```")]
        print(f"Suggested Next Steps count: {len(raw_lines)}")
        for s in raw_lines:
            clean = re.sub(r"^[0-9*.-]+\s*", "", s).strip()
            first_word = clean.split()[0] if clean.split() else ""
            print(f"  len={len(clean)} | verb={first_word} | text=\"{clean}\"")
    else:
        print("Suggested Next Steps NOT FOUND")
