import subprocess, os, json
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
os.makedirs('review', exist_ok=True)

# Helper script to force reveal elements
reveal_script = """<script>
window.addEventListener('load', () => {
    document.querySelectorAll('[data-reveal]').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
        el.style.visibility = 'visible';
    });
});
</script>"""

pages = ['index.html', 'about.html', 'coming-soon.html']
devices = [
    ('desktop', 1440, 1000),
    ('ipad', 820, 1180),
    ('iphone', 390, 844)
]

# 1. Capture viewport screenshots of hero & CTA areas
for page in pages:
    base = page.replace('.html', '')
    with open(page, 'r', encoding='utf-8') as f:
        c = f.read()
    temp = os.path.abspath(f'temp_v_{page}')
    with open(temp, 'w', encoding='utf-8') as f:
        f.write(c.replace('</body>', reveal_script + '</body>'))
        
    for dev_name, w, h in devices:
        shot = os.path.abspath(f'review/{base}_{dev_name}.png')
        cmd = [
            chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
            '--allow-file-access-from-files', '--hide-scrollbars',
            '--force-prefers-reduced-motion',
            f'--window-size={w},{h}',
            f'--screenshot={shot}',
            'file:///' + temp.replace('\\', '/')
        ]
        subprocess.run(cmd, capture_output=True)
        print(f'Captured review/{base}_{dev_name}.png')
        
    if os.path.exists(temp):
        os.remove(temp)

print("Device verification complete.")

