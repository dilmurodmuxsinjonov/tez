import re
import sys
import unittest
from pathlib import Path

vault = Path(r"D:\obsidian file")
sys.path.insert(0, str(vault))
sys.stdout.reconfigure(encoding="utf-8")

# 1. Test regex on proposed extract_wikilinks
def proposed_extract_wikilinks(content: str):
    links = []
    pattern = re.compile(r"(!?)\[\[([^\]\r\n]+)\]\]")
    for match in pattern.finditer(content):
        is_embed = bool(match.group(1))
        inner = match.group(2).strip()
        
        alias = None
        if "|" in inner:
            parts = re.split(r"\\?\|", inner, maxsplit=1)
            raw_target = parts[0].rstrip("\\").strip()
            alias = parts[1].strip()
        else:
            raw_target = inner
            
        anchor = None
        if "#" in raw_target:
            parts = raw_target.split("#", 1)
            target = parts[0].rstrip("\\").strip()
            anchor = parts[1].rstrip("\\").strip()
        else:
            target = raw_target.rstrip("\\").strip()
            
        links.append({
            "raw": match.group(0),
            "target": target,
            "anchor": anchor,
            "alias": alias,
            "is_embed": is_embed,
            "span": match.span()
        })
    return links

# Test cases
test_inputs = [
    "| [[00 Inbox/00 Inbox\\|00 Inbox]] |",
    "| [[10 Projects/10 Projects\\|10 Projects]] |",
    "| [[20 Areas/20 Areas\\|20 Areas]] |",
    "| [[30 Resources/30 Resources\\|30 Resources]] |",
    "| [[40 Archives/40 Archives\\|40 Archives]] |",
    "| [[30 Resources/Agent Skills/Skills Dashboard\\|Skills Dashboard]] |",
    "| [[50 Templates/Daily Note Template\\|Daily Note Template]] |",
    "| [[50 Templates/Project Template\\|Project Template]] |",
    "| [[50 Templates/Resource Template\\|Resource Template]] |",
    "[[AI Sozlangan Miyyasi#🤖 AI Agentlar Floti Indeksi (AI Agent Fleet Index)\\|🤖 AI Agentlar Floti Indeksi]]",
    "[[RegularNote]]",
    "[[RegularNote|With Alias]]",
    "[[RegularNote#Heading]]",
    "[[RegularNote#Heading|With Alias]]"
]

print("=== 1. Proposed extract_wikilinks verification ===")
for inp in test_inputs:
    res = proposed_extract_wikilinks(inp)[0]
    has_bs = "\\" in res["target"] or (res["anchor"] and "\\" in res["anchor"])
    print(f"Input: {inp[:45]:<45} -> target='{res['target']}', anchor={repr(res['anchor'])}, alias={repr(res['alias'])}, backslash={has_bs}")
    assert not has_bs, f"Failed on {inp}"

print("ALL 14 WIKILINK EXTRACTION CASES PASSED WITHOUT BACKSLASH!\n")

# 2. Test CommonMark table delimiter splitting
print("=== 2. CommonMark row splitting with escaped pipes ===")
row_sample = "| 📥 **00 Inbox** | Tezkor fikrlar qabulxonasi | [[00 Inbox/00 Inbox\\|00 Inbox]] |"
cols = [c.strip() for c in re.split(r"(?<!\\)\|", row_sample.strip())[1:-1]]
print(f"Row: {row_sample}")
print(f"Columns ({len(cols)}): {cols}")
assert len(cols) == 3, f"Expected 3 columns, got {len(cols)}"
print("COMMONMARK SPLITTING VERIFIED: EXACTLY 3 COLUMNS!\n")

# 3. Test proposed validate_vault.py regex
print("=== 3. Proposed validate_vault regex verification ===")
wikilink_regex = re.compile(r'!?\[\[([^\]|#\\]+)(?:#[^\]|\\]*)?(?:\\?\|[^\]]*)?\]\]')
for inp in test_inputs:
    m = wikilink_regex.search(inp)
    assert m is not None, f"Regex failed to match {inp}"
    target = m.group(1).rstrip("\\").strip()
    assert "\\" not in target, f"Target has backslash: {target}"
    print(f"Input: {inp[:45]:<45} -> validate_vault target='{target}'")

print("VALIDATE_VAULT REGEX VERIFIED: 100% CLEAN TARGET EXTRACTION!\n")
