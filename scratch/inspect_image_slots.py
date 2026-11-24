import re

pages = [
    ('beauty-campaign-production.html', 'campaign-shoots.css'),
    ('beauty-brand-identity-design.html', 'brand-identity.css'),
    ('med-spa-website-design.html', 'website-design.css')
]

for html_file, css_file in pages:
    print(f"\n=======================================================")
    print(f"*** PAGE: {html_file} ({css_file}) ***")
    print(f"=======================================================")
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find section headers and image contexts
    lines = html.splitlines()
    for i, line in enumerate(lines):
        if '<img' in line and not any(k in line.lower() for k in ['logo', 'favicon', 'icon', 'svg']):
            # Print context lines around this image
            start = max(0, i - 12)
            end = min(len(lines), i + 10)
            print(f"\n--- Line {i+1} ---")
            for j in range(start, end):
                prefix = ">>> " if j == i else "    "
                print(f"{prefix}{lines[j]}")
