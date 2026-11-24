from PIL import Image

# Option A: IMG_2600.jpg (4 models beauty shot, cropped across faces)
im_models = Image.open('scratch/dropbox_extracted/Work/IMG_2600.jpg')
# Size is 4235 x 6352. The faces are in the upper-middle area (y: 1200 to 3600)
# A wide banner aspect ratio is ~710:168 (~4.2:1) or ~3:1
w, h = im_models.size
# Crop wide banner around faces
crop_models = im_models.crop((200, 1400, 4000, 2700))
crop_models.thumbnail((1200, 400))
crop_models.save('scratch/proof_option_models.jpg', quality=90)

# Option B: DSC06394.JPG (Model in leather jacket holding luxury skincare bottles)
im_prod = Image.open('scratch/dropbox_extracted/Work/DSC06394.JPG')
# Size: 4672 x 7008. Skincare bottles are in hands at y: 2200 to 4500
crop_prod = im_prod.crop((500, 2400, 4200, 4200))
crop_prod.thumbnail((1200, 400))
crop_prod.save('scratch/proof_option_products.jpg', quality=90)

# Option C: IMG_5893.JPG (ZO luxury skincare bottles)
im_zo = Image.open('scratch/dropbox_extracted/Work/IMG_5893.JPG')
# Size: 2400 x 3600.
crop_zo = im_zo.crop((100, 1000, 2300, 2200))
crop_zo.thumbnail((1200, 400))
crop_zo.save('scratch/proof_option_zo.jpg', quality=90)

print('Generated proof banner options.')
