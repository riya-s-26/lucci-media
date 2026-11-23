import os
from PIL import Image

db_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\dropbox_photos"
files = [f for f in os.listdir(db_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

out_html = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\view_dropbox_photos.html"

cards = []
thumbs_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\db_thumbs"
os.makedirs(thumbs_dir, exist_ok=True)

for i, f in enumerate(files):
    p = os.path.join(db_dir, f)
    try:
        im = Image.open(p)
        # Create thumbnail
        t_path = os.path.join(thumbs_dir, f"thumb_{i}.jpg")
        im_thumb = im.copy()
        im_thumb.thumbnail((300, 300))
        im_thumb.convert('RGB').save(t_path, "JPEG", quality=75)
        
        cards.append(f"""
        <div style="border: 1px solid #ccc; padding: 10px; margin: 10px; width: 320px; display: inline-block; vertical-align: top; font-family: sans-serif; font-size: 12px;">
            <img src="db_thumbs/thumb_{i}.jpg" style="width: 100%; height: 200px; object-fit: cover;">
            <p><strong>{f}</strong></p>
            <p>Size: {im.size[0]}x{im.size[1]} ({os.path.getsize(p)} bytes)</p>
        </div>
        """)
    except Exception as e:
        print(f"Error {f}: {e}")

html_content = f"""<!doctype html>
<html>
<head><title>Dropbox Photos Gallery</title></head>
<body>
<h1>Dropbox Photos Catalog ({len(files)} items)</h1>
{"".join(cards)}
</body>
</html>"""

with open(out_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Gallery written to {out_html}")
