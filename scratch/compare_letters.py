from PIL import Image

im_ref = Image.open('scratch/user_ref1_isolated.png')
print("Ref size:", im_ref.size)

# Let's inspect the master logo in assets
im_master = Image.open('assets/lucci-client-logo-black.png')
# Top is LUCCI, Bottom is MEDIA
top_crop = im_master.crop((29, 0, 1258, 344))
bot_crop = im_master.crop((0, 344, 1316, 688))

print("Master LUCCI size:", top_crop.size)
print("Master MEDIA size:", bot_crop.size)

# In ref 1, what is the height ratio between LUCCI and MEDIA?
# Let's inspect the heights of LUCCI and MEDIA in Ref 1:

