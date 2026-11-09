from PIL import Image

def find_content_bottom(img_path):
    im = Image.open(img_path).convert('RGB')
    bg = im.getpixel((0, im.height - 1))
    print(f"{img_path}: bottom pixel color is {bg}")
    # scan up from bottom
    for y in range(im.height - 1, 0, -1):
        row = [im.getpixel((x, y)) for x in range(0, im.width, 10)]
        # if any pixel differs significantly from bg
        if any(abs(p[0] - bg[0]) > 10 or abs(p[1] - bg[1]) > 10 or abs(p[2] - bg[2]) > 10 for p in row):
            return y
    return im.height

print("Desktop content bottom:", find_content_bottom('review/desktop_about.png'))
print("Mobile content bottom:", find_content_bottom('review/mobile_about.png'))

