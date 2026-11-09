import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def capture(page_file, w, h, out_name):
    out_path = os.path.abspath(f"review/{out_name}")
    url = f"file:///C:/xampp/htdocs/luci/{page_file}"
    cmd = [
        chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--allow-file-access-from-files", "--hide-scrollbars",
        "--force-prefers-reduced-motion",
        f"--window-size={w},{h}", f"--screenshot={out_path}", url
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(out_path)
    print(f"Captured {out_name}: size {im.size}")
    return im

os.makedirs("review", exist_ok=True)

# 1. Full About page screenshots
im_d = capture("about.html", 1440, 4420, "desktop_about.png")
im_t = capture("about.html", 768, 5700, "tablet_about.png")
im_m = capture("about.html", 390, 7450, "mobile_about.png")

# 2. About footer preview
im_ab_footer = im_d.crop((0, im_d.height - 460, im_d.width, im_d.height))
im_ab_footer.save("review/about_footer_preview.png")
print("Saved review/about_footer_preview.png")

# 3. Index footer preview
idx_shot = os.path.abspath("scratch/temp_idx_shot.png")
cmd_idx = [
    chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--allow-file-access-from-files", "--hide-scrollbars",
    "--force-prefers-reduced-motion",
    "--window-size=1440,9500", f"--screenshot={idx_shot}",
    "file:///C:/xampp/htdocs/luci/index.html"
]
subprocess.run(cmd_idx, check=True)
im_idx = Image.open(idx_shot)
# Footer starts around y=8650 on index.html
im_idx_footer = im_idx.crop((0, 8640, im_idx.width, 9160))
im_idx_footer.save("review/index_footer_preview.png")
print("Saved review/index_footer_preview.png")

# 4. Coming soon footer preview
cs_shot = os.path.abspath("scratch/temp_cs_shot.png")
cmd_cs = [
    chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--allow-file-access-from-files", "--hide-scrollbars",
    "--force-prefers-reduced-motion",
    "--window-size=1440,2400", f"--screenshot={cs_shot}",
    "file:///C:/xampp/htdocs/luci/coming-soon.html"
]
subprocess.run(cmd_cs, check=True)
im_cs = Image.open(cs_shot)
# Find the footer in coming soon (around y=1900..2400)
coords = [(x, y) for y in range(im_cs.height - 600, im_cs.height) for x in range(400, 1040) if im_cs.getpixel((x, y))[0] < 50]
if coords:
    min_y = min(p[1] for p in coords)
    max_y = max(p[1] for p in coords)
    im_cs_footer = im_cs.crop((0, max(0, min_y - 120), im_cs.width, min(im_cs.height, max_y + 160)))
    im_cs_footer.save("review/coming_soon_footer_preview.png")
    print("Saved review/coming_soon_footer_preview.png")

print("All review deliverables regenerated successfully.")
