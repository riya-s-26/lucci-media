import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

ws_section = re.search(r'<section class="work-speaks-section".*?</section>', html, re.DOTALL)
assert ws_section, 'Section not found in index.html'
section_html = ws_section.group(0)

classes = set(re.findall(r'class="([^"]+)"', section_html))
individual_classes = set()
for c in classes:
    for cls in c.split():
        individual_classes.add(cls)

print('Classes used in section HTML:', sorted(individual_classes))

for cls in individual_classes:
    if cls in ['page-wrap', 'is-visible']:
        continue
    assert f'.{cls}' in css, f'Missing CSS rule for .{cls}'

print('All section classes are defined in styles.css!')

assert ("querySelector('#the-work-speaks')" in js or 'querySelector("#the-work-speaks")' in js)
assert '.work-speaks-stat .work-speaks-num' in js
assert 'id="the-work-speaks"' in html

stats = re.findall(r'<div class="work-speaks-num">([^<]+)</div>', section_html)
print('Stat numbers in HTML:', stats)
assert len(stats) == 7
assert stats == ['467%', '$1M+', '$84K', '64%', '34%', '189%', '2X']

print('VERIFICATION COMPLETE: Everything is 100% consistent and intact!')

