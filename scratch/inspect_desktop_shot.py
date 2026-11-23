from PIL import Image

desktop = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\render_web_desktop.png")
print("Desktop screenshot size:", desktop.size)

# Let's check dimensions of elements in desktop screenshot
# It captured 1440x900 viewport (header + announcement bar + hero + start of what's included)
# Let's save a reduced version in artifacts directory so it can be viewed if desired
thumb = desktop.resize((720, 450), Image.Resampling.LANCZOS)
thumb.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\web_desktop_preview.jpg", quality=85)

print("Saved preview thumbnail.")
