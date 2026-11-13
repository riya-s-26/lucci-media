import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Read coming-soon.html and remove document.documentElement.classList.add('js')
with open('coming-soon.html', 'r', encoding='utf-8') as f:
    c = f.read()

# remove js class addition
c_nojs = c.replace("document.documentElement.classList.add('js');", "")
temp = os.path.abspath('temp_cs_nojs.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c_nojs)

shot = os.path.abspath('scratch/temp_cs_nojs.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1440,2000', f'--screenshot={shot}',
    f'file:///{temp.replace(os.sep, "/")}'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)
print('No-JS Shot size:', im.size)

# Find coordinates of dark text in bottom half
coords = [(x, y) for y in range(800, im.height) for x in range(300, 1140) if im.getpixel((x, y))[0] < 50]
if coords:
    min_y = min(p[1] for p in coords)
    max_y = max(p[1] for p in coords)
    print(f'Dark pixels between {min_y} and {max_y}')
    crop = im.crop((100, max(0, min_y - 40), 1340, min(im.height, max_y + 40)))
    crop.save('review/footer_available_worldwide_coming_soon.png')
    print('Saved review/footer_available_worldwide_coming_soon.png')

if os.path.exists(temp):
    os.remove(temp)
if os.path.exists(shot):
    os.remove(shot)

