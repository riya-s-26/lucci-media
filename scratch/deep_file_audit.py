import os

prod_files = [
    'index.html',
    'about.html',
    'coming-soon.html',
    'services.html',
    'the-work.html',
    'our-studio.html',
    'inquire.html',
    'styles.css',
    'about.css',
    'coming-soon.css',
    'script.js',
    'README.md'
]

# Read all production code to build a comprehensive string pool for exact references
prod_code = {}
for pf in prod_files:
    if os.path.exists(pf):
        with open(pf, 'r', encoding='utf-8', errors='ignore') as f:
            prod_code[pf] = f.read()

combined_prod_text = "\n".join(prod_code.values())

workspace_files = []
for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        p = os.path.join(root, f).replace('\\', '/')
        if p.startswith('./'):
            p = p[2:]
        workspace_files.append(p)

print(f"Total workspace files: {len(workspace_files)}")

# Check references for every file
ref_map = {}
for wf in workspace_files:
    # check basename and full path
    base = os.path.basename(wf)
    path_clean = wf.replace('\\', '/')
    is_ref = (path_clean in combined_prod_text) or (base in combined_prod_text and not wf.startswith('scratch/'))
    ref_map[wf] = is_ref

# Group by directory / role
print("\n--- ROOT FILES ---")
for wf in sorted([f for f in workspace_files if '/' not in f]):
    print(f"  {wf:30} Size: {os.path.getsize(wf):8} bytes | Ref'd: {ref_map[wf]}")

print("\n--- ASSETS FILES ---")
for wf in sorted([f for f in workspace_files if f.startswith('assets/')]):
    print(f"  {wf:45} Size: {os.path.getsize(wf):8} bytes | Ref'd: {ref_map[wf]}")

print("\n--- SCRATCH FILES ---")
scratch_files = [f for f in workspace_files if f.startswith('scratch/')]
print(f"Total scratch files: {len(scratch_files)}")

