from pathlib import Path
import re
import sys
sys.path.insert(0, r"D:\obsidian file")
from tests.e2e.helpers import validate_suggested_next_step

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
    m = re.search(r"## 🎯 Suggested Next Steps\s*\n+([\s\S]*?)(?=\n{5,}```)", content)
    print(f"\n--- {fname} ---")
    if not m:
        print("FAILED TO MATCH NEXT STEPS SECTION")
        continue
    steps = [line.strip().lstrip("-* ").strip() for line in m.group(1).splitlines() if line.strip()]
    print(f"Step count: {len(steps)}")
    for s in steps:
        v = validate_suggested_next_step(s)
        print(f"[{len(s)} chars] '{s}' | Valid: {v['is_valid']}, Verb: {v['first_word']}, VerbOk: {v['is_action_verb']}, LenOk: {v['length_valid']}")
