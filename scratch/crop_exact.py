import os
from PIL import Image

mockup_path = r"C:\Users\ekta bansal\.gemini\antigravity\brain\f5f3c267-89c4-44aa-8b83-5fc2de891e69\.user_uploaded\media_1795430504285_53187fb7.jpg"
m_img = Image.open(mockup_path)

# Let's crop Concept 1 Hero:
# In detect_box: left=220, top=30, right=488, bottom=239 (width 268, height 209)
# Let's crop exactly the photo inside the border
# Let's check around (224, 37) to (488, 230)
hero_img = m_img.crop((225, 36, 488, 230))
hero_img.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\concept1_hero_crop.jpg", quality=100)

# Who crop: left=23, top=295, right=249, bottom=419 (width 226, height 124)
# Let's crop exactly:
who_img = m_img.crop((24, 305, 236, 410))
who_img.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\concept1_who_crop.jpg", quality=100)

print("Saved concept1_hero_crop.jpg and concept1_who_crop.jpg")
print("Hero crop size:", hero_img.size, "Aspect ratio:", hero_img.width / hero_img.height)
print("Who crop size:", who_img.size, "Aspect ratio:", who_img.width / who_img.height)
