import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# First, capture actual mobile index page including WWDB
shot = os.path.abspath('scratch/temp_mobile_full.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=390,3000', f'--screenshot={shot}',
    'file:///C:/xampp/htdocs/luci/index.html'
]
subprocess.run(cmd, check=True)
im_m = Image.open(shot)

# Crop mobile WWDB
crop_m_wwdb = im_m.crop((0, 1600, 390, 1850))
crop_m_wwdb.save('scratch/actual_wwdb_mobile.png')

print('Mobile WWDB saved')

