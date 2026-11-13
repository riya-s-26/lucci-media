import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html = """<script>
window.addEventListener('load', () => {
    const f = document.querySelector('.site-footer');
    document.title = 'OPACITY:' + (f ? window.getComputedStyle(f).opacity : 'no footer');
});
</script>"""

with open('coming-soon.html', 'r', encoding='utf-8') as file:
    c = file.read()
temp = os.path.abspath('temp_op.html')
with open(temp, 'w', encoding='utf-8') as file:
    file.write(c.replace('</body>', html + '</body>'))

cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    f'--window-size=1440,2000',
    f'file:///{temp.replace(os.sep, "/")}',
    '--dump-dom'
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
for l in res.stdout.splitlines():
    if '<title>OPACITY:' in l:
        print(l)
if os.path.exists(temp):
    os.remove(temp)

