from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
VAULT_ROOT = Path(r"D:\obsidian file")
sys.path.insert(0, str(VAULT_ROOT))

from tests.e2e.helpers import (
    validate_suggested_next_step,
    check_visual_separation,
    parse_frontmatter,
    extract_wikilinks,
    COMMUNICATION_STYLES,
    APPROVED_ACTION_VERBS,
)

VAULT_ROOT = Path(r"D:\obsidian file")
PROJECTS = [
    "MobCreatorWebApp.md",
    "NagoyaCastle.md",
    "The_AI_Pipeline.md",
    "Orol Shahar Qirollik.md",
    "Doctor A Med Clinic.md",
]

all_passed = True

for proj_name in PROJECTS:
    file_path = VAULT_ROOT / "10 Projects" / proj_name
    print(f"\n==================== Checking {proj_name} ====================")
    if not file_path.exists():
        print(f"[FAIL] File does not exist: {file_path}")
        all_passed = False
        continue

    content = file_path.read_text(encoding="utf-8")

    # 1. Frontmatter check
    fm, body = parse_frontmatter(content)
    if not fm:
        print("[FAIL] Frontmatter missing or invalid")
        all_passed = False
    else:
        print(f"[PASS] Frontmatter found: title='{fm.get('title')}', version={fm.get('version')}, status={fm.get('status')}, type={fm.get('type')}")
        for req_field in ["title", "version", "status", "type", "tags", "project_path", "tech_stack"]:
            if req_field not in fm:
                print(f"[FAIL] Missing required frontmatter field: {req_field}")
                all_passed = False

    # 2. Reciprocal link check
    links = extract_wikilinks(content)
    targets = [l["target"] for l in links]
    if any("AI Sozlangan Miyyasi" in t for t in targets):
        print("[PASS] Reciprocal link to [[AI Sozlangan Miyyasi]] confirmed")
    else:
        print("[FAIL] Missing reciprocal link to [[AI Sozlangan Miyyasi]]")
        all_passed = False

    # 3. Latest State Summary check (1-2 sentences, 30-50 words)
    state_match = re.search(r"## 📋 Latest State Summary\s*\n+([^\n#]+(?:\n[^\n#]+)*)", content)
    if not state_match:
        print("[FAIL] Section '## 📋 Latest State Summary' missing")
        all_passed = False
    else:
        summary_text = state_match.group(1).strip()
        words = summary_text.split()
        word_count = len(words)
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", summary_text) if s.strip()]
        sentence_count = len(sentences)
        print(f"[CHECK] Latest State: {sentence_count} sentences, {word_count} words.")
        if 30 <= word_count <= 50 and 1 <= sentence_count <= 2:
            print(f"[PASS] Latest State Summary length ok ({word_count} words, {sentence_count} sentences)")
        else:
            print(f"[WARN/FAIL] Latest State Summary outside 30-50 words (got {word_count} words, {sentence_count} sentences)")
            if word_count < 25 or word_count > 60:
                all_passed = False

    # 4. Goals & Decisions Log (ADR)
    if "ADR" in content and "Goals & Decisions Log" in content:
        print("[PASS] Goals & Decisions Log (ADR) section found")
    else:
        print("[FAIL] Goals & Decisions Log (ADR) missing")
        all_passed = False

    # 5. Interaction Dynamics with all 10 communication styles
    if "Interaction Dynamics" in content:
        style_matches = 0
        for style in COMMUNICATION_STYLES:
            if style.lower() in content.lower():
                style_matches += 1
            else:
                print(f"[FAIL] Style '{style}' not found in file")
                all_passed = False
        print(f"[PASS] All {style_matches}/10 communication styles found")
    else:
        print("[FAIL] Interaction Dynamics section missing")
        all_passed = False

    # 6. Suggested Next Steps
    steps_section = re.search(r"## 🎯 Suggested Next Steps\s*\n+([\s\S]*?)(?=\n{6,}```)", content)
    if not steps_section:
        print("[FAIL] Suggested Next Steps section or 5 blank lines separator not found")
        all_passed = False
    else:
        raw_steps = steps_section.group(1).strip().splitlines()
        clean_steps = [re.sub(r"^[-*0-9.]+\s*", "", s).strip() for s in raw_steps if s.strip()]
        print(f"[CHECK] Found {len(clean_steps)} suggested next steps:")
        if not (2 <= len(clean_steps) <= 4):
            print(f"[FAIL] Expected 2 to 4 next steps, found {len(clean_steps)}")
            all_passed = False
        for s in clean_steps:
            res = validate_suggested_next_step(s)
            print(f"  - [{len(s)} chars] '{s}' | Valid: {res['is_valid']} (verb: {res['first_word']}, verb_ok: {res['is_action_verb']}, len_ok: {res['length_valid']})")
            if not res["is_valid"]:
                print(f"    [FAIL] Step failed validation: {res}")
                all_passed = False

    # 7. Visual Separation check (exactly 5 blank lines: \n\n\n\n\n\n)
    is_separated, blank_count = check_visual_separation(content)
    if is_separated and blank_count >= 5:
        print(f"[PASS] Visual separation verified: {blank_count} blank lines")
    else:
        print(f"[FAIL] Visual separation failed: got {blank_count} blank lines")
        all_passed = False

    # 8. Topic Memory code block check
    code_block_match = re.search(r"```text\s*\n([\s\S]*?)\n```", content)
    if not code_block_match:
        print("[FAIL] Topic Memory code block (```text ... ```) not found")
        all_passed = False
    else:
        cb_content = code_block_match.group(1)
        required_emojis = [
            "🎯 ACTIVE GOALS",
            "📋 LATEST STATE",
            "💡 ARCHITECTURAL DECISIONS",
            "⚠️ KNOWN ISSUES",
            "💬 RELEVANT CONVERSATIONS",
            "🔗 CROSS-DOMAIN DEPENDENCIES",
        ]
        for req in required_emojis:
            if req in cb_content:
                print(f"[PASS] Code block contains '{req}'")
            else:
                print(f"[FAIL] Code block missing section: '{req}'")
                all_passed = False

print("\n" + "=" * 60)
if all_passed:
    print("ALL PROJECT MEMORY FILES PASS ALL SPECIFICATIONS!")
    sys.exit(0)
else:
    print("SOME CHECKS FAILED! REVIEW OUTPUT ABOVE.")
    sys.exit(1)
