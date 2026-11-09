from PIL import Image

im = Image.open('scratch/final_proof_header_logo.png').convert('RGB')
dark = sum(1 for p in im.getdata() if p[0] < 50 and p[1] < 50 and p[2] < 50)
print("Header logo dark pixels:", dark)

