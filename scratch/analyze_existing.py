import os
from PIL import Image

def analyze_img(path, name):
    im = Image.open(path)
    print(f"=== {name} ({im.size}) ===")
    # sample some corner and center pixels
    print("  center pixel:", im.getpixel((im.width//2, im.height//2)))
    # save thumbnail in scratch for review
    im.thumbnail((200, 200))
    im.save(rf"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\{name}.png")

analyze_img(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\website-design-preview.jpg", "preview_thumb")
analyze_img(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\website-design-who-for.webp", "who_thumb")
analyze_img(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\website-design-hero-main.webp", "hero_main_thumb")
