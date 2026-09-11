from pathlib import Path
import re
import sys
sys.path.insert(0, r"D:\obsidian file")
from tests.e2e.helpers import check_visual_separation

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
    is_sep, count = check_visual_separation(content)
    print(f"{fname}: is_separated={is_sep}, blank_lines_count={count}")
    assert is_sep and count == 5, f"Visual separation failed for {fname}: got {count}"
print("\nALL 5 FILES HAVE EXACTLY 5 BLANK LINES VISUAL SEPARATION!")
