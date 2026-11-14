import subprocess, os, json
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
os.makedirs('review', exist_ok=True)

# 1. Test pause/play click toggle in Chrome
test_click_script = """<script>
window.addEventListener('load', () => {
    const btn = document.querySelector('#archive-pause-toggle');
    const pauseIcon = btn.querySelector('.icon-pause');
    const playIcon = btn.querySelector('.icon-play');
    const pauseText = btn.querySelector('.pause-text');
    const tracks = document.querySelectorAll('.archive-track');
    
    // State 1: Initial
    const s1 = {
        pressed: btn.getAttribute('aria-pressed'),
        text: pauseText.textContent,
        pauseDisplay: window.getComputedStyle(pauseIcon).display,
        playDisplay: window.getComputedStyle(playIcon).display,
        trackPaused: tracks[0].classList.contains('is-paused')
    };
    
    // Trigger click -> Paused
    btn.click();
    const s2 = {
        pressed: btn.getAttribute('aria-pressed'),
        text: pauseText.textContent,
        pauseDisplay: window.getComputedStyle(pauseIcon).display,
        playDisplay: window.getComputedStyle(playIcon).display,
        trackPaused: tracks[0].classList.contains('is-paused')
    };
    
    // Trigger click again -> Playing
    btn.click();
    const s3 = {
        pressed: btn.getAttribute('aria-pressed'),
        text: pauseText.textContent,
        pauseDisplay: window.getComputedStyle(pauseIcon).display,
        playDisplay: window.getComputedStyle(playIcon).display,
        trackPaused: tracks[0].classList.contains('is-paused')
    };
    
    document.title = 'CLICK_TEST:' + JSON.stringify({initial: s1, afterClick1: s2, afterClick2: s3});
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

temp = os.path.abspath('temp_test_click.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', test_click_script + '</body>'))

cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1440,900',
    '--dump-dom',
    'file:///' + temp.replace('\\', '/')
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
for l in res.stdout.splitlines():
    if '<title>CLICK_TEST:' in l:
        print(l)

if os.path.exists(temp):
    os.remove(temp)

# 2. Capture desktop, iPad, and iPhone screenshots of the affected elements
reveal_and_bounds_script = """<script>
window.addEventListener('load', () => {
    document.querySelectorAll('[data-reveal]').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
        el.style.visibility = 'visible';
    });
    
    const pauseToggle = document.querySelector('#archive-pause-toggle');
    const sparkle = document.querySelector('.studio-sparkle');
    const flower = document.querySelector('.contact-flower');
    const founderSec = document.querySelector('#meet-the-founder') || document.querySelector('.studio-section');
    const contactSec = document.querySelector('#contact');
    const archiveSec = document.querySelector('#archive');
    
    const getRect = (el) => {
        if (!el) return null;
        const r = el.getBoundingClientRect();
        return {
            left: Math.round(r.left),
            top: Math.round(r.top + window.scrollY),
            width: Math.round(r.width),
            height: Math.round(r.height)
        };
    };
    
    document.title = 'LOCATIONS:' + JSON.stringify({
        pauseToggle: getRect(pauseToggle),
        sparkle: getRect(sparkle),
        flower: getRect(flower),
        founderSec: getRect(founderSec),
        contactSec: getRect(contactSec),
        archiveSec: getRect(archiveSec)
    });
});
</script>"""

with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', reveal_and_bounds_script + '</body>'))

devices = [
    ('desktop', 1440, 9500),
    ('ipad', 820, 11000),
    ('iphone', 390, 13500)
]

for dev_name, w, h in devices:
    shot = os.path.abspath(f'scratch/full_{dev_name}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        f'--window-size={w},{h}',
        f'--screenshot={shot}',
        '--dump-dom',
        'file:///' + temp.replace('\\', '/')
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    locs = {}
    for l in r.stdout.splitlines():
        if '<title>LOCATIONS:' in l:
            locs = json.loads(l.split('<title>LOCATIONS:')[1].split('</title>')[0])
            break
            
    if os.path.exists(shot):
        im = Image.open(shot)
        # 1. Crop Founder Section
        if locs.get('founderSec'):
            b = locs['founderSec']
            crop_founder = im.crop((0, max(0, b['top'] - 20), im.width, min(im.height, b['top'] + b['height'] + 20)))
            crop_founder.save(f'review/proof_founder_{dev_name}.png')
            print(f'Saved review/proof_founder_{dev_name}.png')
            
        # 2. Crop Contact Section
        if locs.get('contactSec'):
            b = locs['contactSec']
            crop_contact = im.crop((0, max(0, b['top'] - 20), im.width, min(im.height, b['top'] + b['height'] + 20)))
            crop_contact.save(f'review/proof_contact_{dev_name}.png')
            print(f'Saved review/proof_contact_{dev_name}.png')
            
        # 3. Crop Pause Button in Archive
        if locs.get('pauseToggle'):
            b = locs['pauseToggle']
            crop_pause = im.crop((max(0, b['left'] - 30), max(0, b['top'] - 20), min(im.width, b['left'] + b['width'] + 80), min(im.height, b['top'] + b['height'] + 20)))
            crop_pause.save(f'review/proof_pause_{dev_name}.png')
            print(f'Saved review/proof_pause_{dev_name}.png')

if os.path.exists(temp):
    os.remove(temp)

# 3. Also capture Play State (paused archive)
play_script = """<script>
window.addEventListener('load', () => {
    document.querySelectorAll('[data-reveal]').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
        el.style.visibility = 'visible';
    });
    const btn = document.querySelector('#archive-pause-toggle');
    if (btn) btn.click(); // toggle to paused
});
</script>"""

with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', play_script + '</body>'))

shot_play = os.path.abspath('scratch/play_state_desktop.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,9500',
    f'--screenshot={shot_play}',
    'file:///' + temp.replace('\\', '/')
]
subprocess.run(cmd, capture_output=True)

if os.path.exists(shot_play) and locs.get('pauseToggle'):
    im = Image.open(shot_play)
    b = locs['pauseToggle']
    crop_play = im.crop((max(0, b['left'] - 30), max(0, b['top'] - 20), min(im.width, b['left'] + b['width'] + 80), min(im.height, b['top'] + b['height'] + 20)))
    crop_play.save('review/proof_play_state_desktop.png')
    print('Saved review/proof_play_state_desktop.png')

if os.path.exists(temp):
    os.remove(temp)

print("Verification script finished.")

