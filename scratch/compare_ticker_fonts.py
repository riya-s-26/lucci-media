import subprocess
import os
import shutil
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Read styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

tests = [
    ('400_14', "font: 400 14px/1.7 'ShapiroWideRegular', var(--sans); letter-spacing: .08em;"),
    ('500_14', "font: 500 14px/1.7 'ShapiroWideRegular', var(--sans); letter-spacing: .08em;"),
    ('600_14', "font: 600 14px/1.7 'ShapiroWideRegular', var(--sans); letter-spacing: .08em;"),
    ('700_14', "font: 700 14px/1.7 'ShapiroWideRegular', var(--sans); letter-spacing: .08em;"),
    ('500_15', "font: 500 15px/1.7 'ShapiroWideRegular', var(--sans); letter-spacing: .08em;"),
    ('700_15', "font: 700 15px/1.7 'ShapiroWideRegular', var(--sans); letter-spacing: .08em;")
]

old_rule = ".ticker-track > span { color: #55504B; font: 400 16px/1.7 var(--typewriter); letter-spacing: .04em; }"

for label, font_rule in tests:
    new_rule = f".ticker-track > span {{ color: #55504B; {font_rule} }}"
    modified_css = css_content.replace(old_rule, new_rule)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(modified_css)
        
    for vp, w, h, box in [
        ('desktop', 1440, 1600, (0, 780, 1440, 1020)),
        ('mobile', 390, 1600, (0, 650, 390, 850))
    ]:
        shot = os.path.abspath(f'scratch/temp_{label}_{vp}.png')
        cmd = [
            chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
            '--allow-file-access-from-files', '--hide-scrollbars',
            '--force-prefers-reduced-motion',
            f'--window-size={w},{h}', f'--screenshot={shot}',
            'file:///C:/xampp/htdocs/luci/index.html'
        ]
        subprocess.run(cmd, check=True)
        im = Image.open(shot)
        crop = im.crop(box)
        crop.save(f'scratch/ticker_{label}_{vp}.png')
        if os.path.exists(shot):
            os.remove(shot)

# Restore original styles.css
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print('Done rendering all variations')

