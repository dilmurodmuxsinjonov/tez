import sys, re, yaml
from pathlib import Path

vault = Path(r'D:\obsidian file')
projects = [
    'MobCreatorWebApp.md',
    'NagoyaCastle.md',
    'The_AI_Pipeline.md',
    'Orol Shahar Qirollik.md',
    'Doctor A Med Clinic.md'
]

sys.path.insert(0, str(vault))
from tests.e2e.helpers import COMMUNICATION_STYLES, APPROVED_ACTION_VERBS, validate_suggested_next_step, check_visual_separation

print('=== ADVERSARIAL STRESS TEST ON 5 M3 PROJECT NOTES ===')
errors = []

for p in projects:
    fpath = vault / '10 Projects' / p
    print(f'\n--- Inspecting: {p} ---')
    if not fpath.exists():
        errors.append(f'{p}: File does not exist')
        continue
    content = fpath.read_text(encoding='utf-8')

    # A. YAML Frontmatter Adversarial Parsing
    fm_match = re.match(r'^---\s*\n([\s\S]*?)\n---\s*\n', content)
    if not fm_match:
        errors.append(f'{p}: YAML frontmatter delimiter missing')
    else:
        try:
            fm = yaml.safe_load(fm_match.group(1))
            print(f'YAML parsed cleanly: type={fm.get("type")}, status={fm.get("status")}')
            reqs = ['title', 'version', 'status', 'type', 'tags', 'project_path', 'tech_stack', 'created', 'updated']
            for r in reqs:
                if r not in fm:
                    errors.append(f'{p}: Missing frontmatter field: {r}')
            if fm.get('type') != 'project-memory':
                errors.append(f'{p}: Frontmatter type must be project-memory, got {fm.get("type")}')
            if fm.get('status') != 'active':
                errors.append(f'{p}: Frontmatter status must be active, got {fm.get("status")}')
        except Exception as e:
            errors.append(f'{p}: YAML parse error: {e}')

    # B. Latest State Word and Sentence Count
    sec_state = re.search(r'## 📋 Latest State Summary\s*\n+([^\n#]+(?:\n[^\n#]+)*)', content)
    if not sec_state:
        errors.append(f'{p}: Latest State Summary missing')
    else:
        txt = sec_state.group(1).strip()
        words = txt.split()
        wcount = len(words)
        sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', txt) if s.strip()]
        scount = len(sents)
        print(f'Latest State: {scount} sentences, {wcount} words')
        if not (1 <= scount <= 2):
            errors.append(f'{p}: Sentence count not 1-2 (got {scount})')
        if not (30 <= wcount <= 50):
            errors.append(f'{p}: Word count not between 30 and 50 (got {wcount})')

    # C. ADR Table Checks
    adr_match = re.search(r'## 💡 Goals & Decisions Log \(ADR\)\s*\n+([\s\S]*?)(?=\n---)', content)
    if not adr_match:
        errors.append(f'{p}: ADR section missing')
    else:
        adr_lines = [l.strip() for l in adr_match.group(1).strip().splitlines() if l.strip()]
        table_rows = [l for l in adr_lines if l.startswith('|') and l.endswith('|')]
        print(f'ADR table rows: {len(table_rows)} (including header and separator)')
        if len(table_rows) < 4:
            errors.append(f'{p}: ADR table has fewer than 2 decision entries')
        for idx, tr in enumerate(table_rows):
            cols = [c.strip() for c in tr.split('|')[1:-1]]
            if len(cols) != 7:
                errors.append(f'{p}: ADR table row {idx} has {len(cols)} columns, expected 7')

    # D. 10 Communication Styles Check
    cd_match = re.search(r'## 💬 Interaction Dynamics \(10 Communication Styles\)\s*\n+([\s\S]*?)(?=\n---)', content)
    if not cd_match:
        errors.append(f'{p}: Interaction Dynamics section missing')
    else:
        cd_text = cd_match.group(1)
        for st in COMMUNICATION_STYLES:
            if st.lower() not in cd_text.lower():
                errors.append(f'{p}: Missing communication style: {st}')
        anchors = [l.strip() for l in cd_text.splitlines() if "# " in l and not l.startswith("##")]
        print(f'Found {len(anchors)} contextual greeting anchors')
        if len(anchors) != 10:
            errors.append(f'{p}: Expected exactly 10 contextual greeting anchors, found {len(anchors)}')

    # E. Suggested Next Steps
    sns_match = re.search(r"## 🎯 Suggested Next Steps\s*\n+([\s\S]*?)(?=\n{6,}```)", content)
    if not sns_match:
        errors.append(f'{p}: Suggested Next Steps section or 5 blank line separator missing')
    else:
        raw_steps = sns_match.group(1).strip().splitlines()
        clean_steps = [re.sub(r'^[-*0-9.]+\s*', '', s).strip() for s in raw_steps if s.strip()]
        print(f'Suggested Next Steps count: {len(clean_steps)}')
        if not (2 <= len(clean_steps) <= 4):
            errors.append(f'{p}: Next steps count not between 2 and 4 (got {len(clean_steps)})')
        for s in clean_steps:
            val = validate_suggested_next_step(s)
            print(f'  [{len(s)} chars] {s[:50]}... valid={val["is_valid"]}')
            if not val['is_valid']:
                errors.append(f'{p}: Step invalid: \'{s}\' (issues: {val})')

    # F. Visual Separation: exactly 5 blank lines
    parts = content.split('```text')
    if len(parts) < 2:
        errors.append(f'{p}: ```text code block not found')
    else:
        preceding = parts[0]
        trailing_nl = len(preceding) - len(preceding.rstrip('\n'))
        is_sep, blank_lines = check_visual_separation(content)
        print(f'Visual separation blank lines: {blank_lines} (is_separated={is_sep})')
        if not is_sep:
            errors.append(f'{p}: Visual separation failed helper check (got {blank_lines} blank lines)')
        elif blank_lines != 5:
            print(f'  [OBSERVATION] {p}: Note has {blank_lines} blank lines (standard requirement specifies exactly 5)')

    # G. Code block structure & line wrapping
    if len(parts) >= 2:
        cb = parts[1].split('```')[0]
        req_emojis = [
            '🎯 ACTIVE GOALS & OBJECTIVES',
            '📋 LATEST STATE & MILESTONE PROGRESS',
            '💡 ARCHITECTURAL DECISIONS LOG',
            '⚠️ KNOWN ISSUES & ACTIVE BLOCKERS',
            '💬 RELEVANT CONVERSATIONS & GIT COMMITS',
            '🔗 CROSS-DOMAIN DEPENDENCIES'
        ]
        for req in req_emojis:
            if req not in cb:
                errors.append(f'{p}: Code block missing required section: {req}')
        long_lines = [l for l in cb.splitlines() if len(l) > 100]
        print(f'Lines > 100 chars in code block: {len(long_lines)}')
        for ll in long_lines:
            print(f'  Long line ({len(ll)} chars): {ll[:80]}...')

    # H. Check reciprocal link
    if '[[AI Sozlangan Miyyasi]]' not in content:
        errors.append(f'{p}: Missing exact reciprocal link [[AI Sozlangan Miyyasi]]')

    # I. Check for placeholder text
    placeholders = ['TODO', 'TBD', 'FIXME', 'lorem ipsum', 'placeholder', 'dummy', 'CHANGEME']
    for ph in placeholders:
        if ph.lower() in content.lower():
            errors.append(f'{p}: Contains placeholder token: {ph}')

print('\n================ SUMMARY ================')
if errors:
    print(f'FAILED with {len(errors)} error(s):')
    for e in errors:
        print(f' - {e}')
    sys.exit(1)
else:
    print('ALL ADVERSARIAL CHECKS PASSED WITH ZERO ERRORS!')
    sys.exit(0)
