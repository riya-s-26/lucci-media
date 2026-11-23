import os
from PIL import Image

mockup_path = r"C:\Users\ekta bansal\.gemini\antigravity\brain\f5f3c267-89c4-44aa-8b83-5fc2de891e69\.user_uploaded\media_1795430504285_53187fb7.jpg"
m_img = Image.open(mockup_path)
print("Mockup dimensions:", m_img.size)

# Let's crop Concept 1:
# The mockup has two sides: Left Concept is x: 0 to 512, Right Concept is x: 512 to 1024.
# Let's find the exact bounding boxes of the hero image and who image in Left Concept.
# Let's crop the whole top of the left concept to inspect where the image starts and ends.
hero_region = m_img.crop((215, 30, 500, 240))
hero_region.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\hero_region.jpg")

who_region = m_img.crop((15, 295, 250, 420))
who_region.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\who_region.jpg")

print("Saved hero_region and who_region")
