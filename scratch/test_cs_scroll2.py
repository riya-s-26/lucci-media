import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open('coming-soon.html', 'r', encoding='utf-8') as f:
    c = f.read()

scroll_code = """<script>
window.addEventListener('load', () => {
    window.scrollTo({top: 2000, behavior: 'instant'});
    document.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('is-visible'));
});
</script>"""

temp = os.path.abspath('temp_cs_scroll2.html')
with open(temp, 'w', encoding='utf-8') as f:
    f.write(c.replace('</body>', scroll_code + '</body>'))

shot = os.path.abspath('scratch/temp_cs_scrolled2.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files',
    '--window-size=1440,900', f'--screenshot={shot}',
    f'file:///{temp.replace(os.sep, "/")}'
]
subprocess.run(cmd, check=True)
im = Image.open(shot)
im.save('scratch/cs_scrolled_to_footer.png')
print('Saved cs_scrolled_to_footer.png')

# Now crop the footer zone from this scrolled view
# The footer is in the lower half of the 900px viewport
crop = im.crop((100, 200, 1340, 700))
crop.save('review/footer_available_worldwide_coming_soon.png')
print('Saved review/footer_available_worldwide_coming_soon.png')

if os.path.exists(temp):
    os.remove(temp)
if os.path.exists(shot):
    os.remove(shot)

