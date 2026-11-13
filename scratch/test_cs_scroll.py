import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Let's create a temp html with a small scroll trigger
with open('coming-soon.html', 'r', encoding='utf-8') as f:
    c = f.read()

scroll_code = """<script>
window.addEventListener('load', () => {
    window.scrollTo(0, 1000);
    setTimeout(() => {
        document.title = 'SCROLLED';
    }, 200);
});
</script>"""

temp = os.path.abspath('temp_cs_scroll.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', scroll_code + '</body>'))

shot = os.path.abspath('scratch/temp_cs_scrolled.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1440,900', f'--screenshot={shot}',
    f'file:///{temp.replace(os.sep, "/")}'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)
im.save('scratch/cs_scrolled_viewport.png')
print('Saved cs_scrolled_viewport.png')

if os.path.exists(temp):
    os.remove(temp)
if os.path.exists(shot):
    os.remove(shot)

