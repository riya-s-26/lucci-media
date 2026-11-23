import os
from PIL import Image

mockup_path = r"C:\Users\ekta bansal\.gemini\antigravity\brain\f5f3c267-89c4-44aa-8b83-5fc2de891e69\.user_uploaded\media_1795432010914_cc8da773.jpg"
m_img = Image.open(mockup_path)
print("Mockup size:", m_img.size) # 1024 x 682

# Concept 1 (Left half: x 0 to 512)
# Hero: (230, 36, 490, 235)
c1_hero = m_img.crop((230, 36, 490, 235))
c1_hero.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_c1_hero.jpg")
print("C1 Hero size:", c1_hero.size)

# Who It's For: (24, 305, 236, 410)
c1_who = m_img.crop((24, 305, 236, 410))
c1_who.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_c1_who.jpg")
print("C1 Who size:", c1_who.size)

# Concept 2 (Right half: x 512 to 1024)
# Hero: (745, 36, 1005, 235) - Storefront blade sign "LUCCI MEDIA" on brick wall!
c2_hero = m_img.crop((745, 36, 1005, 235))
c2_hero.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_c2_hero.jpg")
print("C2 Hero size:", c2_hero.size)

# Who It's For: (538, 305, 750, 410) - Laptop/tablet on desk with Google search
c2_who = m_img.crop((538, 305, 750, 410))
c2_who.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_c2_who.jpg")
print("C2 Who size:", c2_who.size)

# Also check google-business-profile-preview.jpg in assets/services
p_prev = r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\assets\services\google-business-profile-preview.jpg"
if os.path.exists(p_prev):
    prev_im = Image.open(p_prev)
    print("Existing google-business-profile-preview.jpg size:", prev_im.size)
    prev_im.save(r"c:\Users\ekta bansal\OneDrive\Desktop\lucci media\lucci-media\scratch\gbp_preview_check.jpg")
