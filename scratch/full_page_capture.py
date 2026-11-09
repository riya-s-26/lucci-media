import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = "file:///C:/xampp/htdocs/luci/about.html"

# Desktop: let's test with height 3600
desktop_out = os.path.abspath("review/desktop_about.png")
cmd_desktop = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--allow-file-access-from-files",
    "--hide-scrollbars",
    "--window-size=1440,3600",
    f"--screenshot={desktop_out}",
    file_url
]
subprocess.run(cmd_desktop, check=True)

# Mobile: test with width 390, height 4800
mobile_out = os.path.abspath("review/mobile_about.png")
cmd_mobile = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--allow-file-access-from-files",
    "--hide-scrollbars",
    "--window-size=390,4800",
    f"--screenshot={mobile_out}",
    file_url
]
subprocess.run(cmd_mobile, check=True)

print("Screenshots captured successfully.")

