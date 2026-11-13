import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

shot = os.path.abspath('scratch/temp_cs_1500.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,1500', f'--screenshot={shot}',
    'file:///C:/xampp/htdocs/luci/coming-soon.html'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)
# Find bounding box of all dark pixels below y=800
coords = [(x, y) for y in range(800, im.height) for x in range(im.width) if sum(im.getpixel((x, y))[:3]) < 600]
if coords:
    min_y = min(c[1] for c in coords)
    max_y = max(c[1] for c in coords)
    print(f'Dark pixels between {min_y} and {max_y}')
    crop = im.crop((100, min_y - 20, 1340, max_y + 20))
    crop.save('review/footer_available_worldwide_coming_soon.png')
    print('Saved review/footer_available_worldwide_coming_soon.png')
else:
    print('No dark pixels found below 800')

