import os
import subprocess
import tempfile

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

html_file = os.path.abspath(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\med-spa-website-design.html")
file_url = f"file:///{html_file.replace(os.sep, '/')}"
out_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch"
temp_profile = os.path.join(out_dir, "edge_profile")
os.makedirs(temp_profile, exist_ok=True)

out_img = os.path.join(out_dir, "render_web_desktop.png")
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    f"--user-data-dir={temp_profile}",
    "--window-size=1440,900",
    f"--screenshot={out_img}",
    file_url
]

try:
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if os.path.exists(out_img):
        print(f"Screenshot success! File size: {os.path.getsize(out_img)} bytes")
    else:
        print("No screenshot file created:", res.stderr)
except Exception as e:
    print("Edge run error:", e)
