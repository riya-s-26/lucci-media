import subprocess
import os
import json
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
os.makedirs('review', exist_ok=True)

# 1. Capture desktop screenshot
shot_desk = os.path.abspath('scratch/verify_about_desktop.png')
cmd_desk = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,1100', f'--screenshot={shot_desk}',
    'file:///C:/xampp/htdocs/luci/about.html'
]
subprocess.run(cmd_desk, check=True)
im_d = Image.open(shot_desk)
crop_d = im_d.crop((0, 60, 1440, 800))
crop_d.save('review/about_headline_desktop.png')
print('Saved review/about_headline_desktop.png')

# 2. Capture mobile screenshot (390px)
shot_mob = os.path.abspath('scratch/verify_about_mobile.png')
cmd_mob = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=390,900', f'--screenshot={shot_mob}',
    'file:///C:/xampp/htdocs/luci/about.html'
]
subprocess.run(cmd_mob, check=True)
im_m = Image.open(shot_mob)
crop_m = im_m.crop((0, 50, 390, 600))
crop_m.save('review/about_headline_mobile.png')
print('Saved review/about_headline_mobile.png')

# 3. Check computed styles via dump-dom
html = """<script>
window.addEventListener('load', () => {
    const title = document.querySelector('.about-hero-title');
    const res = {
        fontFamily: window.getComputedStyle(title).fontFamily,
        fontWeight: window.getComputedStyle(title).fontWeight,
        fontStyle: window.getComputedStyle(title).fontStyle,
        fontSize: window.getComputedStyle(title).fontSize,
        letterSpacing: window.getComputedStyle(title).letterSpacing,
        lineHeight: window.getComputedStyle(title).lineHeight,
        textTransform: window.getComputedStyle(title).textTransform
    };
    document.title = 'ABOUT_TITLE_COMPUTED:' + JSON.stringify(res);
});
</script>"""

temp = os.path.abspath('temp_verify_about.html')
with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', html + '</body>'))

cmd_verify = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1440,1100',
    f'file:///{temp.replace(os.sep, "/")}',
    '--dump-dom'
]
res = subprocess.run(cmd_verify, capture_output=True, text=True, encoding='utf-8')
for l in res.stdout.splitlines():
    if '<title>ABOUT_TITLE_COMPUTED:' in l:
        print(l)

if os.path.exists(temp):
    os.remove(temp)

