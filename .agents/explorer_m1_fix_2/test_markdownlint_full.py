import re
import subprocess
from pathlib import Path

vault = Path(r"D:\obsidian file")
agent_dir = Path(r"D:\obsidian file\.agents\explorer_m1_fix_2")

mb_text = (vault / "AI Sozlangan Miyyasi.md").read_text(encoding="utf-8")
db_text = (vault / "Dashboard.md").read_text(encoding="utf-8")

# Escape table pipes in both files
def escape_tables(text):
    lines = text.splitlines()
    out = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            def repl(m):
                content = m.group(1)
                if "|" in content and not "\\|" in content:
                    content = content.replace("|", "\\|")
                return f"[[{content}]]"
            new_line = re.sub(r"\[\[([^\]]+)\]\]", repl, line)
            out.append(new_line)
        else:
            out.append(line)
    return "\n".join(out) + "\n"

sim_mb = escape_tables(mb_text)
sim_db = escape_tables(db_text)

# Also fix the blank lines in Dashboard.md to see pure MD056 result
# In Dashboard.md: add blank lines around headings and lists
fixed_mb_path = agent_dir / "sim_AI_Sozlangan_Miyyasi.md"
fixed_db_path = agent_dir / "sim_Dashboard.md"

fixed_mb_path.write_text(sim_mb, encoding="utf-8")
fixed_db_path.write_text(sim_db, encoding="utf-8")

res = subprocess.run(
    ["npx.cmd", "markdownlint-cli", str(fixed_mb_path), str(fixed_db_path)],
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="replace"
)

output = (res.stdout + res.stderr).strip()
md056_errors = [l for l in output.splitlines() if "MD056" in l]
print(f"Total MD056 errors found with escaped pipes: {len(md056_errors)}")
for e in md056_errors:
    print("  ", e)
