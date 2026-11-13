import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

shot = os.path.abspath('scratch/temp_cs_full2.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,2000', f'--screenshot={shot}',
    'file:///C:/xampp/htdocs/luci/coming-soon.html'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)

# Crop bottom area (y: 1300 to 1900)
crop = im.crop((100, 1300, 1340, 1900))
crop.save('review/footer_available_worldwide_coming_soon.png')
print('Saved coming soon footer crop')
if os.path.exists(shot):
    os.remove(shot)

