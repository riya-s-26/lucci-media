import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html = """<script>
window.addEventListener('load', () => {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    
    const results = {};
    for (let fs of [28, 30, 32]) {
        ctx.font = `700 ${fs}px ShapiroWideRegular, Montserrat`;
        results[`${fs}px_normal`] = ctx.measureText('OTHER BRANDS').width;
    }
    document.title = 'MEASURE:' + JSON.stringify(results);
});
</script>"""

temp = os.path.abspath('temp_measure.html')
with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

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
    if '<title>MEASURE:' in l:
        print(l)

if os.path.exists(temp):
    os.remove(temp)

