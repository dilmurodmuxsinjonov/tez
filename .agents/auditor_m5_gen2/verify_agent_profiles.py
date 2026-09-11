import re
from pathlib import Path
import sys

VAULT_ROOT = Path(r"D:\obsidian file")
sys.path.insert(0, str(VAULT_ROOT))

from tests.e2e.helpers import parse_frontmatter, extract_wikilinks

profiles = [
    "Antigravity 1",
    "Antigravity 2",
    "Codex LLM Assistant",
    "Concurrency & Sync Protocol"
]

print("=== VERIFYING AGENT PROFILES ===")
for p_name in profiles:
    p_file = VAULT_ROOT / "20 Areas" / "Agent Profiles" / f"{p_name}.md"
    assert p_file.exists(), f"{p_name}.md missing"
    content = p_file.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)
    assert fm.get("status") == "active"
    t = fm.get("type")
    assert t in ("agent-profile", "protocol-spec", "system-protocol", "protocol"), f"unexpected type: {t}"
    
    # Check backlinks
    links = extract_wikilinks(content)
    targets = [l["target"] for l in links]
    print(f"[{p_name}] Links count: {len(links)}")
    has_mb = any("AI Sozlangan Miyyasi" in t for t in targets)
    assert has_mb, f"{p_name} lacks backlink to AI Sozlangan Miyyasi"
    print(f"[{p_name}] Backlink to Master Brain: OK")

print("ALL 4 AGENT PROFILES VERIFIED OK!")
