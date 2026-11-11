import os
import re

prod_files = [
    'index.html', 'about.html', 'coming-soon.html', 'services.html',
    'the-work.html', 'our-studio.html', 'inquire.html',
    'styles.css', 'about.css', 'coming-soon.css', 'script.js', '.htaccess'
]

prod_content = ""
for p in prod_files:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            prod_content += f.read() + "\n"

# Also check for basenames
assets = []
for dirpath, dirnames, filenames in os.walk('assets'):
    for f in filenames:
        rel = os.path.relpath(os.path.join(dirpath, f), '.').replace('\\', '/')
        assets.append(rel)

print(f"Total assets: {len(assets)}")

used_assets = []
unused_assets = []

for a in assets:
    # check full path or basename or URL encoded
    basename = os.path.basename(a)
    url_encoded = a.replace(' ', '%20')
    base_encoded = basename.replace(' ', '%20')
    
    if (a in prod_content or 
        basename in prod_content or 
        url_encoded in prod_content or 
        base_encoded in prod_content):
        used_assets.append(a)
    else:
        unused_assets.append(a)

print(f"Used assets: {len(used_assets)}")
print(f"Unused assets: {len(unused_assets)}")

print("\n--- UNUSED ASSETS IN assets/ ---")
for u in unused_assets:
    size = os.path.getsize(u)
    print(f"  {u:45} | {size:>8} bytes")

