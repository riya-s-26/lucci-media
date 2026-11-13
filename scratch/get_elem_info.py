import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html = """<script>
window.addEventListener('load', () => {
    const wwdb = document.querySelector('.tsa-services-headline');
    const ticker = document.querySelector('.ticker-track');
    const b_wwdb = wwdb ? wwdb.getBoundingClientRect() : null;
    const b_ticker = ticker ? ticker.getBoundingClientRect() : null;
    const cs_wwdb = wwdb ? {
        fontFamily: window.getComputedStyle(wwdb).fontFamily,
        fontSize: window.getComputedStyle(wwdb).fontSize,
        fontWeight: window.getComputedStyle(wwdb).fontWeight,
        letterSpacing: window.getComputedStyle(wwdb).letterSpacing
    } : null;
    const cs_ticker = ticker ? {
        fontFamily: window.getComputedStyle(ticker.querySelector('span')).fontFamily,
        fontSize: window.getComputedStyle(ticker.querySelector('span')).fontSize,
        fontWeight: window.getComputedStyle(ticker.querySelector('span')).fontWeight,
        letterSpacing: window.getComputedStyle(ticker.querySelector('span')).letterSpacing
    } : null;
    document.title = 'INFO:' + JSON.stringify({b_wwdb, b_ticker, cs_wwdb, cs_ticker});
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

temp = os.path.abspath('temp_info.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', html + '</body>'))

for vp, w, h in [('desktop', 1440, 3000), ('mobile', 390, 4000)]:
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files',
        f'--window-size={w},{h}',
        f'file:///{temp.replace(os.sep, "/")}',
        '--dump-dom'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    for l in res.stdout.splitlines():
        if '<title>INFO:' in l:
            print(f'{vp}: {l}')

if os.path.exists(temp):
    os.remove(temp)

