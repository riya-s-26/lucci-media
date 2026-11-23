import os
from PIL import Image

mockup_path = r"C:\Users\ekta bansal\.gemini\antigravity\brain\f5f3c267-89c4-44aa-8b83-5fc2de891e69\.user_uploaded\media_1795430504285_53187fb7.jpg"
if os.path.exists(mockup_path):
    img = Image.open(mockup_path)
    print(f"Mockup size: {img.size}")
else:
    print("Mockup not found at path")
