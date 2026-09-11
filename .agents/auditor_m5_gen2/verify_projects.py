import re
from pathlib import Path
import sys

VAULT_ROOT = Path(r"D:\obsidian file")
sys.path.insert(0, str(VAULT_ROOT))

from tests.e2e.helpers import parse_frontmatter, validate_suggested_next_step, check_visual_separation

projects = [
    "MobCreatorWebApp",
    "NagoyaCastle",
    "The_AI_Pipeline",
    "Orol Shahar Qirollik",
    "Doctor A Med Clinic"
]

print("=== VERIFYING GEMINI TOPICS ACTIVE PROJECTS ===")
for p_name in projects:
    p_file = VAULT_ROOT / "10 Projects" / f"{p_name}.md"
    assert p_file.exists(), f"{p_name}.md missing"
    content = p_file.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)
    t = fm.get("type")
    assert t == "project-memory", f"wrong type: {t}"
    assert fm.get("status") == "active"
    
    # Check Latest State
    m_state = re.search(r"##\s*📋\s*Latest State Summary\s*\n+([^\n#]+)", content)
    assert m_state, f"Missing Latest State in {p_name}"
    words = m_state.group(1).strip().split()
    sentences = [s.strip() for s in re.split(r"[.!?]+(?:\s+|\Z)", m_state.group(1).strip()) if s.strip()]
    print(f"[{p_name}] Latest State words: {len(words)}, sentences: {len(sentences)}")
    assert 30 <= len(words) <= 50, f"Word count {len(words)} not in [30, 50]"
    assert 1 <= len(sentences) <= 2, f"Sentence count {len(sentences)} not in [1, 2]"
    
    # Check Suggested Next Steps
    m_steps = re.search(r"##\s*🎯\s*Suggested Next Steps\s*\n+([\s\S]*?)(?=\n{3,}|\Z)", content)
    assert m_steps, f"Missing steps in {p_name}"
    raw_lines = [s.strip() for s in m_steps.group(1).splitlines() if s.strip() and not s.strip().startswith("```")]
    clean_steps = [re.sub(r"^[0-9*.-]+\s*", "", s).strip() for s in raw_lines]
    print(f"[{p_name}] Steps count: {len(clean_steps)}")
    assert 2 <= len(clean_steps) <= 4
    for cs in clean_steps:
        res = validate_suggested_next_step(cs)
        print(f"   Step ({len(cs)} chars): {cs} -> {res['is_valid']}")
        assert res["is_valid"], f"Invalid step: {cs} -> {res}"
        
    # Check visual separation
    is_sep, count = check_visual_separation(content)
    print(f"[{p_name}] Visual separation blank lines: {count} -> {is_sep}")
    assert is_sep, f"Visual separation failed ({count} blank lines)"
    
    # Check topic memory block
    assert "```text" in content
    assert "🎯 ACTIVE GOALS & OBJECTIVES" in content
    assert "📋 LATEST STATE & MILESTONE PROGRESS" in content
    assert "💡 ARCHITECTURAL DECISIONS LOG" in content
    print(f"[{p_name}] Topic memory block: VERIFIED OK\n")

print("ALL 5 ACTIVE PROJECT PROFILES PASS FORENSIC AUDIT EMPIRICALLY!")
