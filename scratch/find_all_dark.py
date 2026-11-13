import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

shot = os.path.abspath('scratch/entire_cs_shot.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--window-size=1440,2500', f'--screenshot={shot}',
    'file:///C:/xampp/htdocs/luci/coming-soon.html'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)
print('Entire image size:', im.size)

# Find all black/dark pixels
dark_pixels = []
for y in range(im.height):
    for x in range(im.width):
        r, g, b = im.getpixel((x, y))[:3]
        if r < 100 and g < 100 and b < 100:
            dark_pixels.append((x, y))

if dark_pixels:
    print(f'Total dark pixels: {len(dark_pixels)}')
    print(f'Y range: {min(p[1] for p in dark_pixels)} to {max(p[1] for p in dark_pixels)}')
    # Let's print dark pixel clusters
    y_vals = sorted(list(set(p[1] for p in dark_pixels)))
    # find gaps > 100px
    clusters = []
    curr = [y_vals[0]]
    for y in y_vals[1:]:
        if y - curr[-1] > 100:
            clusters.append((curr[0], curr[-1]))
            curr = [y]
        else:
            curr.append(y)
    clusters.append((curr[0], curr[-1]))
    print('Y clusters:', clusters)
else:
    print('No dark pixels at all!')

