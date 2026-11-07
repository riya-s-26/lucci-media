from PIL import Image

def summarize(name, path):
    im = Image.open(path)
    w, h = im.size
    print(f"{name} ({w}x{h})")
    # let's describe what is inside by checking color regions
    # top 20%
    top = im.crop((0, 0, w, int(h*0.2))).convert('RGB').resize((1, 1)).getpixel((0,0))
    # bottom 20%
    bot = im.crop((0, int(h*0.8), w, h)).convert('RGB').resize((1, 1)).getpixel((0,0))
    center = im.crop((int(w*0.3), int(h*0.3), int(w*0.7), int(h*0.7))).convert('RGB').resize((1, 1)).getpixel((0,0))
    print(f"  Top: {top}, Center: {center}, Bot: {bot}")

summarize("lex-studio-pose", "assets/lucci/lex-studio-pose.jpg")
summarize("hero-lex-portrait", "assets/hero-lex-portrait.jpg")
summarize("hero-bg-center", "assets/hero-bg-center.jpg")
summarize("lex-portrait-main", "assets/lucci/lex-portrait-main.jpg")

