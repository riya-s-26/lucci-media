from PIL import Image

im1 = Image.open('scratch/ref_hero_img.png').convert('RGB')
im2 = Image.open('assets/lucci/lex-studio-pose.jpg').convert('RGB')
im3 = Image.open('assets/hero-lex-portrait.jpg').convert('RGB')
im4 = Image.open('assets/about/about_portrait.jpg').convert('RGB')

print("Ref Hero avg:", [sum(x[i] for x in im1.resize((10,10)).getdata())//100 for i in range(3)])
print("lex-studio-pose avg:", [sum(x[i] for x in im2.resize((10,10)).getdata())//100 for i in range(3)])
print("hero-lex-portrait avg:", [sum(x[i] for x in im3.resize((10,10)).getdata())//100 for i in range(3)])
print("about_portrait avg:", [sum(x[i] for x in im4.resize((10,10)).getdata())//100 for i in range(3)])

