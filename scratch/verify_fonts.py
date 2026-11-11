import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html = """<script>
document.fonts.ready.then(() => {
    const el = document.querySelector('.footer-script');
    const ws = document.querySelector('.work-speaks-title');
    const wsem = document.querySelector('.work-speaks-title em');
    const isLoaded = document.fonts.check('16px "Hello January"');
    const res = {
        fontLoadedInBrowser: isLoaded,
        footerScript: el ? window.getComputedStyle(el).fontFamily : null,
        workSpeaks: ws ? window.getComputedStyle(ws).fontFamily : null,
        workSpeaksEm: wsem ? window.getComputedStyle(wsem).fontFamily : null
    };
    document.title = 'RESULT:' + JSON.stringify(res);
});
</script>"""

for page in ['index.html', 'about.html', 'coming-soon.html']:
    with open(page, 'r', encoding='utf-8') as f:
        c = f.read()
    temp = os.path.abspath(f'temp_test_font_{page}')
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
        if '<title>RESULT:' in l:
            print(f'{page:18}: {l}')
    if os.path.exists(temp):
        os.remove(temp)
