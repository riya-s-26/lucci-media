import subprocess, os, json

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = """<script>
window.addEventListener('load', () => {
    const wide = [];
    document.querySelectorAll('*').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.width > 400 && el.tagName !== 'HTML' && el.tagName !== 'BODY' && el.tagName !== 'MAIN') {
            wide.push({tag: el.tagName, cls: el.className, id: el.id, w: Math.round(r.width)});
        }
    });
    document.title = 'WIDE_ELS:' + JSON.stringify(wide.slice(0, 10));
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

temp = os.path.abspath('temp_wide.html')
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
    if '<title>WIDE_ELS:' in l:
        print(l)

if os.path.exists(temp):
    os.remove(temp)

