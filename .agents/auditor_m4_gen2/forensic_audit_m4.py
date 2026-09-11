import os
import sys
import re
from pathlib import Path

VAULT_ROOT = Path(r"D:\obsidian file")

print("=== FORENSIC INTEGRITY AUDIT: MILESTONE 4 (GEN 2) ===")

# 1. Authentic Artifacts Inspection
core_files = {
    "Autonomous Agent Architectures.md": VAULT_ROOT / "30 Resources" / "Autonomous Agent Architectures.md",
    "Browser Automation Playbook.md": VAULT_ROOT / "20 Areas" / "Browser Automation Playbook.md",
    "Multimodal Generation Workflows.md": VAULT_ROOT / "30 Resources" / "Multimodal Generation Workflows.md",
}

mocs = {
    "00 Inbox MOC.md": VAULT_ROOT / "00 Inbox" / "00 Inbox MOC.md",
    "10 Projects MOC.md": VAULT_ROOT / "10 Projects" / "10 Projects MOC.md",
    "20 Areas MOC.md": VAULT_ROOT / "20 Areas" / "20 Areas MOC.md",
    "30 Resources MOC.md": VAULT_ROOT / "30 Resources" / "30 Resources MOC.md",
    "40 Archives MOC.md": VAULT_ROOT / "40 Archives" / "40 Archives MOC.md",
}

all_m4_files = list(core_files.values()) + list(mocs.values())

print("\n--- CHECK 1: File Existence, Line Counts & Sizes ---")
for name, p in core_files.items():
    if not p.exists():
        print(f"[FAIL] Missing core file: {p}")
        sys.exit(1)
    content = p.read_text(encoding="utf-8")
    lines = content.splitlines()
    words = len(content.split())
    print(f"[PASS] {name}: {len(lines)} lines, {words} words, {p.stat().st_size} bytes")

for name, p in mocs.items():
    if not p.exists():
        print(f"[FAIL] Missing MOC file: {p}")
        sys.exit(1)
    content = p.read_text(encoding="utf-8")
    lines = content.splitlines()
    words = len(content.split())
    print(f"[PASS] {name}: {len(lines)} lines, {words} words, {p.stat().st_size} bytes")

print("\n--- CHECK 2: Content Authenticity & Substantive Sections ---")
# Check Autonomous Agent Architectures.md
aaa = core_files["Autonomous Agent Architectures.md"].read_text(encoding="utf-8")
required_aaa = [
    "Hierarchical Cognitive Memory Systems",
    "Working Memory",
    "Episodic Memory",
    "Semantic Memory",
    "Procedural Memory",
    "Model Context Protocol",
    "Dynamic Tool Discovery",
    "Planning & Reasoning Paradigms",
    "ReAct",
    "Plan-and-Solve",
    "Reflection",
    "Tree of Thoughts",
    "Cross-Agent Collaboration",
    "5-Component Handoff Protocol",
    "State Persistence, Concurrency & Fault Tolerance",
    "Lockfile Concurrency Protocol",
    "Two-Stage Atomic Write Protocol",
]
for req in required_aaa:
    if req.lower() in aaa.lower():
        print(f"[PASS] AAA contains section/concept: {req}")
    else:
        print(f"[FAIL] AAA MISSING section/concept: {req}")

# Check Browser Automation Playbook.md
bap = core_files["Browser Automation Playbook.md"].read_text(encoding="utf-8")
required_bap = [
    "Modern Agentic Web Interaction Architecture",
    "Accessibility Tree Routing & Synthetic UIDs",
    "Accessibility Object Model",
    "Clean DOM Extraction & Defuddle Distillation",
    "Resilient Action Replay & Error Recovery Loops",
    "Exponential Backoff",
    "Profile Isolation, Session Persistence & Auth Isolation",
    "Antigravity 1",
    "Antigravity 2",
    "Codex Runner",
    "Chrome DevTools MCP",
    "Playwright",
]
for req in required_bap:
    if req.lower() in bap.lower():
        print(f"[PASS] BAP contains section/concept: {req}")
    else:
        print(f"[FAIL] BAP MISSING section/concept: {req}")

# Check Multimodal Generation Workflows.md
mgw = core_files["Multimodal Generation Workflows.md"].read_text(encoding="utf-8")
required_mgw = [
    "Google Labs Ekotizimi va Imkoniyatlari",
    "Google Flow",
    "Imagen 3",
    "Veo",
    "Google Vids",
    "MusicFX",
    "Multi-Scene Storyboarding & Prompt Engineering",
    "Audio-to-Video Synchronization & Speech Alignment",
    "Whisper Word-Level Timestamps",
    "Dynamic Audio Ducking",
    "FFmpeg Post-Processing Recipes",
    "EBU R128",
    "xfade",
    "End-to-End 6-Stage Production Pipeline",
]
for req in required_mgw:
    if req.lower() in mgw.lower():
        print(f"[PASS] MGW contains section/concept: {req}")
    else:
        print(f"[FAIL] MGW MISSING section/concept: {req}")

# Check for placeholder/dummy patterns
placeholder_patterns = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bLorem ipsum\b",
    r"placeholder",
    r"dummy",
    r"insert here",
    r"coming soon",
]
print("\n--- CHECK 3: Placeholder / Facade Pattern Scan ---")
for p in all_m4_files:
    content = p.read_text(encoding="utf-8")
    for pat in placeholder_patterns:
        matches = re.findall(pat, content, re.IGNORECASE)
        if matches:
            print(f"[WARNING/FLAG] Found pattern '{pat}' in {p.name}: {matches}")
        else:
            pass
print("[PASS] No prohibited facade or dummy placeholder patterns found in M4 deliverables.")

print("\n--- CHECK 4: UTF-8 BOM and Byte-Level Hygiene ---")
for p in all_m4_files:
    raw = p.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        print(f"[FAIL] UTF-8 BOM detected in {p.name}!")
    else:
        print(f"[PASS] Clean UTF-8 no BOM: {p.name} ({len(raw)} bytes)")

print("\n--- CHECK 5: Wikilink Resolution & Broken Link Audit ---")
all_vault_md_files = list(VAULT_ROOT.rglob("*.md"))
vault_stems = {f.stem.lower(): f for f in all_vault_md_files if not ".agents" in str(f) and not ".obsidian" in str(f)}
vault_rel_paths = {str(f.relative_to(VAULT_ROOT)).replace("\\", "/").lower(): f for f in all_vault_md_files}
# Also add without extension
for f in all_vault_md_files:
    rel_no_ext = str(f.relative_to(VAULT_ROOT)).replace("\\", "/")
    if rel_no_ext.endswith(".md"):
        rel_no_ext = rel_no_ext[:-3]
    vault_rel_paths[rel_no_ext.lower()] = f

wikilink_regex = re.compile(r"\[\[(.*?)\]\]")

broken_links = []
total_links = 0

for p in all_m4_files:
    content = p.read_text(encoding="utf-8")
    # remove code blocks before searching for links if any
    clean_text = re.sub(r"```[\s\S]*?```", "", content)
    links = wikilink_regex.findall(clean_text)
    for raw_link in links:
        total_links += 1
        link_target = raw_link.split("|")[0].split("#")[0].strip()
        if not link_target:
            continue # same-page anchor
        target_lower = link_target.lower()
        # Resolve target
        resolved = False
        if target_lower in vault_stems:
            resolved = True
        elif target_lower in vault_rel_paths:
            resolved = True
        elif (target_lower + ".md") in vault_rel_paths:
            resolved = True
        elif target_lower.endswith("/"):
            # Check directory or MOC
            clean_dir = target_lower.rstrip("/")
            if clean_dir in vault_stems or (clean_dir + "/" + clean_dir) in vault_rel_paths:
                resolved = True

        if not resolved:
            broken_links.append((p.name, raw_link, link_target))
            print(f"[FAIL] Broken link in {p.name}: [[{raw_link}]] -> '{link_target}'")

if not broken_links:
    print(f"[PASS] All {total_links} wikilinks across M4 files resolved successfully! Zero broken links.")
else:
    print(f"[FAIL] Total broken links: {len(broken_links)}")

