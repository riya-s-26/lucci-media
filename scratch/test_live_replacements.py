import subprocess, os, json, re
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
os.makedirs('review', exist_ok=True)

# Define the SVG icon replacement
# Option: <svg class="cta-arrow-icon" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M1.5 8.5L8.5 1.5M8.5 1.5H3.5M8.5 1.5V6.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round"/></svg>
svg_code = '<svg class="cta-arrow-icon" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M1.5 8.5L8.5 1.5M8.5 1.5H3.5M8.5 1.5V6.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# Helper CSS for the SVG icon
css_addition = """
<style>
.cta-arrow-icon {
  width: 0.8em;
  height: 0.8em;
  display: inline-block;
  vertical-align: -0.05em;
  margin-left: 0.35em;
  flex-shrink: 0;
  stroke: currentColor;
}
.header-cta .cta-arrow-icon,
.button .cta-arrow-icon,
.text-link .cta-arrow-icon {
  margin-left: 0;
}
.archive-work-btn .cta-arrow-icon {
  margin-left: 0.25em;
  vertical-align: -0.02em;
}
.mobile-menu .mobile-contact .cta-arrow-icon {
  margin-left: 0;
  width: 0.9em;
  height: 0.9em;
}
</style>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace arrows in index.html
# 1. header-cta: <span aria-hidden="true">↗</span> -> <span aria-hidden="true">`+svg_code+`</span>
# 2. archive-work-btn: VIEW SERVICES ↗ -> VIEW SERVICES `+svg_code+`
# 3. etc.

c_test = c.replace('<span aria-hidden="true">↗</span>', f'<span aria-hidden="true">{svg_code}</span>')
c_test = c_test.replace('<span>↗</span>', f'<span>{svg_code}</span>')
c_test = c_test.replace('VIEW SERVICES ↗', f'VIEW SERVICES {svg_code}')
c_test = c_test.replace('</head>', css_addition + '</head>')

temp_file = os.path.abspath('temp_test_index.html')
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(c_test)

# Let's capture desktop (1440), iPad (820), and iPhone (390)
viewports = [
    ('desktop', 1440, 9500),
    ('ipad', 820, 11000),
    ('iphone', 390, 13500)
]

for name, w, h in viewports:
    shot = os.path.abspath(f'scratch/live_{name}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        f'--window-size={w},{h}',
        f'--screenshot={shot}',
        'file:///' + temp_file.replace('\\', '/')
    ]
    subprocess.run(cmd, capture_output=True)
    print(f'Captured {name}')

if os.path.exists(temp_file):
    os.remove(temp_file)

print('Screenshots complete.')

