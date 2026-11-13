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

for page in ['index.html', 'about.html', 'coming-soon.html']:
    shot = os.path.abspath(f'scratch/temp_footer_{page}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        '--window-size=1440,2500', f'--screenshot={shot}',
        f'file:///C:/xampp/htdocs/luci/{page}'
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(shot)
    # Crop footer
    crop = im.crop((300, im.height - 400, 1140, im.height - 50))
    crop.save(f'scratch/footer_crop_{page}.png')
    if os.path.exists(shot):
        os.remove(shot)

# Restore originals
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(s_orig)
with open('about.css', 'w', encoding='utf-8') as f:
    f.write(a_orig)
with open('coming-soon.css', 'w', encoding='utf-8') as f:
    f.write(c_orig)

print('Done rendering footer test crops')

