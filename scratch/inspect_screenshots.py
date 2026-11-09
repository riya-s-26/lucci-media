from PIL import Image

d_im = Image.open('review/desktop_about.png')
m_im = Image.open('review/mobile_about.png')

print("Desktop screenshot dimensions:", d_im.size)
print("Mobile screenshot dimensions:", m_im.size)

# Let's crop header from desktop to check the horizontal logo
header_crop = d_im.crop((0, 0, d_im.width, 160))
header_crop.save('scratch/review_header.png')

# Let's crop hero
hero_crop = d_im.crop((0, 160, d_im.width, 800))
hero_crop.save('scratch/review_hero.png')

# Let's crop Our Story section
story_crop = d_im.crop((0, 800, d_im.width, 1400))
story_crop.save('scratch/review_story.png')

# Let's crop Team section
team_crop = d_im.crop((0, 2000, d_im.width, 2700))
team_crop.save('scratch/review_team.png')

# Let's crop Footer
footer_crop = d_im.crop((0, 2700, d_im.width, d_im.height))
footer_crop.save('scratch/review_footer.png')

print("Saved inspection crops in scratch/")

