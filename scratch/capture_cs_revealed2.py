import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open('coming-soon.html', 'r', encoding='utf-8') as f:
    c = f.read()

scroll_script = """<style>
.js [data-reveal], .js [data-reveal="image"], .site-footer {
    opacity: 1 !important;
    transform: none !important;
}
</style>"""

temp = os.path.abspath('temp_cs_reveal.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</head>', scroll_script + '</head>'))

shot = os.path.abspath('scratch/temp_cs_revealed_shot.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--window-size=1440,2000', f'--screenshot={shot}',
    f'file:///{temp.replace(os.sep, "/")}'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)
# rs was at y=1530
crop = im.crop((100, 1460, 1340, 1620))
crop.save('review/footer_available_worldwide_coming_soon.png')
print('Saved revealed coming-soon footer crop')

if os.path.exists(temp):
    os.remove(temp)
if os.path.exists(shot):
    os.remove(shot)

