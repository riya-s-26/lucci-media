import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
os.makedirs('review', exist_ok=True)

# 1. Capture full desktop index
shot_desk = os.path.abspath('scratch/verify_index_desktop.png')
cmd_desk = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,2500', f'--screenshot={shot_desk}',
    'file:///C:/xampp/htdocs/luci/index.html'
]
subprocess.run(cmd_desk, check=True)
im_d = Image.open(shot_desk)

# Crop trust band with ticker on desktop (y: 800 to 980)
crop_d_ticker = im_d.crop((0, 800, 1440, 960))
crop_d_ticker.save('review/ticker_desktop.png')
print('Saved review/ticker_desktop.png')

# 2. Capture full mobile index
shot_mob = os.path.abspath('scratch/verify_index_mobile.png')
cmd_mob = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=390,2000', f'--screenshot={shot_mob}',
    'file:///C:/xampp/htdocs/luci/index.html'
]
subprocess.run(cmd_mob, check=True)
im_m = Image.open(shot_mob)

# Crop trust band with ticker on mobile (y: 650 to 820)
crop_m_ticker = im_m.crop((0, 660, 390, 810))
crop_m_ticker.save('review/ticker_mobile.png')
print('Saved review/ticker_mobile.png')

# 3. Check computed style via dump-dom
html = """<script>
window.addEventListener('load', () => {
    const s = document.querySelector('.ticker-track span');
    const b = document.querySelector('.ticker-track b');
    const wwdb = document.querySelector('.tsa-services-headline');
    const res = {
        tickerSpanFontFamily: window.getComputedStyle(s).fontFamily,
        tickerSpanFontWeight: window.getComputedStyle(s).fontWeight,
        tickerSpanFontSize: window.getComputedStyle(s).fontSize,
        tickerSpanLetterSpacing: window.getComputedStyle(s).letterSpacing,
        tickerBulletFont: window.getComputedStyle(b).fontFamily,
        wwdbFontFamily: window.getComputedStyle(wwdb).fontFamily,
        wwdbFontWeight: window.getComputedStyle(wwdb).fontWeight
    };
    document.title = 'VERIFY_RESULT:' + JSON.stringify(res);
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

temp = os.path.abspath('temp_verify.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', html + '</body>'))

cmd_verify = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1440,1500',
    f'file:///{temp.replace(os.sep, "/")}',
    '--dump-dom'
]
res = subprocess.run(cmd_verify, capture_output=True, text=True, encoding='utf-8')
for l in res.stdout.splitlines():
    if '<title>VERIFY_RESULT:' in l:
        print('COMPUTED_STYLES:', l)

if os.path.exists(temp):
    os.remove(temp)

