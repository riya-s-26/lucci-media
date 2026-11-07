from PIL import Image

for f in [
    'hero_lex.jpg',
    'story_treatment_room.jpg',
    'story_bottles.jpg',
    'story_cream.jpg',
    'how_we_think_camera.jpg',
    'team_lex.jpg',
    'team_studio_chair.jpg',
    'team_laptop.jpg'
]:
    p = 'assets/about/' + f
    im = Image.open(p)
    w, h = im.size
    s = im.resize((10, 10)).convert('RGB')
    pix = list(s.getdata())
    r = sum(x[0] for x in pix)//100
    g = sum(x[1] for x in pix)//100
    b = sum(x[2] for x in pix)//100
    lum = int(0.299*r + 0.587*g + 0.114*b)
    print(f"{f:26} {w}x{h}  RGB: ({r:3},{g:3},{b:3})  Lum: {lum:3}")

