import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))

from tests.e2e.test_tier5_adversarial import get_all_vault_markdown_files, build_vault_graph, VAULT_ROOT

files = get_all_vault_markdown_files(VAULT_ROOT)
g = build_vault_graph(VAULT_ROOT, files)

print(f"Total markdown files: {len(files)}")
print("=" * 80)
for i, (_, rel) in enumerate(files[:20], 1):
    in_c = len(g["in_links"].get(rel, []))
    out_c = len(g["out_links"].get(rel, []))
    in_from = [src for src, _ in g["in_links"].get(rel, [])]
    print(f"{i:2}. {rel:55} | in={in_c:2} | out={out_c:2} | in_from={in_from[:2]}")
