import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Read current CSS files
with open('styles.css', 'r', encoding='utf-8') as f:
    s_orig = f.read()
with open('about.css', 'r', encoding='utf-8') as f:
    a_orig = f.read()
with open('coming-soon.css', 'r', encoding='utf-8') as f:
    c_orig = f.read()

# Apply test rule
s_mod = s_orig.replace("font-family: 'Hello January', 'HelloJanuary', cursive, sans-serif !important;", "font-family: 'ShapiroWideRegular', var(--sans) !important;")
a_mod = a_orig.replace("font-family: 'Hello January', 'HelloJanuary', cursive, sans-serif !important;", "font-family: 'ShapiroWideRegular', var(--sans) !important;")
c_mod = c_orig.replace("font-family: 'Hello January', 'HelloJanuary', cursive, sans-serif !important;", "font-family: 'ShapiroWideRegular', var(--sans) !important;")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(s_mod)
with open('about.css', 'w', encoding='utf-8') as f:
    f.write(a_mod)
with open('coming-soon.css', 'w', encoding='utf-8') as f:
    f.write(c_mod)

pages = [
    ('index.html', 9500, 8731),
    ('about.html', 4500, 4000),
    ('coming-soon.html', 2700, 2411)
]

for page, h, y in pages:
    shot = os.path.abspath(f'scratch/temp_f_{page}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        f'--window-size=1440,{h}', f'--screenshot={shot}',
        f'file:///C:/xampp/htdocs/luci/{page}'
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(shot)
    crop = im.crop((100, int(y - 50), 1340, int(y + 110)))
    crop.save(f'scratch/footer_crop_exact_{page}.png')
    if os.path.exists(shot):
        os.remove(shot)

# Restore originals
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(s_orig)
with open('about.css', 'w', encoding='utf-8') as f:
    f.write(a_orig)
with open('coming-soon.css', 'w', encoding='utf-8') as f:
    f.write(c_orig)

print('Done rendering exact crops')

