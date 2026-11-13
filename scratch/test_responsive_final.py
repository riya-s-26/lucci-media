import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open('about.css', 'r', encoding='utf-8') as f:
    orig_css = f.read()

test_base = """
.about-hero-title {
  margin: 0 0 24px 0;
  font-family: 'ShapiroWideRegular', 'Montserrat', var(--sans);
  font-style: normal;
  font-size: clamp(38px, 4.2vw, 56px);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: 0.02em;
  color: var(--about-text-dark);
  text-transform: uppercase !important;
}
"""

test_media = """
@media (max-width: 540px) {
  .about-hero-title {
    font-size: clamp(28px, 8.2vw, 32px);
    letter-spacing: 0;
  }
"""

mod_css = orig_css.replace("""
.about-hero-title {
  margin: 0 0 24px 0;
  font-family: var(--sans);
  font-style: italic;
  font-size: clamp(38px, 4.2vw, 56px);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -0.025em;
  color: var(--about-text-dark);
  text-transform: uppercase !important;
}
""".strip(), test_base.strip())

mod_css = mod_css.replace("""
@media (max-width: 540px) {
  .about-hero-title {
    font-size: 32px;
  }
""".strip(), test_media.strip())

with open('about.css', 'w', encoding='utf-8') as f:
    f.write(mod_css)

for w, h, name in [(1440, 1000, 'desk_1440'), (1024, 1000, 'tab_1024'), (768, 1000, 'tab_768'), (390, 844, 'mob_390'), (320, 600, 'mob_320')]:
    shot = os.path.abspath(f'scratch/check_{name}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        f'--window-size={w},{h}', f'--screenshot={shot}',
        'file:///C:/xampp/htdocs/luci/about.html'
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(shot)
    crop = im.crop((0, 80, min(w, 800), 550))
    crop.save(f'scratch/final_crop_{name}.png')
    if os.path.exists(shot):
        os.remove(shot)

# Restore
with open('about.css', 'w', encoding='utf-8') as f:
    f.write(orig_css)

print('Rendered all test crops')

