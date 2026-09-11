import re
from pathlib import Path

vault = Path(r"D:\obsidian file")
m4_notes = [
    "30 Resources/Autonomous Agent Architectures.md",
    "20 Areas/Browser Automation Playbook.md",
    "30 Resources/Multimodal Generation Workflows.md",
    "00 Inbox/00 Inbox MOC.md",
    "10 Projects/10 Projects MOC.md",
    "20 Areas/20 Areas MOC.md",
    "30 Resources/30 Resources MOC.md",
    "40 Archives/40 Archives MOC.md",
]

for n in m4_notes:
    text = (vault / n).read_text(encoding="utf-8")
    # Find all inline backtick code
    inline_codes = re.findall(r"`([^`]+)`", text)
    for ic in inline_codes:
        if "[[" in ic and "]]" in ic:
            print(f"In {n}: inline code with wikilink syntax: `{ic}`")
