import subprocess, os, json
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = """<script>
window.addEventListener('load', () => {
    const list = [
        {name: 'header_cta', el: document.querySelector('.header-cta span')},
        {name: 'hero_btn', el: document.querySelector('.hero-actions .button-light span')},
        {name: 'archive_btn', el: document.querySelector('.archive-work-btn')},
        {name: 'text_link', el: document.querySelector('.text-link span')},
        {name: 'tsa_banner', el: document.querySelector('.tsa-cta-arrow')}
    ];
    const res = {};
    list.forEach(item => {
        if (item.el) {
            const r = item.el.getBoundingClientRect();
            const cs = window.getComputedStyle(item.el);
            res[item.name] = {
                w: r.width, h: r.height,
                fontSize: cs.fontSize,
                lineHeight: cs.lineHeight,
                fontFamily: cs.fontFamily
            };
        }
    });
    document.title = 'ARROW_METRICS:' + JSON.stringify(res);
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

temp = os.path.abspath('temp_metrics.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', html + '</body>'))

cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1440,900',
    '--dump-dom',
    'file:///' + temp.replace('\\', '/')
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
for l in res.stdout.splitlines():
    if '<title>ARROW_METRICS:' in l:
        print(l)

if os.path.exists(temp):
    os.remove(temp)

