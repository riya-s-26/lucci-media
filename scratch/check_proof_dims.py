from PIL import Image

for f in ['scratch/proof_header_stacked.png', 'scratch/proof_team_profiles.png', 'scratch/proof_footer_horizontal.png']:
    im = Image.open(f)
    print(f, im.size)

