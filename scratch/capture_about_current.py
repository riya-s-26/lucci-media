import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

shot = os.path.abspath('scratch/about_current_hero.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,1200', f'--screenshot={shot}',
    'file:///C:/xampp/htdocs/luci/about.html'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)
crop = im.crop((0, 0, 1440, 900))
crop.save('scratch/about_current_hero_crop.png')
print('Saved scratch/about_current_hero_crop.png')

