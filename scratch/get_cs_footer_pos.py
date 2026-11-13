import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html = """<script>
window.addEventListener('load', () => {
    const f = document.querySelector('.site-footer');
    const s = document.querySelector('.footer-script');
    const rf = f ? f.getBoundingClientRect() : null;
    const rs = s ? s.getBoundingClientRect() : null;
    document.title = 'FOOTER_POS:' + JSON.stringify({rf, rs, sh: document.body.scrollHeight});
});
</script>"""

with open('coming-soon.html', 'r', encoding='utf-8') as file:
    c = file.read()
temp = os.path.abspath('temp_cs_pos.html')
with open(temp, 'w', encoding='utf-8') as file:
    file.write(c.replace('</body>', html + '</body>'))

cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1440,1500',
    f'file:///{temp.replace(os.sep, "/")}',
    '--dump-dom'
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
for l in res.stdout.splitlines():
    if '<title>FOOTER_POS:' in l:
        print(l)
if os.path.exists(temp):
    os.remove(temp)

