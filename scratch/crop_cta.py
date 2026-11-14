import subprocess, os, json
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = """<script>
window.addEventListener('load', () => {
    const btn1 = document.querySelector('.hero-actions .button-light');
    const btn2 = document.querySelector('.header-cta');
    const r1 = btn1.getBoundingClientRect();
    const r2 = btn2.getBoundingClientRect();
    document.title = 'BOUNDS:' + JSON.stringify({
        btn1: {x: Math.round(r1.left), y: Math.round(r1.top), w: Math.round(r1.width), h: Math.round(r1.height)},
        btn2: {x: Math.round(r2.left), y: Math.round(r2.top), w: Math.round(r2.width), h: Math.round(r2.height)}
    });
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

temp = os.path.abspath('temp_bounds.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', html + '</body>'))

shot = os.path.abspath('scratch/desktop_cta_current.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--window-size=1440,900',
    f'--screenshot={shot}',
    '--dump-dom',
    'file:///' + temp.replace('\\', '/')
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
for l in res.stdout.splitlines():
    if '<title>BOUNDS:' in l:
        print(l)
        bounds = json.loads(l.split('<title>BOUNDS:')[1].split('</title>')[0])
        im = Image.open(shot)
        b1 = bounds['btn1']
        crop1 = im.crop((b1['x'] - 20, b1['y'] - 20, b1['x'] + b1['w'] + 20, b1['y'] + b1['h'] + 20))
        crop1.save('scratch/hero_btn1.png')
        b2 = bounds['btn2']
        crop2 = im.crop((b2['x'] - 20, b2['y'] - 20, b2['x'] + b2['w'] + 20, b2['y'] + b2['h'] + 20))
        crop2.save('scratch/header_btn2.png')
        print("Crops saved.")

if os.path.exists(temp):
    os.remove(temp)
