import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = "file:///C:/xampp/htdocs/luci/about.html"
mobile_out = os.path.abspath("review/mobile_about.png")

cmd_mobile = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--allow-file-access-from-files",
    "--hide-scrollbars",
    "--window-size=390,6800",
    f"--screenshot={mobile_out}",
    file_url
]
subprocess.run(cmd_mobile, check=True)

for i in [4800, 5400, 6000, 6400]:
    slice_img = Image.open(mobile_out).crop((0, i, 390, min(6800, i + 400)))
    slice_img.save(f'scratch/mobile_slice_{i}.png')
    pixels = list(slice_img.getdata())
    non_white = sum(1 for p in pixels if p[0] < 245 or p[1] < 245 or p[2] < 245)
    print(f"Slice {i}: non-white = {non_white} ({non_white / len(pixels) * 100:.1f}%)")

