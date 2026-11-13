import subprocess
import os
from PIL import Image, ImageDraw

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

# Let's capture the exact full index page to be 100% sure
shot = os.path.abspath('scratch/temp_idx.png')
cmd = [
    chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
    '--allow-file-access-from-files', '--hide-scrollbars',
    '--force-prefers-reduced-motion',
    '--window-size=1440,2500', f'--screenshot={shot}',
    'file:///C:/xampp/htdocs/luci/index.html'
]
subprocess.run(cmd, check=True)
im_full = Image.open(shot)

# Crop actual WWDB headline (top: 1653, bottom: 1679)
im_wwdb = im_full.crop((80, 1640, 600, 1700))

# Now let's test weights 400, 500, 700 with styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    orig_css = f.read()

ticker_crops = {}
for w in [400, 500, 700]:
    rule = f".ticker-track > span {{ color: #55504B; font-family: 'ShapiroWideRegular', var(--sans); font-size: 14px; font-weight: {w}; line-height: 1.7; letter-spacing: .08em; text-transform: uppercase; }}"
    test_css = orig_css.replace(".ticker-track > span { color: #55504B; font: 400 16px/1.7 var(--typewriter); letter-spacing: .04em; }", rule)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(test_css)
        
    s_shot = os.path.abspath(f'scratch/temp_t_{w}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        '--window-size=1440,2500', f'--screenshot={s_shot}',
        'file:///C:/xampp/htdocs/luci/index.html'
    ]
    subprocess.run(cmd, check=True)
    im_t = Image.open(s_shot)
    ticker_crops[w] = im_t.crop((740, 850, 1440, 905))
    if os.path.exists(s_shot):
        os.remove(s_shot)

# Restore styles.css
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(orig_css)

# Build clean canvas
canvas = Image.new('RGB', (720, 360), '#FBFBFB')
draw = ImageDraw.Draw(canvas)

draw.text((20, 15), "1. Actual 'WHAT WE DO BEST' heading on page:", fill='#231E1B')
canvas.paste(im_wwdb, (20, 35))

draw.text((20, 105), "2. Ticker with font-weight: 400 (Regular):", fill='#231E1B')
canvas.paste(ticker_crops[400], (20, 125))

draw.text((20, 185), "3. Ticker with font-weight: 500 (Medium):", fill='#231E1B')
canvas.paste(ticker_crops[500], (20, 205))

draw.text((20, 265), "4. Ticker with font-weight: 700 (Bold):", fill='#231E1B')
canvas.paste(ticker_crops[700], (20, 285))

canvas.save('scratch/compare_perfect.png')
print('Comparison saved to scratch/compare_perfect.png')

