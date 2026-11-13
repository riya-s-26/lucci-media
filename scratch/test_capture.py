import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

def capture_crop(page_url, width, height, crop_box, output_path):
    shot = os.path.abspath('scratch/temp_shot.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        f'--window-size={width},{height}', f'--screenshot={shot}',
        page_url
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(shot)
    if crop_box:
        im = im.crop(crop_box)
    im.save(output_path)
    print(f'Saved {output_path}')

# Let's capture trust-band currently
capture_crop('file:///C:/xampp/htdocs/luci/index.html', 1440, 1500, (0, 750, 1440, 1050), 'scratch/current_ticker_desktop.png')
capture_crop('file:///C:/xampp/htdocs/luci/index.html', 390, 1500, (0, 600, 390, 850), 'scratch/current_ticker_mobile.png')
