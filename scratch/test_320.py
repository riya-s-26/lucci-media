import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open('about.css', 'r', encoding='utf-8') as f:
    orig_css = f.read()

for ls in ['0.02em', '0.08em', '-0.025em']:
    test_rule = f"""
.about-hero-title {{
  margin: 0 0 24px 0;
  font-family: 'ShapiroWideRegular', 'Montserrat', var(--sans);
  font-style: normal;
  font-size: clamp(38px, 4.2vw, 56px);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: {ls};
  color: var(--about-text-dark);
  text-transform: uppercase !important;
}}
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
""".strip(), test_rule.strip())

    with open('about.css', 'w', encoding='utf-8') as f:
        f.write(mod_css)
        
    shot = os.path.abspath(f'scratch/vp_320_{ls}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        '--window-size=320,800', f'--screenshot={shot}',
        'file:///C:/xampp/htdocs/luci/about.html'
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(shot)
    crop = im.crop((0, 100, 320, 600))
    crop.save(f'scratch/crop_320_{ls}.png')
    if os.path.exists(shot):
        os.remove(shot)

# Restore
with open('about.css', 'w', encoding='utf-8') as f:
    f.write(orig_css)

print('320 crops done')

