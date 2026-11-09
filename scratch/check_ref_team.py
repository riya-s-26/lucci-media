from PIL import Image

for f in ['scratch/ref_team_studio.png', 'scratch/ref_team_laptop.png', 'scratch/ref_team_founder.png']:
    try:
        im = Image.open(f)
        print(f, im.size)
    except Exception as e:
        print(f, "Error:", e)

