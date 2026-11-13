import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Let's create a temporary html that scrolls to footer so IntersectionObserver reveals it
with open('coming-soon.html', 'r', encoding='utf-8') as f:
    c = f.read()

scroll_script = """<script>
window.addEventListener('load', () => {
    document.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('is-revealed'));
});
</script>"""

temp = os.path.abspath('temp_cs_reveal.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', scroll_script + '</body>'))

shot = os.path.abspath('scratch/temp_cs_revealed_shot.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--window-size=1440,2000', f'--screenshot={shot}',
    f'file:///{temp.replace(os.sep, "/")}'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)
# rs was at y=1530
crop = im.crop((100, 1460, 1340, 1620))
crop.save('review/footer_available_worldwide_coming_soon.png')
print('Saved revealed coming-soon footer crop')

if os.path.exists(temp):
    os.remove(temp)
if os.path.exists(shot):
    os.remove(shot)

