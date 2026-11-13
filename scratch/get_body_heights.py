import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html = """<script>
window.addEventListener('load', () => {
    const el = document.querySelector('.footer-script');
    const b = el ? el.getBoundingClientRect() : null;
    document.title = 'INFO:' + JSON.stringify({h: document.body.scrollHeight, b: b});
});
</script>"""

for p in ['index.html', 'about.html', 'coming-soon.html']:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    temp = os.path.abspath(f'temp_sh_{p}')
    with open(temp, 'w', encoding='utf-8') as f:
        f.write(c.replace('</body>', html + '</body>'))
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files',
        f'file:///{temp.replace(os.sep, "/")}',
        '--dump-dom'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    for l in res.stdout.splitlines():
        if '<title>INFO:' in l:
            print(f'{p:18}: {l}')
    if os.path.exists(temp):
        os.remove(temp)

