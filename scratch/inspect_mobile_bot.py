from PIL import Image

m_im = Image.open('review/mobile_about.png')
crop = m_im.crop((0, m_im.height - 600, m_im.width, m_im.height))
crop.save('scratch/mobile_bottom_inspect.png')
print("Saved mobile bottom inspect")

