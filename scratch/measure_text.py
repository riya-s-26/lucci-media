from PIL import Image
import numpy as np

im_t = Image.open('scratch/user_ref_ticker.png').convert('L')
im_w = Image.open('scratch/user_ref_wwdb.png').convert('L')

print('Ticker image size:', im_t.size)
print('WWDB image size:', im_w.size)

