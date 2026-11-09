from PIL import Image, ImageFilter

chair = Image.open('scratch/chair_crop_test.png')
# resize to 1200x632 (matching aspect ratio 131:69)
w = 1200
h = int(w * (chair.height / chair.width))
chair_hi = chair.resize((w, h), Image.Resampling.LANCZOS)
chair_hi = chair_hi.filter(ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3))
chair_hi.save('assets/about/team_studio_chair.jpg', quality=95)
print("Updated assets/about/team_studio_chair.jpg with dimensions:", chair_hi.size)

