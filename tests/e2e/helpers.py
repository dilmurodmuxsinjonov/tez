"""
Universal AI Second Brain ? E2E Test Suite Helpers
Provides pure-Python parsers, validators, and utilities without third-party dependencies.
"""

from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import re
import time
from typing import Any, Dict, List, Optional, Set, Tuple

VAULT_ROOT = Path(r"D:\obsidian file")

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

ACTIVE_PROJECTS = [
    "MobCreatorWebApp",
    "NagoyaCastle",
    "The_AI_Pipeline",
    "Orol Shahar Qirollik",
    "Doctor A Med Clinic"
]

AGENT_PROFILES = [
    "Antigravity 1",
    "Antigravity 2",
    "Codex LLM Assistant",
    "Concurrency & Sync Protocol"
]

PARA_MOCS = [
    "00 Inbox",
    "10 Projects",
    "20 Areas",
    "30 Resources",
    "40 Archives"
]


def parse_frontmatter(content: str) -> Tuple[Optional[Dict[str, Any]], str]:
    if not content.startswith("---"):
        return None, content
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    
    raw_yaml = parts[1].strip()
    body = parts[2]
    
    data = {}
    current_list_key = None
    
    for line in raw_yaml.splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        
        list_match = re.match(r"^[\s]*[-*]\s+(.*)$", line)
        if list_match and current_list_key:
            val = list_match.group(1).strip().strip(chr(34) + chr(39))
            data[current_list_key].append(val)
            continue
        
        kv_match = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", line)
        if kv_match:
            k = kv_match.group(1).strip()
            v = kv_match.group(2).strip()
            if not v:
                data[k] = []
                current_list_key = k
            else:
                current_list_key = None
                v_clean = v.strip(chr(34) + chr(39))
                data[k] = v_clean
    
    return data, body


def extract_wikilinks(content: str) -> List[Dict[str, str]]:
    links = []
    pattern = re.compile(r"(!?)\[\[([^\]\r\n]+)\]\]")
    for match in pattern.finditer(content):
        is_embed = bool(match.group(1))
        inner = match.group(2).strip()
        
        alias = None
        if "|" in inner:
            parts = inner.split("|", 1)
            raw_target = parts[0].strip()
            alias = parts[1].strip()
        else:
            raw_target = inner
            
        anchor = None
        if "#" in raw_target:
            parts = raw_target.split("#", 1)
            target = parts[0].strip()
            anchor = parts[1].strip()
        else:
            target = raw_target
            
        links.append({
            "raw": match.group(0),
            "target": target,
            "anchor": anchor,
            "alias": alias,
            "is_embed": is_embed,
            "span": match.span()
        })
    return links


def resolve_wikilink(vault_path: Path, current_file: Optional[Path], target: str) -> Optional[Path]:
    if not target:
        return None
    
    norm_target = target.replace(chr(92), "/").strip()
    
    p1 = vault_path / norm_target
    if p1.is_file():
        return p1
        
    p2 = vault_path / f"{norm_target}.md"
    if p2.is_file():
        return p2
        
    for ext in [".base", ".canvas", ".png", ".jpg", ".jpeg", ".svg"]:
        p_ext = vault_path / f"{norm_target}{ext}"
        if p_ext.is_file():
            return p_ext
            
    folder_trimmed = norm_target.rstrip("/")
    p_folder_moc = vault_path / folder_trimmed / f"{Path(folder_trimmed).name}.md"
    if p_folder_moc.is_file():
        return p_folder_moc
        
    target_name = Path(norm_target).name.lower()
    for root, _, files in os.walk(vault_path):
        if ".git" in root:
            continue
        for f in files:
            f_lower = f.lower()
            if f_lower == target_name or f_lower == f"{target_name}.md":
                return Path(root) / f
                
    return None


def validate_suggested_next_step(step: str) -> Dict[str, Any]:
    s = step.strip()
    clean_step = re.sub(r"^([0-9]+\.|\*|-)\s+", "", s).strip()
    
    length = len(clean_step)
    words = clean_step.split()
    first_word = words[0] if words else ""
    first_word_clean = re.sub(r"[^a-zA-Z]", "", first_word)
    
    is_action_verb = first_word_clean in APPROVED_ACTION_VERBS
    length_valid = 60 <= length <= 85
    
    disallowed_starts = ["you should", "we need", "next step", "the team", "please", "i suggest"]
    lower_step = clean_step.lower()
    has_disallowed_start = any(lower_step.startswith(ds) for ds in disallowed_starts)
    
    is_valid = is_action_verb and length_valid and not has_disallowed_start
    
    return {
        "text": clean_step,
        "length": length,
        "first_word": first_word_clean,
        "is_action_verb": is_action_verb,
        "length_valid": length_valid,
        "has_disallowed_start": has_disallowed_start,
        "is_valid": is_valid
    }


def check_visual_separation(text: str) -> Tuple[bool, int]:
    pattern = re.compile(r"(\r?\n[ \t]*){6,}```")
    match = pattern.search(text)
    if match:
        blank_line_count = len(re.findall(r"\n", match.group(0))) - 1
        return (blank_line_count >= 5, blank_line_count)
    return (False, 0)


def check_file_utf8_clean(file_path: Path) -> Tuple[bool, Optional[str]]:
    try:
        with open(file_path, "rb") as f:
            raw = f.read()
        if raw.startswith(b"\xef\xbb\xbf"):
            return False, "Contains UTF-8 BOM"
        raw.decode("utf-8")
        return True, None
    except UnicodeDecodeError as e:
        return False, f"Unicode decode error: {e}"
    except Exception as e:
        return False, str(e)
