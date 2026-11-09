from PIL import Image

m_im = Image.open('review/mobile_about.png')

# Let's save slices every 500px on mobile to check the flow
for i in range(0, m_im.height, 600):
    slice_img = m_im.crop((0, i, m_im.width, min(m_im.height, i + 600)))
    slice_img.save(f'scratch/mobile_slice_{i}.png')

print("Saved mobile slices.")

