import subprocess
import os
import json
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
os.makedirs('review', exist_ok=True)

# 1. Inject script to read computed style and text
script = """<script>
window.addEventListener('load', () => {
    const title = document.querySelector('.work-speaks-title');
    const em = title ? title.querySelector('em') : null;
    const res = {
        title_text: title ? title.innerText : null,
        title_transform: title ? window.getComputedStyle(title).textTransform : null,
        title_font: title ? window.getComputedStyle(title).fontFamily : null,
        title_size: title ? window.getComputedStyle(title).fontSize : null,
        title_weight: title ? window.getComputedStyle(title).fontWeight : null,
        em_text: em ? em.innerText : null,
        em_transform: em ? window.getComputedStyle(em).textTransform : null,
        em_font: em ? window.getComputedStyle(em).fontFamily : null,
        em_style: em ? window.getComputedStyle(em).fontStyle : null
    };
    document.title = 'WS_CHECK:' + JSON.stringify(res);
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

temp_file = os.path.abspath('temp_index_ws.html')
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(content.replace('</body>', script + '</body>'))

cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1440,9000',
    f'file:///{temp_file.replace(os.sep, "/")}',
    '--dump-dom'
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
for line in res.stdout.splitlines():
    if '<title>WS_CHECK:' in line:
        print('COMPUTED RESULTS:', line)

if os.path.exists(temp_file):
    os.remove(temp_file)

# 2. Take desktop screenshot
# First inject script to force reveal on .work-speaks-intro and get its bounding rect
pos_script = """<script>
window.addEventListener('load', () => {
    document.querySelectorAll('[data-reveal]').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
        el.style.visibility = 'visible';
    });
    const section = document.querySelector('#the-work-speaks');
    if (section) {
        const r = section.getBoundingClientRect();
        document.title = 'SECTION_RECT:' + JSON.stringify({top: Math.round(r.top + window.scrollY), left: Math.round(r.left), width: Math.round(r.width), height: Math.round(r.height)});
    }
});
</script>"""

with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(content.replace('</body>', pos_script + '</body>'))

# Desktop
shot_desktop = os.path.abspath('scratch/ws_full_desktop.png')
cmd_desktop = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,9500',
    f'--screenshot={shot_desktop}',
    f'file:///{temp_file.replace(os.sep, "/")}'
]
subprocess.run(cmd_desktop, capture_output=True)

# Mobile
shot_mobile = os.path.abspath('scratch/ws_full_mobile.png')
cmd_mobile = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=390,13500',
    f'--screenshot={shot_mobile}',
    f'file:///{temp_file.replace(os.sep, "/")}'
]
subprocess.run(cmd_mobile, capture_output=True)

# Let's read the section rects
for w, shot_path, name, win_h in [(1440, shot_desktop, 'desktop', 9500), (390, shot_mobile, 'mobile', 13500)]:
    cmd_rect = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files',
        f'--window-size={w},{win_h}',
        f'file:///{temp_file.replace(os.sep, "/")}',
        '--dump-dom'
    ]
    r = subprocess.run(cmd_rect, capture_output=True, text=True, encoding='utf-8')
    rect = None
    for line in r.stdout.splitlines():
        if '<title>SECTION_RECT:' in line:
            json_str = line.split('<title>SECTION_RECT:')[1].split('</title>')[0]
            rect = json.loads(json_str)
            print(f'{name} rect:', rect)
            break
            
    if rect and os.path.exists(shot_path):
        im = Image.open(shot_path)
        # Crop section
        top = max(0, rect['top'] - 40)
        bot = min(im.height, rect['top'] + min(rect['height'] + 40, 900))
        crop_sec = im.crop((0, top, im.width, bot))
        crop_sec.save(f'review/work_speaks_{name}_section.png')
        print(f'Saved review/work_speaks_{name}_section.png')
        
        # Crop specifically the heading & eyebrow
        heading_w = 450 if name == 'desktop' else im.width
        crop_heading = im.crop((0, top, heading_w, min(top + 350, im.height)))
        crop_heading.save(f'review/work_speaks_{name}_heading.png')
        print(f'Saved review/work_speaks_{name}_heading.png')

if os.path.exists(temp_file):
    os.remove(temp_file)
print('Done verification.')
