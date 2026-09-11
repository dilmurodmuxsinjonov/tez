import os
import re
from pathlib import Path

VAULT_ROOT = Path(r"D:\obsidian file")
PROJECT_DIR = VAULT_ROOT / "10 Projects"
FILES = [
    "MobCreatorWebApp.md",
    "NagoyaCastle.md",
    "The_AI_Pipeline.md",
    "Orol Shahar Qirollik.md",
    "Doctor A Med Clinic.md"
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

REQUIRED_EMOJIS = [
    "🎯 ACTIVE GOALS",
    "📋 LATEST STATE",
    "💡 ARCHITECTURAL DECISIONS",
    "⚠️ KNOWN ISSUES",
    "💬 RELEVANT CONVERSATIONS",
    "🔗 CROSS-DOMAIN DEPENDENCIES"
]

results = {}
all_passed = True

for f in FILES:
    p = PROJECT_DIR / f
    res = {"file": f, "errors": []}
    if not p.exists():
        res["errors"].append("File does not exist")
        results[f] = res
        all_passed = False
        continue

    raw = p.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        res["errors"].append("Contains UTF-8 BOM")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        res["errors"].append(f"UTF-8 decode failure: {e}")
        results[f] = res
        all_passed = False
        continue

    if "\ufffd" in text:
        res["errors"].append("Contains Unicode replacement character U+FFFD (corrupted text)")

    # Check frontmatter
    fm_match = re.match(r"^---\r?\n([\s\S]*?)\r?\n---", text)
    if not fm_match:
        res["errors"].append("Missing or invalid frontmatter")
    else:
        fmtext = fm_match.group(1)
        for req in ["title:", "version: 1.0.0", "status: active", "type: project-memory", "tags:", "project_path:", "tech_stack:"]:
            if req not in fmtext:
                res["errors"].append(f"Missing frontmatter requirement: {req}")

    # Check reciprocal link
    if "[[AI Sozlangan Miyyasi]]" not in text:
        res["errors"].append("Missing reciprocal link to [[AI Sozlangan Miyyasi]]")

    # Check Latest State Summary
    lss_m = re.search(r"## 📋 Latest State Summary\s*\r?\n+([^\r\n#]+(?:\r?\n[^\r\n#]+)*)", text)
    if not lss_m:
        res["errors"].append("Missing ## 📋 Latest State Summary section")
    else:
        lss = lss_m.group(1).strip()
        words = lss.split()
        wc = len(words)
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", lss) if s.strip()]
        sc = len(sentences)
        res["latest_state_wc"] = wc
        res["latest_state_sc"] = sc
        if not (30 <= wc <= 50):
            res["errors"].append(f"Latest State Summary word count out of bounds: {wc} words (expected 30-50)")
        if not (1 <= sc <= 2):
            res["errors"].append(f"Latest State Summary sentence count out of bounds: {sc} sentences (expected 1-2)")

    # Check ADR Table
    adr_m = re.search(r"\|\s*Sana\s*\|\s*ADR ID\s*\|\s*Decision & Scope\s*\|\s*Rationale\s*\|\s*Alternatives\s*\|\s*Holat\s*\|\s*Muallif\s*\|", text)
    if not adr_m:
        res["errors"].append("ADR table header does not match exact schema: | Sana | ADR ID | Decision & Scope | Rationale | Alternatives | Holat | Muallif |")
    else:
        rows = [l for l in text.splitlines() if re.match(r"\|\s*\d{4}-\d{2}-\d{2}\s*\|\s*ADR-", l)]
        res["adr_count"] = len(rows)
        if len(rows) < 3:
            res["errors"].append(f"Expected >= 3 ADR rows, found {len(rows)}")

    # Check 10 communication styles
    missing_styles = []
    for s in COMMUNICATION_STYLES:
        if s.lower() not in text.lower():
            missing_styles.append(s)
    if missing_styles:
        res["errors"].append(f"Missing communication styles: {missing_styles}")

    # Check Suggested Next Steps
    sns_m = re.search(r"## 🎯 Suggested Next Steps\s*\r?\n+([\s\S]*?)(?=\r?\n{6,}```)", text)
    if not sns_m:
        res["errors"].append("Suggested Next Steps section or 5-blank-line separator missing")
    else:
        step_lines = [re.sub(r"^\s*[-*0-9.]+\s*", "", l).strip() for l in sns_m.group(1).splitlines() if l.strip()]
        res["step_count"] = len(step_lines)
        if not (2 <= len(step_lines) <= 4):
            res["errors"].append(f"Expected 2-4 next steps, found {len(step_lines)}")
        for step in step_lines:
            w = step.split()[0] if step.split() else ""
            clean_w = re.sub(r"[^a-zA-Z]", "", w)
            if clean_w not in APPROVED_ACTION_VERBS:
                res["errors"].append(f"Step does not start with approved action verb: '{step}' (starts with {clean_w})")
            if not (60 <= len(step) <= 85):
                res["errors"].append(f"Step length outside 60-85 chars: '{step}' ({len(step)} chars)")

    # Check visual separation: exactly 5 blank lines = 6 consecutive newlines
    sep_m = re.search(r"(\r?\n[ \t]*){6,}```text", text)
    if not sep_m:
        res["errors"].append("Visual separation of >= 5 blank lines preceding ```text not found")
    else:
        blank_lines = len(re.findall(r"\n", sep_m.group(0))) - 1
        res["blank_lines"] = blank_lines
        if blank_lines != 5:
            res["errors"].append(f"Visual separation has {blank_lines} blank lines (expected exactly 5)")

    # Check code block sections & line lengths
    cb_m = re.search(r"```text\r?\n([\s\S]*?)\r?\n```", text)
    if not cb_m:
        res["errors"].append("```text ... ``` code block not found")
    else:
        cb = cb_m.group(1)
        for req_e in REQUIRED_EMOJIS:
            if req_e not in cb:
                res["errors"].append(f"Code block missing required section: {req_e}")
        cb_lines = cb.splitlines()
        long_lines = [l for l in cb_lines if len(l) > 80]
        if long_lines:
            res["errors"].append(f"{len(long_lines)} lines exceed 80 chars in code block")

    if res["errors"]:
        all_passed = False
    results[f] = res

print("=" * 80)
print("AUDITOR INDEPENDENT FORENSIC VERIFICATION RESULTS:")
print("=" * 80)
for f, r in results.items():
    print(f"\n--- {f} ---")
    print(f"  Latest State: {r.get('latest_state_sc')} sentences, {r.get('latest_state_wc')} words")
    print(f"  ADR count: {r.get('adr_count')}")
    print(f"  Step count: {r.get('step_count')}")
    print(f"  Blank lines: {r.get('blank_lines')}")
    if r["errors"]:
        print(f"  FAILED CHECKS:")
        for err in r["errors"]:
            print(f"    - {err}")
    else:
        print("  VERDICT: 100% CLEAN (All forensic checks passed)")

print("\n" + "=" * 80)
if all_passed:
    print("FINAL RESULT: ALL 5 PROJECT NOTES PASS FORENSIC VERIFICATION!")
else:
    print("FINAL RESULT: INTEGRITY VIOLATION DETECTED!")
print("=" * 80)
