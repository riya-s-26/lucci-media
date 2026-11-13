import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html = """<script>
window.addEventListener('load', () => {
    const el = document.querySelector('.footer-meta-center');
    const r = el ? el.getBoundingClientRect() : null;
    document.title = 'BBOX:' + JSON.stringify(r);
});
</script>"""

for page, height in [('index.html', 9500), ('about.html', 4500), ('coming-soon.html', 2400)]:
    with open(page, 'r', encoding='utf-8') as f:
        c = f.read()
    temp = os.path.abspath(f'temp_bbox_{page}')
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
        if '<title>BBOX:' in l:
            print(f'{page}: {l}')
    if os.path.exists(temp):
        os.remove(temp)

