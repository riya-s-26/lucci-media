from PIL import Image

im = Image.open('assets/about/team_laptop.jpg')
print("team_laptop:", im.size, im.mode)

# Let's inspect lucci-bts-shoot.jpg, lucci-bts-studio.jpg, lucci-bts-table.jpg, tsa-team-portrait.jpg
for p in ['assets/lucci/lucci-bts-shoot.jpg', 'assets/lucci/lucci-bts-studio.jpg', 'assets/lucci/lucci-bts-table.jpg', 'assets/tsa/tsa-team-portrait.jpg']:
    try:
        im2 = Image.open(p)
        print(p, im2.size)
    except Exception as e:
        print(p, e)

