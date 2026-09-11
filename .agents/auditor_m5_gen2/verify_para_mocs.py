from pathlib import Path
import sys

VAULT_ROOT = Path(r"D:\obsidian file")
sys.path.insert(0, str(VAULT_ROOT))

from tests.e2e.helpers import parse_frontmatter, extract_wikilinks

mocs = [
    "00 Inbox/00 Inbox.md",
    "00 Inbox/00 Inbox MOC.md",
    "10 Projects/10 Projects.md",
    "10 Projects/10 Projects MOC.md",
    "20 Areas/20 Areas.md",
    "20 Areas/20 Areas MOC.md",
    "30 Resources/30 Resources.md",
    "30 Resources/30 Resources MOC.md",
    "40 Archives/40 Archives.md",
    "40 Archives/40 Archives MOC.md",
    "Dashboard.md",
    "AI Sozlangan Miyyasi.md"
]

print("=== VERIFYING PARA MOCS ===")
for m_path in mocs:
    f = VAULT_ROOT / m_path
    assert f.exists(), f"{m_path} does not exist"
    content = f.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)
    assert fm is not None, f"{m_path} missing frontmatter"
    assert fm.get("status") == "active", f"{m_path} status not active: {fm.get('status')}"
    links = extract_wikilinks(content)
    print(f"[{m_path}] Size: {len(content)} bytes, Links: {len(links)}, Frontmatter type: {fm.get('type')}")

print("ALL PARA MOCS VERIFIED OK!")
