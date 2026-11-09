from PIL import Image

im = Image.open('scratch/test_reduced_motion.png')

# 1. Header crop (stacked logo)
im.crop((0, 0, 1440, 120)).save('scratch/proof_final_header_stacked.png')

# 2. Team section crop
im.crop((0, 2350, 1440, 3050)).save('scratch/proof_final_team.png')

# 3. Footer crop (horizontal logo)
im.crop((0, 3050, 1440, 3550)).save('scratch/proof_final_footer.png')

print("Proofs saved.")

