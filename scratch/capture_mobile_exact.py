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
    const s = document.querySelector('.studio-sparkle');
    const f = document.querySelector('.contact-flower');
    const p = document.querySelector('#archive-pause-toggle');
    const founder = document.querySelector('.studio-section');
    const contact = document.querySelector('#contact');
    const archive = document.querySelector('#archive');
    
    document.title = 'EXACT_RECTS:' + JSON.stringify({
        s: s ? s.getBoundingClientRect() : null,
        f: f ? f.getBoundingClientRect() : null,
        founder: founder ? {top: founder.getBoundingClientRect().top + window.scrollY, height: founder.getBoundingClientRect().height} : null,
        contact: contact ? {top: contact.getBoundingClientRect().top + window.scrollY, height: contact.getBoundingClientRect().height} : null,
        archive: archive ? {top: archive.getBoundingClientRect().top + window.scrollY, height: archive.getBoundingClientRect().height} : null
    });
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

temp = os.path.abspath('temp_exact.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', html + '</body>'))

# Let's run with window-size=500,14000 so the entire width is captured
shot = os.path.abspath('scratch/mobile_exact.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=520,14000',
    f'--screenshot={shot}',
    '--dump-dom',
    'file:///' + temp.replace('\\', '/')
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
locs = {}
for l in res.stdout.splitlines():
    if '<title>EXACT_RECTS:' in l:
        locs = json.loads(l.split('<title>EXACT_RECTS:')[1].split('</title>')[0])
        print(l)
        break

if os.path.exists(shot) and locs:
    im = Image.open(shot)
    if locs.get('founder'):
        b = locs['founder']
        crop = im.crop((0, max(0, int(b['top']) - 20), im.width, min(im.height, int(b['top'] + b['height']) + 20)))
        crop.save('review/mobile_founder_section.png')
        print("Saved review/mobile_founder_section.png")
    if locs.get('contact'):
        b = locs['contact']
        crop = im.crop((0, max(0, int(b['top']) - 20), im.width, min(im.height, int(b['top'] + b['height']) + 20)))
        crop.save('review/mobile_contact_section.png')
        print("Saved review/mobile_contact_section.png")

if os.path.exists(temp):
    os.remove(temp)

