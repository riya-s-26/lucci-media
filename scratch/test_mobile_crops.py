import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open('styles.css', 'r', encoding='utf-8') as f:
    orig_css = f.read()

# Let's test weight 400 and weight 700 on mobile
for w in [400, 700]:
    rule = f".ticker-track > span {{ color: #55504B; font-family: 'ShapiroWideRegular', var(--sans); font-size: 14px; font-weight: {w}; line-height: 1.7; letter-spacing: .08em; text-transform: uppercase; }}"
    test_css = orig_css.replace(".ticker-track > span { color: #55504B; font: 400 16px/1.7 var(--typewriter); letter-spacing: .04em; }", rule)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(test_css)
        
    s_shot = os.path.abspath(f'scratch/mobile_{w}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        '--window-size=390,1600', f'--screenshot={s_shot}',
        'file:///C:/xampp/htdocs/luci/index.html'
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(s_shot)
    crop = im.crop((0, 710, 390, 800))
    crop.save(f'scratch/ticker_mobile_{w}_crop.png')
    if os.path.exists(s_shot):
        os.remove(s_shot)

# Restore styles.css
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(orig_css)

print('Done mobile crops')

