import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = "file:///C:/xampp/htdocs/luci/about.html"

def capture(w, h, out_name):
    out_path = os.path.abspath(f"review/{out_name}")
    cmd = [
        chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--allow-file-access-from-files", "--hide-scrollbars",
        "--force-prefers-reduced-motion",
        f"--window-size={w},{h}", f"--screenshot={out_path}", file_url
    ]
    subprocess.run(cmd, check=True)
    im = Image.open(out_path)
    print(f"Captured {out_name}: dimensions {im.size}")

os.makedirs("review", exist_ok=True)

capture(1440, 4350, "desktop_about.png")
capture(768, 5670, "tablet_about.png")
capture(390, 7350, "mobile_about.png")

print("All review screenshots generated and verified successfully.")
