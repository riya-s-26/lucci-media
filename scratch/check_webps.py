from PIL import Image

for f in ['product-content.webp', 'brown-sugar-skin.webp', 'behind-the-lens.webp', 'on-set.webp', 'studio-story.webp']:
    im = Image.open('assets/' + f)
    w, h = im.size
    print(f"{f:22} {w}x{h}")

