import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with open('index.html', 'r', encoding='utf-8') as f:
    orig_html = f.read()

weights = [400, 500, 600, 700]
sizes = [13, 14, 15]

for w in weights:
    for s in sizes:
        test_css = f"""
        <style>
        .ticker-track > span {{
            font-family: 'ShapiroWideRegular', var(--sans) !important;
            font-weight: {w} !important;
            font-size: {s}px !important;
            letter-spacing: 0.08em !important;
        }}
        </style>
        """
        temp_html = os.path.abspath(f'scratch/test_{w}_{s}.html')
        with open(temp_html, 'w', encoding='utf-8') as f:
            f.write(orig_html.replace('</head>', test_css + '</head>'))
            
        shot = os.path.abspath(f'scratch/shot_{w}_{s}.png')
        cmd = [
            chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
            '--allow-file-access-from-files', '--hide-scrollbars',
            '--force-prefers-reduced-motion',
            '--window-size=1440,1500', f'--screenshot={shot}',
            f'file:///{temp_html.replace(os.sep, "/")}'
        ]
        subprocess.run(cmd, check=True)
        im = Image.open(shot)
        # crop trust band (y: 750 to 950)
        crop = im.crop((0, 750, 1440, 950))
        crop.save(f'scratch/crop_{w}_{s}.png')
        if os.path.exists(temp_html):
            os.remove(temp_html)
        if os.path.exists(shot):
            os.remove(shot)

print('Done rendering variations')

