from PIL import Image

im1 = Image.open('assets/about/team_studio_chair.jpg')
im2 = Image.open('assets/about/hero_lex.jpg')
print("team_studio_chair:", im1.size)
print("hero_lex:", im2.size)

# Are they identical bytes?
with open('assets/about/team_studio_chair.jpg', 'rb') as f1, open('assets/about/hero_lex.jpg', 'rb') as f2:
    b1 = f1.read()
    b2 = f2.read()
    print("Exact same bytes?:", b1 == b2)

