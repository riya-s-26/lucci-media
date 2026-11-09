import os
import re

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

referenced_assets = set()
referenced_pages = set()

# Regex patterns for finding asset references
patterns = [
    r'(?:src|href)=["\']([^"\']+)["\']',
    r'url\(["\']?([^"\'\)]+)["\']?\)',
    r'["\'](assets/[^"\']+)["\']',
    r'["\'](assets\\[^"\']+)["\']',
]

for pf in prod_files:
    if not os.path.exists(pf):
        continue
    with open(pf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    for pat in patterns:
        for match in re.findall(pat, content):
            # clean query params like ?v=26.0 or #hash
            clean = match.split('?')[0].split('#')[0].replace('\\', '/')
            if clean.startswith('assets/'):
                referenced_assets.add(clean)
            elif clean.endswith(('.html', '.css', '.js', '.png', '.jpg', '.jpeg', '.webp', '.mp4', '.woff', '.woff2')):
                if not clean.startswith('http') and not clean.startswith('//'):
                    referenced_pages.add(clean)

print("=== REFERENCED IN PRODUCTION FILES ===")
print(f"Total production files: {len(prod_files)}")
print(f"Total referenced assets: {len(referenced_assets)}")
for a in sorted(referenced_assets):
    print("  ASSET:", a, "EXISTS?", os.path.exists(a))

print(f"\nTotal referenced pages/scripts/styles: {len(referenced_pages)}")
for p in sorted(referenced_pages):
    print("  PAGE/FILE:", p, "EXISTS?", os.path.exists(p))

