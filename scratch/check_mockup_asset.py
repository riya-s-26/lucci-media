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

matches = []
for pf in prod_files:
    if os.path.exists(pf):
        with open(pf, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        if 'mockup_corrected' in content:
            matches.append(pf)

print(f"Target 'mockup_corrected' found in: {matches}")

