import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Let's test uppercase in HTML and CSS
with open('index.html', 'r', encoding='utf-8') as f:
    idx_orig = f.read()
with open('styles.css', 'r', encoding='utf-8') as f:
    css_orig = f.read()

# Update HTML to uppercase
idx_mod = idx_orig.replace(
    '<h2 class="work-speaks-title" id="work-speaks-title">The work<br><em>speaks</em></h2>',
    '<h2 class="work-speaks-title" id="work-speaks-title">THE WORK<br><em>SPEAKS</em></h2>'
)

# Update CSS text-transform to uppercase
css_mod = css_orig.replace(
    "text-transform: none !important;",
    "text-transform: uppercase !important;"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_mod)
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_mod)

for vp, w, h, box in [
    ('desktop', 1440, 3500, (80, 2100, 650, 2550)),
    ('mobile', 390, 3500, (20, 1900, 370, 2250))
]:
    shot = os.path.abspath(f'scratch/test_ws_{vp}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        f'--window-size={w},{h}', f'--screenshot={shot}',
        'file:///C:/xampp/htdocs/luci/index.html'
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(shot)
    # Find bounding box of work speaks in screenshot
    im.save(f'scratch/full_test_ws_{vp}.png')
    print(f'Saved scratch/full_test_ws_{vp}.png')
    if os.path.exists(shot):
        os.remove(shot)

# Restore originals for now
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_orig)
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_orig)

print('Done rendering work speaks tests')

