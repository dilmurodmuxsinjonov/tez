import os
import re
import sys
import yaml
from pathlib import Path

vault_root = Path(r"D:\obsidian file")

print("=== STARTING PHASE 1 & 2 AUDIT ===")

# 1. R1: Agent profiles & Resource Guides
expected_agents = [
    "Nous Hermes.md",
    "GitHub Copilot.md",
    "OpenCode CLI.md",
    "Google Antigravity CLI.md",
    "Ruflo Swarm.md"
]
agent_dir = vault_root / "20 Areas" / "Agent Profiles"
agent_results = {}
for agent in expected_agents:
    p = agent_dir / agent
    exists = p.exists()
    size = p.stat().st_size if exists else 0
    content = p.read_text(encoding='utf-8') if exists else ""
    has_backlink = "[[AI Sozlangan Miyyasi]]" in content
    # YAML check
    yaml_valid = False
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                parsed = yaml.safe_load(parts[1])
                yaml_valid = isinstance(parsed, dict)
            except Exception as e:
                yaml_valid = False
    agent_results[agent] = {
        "exists": exists,
        "size": size,
        "has_backlink": has_backlink,
        "yaml_valid": yaml_valid
    }

print("Agent Profiles Check:")
for k, v in agent_results.items():
    print(f"  {k}: exists={v['exists']}, size={v['size']} bytes, backlink={v['has_backlink']}, yaml_valid={v['yaml_valid']}")

expected_resources = [
    "AI Agent Ecosystem Map.md",
    "Free LLM Models Registry.md",
    "Codex Skills Encyclopedia.md"
]
resource_dir = vault_root / "30 Resources"
resource_results = {}
for res in expected_resources:
    p = resource_dir / res
    exists = p.exists()
    size = p.stat().st_size if exists else 0
    content = p.read_text(encoding='utf-8') if exists else ""
    has_backlink = "[[AI Sozlangan Miyyasi]]" in content
    yaml_valid = False
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                parsed = yaml.safe_load(parts[1])
                yaml_valid = isinstance(parsed, dict)
            except Exception as e:
                yaml_valid = False
    resource_results[res] = {
        "exists": exists,
        "size": size,
        "has_backlink": has_backlink,
        "yaml_valid": yaml_valid,
        "content": content
    }

print("\nResource Guides Check:")
for k, v in resource_results.items():
    print(f"  {k}: exists={v['exists']}, size={v['size']} bytes, backlink={v['has_backlink']}, yaml_valid={v['yaml_valid']}")

# Check 20+ models in Free LLM Models Registry
models_content = resource_results["Free LLM Models Registry.md"]["content"]
# Count table rows or model entries
# Typically models are in markdown tables or bullet points
model_rows = [line for line in models_content.splitlines() if line.strip().startswith("|") and not line.strip().startswith("|---") and not "Model Name" in line and not "Provider" in line]
print(f"  Free LLM Models Registry table rows / entries: {len(model_rows)}")

# Check 14 skills in Codex Skills Encyclopedia
skills_content = resource_results["Codex Skills Encyclopedia.md"]["content"]
# Check skills list or headings
skill_matches = re.findall(r"(?:###|####|\d+\.)\s*?([a-z0-9_]+)?", skills_content)
# Let's also check for explicit skill names from ORIGINAL_REQUEST.md
known_skills = [
    "chuqur_muhandislik", "kontekst_muhit_tarixi", "kontekst_psixologik_profil",
    "kontekst_strategik_reja", "loyihani_rejalashtirish", "loyiha_infratuzilmasi_qoidalari",
    "memor_shaxsiyati", "oq_haker_muhiti", "oq_haker_vositalari",
    "veb_dasturlash", "xavfsizlik_qoidalari", "tashqi_ai_agentlar"
]
present_known = [s for s in known_skills if s in skills_content]
print(f"  Codex Skills found in Encyclopedia: {len(present_known)}/12 known from request, total skills count in text: {skills_content.count('### ')}")

# Check MOC inclusion for all 5 agents and 3 resources
mocs = list(vault_root.glob("*/*MOC*.md")) + list(vault_root.glob("*MOC*.md")) + [vault_root / "AI Sozlangan Miyyasi.md"]
print(f"\nChecking MOC Inclusion across {len(mocs)} MOCs:")
for item in expected_agents + expected_resources:
    name_no_ext = item.replace(".md", "")
    referencing_mocs = []
    for moc in mocs:
        moc_text = moc.read_text(encoding='utf-8')
        if name_no_ext in moc_text or item in moc_text:
            referencing_mocs.append(moc.name)
    print(f"  {item}: referenced by {referencing_mocs}")

# R4: 3 production templates
templates_dir = vault_root / "50 Templates"
templates = list(templates_dir.glob("*.md"))
print(f"\nTemplates in 50 Templates ({len(templates)} found):")
for t in templates:
    print(f"  {t.name} ({t.stat().st_size} bytes)")

master_brain = vault_root / "AI Sozlangan Miyyasi.md"
master_text = master_brain.read_text(encoding='utf-8')
print("\nChecking Template links in Master Brain (AI Sozlangan Miyyasi.md):")
for t in templates:
    t_no_ext = t.name.replace(".md", "")
    linked = t_no_ext in master_text or t.name in master_text
    print(f"  {t.name}: linked in Master Brain = {linked}")

