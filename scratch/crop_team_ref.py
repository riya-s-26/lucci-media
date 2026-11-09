from PIL import Image

ref_im = Image.open('C:/Users/riyas/.gemini/antigravity/brain/91a1ccde-d165-4dfe-810e-513091b2e231/.user_uploaded/media_1794049842470_6953d09f.jpg')
W, H = ref_im.size

# In ref_im, let's find the exact coordinates of the studio chair image and laptop image in Section .04
# Section .04 is near bottom (around y=800 to 950)
chair_crop = ref_im.crop((524, 807, 655, 876))
laptop_crop = ref_im.crop((524, 882, 655, 950))

print("Chair crop size:", chair_crop.size)
print("Laptop crop size:", laptop_crop.size)

chair_crop.save('scratch/chair_crop_test.png')
laptop_crop.save('scratch/laptop_crop_test.png')

