import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

shot = os.path.abspath('scratch/temp_cs_footer_real.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,1100', f'--screenshot={shot}',
    'file:///C:/xampp/htdocs/luci/coming-soon.html'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)
crop = im.crop((100, 650, 1340, 850))
crop.save('review/footer_available_worldwide_coming_soon.png')
print('Saved footer crop for coming-soon!')
if os.path.exists(shot):
    os.remove(shot)

