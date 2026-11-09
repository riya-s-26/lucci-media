from PIL import Image

ref = Image.open('scratch/ref1_cropped.png').convert('L')
comp = Image.open('scratch/test_interlocking_logo.png').convert('RGBA')

# Resize comp to match ref height (35px)
h = ref.height
w = int(comp.width * (h / comp.height))
comp_small = comp.resize((w, h), Image.Resampling.LANCZOS)

# Create a comparison image
comp_bg = Image.new('RGB', (comp_small.width, comp_small.height), (255, 255, 255))
comp_bg.paste(comp_small, mask=comp_small.split()[-1])

diff_w = max(ref.width, comp_small.width)
side_by_side = Image.new('RGB', (diff_w, h * 2 + 20), (255, 255, 255))
side_by_side.paste(ref, (0, 0))
side_by_side.paste(comp_bg, (0, h + 20))
side_by_side.save('scratch/logo_comparison_proof.png')
print("Comparison saved: ref size", ref.size, "comp size", comp_bg.size)

