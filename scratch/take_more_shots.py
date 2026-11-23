import os
import subprocess

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

html_file = os.path.abspath(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\med-spa-website-design.html")
file_url = f"file:///{html_file.replace(os.sep, '/')}"
out_dir = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch"
temp_profile = os.path.join(out_dir, "edge_profile")

viewports = [
    ("tablet", 1024, 768),
    ("mobile", 390, 844)
]

for name, w, h in viewports:
    out_img = os.path.join(out_dir, f"render_web_{name}.png")
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--user-data-dir={temp_profile}",
        f"--window-size={w},{h}",
        f"--screenshot={out_img}",
        file_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    if os.path.exists(out_img):
        print(f"{name} screenshot success: {os.path.getsize(out_img)} bytes")
    else:
        print(f"Failed {name}: {res.stderr}")

print("All screenshots generated successfully!")
