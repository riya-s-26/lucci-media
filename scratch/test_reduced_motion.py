import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = "file:///C:/xampp/htdocs/luci/about.html"
desktop_out = os.path.abspath("scratch/test_reduced_motion.png")

cmd = [
    chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--allow-file-access-from-files", "--hide-scrollbars",
    "--force-prefers-reduced-motion",
    "--window-size=1440,3600", f"--screenshot={desktop_out}", file_url
]
subprocess.run(cmd, check=True)

im = Image.open(desktop_out).convert('RGB')
print("Image size:", im.size)
for y in range(0, im.height, 200):
    box = im.crop((0, y, im.width, min(im.height, y + 200)))
    dark_count = sum(1 for p in box.getdata() if p[0] < 50 and p[1] < 50 and p[2] < 50)
    print(f"y={y:4d} to {y+200:4d}: dark pixels = {dark_count:6d}")

