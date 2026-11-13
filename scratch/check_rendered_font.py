import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

html = """<script>
window.addEventListener('load', () => {
    const wwdb = document.querySelector('.tsa-services-headline');
    // We can test width of 'WHAT WE DO BEST' in ShapiroWideRegular vs Montserrat
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    
    ctx.font = '700 21px ShapiroWideRegular';
    const w_shapiro = ctx.measureText('WHAT WE DO BEST').width;
    
    ctx.font = '700 21px Montserrat';
    const w_mont = ctx.measureText('WHAT WE DO BEST').width;
    
    ctx.font = '700 21px ShapiroWideRegular, Montserrat';
    const w_actual = ctx.measureText('WHAT WE DO BEST').width;
    
    document.title = 'FONT_CHECK:' + JSON.stringify({w_shapiro, w_mont, w_actual});
});
</script>"""

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

temp = os.path.abspath('temp_fc.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', html + '</body>'))

cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1440,1500',
    f'file:///{temp.replace(os.sep, "/")}',
    '--dump-dom'
]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
for l in res.stdout.splitlines():
    if '<title>FONT_CHECK:' in l:
        print(l)

if os.path.exists(temp):
    os.remove(temp)

