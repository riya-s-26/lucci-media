from PIL import Image
import os

img_path = r'C:/Users/riyas/.gemini/antigravity/brain/91a1ccde-d165-4dfe-810e-513091b2e231/.user_uploaded/media_1794557249082_e1969981.jpg'
im = Image.open(img_path)
print('User screenshot size:', im.size)

# Ticker is near the top (around y = 120 to 220)
ticker_crop = im.crop((0, 100, im.width, 220))
ticker_crop.save('scratch/user_ref_ticker.png')

# "WHAT WE DO BEST" is near the bottom (around y = 740 to 860)
wwdb_crop = im.crop((0, 750, im.width, 870))
wwdb_crop.save('scratch/user_ref_wwdb.png')
print('Saved user_ref_ticker.png and user_ref_wwdb.png')

