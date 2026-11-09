from PIL import Image

im = Image.open('review/desktop_about.png').convert('RGB')
# Let's crop y from 2200 to 3200 and save
im.crop((0, 2200, 1440, 3200)).save('scratch/full_team_region.png')
print("Full team region saved.")

