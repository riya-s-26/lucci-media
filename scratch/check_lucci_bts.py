from PIL import Image

for p in ['assets/lucci/lucci-bts-shoot.jpg', 'assets/lucci/lucci-bts-studio.jpg', 'assets/lucci/lucci-bts-table.jpg']:
    im = Image.open(p)
    print(f"{p}: size={im.size}")

