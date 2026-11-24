from PIL import Image

def smart_crop(im, target_w, target_h, center_x_pct=0.5, center_y_pct=0.5):
    src_w, src_h = im.size
    target_ratio = target_w / target_h
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        new_w = int(src_h * target_ratio)
        new_h = src_h
        ideal_x = int(src_w * center_x_pct)
        x1 = max(0, min(src_w - new_w, ideal_x - new_w // 2))
        y1 = 0
    else:
        new_w = src_w
        new_h = int(src_w / target_ratio)
        ideal_y = int(src_h * center_y_pct)
        x1 = 0
        y1 = max(0, min(src_h - new_h, ideal_y - new_h // 2))

    cropped = im.crop((x1, y1, x1 + new_w, y1 + new_h))
    return cropped

# Test IMG_5893 at center_y = 0.52
im_zo = Image.open('scratch/dropbox_extracted/Work/IMG_5893.JPG')
c_zo = smart_crop(im_zo, 1420, 336, 0.5, 0.52)
c_zo.resize((710, 168), Image.Resampling.LANCZOS).save('scratch/test_zo_tuned.jpg', quality=92)

# Test IMG_2600 (beauty models) at 1420x336
im_models = Image.open('scratch/dropbox_extracted/Work/IMG_2600.jpg')
c_models = smart_crop(im_models, 1420, 336, 0.5, 0.35)
c_models.resize((710, 168), Image.Resampling.LANCZOS).save('scratch/test_models_tuned.jpg', quality=92)

# Test DSC00336.JPG or DSC05857.JPG
print('Generated tuned tests.')
