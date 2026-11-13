import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

shot = os.path.abspath('scratch/temp_index_full.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,3000', f'--screenshot={shot}',
    'file:///C:/xampp/htdocs/luci/index.html'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)

# Find .tsa-services-headline in the screenshot
# We know it's after the archive section (around y=1800 to 2400)
crop_wwdb = im.crop((0, 1800, 1440, 2200))
crop_wwdb.save('scratch/actual_wwdb_desktop.png')
print('Saved actual_wwdb_desktop.png')

