from pathlib import Path
import re

VAULT = Path(r"D:\obsidian file\10 Projects")
files = [
    "MobCreatorWebApp.md",
    "NagoyaCastle.md",
    "The_AI_Pipeline.md",
    "Orol Shahar Qirollik.md",
    "Doctor A Med Clinic.md"
]

for fname in files:
    content = (VAULT / fname).read_text(encoding="utf-8")
    m = re.search(r"```text\s*\n([\s\S]*?)\n```", content)
    print(f"\n--- {fname} Code Block Lines > 80 chars ---")
    if not m:
        continue
    lines = m.group(1).splitlines()
    for idx, l in enumerate(lines, 1):
        if len(l) > 80:
            print(f"Line {idx} ({len(l)} chars): {l}")
