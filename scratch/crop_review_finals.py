from PIL import Image

d_im = Image.open('review/desktop_about.png')
# crop to height 3520
d_crop = d_im.crop((0, 0, d_im.width, min(3520, d_im.height)))
d_crop.save('review/desktop_about.png', optimize=True)
print("Saved review/desktop_about.png:", d_crop.size)

m_im = Image.open('review/mobile_about.png')
# crop to height 5600
m_crop = m_im.crop((0, 0, m_im.width, min(5600, m_im.height)))
m_crop.save('review/mobile_about.png', optimize=True)
print("Saved review/mobile_about.png:", m_crop.size)

