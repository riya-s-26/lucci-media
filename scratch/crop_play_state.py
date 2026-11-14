import subprocess, os, json
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html = """<script>
window.addEventListener('load', () => {
    document.querySelectorAll('[data-reveal]').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
        el.style.visibility = 'visible';
    });
    const btn = document.querySelector('#archive-pause-toggle');
    if (btn) btn.click();
    const r = btn ? btn.getBoundingClientRect() : null;
    document.title = 'PLAY_RECT:' + JSON.stringify(r ? {left: Math.round(r.left), top: Math.round(r.top + window.scrollY), width: Math.round(r.width), height: Math.round(r.height)} : null);
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

temp = os.path.abspath('temp_play_shot.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', html + '</body>'))

shot = os.path.abspath('scratch/play_shot.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,9500',
    f'--screenshot={shot}',
    '--dump-dom',
    'file:///' + temp.replace('\\', '/')
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
rect = None
for l in res.stdout.splitlines():
    if '<title>PLAY_RECT:' in l:
        rect = json.loads(l.split('<title>PLAY_RECT:')[1].split('</title>')[0])
        print("Play rect:", rect)
        break

if rect and os.path.exists(shot):
    im = Image.open(shot)
    crop = im.crop((rect['left'] - 20, rect['top'] - 15, rect['left'] + rect['width'] + 20, rect['top'] + rect['height'] + 15))
    crop.save('review/proof_play_button_desktop.png')
    print("Saved review/proof_play_button_desktop.png")

if os.path.exists(temp):
    os.remove(temp)
