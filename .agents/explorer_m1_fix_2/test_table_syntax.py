import subprocess
from pathlib import Path

test_dir = Path(r"D:\obsidian file\.agents\explorer_m1_fix_2")

test_cases = {
    "unescaped_pipe": """# Test

| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| A | B | [[Target/Sub|Alias]] |
""",
    "escaped_pipe": """# Test

| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| A | B | [[Target/Sub\\|Alias]] |
""",
    "without_alias": """# Test

| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| A | B | [[00 Inbox/00 Inbox]] |
""",
    "html_code_entity": """# Test

| Col 1 | Col 2 | Col 3 |
| :--- | :--- | :--- |
| A | B | [[Target/Sub&#124;Alias]] |
"""
}

for name, content in test_cases.items():
    p = test_dir / f"test_{name}.md"
    p.write_text(content, encoding="utf-8")
    res = subprocess.run(
        ["npx.cmd", "markdownlint-cli", str(p)],
        capture_output=True,
        text=True
    )
    print(f"=== {name} ===")
    out = (res.stdout + res.stderr).strip()
    print(out if out else "No errors!")
