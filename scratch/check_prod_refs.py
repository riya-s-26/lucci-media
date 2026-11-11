prod_files = [
    'index.html', 'about.html', 'coming-soon.html', 'services.html',
    'the-work.html', 'our-studio.html', 'inquire.html',
    'styles.css', 'about.css', 'coming-soon.css', 'script.js', '.htaccess'
]

matches = []
for p in prod_files:
    try:
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f, 1):
                if 'scratch' in line:
                    matches.append((p, i, line.strip()))
    except Exception as e:
        print(f'Error reading {p}: {e}')

print(f"Total references to 'scratch' in production files: {len(matches)}")
for p, i, line in matches:
    print(f"  {p}:{i}: {line}")

