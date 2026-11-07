from PIL import Image

def test_crop_aspect(src, aspect_w, aspect_h):
    im = Image.open(src)
    w, h = im.size
    target_ratio = aspect_w / aspect_h
    current_ratio = w / h
    if current_ratio > target_ratio:
        # crop width
        new_w = int(h * target_ratio)
        box = ((w - new_w)//2, 0, (w + new_w)//2, h)
    else:
        # crop height
        new_h = int(w / target_ratio)
        box = (0, int(h * 0.1), w, int(h * 0.1) + new_h)
    crop = im.crop(box)
    s = crop.resize((10, 10)).convert('RGB')
    pix = list(s.getdata())
    r = sum(p[0] for p in pix)//100
    g = sum(p[1] for p in pix)//100
    b = sum(p[2] for p in pix)//100
    lum = int(0.299*r + 0.587*g + 0.114*b)
    return crop.size, (r, g, b), lum

print("Team Founder (hero-lex-portrait 3:4):", test_crop_aspect('assets/hero-lex-portrait.jpg', 3, 4))
print("Team Founder (lex-studio-pose 3:4):", test_crop_aspect('assets/lucci/lex-studio-pose.jpg', 3, 4))
print("Team Right 1 (lucci-bts-shoot 16:10):", test_crop_aspect('assets/lucci/lucci-bts-shoot.jpg', 16, 10))
print("Team Right 1 (behind-the-lens 16:10):", test_crop_aspect('assets/behind-the-lens.webp', 16, 10))
print("Team Right 2 (bot_06 16:10):", test_crop_aspect('assets/archive/bot_06.jpg', 16, 10))
print("Team Right 2 (photo_dec_13 16:10):", test_crop_aspect('assets/lucci/photo_dec_13_2025_2_36_15_pm.jpg', 16, 10))
print("Team Right 2 (top_13 16:10):", test_crop_aspect('assets/archive/top_13.jpg', 16, 10))

