# Let's inspect bot_01 through bot_13 and top_01 through top_13 in detail
import os
from PIL import Image

for f in sorted(os.listdir('assets/archive')):
    p = os.path.join('assets/archive', f)
    im = Image.open(p)
    w, h = im.size
    # let's look at average RGB
    s = im.resize((10, 10)).convert('RGB')
    p_data = list(s.getdata())
    r = sum(x[0] for x in p_data)//100
    g = sum(x[1] for x in p_data)//100
    b = sum(x[2] for x in p_data)//100
    lum = int(0.299*r + 0.587*g + 0.114*b)
    print(f"{f:12} {w}x{h} RGB:({r:3},{g:3},{b:3}) Lum:{lum:3}")

