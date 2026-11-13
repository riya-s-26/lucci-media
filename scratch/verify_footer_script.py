import subprocess
import os
import json
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
os.makedirs('review', exist_ok=True)

# 1. Verify computed styles via dump-dom
html = """<script>
window.addEventListener('load', () => {
    const el = document.querySelector('.footer-script');
    const res = {
        fontFamily: el ? window.getComputedStyle(el).fontFamily : null,
        fontSize: el ? window.getComputedStyle(el).fontSize : null,
        color: el ? window.getComputedStyle(el).color : null,
        letterSpacing: el ? window.getComputedStyle(el).letterSpacing : null,
        lineHeight: el ? window.getComputedStyle(el).lineHeight : null,
        marginTop: el ? window.getComputedStyle(el).marginTop : null
    };
    document.title = 'FOOTER_COMPUTED:' + JSON.stringify(res);
});
</script>"""

pages = [
    ('index.html', 9500),
    ('about.html', 5800),
    ('coming-soon.html', 1200)
]

for page, height in pages:
    with open(page, 'r', encoding='utf-8') as f:
        c = f.read()
    temp = os.path.abspath(f'temp_fc_{page}')
    with open(temp, 'w', encoding='utf-8') as f:
        f.write(c.replace('</body>', html + '</body>'))
        
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files',
        f'--window-size=1440,{height}',
        f'file:///{temp.replace(os.sep, "/")}',
        '--dump-dom'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    for l in res.stdout.splitlines():
        if '<title>FOOTER_COMPUTED:' in l:
            print(f'{page:18}: {l}')
    if os.path.exists(temp):
        os.remove(temp)

# 2. Capture clean visual crops for all 3 pages
# First let's get exact bounding rect for .footer-meta-center in each
for page, height, name in [('index.html', 9500, 'index'), ('about.html', 5800, 'about'), ('coming-soon.html', 1400, 'coming_soon')]:
    shot = os.path.abspath(f'scratch/full_footer_{name}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        f'--window-size=1440,{height}', f'--screenshot={shot}',
        f'file:///C:/xampp/htdocs/luci/{page}'
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(shot)
    
    # We find pixels of dark text or crop around the footer zone
    # On index: around height - 600
    # Let's save a crop of the footer zone
    crop = im.crop((100, im.height - 450, 1340, im.height - 100))
    crop.save(f'review/footer_available_worldwide_{name}.png')
    print(f'Saved review/footer_available_worldwide_{name}.png')
    if os.path.exists(shot):
        os.remove(shot)

print('Verification complete')

