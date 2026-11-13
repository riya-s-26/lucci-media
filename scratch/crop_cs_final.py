import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

shot = os.path.abspath('scratch/temp_cs_correct_final.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,2000', f'--screenshot={shot}',
    'file:///C:/xampp/htdocs/luci/coming-soon.html'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)
# Crop around rs: y=1530
crop = im.crop((100, 1460, 1340, 1620))
crop.save('review/footer_available_worldwide_coming_soon.png')
print('Saved footer crop for coming-soon!')
if os.path.exists(shot):
    os.remove(shot)

