import subprocess
import os
import shutil
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Copy the verified index and about crops
shutil.copy('scratch/footer_crop_exact_index.html.png', 'review/footer_available_worldwide_index.png')
shutil.copy('scratch/footer_crop_exact_about.html.png', 'review/footer_available_worldwide_about.png')

# For coming-soon.html:
shot = os.path.abspath('scratch/temp_cs_full.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,2000', f'--screenshot={shot}',
    'file:///C:/xampp/htdocs/luci/coming-soon.html'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)

# Find dark pixels in footer area (bottom half)
coords = [(x, y) for y in range(500, im.height) for x in range(300, 1140) if im.getpixel((x, y))[0] < 50]
if coords:
    min_y = min(p[1] for p in coords)
    max_y = max(p[1] for p in coords)
    print(f'Detected text y range: {min_y} to {max_y}')
    crop = im.crop((100, max(0, min_y - 60), 1340, min(im.height, max_y + 60)))
    crop.save('review/footer_available_worldwide_coming_soon.png')
    print('Saved review/footer_available_worldwide_coming_soon.png')

if os.path.exists(shot):
    os.remove(shot)

