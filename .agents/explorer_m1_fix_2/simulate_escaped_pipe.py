import re
import sys
from pathlib import Path

vault = Path(r"D:\obsidian file")
sys.path.insert(0, str(vault))

from tests.e2e.helpers import extract_wikilinks, resolve_wikilink

mb_text = (vault / "AI Sozlangan Miyyasi.md").read_text(encoding="utf-8")
db_text = (vault / "Dashboard.md").read_text(encoding="utf-8")

# Simulate escaping pipes in tables
# In tables, [[Target|Alias]] -> [[Target\|Alias]]
def escape_table_pipes(text):
    lines = text.splitlines()
    out = []
    in_table = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            # Replace unescaped | inside [[...]] with \|
            def repl(m):
                content = m.group(1)
                if "|" in content and not "\\|" in content:
                    content = content.replace("|", "\\|")
                return f"[[{content}]]"
            new_line = re.sub(r"\[\[([^\]]+)\]\]", repl, line)
            out.append(new_line)
        else:
            out.append(line)
    return "\n".join(out)

sim_mb = escape_table_pipes(mb_text)
sim_db = escape_table_pipes(db_text)

print("Testing extract_wikilinks on escaped table content:")
mb_links = extract_wikilinks(sim_mb)
db_links = extract_wikilinks(sim_db)

print(f"Total MB links: {len(mb_links)}, Total DB links: {len(db_links)}")

backslash_targets = []
for l in mb_links + db_links:
    if "\\" in l["target"]:
        backslash_targets.append(l)

print(f"Links with backslash in target: {len(backslash_targets)}")
for b in backslash_targets[:5]:
    print("  ", b)
