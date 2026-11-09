from PIL import Image

d_im = Image.open('review/desktop_about.png')
print("Desktop size:", d_im.size)

# 1. Header (stacked logo check)
# Let's crop x: 20 to 220, y: 15 to 95
header_logo = d_im.crop((20, 15, 220, 95))
header_logo.save('scratch/final_proof_header_logo.png')
print("Header logo crop saved.")

# 2. Team section (all 4 profiles)
# y: 2320 to 3000
team_crop = d_im.crop((0, 2320, d_im.width, 3000))
team_crop.save('scratch/final_proof_team_section.png')
print("Team section crop saved.")

# 3. Footer logo
# y: 3100 to 3550
footer_crop = d_im.crop((0, 3100, d_im.width, 3550))
footer_crop.save('scratch/final_proof_footer_logo.png')
print("Footer logo crop saved.")

