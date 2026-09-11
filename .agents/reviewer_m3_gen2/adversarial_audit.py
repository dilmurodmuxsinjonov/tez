import os
import sys
import re
from pathlib import Path

VAULT_ROOT = Path(r"D:\obsidian file")
PROJECTS = [
    "MobCreatorWebApp.md",
    "NagoyaCastle.md",
    "The_AI_Pipeline.md",
    "Orol Shahar Qirollik.md",
    "Doctor A Med Clinic.md",
]

APPROVED_ACTION_VERBS = {
    "Review", "Inspect", "Refactor", "Draft", "Implement", "Audit",
    "Benchmark", "Verify", "Integrate", "Configure", "Test", "Document",
    "Extract", "Optimize", "Deploy", "Analyze", "Update", "Design",
    "Compile", "Validate", "Secure", "Align", "Migrate", "Build"
}

COMMUNICATION_STYLES = [
    "Thoughtful check-in",
    "Progress celebration",
    "Reflection prompt",
    "Callback to detail",
    "Invitation to continue",
    "Anticipation builder",
    "Gentle nudge",
    "Curiosity spark",
    "Empathetic acknowledgment",
    "Low-pressure opener"
]

REQUIRED_CODE_BLOCK_SECTIONS = [
    "🎯 ACTIVE GOALS & OBJECTIVES",
    "📋 LATEST STATE & MILESTONE PROGRESS",
    "💡 ARCHITECTURAL DECISIONS LOG",
    "⚠️ KNOWN ISSUES & ACTIVE BLOCKERS",
    "💬 RELEVANT CONVERSATIONS & GIT COMMITS",
    "🔗 CROSS-DOMAIN DEPENDENCIES",
]

EXPECTED_ADR_HEADER = ["Sana", "ADR ID", "Decision & Scope", "Rationale", "Alternatives", "Holat", "Muallif"]

print("=" * 80)
print("INDEPENDENT ADVERSARIAL AUDIT OF 5 ACTIVE PROJECT NOTES")
print("=" * 80)

failures = []
greetings_seen = set()

for proj in PROJECTS:
    p = VAULT_ROOT / "10 Projects" / proj
    print(f"\n--- Auditing {proj} ---")
    if not p.exists():
        failures.append(f"{proj}: File does not exist")
        continue

    raw_bytes = p.read_bytes()
    if raw_bytes.startswith(b"\xef\xbb\xbf"):
        failures.append(f"{proj}: Contains UTF-8 BOM")
    try:
        content = raw_bytes.decode("utf-8")
    except Exception as e:
        failures.append(f"{proj}: UTF-8 decode error: {e}")
        continue

    # 1. Frontmatter
    if not content.startswith("---\n"):
        failures.append(f"{proj}: Does not start with --- frontmatter")
    parts = content.split("---", 2)
    if len(parts) < 3:
        failures.append(f"{proj}: Incomplete frontmatter block")
    else:
        fm_text = parts[1]
        for field in ["title", "version: 1.0.0", "status: active", "type: project-memory", "project_path", "tech_stack"]:
            if field not in fm_text:
                failures.append(f"{proj}: Missing frontmatter field or value '{field}'")
        
        # Check if project_path physically exists on the machine (Integrity check)
        m_path = re.search(r'project_path:\s*"(.*?)"', fm_text)
        if m_path:
            raw_path = m_path.group(1).replace("\\\\", "\\")
            disk_path = Path(raw_path)
            exists = disk_path.exists()
            print(f"  [Integrity] Physical project path exists: {exists} ({disk_path})")
            if not exists:
                print(f"  [WARN] Path does not exist on disk: {disk_path}")

    # 2. Reciprocal link
    if "[[AI Sozlangan Miyyasi]]" not in content:
        failures.append(f"{proj}: Missing reciprocal link [[AI Sozlangan Miyyasi]]")
    else:
        # Check header link
        if "> Master Brain Entrypoint: [[AI Sozlangan Miyyasi]]" not in content:
            failures.append(f"{proj}: Missing standard blockquote reciprocal link")
        if "- Master Brain: [[AI Sozlangan Miyyasi]]" not in content:
            failures.append(f"{proj}: Missing code block reciprocal link")

    # 3. Latest State Summary
    lss_match = re.search(r"## 📋 Latest State Summary\s*\n+([^\n#]+(?:\n[^\n#]+)*)", content)
    if not lss_match:
        failures.append(f"{proj}: Missing '## 📋 Latest State Summary' section")
    else:
        lss_text = lss_match.group(1).strip()
        words = lss_text.split()
        word_count = len(words)
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", lss_text) if s.strip()]
        sentence_count = len(sentences)
        print(f"  [LSS] Words: {word_count}, Sentences: {sentence_count}")
        if not (30 <= word_count <= 50):
            failures.append(f"{proj}: Latest State Summary word count {word_count} outside 30-50 bounds")
        if not (1 <= sentence_count <= 2):
            failures.append(f"{proj}: Latest State Summary sentence count {sentence_count} outside 1-2 bounds")

    # 4. Goals & Decisions Log (ADR)
    adr_match = re.search(r"## 💡 Goals & Decisions Log \(ADR\)\s*\n+([\s\S]*?)(?=\n---|\n## )", content)
    if not adr_match:
        failures.append(f"{proj}: Missing '## 💡 Goals & Decisions Log (ADR)' section")
    else:
        adr_block = adr_match.group(1).strip()
        table_lines = [l.strip() for l in adr_block.splitlines() if l.strip().startswith("|")]
        if len(table_lines) < 3:
            failures.append(f"{proj}: ADR table has fewer than 3 lines (header, sep, rows)")
        else:
            header_cols = [c.strip() for c in table_lines[0].split("|")[1:-1]]
            if header_cols != EXPECTED_ADR_HEADER:
                failures.append(f"{proj}: ADR table header mismatch. Got {header_cols}, expected {EXPECTED_ADR_HEADER}")
            data_rows = table_lines[2:]
            print(f"  [ADR] Rows found: {len(data_rows)}")
            if len(data_rows) < 3:
                failures.append(f"{proj}: ADR table has fewer than 3 decision entries")
            for row_idx, r in enumerate(data_rows):
                cols = [c.strip() for c in r.split("|")[1:-1]]
                if len(cols) != 7:
                    failures.append(f"{proj}: ADR row {row_idx+1} has {len(cols)} columns, expected 7")

    # 5. Interaction Dynamics
    id_match = re.search(r"## 💬 Interaction Dynamics \(10 Communication Styles\)\s*\n+([\s\S]*?)(?=\n---|\n## )", content)
    if not id_match:
        failures.append(f"{proj}: Missing '## 💬 Interaction Dynamics (10 Communication Styles)' section")
    else:
        id_text = id_match.group(1)
        for idx, style in enumerate(COMMUNICATION_STYLES, 1):
            if style.lower() not in id_text.lower():
                failures.append(f"{proj}: Missing style '{style}'")
            # Check for greeting anchor `# <Greeting Text>`
            pattern = re.compile(rf"{idx}\.\s+\*\*{re.escape(style)}\*\*.*?\n\s+`# ([^`]+)`", re.DOTALL)
            g_match = pattern.search(id_text)
            if not g_match:
                failures.append(f"{proj}: Style {idx} ({style}) missing `# <Greeting Text>` anchor format")
            else:
                greeting = g_match.group(1).strip()
                if greeting in greetings_seen:
                    failures.append(f"{proj}: Duplicate greeting across projects: '{greeting}'")
                greetings_seen.add(greeting)
        print(f"  [Interaction Dynamics] 10 styles verified with unique `# <Greeting Text>` anchors")

    # 6. Suggested Next Steps
    sns_match = re.search(r"## 🎯 Suggested Next Steps\s*\n+([\s\S]*?)(?=\n{6,}```text)", content)
    if not sns_match:
        failures.append(f"{proj}: Suggested Next Steps section or separator not matching pattern")
    else:
        raw_steps = [l.strip() for l in sns_match.group(1).strip().splitlines() if l.strip()]
        clean_steps = [re.sub(r"^[-*0-9.]+\s*", "", s).strip() for s in raw_steps]
        print(f"  [Next Steps] Found {len(clean_steps)} items:")
        if not (2 <= len(clean_steps) <= 4):
            failures.append(f"{proj}: Step count {len(clean_steps)} outside 2-4 bounds")
        for s in clean_steps:
            s_len = len(s)
            first_w = re.sub(r"[^a-zA-Z]", "", s.split()[0])
            is_verb = first_w in APPROVED_ACTION_VERBS
            len_ok = 60 <= s_len <= 85
            print(f"    '{s}' ({s_len} chars, verb: {first_w}, ok: {is_verb and len_ok})")
            if not len_ok:
                failures.append(f"{proj}: Step length {s_len} outside 60-85 bounds: '{s}'")
            if not is_verb:
                failures.append(f"{proj}: First word '{first_w}' not in approved action verbs: '{s}'")

    # 7. Visual Separation check (strictly 5 blank lines)
    sep_pattern = re.compile(r"(\r?\n[ \t]*){6,}```text")
    sep_m = sep_pattern.search(content)
    if not sep_m:
        failures.append(f"{proj}: Visual separation before ```text failed (did not find >= 6 newlines)")
    else:
        newline_count = len(re.findall(r"\n", sep_m.group(0)))
        blank_lines = newline_count - 1
        print(f"  [Separation] Blank lines count: {blank_lines}")
        if blank_lines != 5:
            failures.append(f"{proj}: Visual separation must be EXACTLY 5 blank lines, found {blank_lines}")

    # 8. Topic Memory Code Block
    cb_match = re.search(r"```text\s*\n([\s\S]*?)\n```", content)
    if not cb_match:
        failures.append(f"{proj}: Missing ```text ... ``` code block")
    else:
        cb_text = cb_match.group(1)
        for sec in REQUIRED_CODE_BLOCK_SECTIONS:
            if sec not in cb_text:
                failures.append(f"{proj}: Code block missing section '{sec}'")
        
        # Check line lengths <= 80 characters
        cb_lines = cb_text.splitlines()
        long_lines = [(i+1, l, len(l)) for i, l in enumerate(cb_lines) if len(l) > 80]
        max_len = max(len(l) for l in cb_lines) if cb_lines else 0
        print(f"  [Code Block] Lines: {len(cb_lines)}, Max line length: {max_len}")
        if long_lines:
            for l_num, l_val, l_len in long_lines:
                failures.append(f"{proj}: Code block line {l_num} exceeds 80 chars ({l_len} chars): '{l_val[:40]}...'")

print("\n" + "=" * 80)
print("AUDIT SUMMARY")
print("=" * 80)
if failures:
    print(f"FAILED: {len(failures)} issues found:")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
else:
    print("SUCCESS: 100% OF CHECKS PASSED WITH ZERO FAILURES!")
    sys.exit(0)
