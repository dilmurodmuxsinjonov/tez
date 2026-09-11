import re
import sys
from pathlib import Path

vault = Path(r"D:\obsidian file")
sys.path.insert(0, str(vault / ".agents" / "explorer_survey_projects"))

import validate_vault

# Test current validate_vault logic on simulated escaped pipes
mb_text = (vault / "AI Sozlangan Miyyasi.md").read_text(encoding="utf-8")
sim_escaped = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"[[\1\\|\2]]", mb_text)

# Let's see what wikilink_regex in validate_vault.py extracts:
r_old = re.compile(r'!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')
r_new = re.compile(r'!?\[\[([^\]|#\\]+)(?:#[^\]|\\]*)?(?:\\?\|[^\]]*)?\]\]')

print("Old regex matches on escaped table links:")
for m in r_old.finditer(sim_escaped):
    if "\\" in m.group(1):
        print("  OLD captured backslash:", repr(m.group(1)))

print("\nNew regex matches on escaped table links:")
for m in r_new.finditer(sim_escaped):
    if "\\" in m.group(1):
        print("  NEW captured backslash:", repr(m.group(1)))
print("  Total new matches:", sum(1 for _ in r_new.finditer(sim_escaped)))
