import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
os.makedirs('review', exist_ok=True)

targets = [
    ('index.html', 8600, 7986, 'index'),
    ('about.html', 5900, 5333, 'about'),
    ('coming-soon.html', 1300, 736, 'coming_soon')
]

for page, height, y, name in targets:
    shot = os.path.abspath(f'scratch/temp_crop_{name}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        f'--window-size=1440,{height}', f'--screenshot={shot}',
        f'file:///C:/xampp/htdocs/luci/{page}'
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(shot)
    crop = im.crop((100, int(y - 100), 1340, int(y + 100)))
    crop.save(f'review/footer_available_worldwide_{name}.png')
    print(f'Saved review/footer_available_worldwide_{name}.png')
    if os.path.exists(shot):
        os.remove(shot)

print('Done cropping all 3 footers')

