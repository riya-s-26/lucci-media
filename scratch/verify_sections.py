from PIL import Image

im = Image.open('review/desktop_about.png')

# 1. Header (y=0 to 120)
im.crop((0, 0, 1440, 120)).save('scratch/crop_final_header.png')

# 2. Hero copy (x=100 to 700, y=140 to 650)
im.crop((100, 140, 750, 650)).save('scratch/crop_final_hero.png')

# 3. Story text (x=700 to 1340, y=750 to 1350)
im.crop((700, 750, 1340, 1350)).save('scratch/crop_final_story.png')

# 4. Feels like (y=1750 to 2200)
im.crop((100, 1750, 1340, 2200)).save('scratch/crop_final_feels.png')

# 5. Team section (y=2150 to 2750)
im.crop((100, 2150, 1340, 2750)).save('scratch/crop_final_team.png')

# 6. Footer (y=2950 to 3520)
im.crop((100, 2950, 1340, 3520)).save('scratch/crop_final_footer.png')

print("All section verification crops saved.")

