import subprocess, os, json

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = """<script>
window.addEventListener('load', () => {
    document.querySelectorAll('[data-reveal]').forEach(el => {
        el.style.opacity = '1';
        el.style.transform = 'none';
        el.style.visibility = 'visible';
    });
    const sparkle = document.querySelector('.studio-sparkle');
    const copy = document.querySelector('.studio-copy');
    const rS = sparkle ? sparkle.getBoundingClientRect() : null;
    const rC = copy ? copy.getBoundingClientRect() : null;
    const cs = sparkle ? window.getComputedStyle(sparkle) : null;
    document.title = 'SPARKLE_CHECK:' + JSON.stringify({
        rect: rS ? {left: rS.left, top: rS.top + window.scrollY, width: rS.width, height: rS.height} : null,
        copyRect: rC ? {left: rC.left, top: rC.top + window.scrollY, width: rC.width, height: rC.height} : null,
        display: cs ? cs.display : null,
        visibility: cs ? cs.visibility : null,
        opacity: cs ? cs.opacity : null,
        overflow: copy ? window.getComputedStyle(copy).overflow : null
    });
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

temp = os.path.abspath('temp_check_sparkle.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', html + '</body>'))

cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=390,13500',
    '--dump-dom',
    'file:///' + temp.replace('\\', '/')
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
for l in res.stdout.splitlines():
    if '<title>SPARKLE_CHECK:' in l:
        print(l)

if os.path.exists(temp):
    os.remove(temp)

