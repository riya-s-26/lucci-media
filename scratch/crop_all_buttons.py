import subprocess, os, json
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Let's get bounding boxes of key CTA buttons across viewports
def get_boxes(w, h):
    # reuse temp_test_index
    svg_code = '<svg class="cta-arrow-icon" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M1.5 8.5L8.5 1.5M8.5 1.5H3.5M8.5 1.5V6.5" stroke="currentColor" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    with open('index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('<span aria-hidden="true">↗</span>', f'<span aria-hidden="true">{svg_code}</span>')
    c = c.replace('<span>↗</span>', f'<span>{svg_code}</span>')
    c = c.replace('VIEW SERVICES ↗', f'VIEW SERVICES {svg_code}')
    
    script = """<script>
    window.addEventListener('load', () => {
        document.querySelectorAll('[data-reveal]').forEach(el => {
            el.style.opacity = '1';
            el.style.transform = 'none';
            el.style.visibility = 'visible';
        });
        const targets = {
            header_cta: document.querySelector('.header-cta'),
            hero_btn: document.querySelector('.hero-actions .button-light'),
            archive_btn: document.querySelector('.archive-work-btn'),
            tsa_banner_btn: document.querySelector('.tsa-cta-banner-link'),
            contact_btn: document.querySelector('.contact-section .button-light')
        };
        const res = {};
        for (let k in targets) {
            const el = targets[k];
            if (el) {
                const r = el.getBoundingClientRect();
                res[k] = {
                    left: Math.round(r.left),
                    top: Math.round(r.top + window.scrollY),
                    width: Math.round(r.width),
                    height: Math.round(r.height)
                };
            }
        }
        document.title = 'BOXES:' + JSON.stringify(res);
    });
    </script>"""
    
    temp = os.path.abspath('temp_box.html')
    with open(temp, 'w', encoding='utf-8') as f:
        f.write(c.replace('</body>', script + '</body>'))
        
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files',
        f'--window-size={w},{h}',
        '--dump-dom',
        'file:///' + temp.replace('\\', '/')
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    boxes = {}
    for l in res.stdout.splitlines():
        if '<title>BOXES:' in l:
            boxes = json.loads(l.split('<title>BOXES:')[1].split('</title>')[0])
            break
    if os.path.exists(temp):
        os.remove(temp)
    return boxes

# Desktop crops
boxes_d = get_boxes(1440, 9500)
print('Desktop boxes:', boxes_d)
im_d = Image.open('scratch/live_desktop.png')
for k, b in boxes_d.items():
    crop = im_d.crop((max(0, b['left'] - 10), max(0, b['top'] - 10), min(im_d.width, b['left'] + b['width'] + 10), min(im_d.height, b['top'] + b['height'] + 10)))
    crop.save(f'scratch/crop_d_{k}.png')

# iPad crops
boxes_t = get_boxes(820, 11000)
print('iPad boxes:', boxes_t)
im_t = Image.open('scratch/live_ipad.png')
for k, b in boxes_t.items():
    crop = im_t.crop((max(0, b['left'] - 10), max(0, b['top'] - 10), min(im_t.width, b['left'] + b['width'] + 10), min(im_t.height, b['top'] + b['height'] + 10)))
    crop.save(f'scratch/crop_ipad_{k}.png')

# iPhone crops
boxes_m = get_boxes(390, 13500)
print('iPhone boxes:', boxes_m)
im_m = Image.open('scratch/live_iphone.png')
for k, b in boxes_m.items():
    crop = im_m.crop((max(0, b['left'] - 10), max(0, b['top'] - 10), min(im_m.width, b['left'] + b['width'] + 10), min(im_m.height, b['top'] + b['height'] + 10)))
    crop.save(f'scratch/crop_m_{k}.png')

print("All crops saved.")

