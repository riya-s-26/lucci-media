import subprocess
import os
from PIL import Image

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
os.makedirs('review', exist_ok=True)

pages = [
    ('index.html', 9500),
    ('about.html', 4420),
    ('coming-soon.html', 2400)
]

for page, height in pages:
    shot = os.path.abspath(f'scratch/temp_proof_{page}.png')
    cmd = [
        chrome_path, '--headless=new', '--disable-gpu', '--no-sandbox',
        '--allow-file-access-from-files', '--hide-scrollbars',
        '--force-prefers-reduced-motion',
        f'--window-size=1440,{height}', f'--screenshot={shot}',
        f'file:///C:/xampp/htdocs/luci/{page}'
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(shot)
    
    if page == 'index.html':
        # Crop work speaks
        crop_ws = im.crop((80, 2900, 650, 3350))
        crop_ws.save('review/proof_work_speaks.png')
        print('Saved review/proof_work_speaks.png')
        
        # Crop index footer metadata
        crop_f = im.crop((200, 8700, 1240, 9150))
        crop_f.save('review/proof_index_footer.png')
        print('Saved review/proof_index_footer.png')
        
    elif page == 'about.html':
        # Crop about footer metadata
        crop_f = im.crop((200, im.height - 650, 1240, im.height - 200))
        crop_f.save('review/proof_about_footer.png')
        print('Saved review/proof_about_footer.png')
        
    elif page == 'coming-soon.html':
        # Crop coming soon footer metadata
        # Find dark pixels
        coords = [(x, y) for y in range(im.height - 600, im.height) for x in range(300, 1140) if im.getpixel((x, y))[0] < 50]
        if coords:
            min_y = min(p[1] for p in coords)
            max_y = max(p[1] for p in coords)
            crop_f = im.crop((200, max(0, min_y - 120), 1240, min(im.height, max_y + 160)))
        else:
            crop_f = im.crop((200, 1500, 1240, 2100))
        crop_f.save('review/proof_coming_soon_footer.png')
        print('Saved review/proof_coming_soon_footer.png')
        
    if os.path.exists(shot):
        os.remove(shot)

print('All proofs captured successfully.')

