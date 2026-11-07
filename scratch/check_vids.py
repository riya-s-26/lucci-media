# Check if cv2 or ffprobe or anything is available, or check where about_clip.mp4 was downloaded from
with open('scratch_luccimedia.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
vids = re.findall(r'https?://[^\s"\'\)]+?\.mp4', text)
print("Showit MP4s:", vids)

