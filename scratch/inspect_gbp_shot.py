from PIL import Image

im = Image.open(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\render_gbp_desktop.png")
print("Desktop screenshot size:", im.size)
thumb = im.resize((720, 450), Image.Resampling.LANCZOS)
thumb.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_desktop_preview.jpg", quality=85)
print("Saved gbp_desktop_preview.jpg")
