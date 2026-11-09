import subprocess

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
file_url = "file:///C:/xampp/htdocs/luci/about.html"

# Run chrome with --dump-dom to check what HTML is actually rendered
res = subprocess.run([
    chrome_path, "--headless=new", "--disable-gpu", "--no-sandbox",
    "--allow-file-access-from-files", "--dump-dom", file_url
], capture_output=True, text=True)

dom = res.stdout
print("DOM length:", len(dom))
for phrase in ["about-team-section", "about-team-grid", "LEX LUCIANO", "SOPH", "NICOLE", "DEANDRA"]:
    print(phrase, "in DOM?:", phrase in dom)

