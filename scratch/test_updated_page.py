import subprocess
import os
from PIL import Image

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = "file:///C:/xampp/htdocs/luci/about.html"

# Desktop (1440 x 3600)
desktop_out = os.path.abspath("review/desktop_about.png")
subprocess.run([
    chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--allow-file-access-from-files", "--hide-scrollbars",
    "--window-size=1440,3600", f"--screenshot={desktop_out}", file_url
], check=True)

# Tablet (768 x 4200)
tablet_out = os.path.abspath("review/tablet_about.png")
subprocess.run([
    chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--allow-file-access-from-files", "--hide-scrollbars",
    "--window-size=768,4200", f"--screenshot={tablet_out}", file_url
], check=True)

# Mobile (390 x 5600)
mobile_out = os.path.abspath("review/mobile_about.png")
subprocess.run([
    chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--allow-file-access-from-files", "--hide-scrollbars",
    "--window-size=390,5600", f"--screenshot={mobile_out}", file_url
], check=True)

print("Screenshots captured.")

