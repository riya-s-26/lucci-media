import os

categories = {
    'python_scripts': [],
    'php_scripts': [],
    'powershell_scripts': [],
    'temporary_images': [],
    'html_dumps': [],
    'json_and_text': [],
    'browser_profiles': [],
    'fonts': [],
    'other': []
}

for root, dirs, files in os.walk('scratch'):
    for f in files:
        p = os.path.join(root, f).replace('\\', '/')
        size = os.path.getsize(p)
        ext = os.path.splitext(f)[1].lower()
        
        if 'edge_profile' in p:
            categories['browser_profiles'].append((p, size))
        elif ext == '.py':
            categories['python_scripts'].append((p, size))
        elif ext == '.php':
            categories['php_scripts'].append((p, size))
        elif ext == '.ps1':
            categories['powershell_scripts'].append((p, size))
        elif ext in ['.png', '.jpg', '.jpeg']:
            categories['temporary_images'].append((p, size))
        elif ext in ['.html', '.htm']:
            categories['html_dumps'].append((p, size))
        elif ext in ['.json', '.txt']:
            categories['json_and_text'].append((p, size))
        elif ext in ['.ttf', '.otf', '.woff', '.woff2']:
            categories['fonts'].append((p, size))
        else:
            categories['other'].append((p, size))

for cat, items in categories.items():
    total_size = sum(s for _, s in items)
    print(f"\n=== {cat.upper()} (Count: {len(items)}, Total Size: {total_size} bytes) ===")
    for p, s in sorted(items):
        print(f"  {p:55} {s} bytes")

