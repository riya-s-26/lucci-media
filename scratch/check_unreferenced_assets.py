import os

# Find all files in assets/
all_assets = []
for root, dirs, files in os.walk('assets'):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), '.').replace('\\', '/')
        all_assets.append(rel)

print(f"Total files in assets/: {len(all_assets)}")

# Cross-reference with our audit_references
with open('scratch/audit_references.py', 'r') as f:
    pass

import subprocess
res = subprocess.run(['python', 'scratch/audit_references.py'], capture_output=True, text=True)
ref_lines = [line.split('ASSET: ')[1].split(' EXISTS?')[0].strip() for line in res.stdout.splitlines() if 'ASSET: ' in line]
ref_set = set(ref_lines)

unreferenced = [a for a in all_assets if a not in ref_set]
print(f"\nUnreferenced files in assets/ ({len(unreferenced)}):")
for u in sorted(unreferenced):
    print(" ", u, f"({os.path.getsize(u)} bytes)")

