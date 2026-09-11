import re
import sys
from pathlib import Path

vault = Path(r"D:\obsidian file")

# Test cases
samples = [
    "[[00 Inbox/00 Inbox|00 Inbox]]",
    "[[00 Inbox/00 Inbox\\|00 Inbox]]",
    "[[AI Sozlangan Miyyasi#Heading|Alias]]",
    "[[AI Sozlangan Miyyasi#Heading\\|Alias]]",
    "[[AI Sozlangan Miyyasi#Heading (Subtitle)\\|Alias]]",
    "[[SimpleNote]]",
    "[[Folder/Subnote]]",
    "![[Image.png]]",
    "![[Image.png\\|300]]"
]

# Regex 1: current in validate_vault.py
r1 = re.compile(r'!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')

# Regex 2: excluding backslash or stripping
r2 = re.compile(r'!?\[\[([^\]|#\\]+)(?:#[^\]|\\]*)?(?:\\?\|[^\]]*)?\]\]')

# Regex 3: general extraction then clean
r3 = re.compile(r'!?\[\[([^\]\r\n]+)\]\]')

print("--- REGEX 1 (Current) ---")
for s in samples:
    m = r1.search(s)
    print(f"{s} -> group(1): {m.group(1) if m else None}")

print("\n--- REGEX 2 (Excluding backslash) ---")
for s in samples:
    m = r2.search(s)
    print(f"{s} -> group(1): {m.group(1) if m else None}")

print("\n--- PARSER FUNCTION (General & Clean) ---")
def parse_link(s):
    m = r3.search(s)
    if not m: return None
    inner = m.group(1).strip()
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
    return {"target": target, "anchor": anchor, "alias": alias}

for s in samples:
    print(f"{s} -> {parse_link(s)}")
