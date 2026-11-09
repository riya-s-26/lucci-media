import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = "file:///C:/xampp/htdocs/luci/about.html"
desktop_out = os.path.abspath("review/desktop_about.png")
mobile_out = os.path.abspath("review/mobile_about.png")

# Desktop screenshot
cmd_desktop = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--allow-file-access-from-files",
    "--window-size=1440,3400",
    f"--screenshot={desktop_out}",
    file_url
]
print("Capturing desktop...")
res_d = subprocess.run(cmd_desktop, capture_output=True, text=True)
print("Desktop result:", res_d.returncode, "Output exists:", os.path.exists(desktop_out))
if os.path.exists(desktop_out):
    print("Desktop screenshot size:", os.path.getsize(desktop_out))

# Mobile screenshot
cmd_mobile = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--allow-file-access-from-files",
    "--window-size=390,4200",
    f"--screenshot={mobile_out}",
    file_url
]
print("Capturing mobile...")
res_m = subprocess.run(cmd_mobile, capture_output=True, text=True)
print("Mobile result:", res_m.returncode, "Output exists:", os.path.exists(mobile_out))
if os.path.exists(mobile_out):
    print("Mobile screenshot size:", os.path.getsize(mobile_out))

