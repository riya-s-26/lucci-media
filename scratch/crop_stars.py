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
    const s1 = document.querySelector('.studio-sparkle');
    const s2 = document.querySelector('.contact-flower');
    const r1 = s1 ? s1.getBoundingClientRect() : null;
    const r2 = s2 ? s2.getBoundingClientRect() : null;
    document.title = 'STARS:' + JSON.stringify({
        sparkle: r1 ? {left: Math.round(r1.left), top: Math.round(r1.top + window.scrollY), width: Math.round(r1.width), height: Math.round(r1.height)} : null,
        flower: r2 ? {left: Math.round(r2.left), top: Math.round(r2.top + window.scrollY), width: Math.round(r2.width), height: Math.round(r2.height)} : null
    });
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

temp = os.path.abspath('temp_stars.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', html + '</body>'))

shot = os.path.abspath('scratch/stars_desktop_full.png')
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
for l in res.stdout.splitlines():
    if '<title>STARS:' in l:
        print(l)
        data = json.loads(l.split('<title>STARS:')[1].split('</title>')[0])
        im = Image.open(shot)
        if data['sparkle']:
            b = data['sparkle']
            crop1 = im.crop((max(0, b['left'] - 20), max(0, b['top'] - 20), min(im.width, b['left'] + b['width'] + 20), min(im.height, b['top'] + b['height'] + 20)))
            crop1.save('scratch/star_sparkle_crop.png')
            print("Saved scratch/star_sparkle_crop.png")
        if data['flower']:
            b = data['flower']
            crop2 = im.crop((max(0, b['left'] - 20), max(0, b['top'] - 20), min(im.width, b['left'] + b['width'] + 20), min(im.height, b['top'] + b['height'] + 20)))
            crop2.save('scratch/star_flower_crop.png')
            print("Saved scratch/star_flower_crop.png")

if os.path.exists(temp):
    os.remove(temp)

