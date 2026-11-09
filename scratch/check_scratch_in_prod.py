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

found = []
for pf in prod_files:
    if os.path.exists(pf):
        with open(pf, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        for idx, line in enumerate(lines):
            if 'scratch' in line.lower():
                found.append((pf, idx + 1, line.strip()))

print(f"Total occurrences of 'scratch' in production files: {len(found)}")
for pf, line_no, line in found:
    print(f"  {pf}:{line_no}: {line}")

