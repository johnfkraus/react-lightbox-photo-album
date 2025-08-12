
# a function that will:
# 1. Iterate through all files in the 'start' directory.
# 2. For each file, check if it is a JPG or JPEG image (case-insensitive).
# 3. Open the image to get its dimensions.
# 4. Rename the file according to the rules (extension to .jpg, append .WIDTHxHEIGHT).
# 5. Save the renamed file in the 'renamed' directory.

# step 1

import os
from PIL import Image
import shutil

def rename_images_add_dimensions(start_dir, renamed_dir):
    if not os.path.exists(renamed_dir):
        os.makedirs(renamed_dir)
    for filename in os.listdir(start_dir):
        file_lower = filename.lower()
        if file_lower.endswith('.jpg') or file_lower.endswith('.jpeg'):
            name, ext = os.path.splitext(filename)
            ext = '.jpg'  # always use .jpg
            img_path = os.path.join(start_dir, filename)
            try:
                with Image.open(img_path) as img:
                    width, height = img.size
            except Exception as e:
                print(f"Could not open {filename}: {e}")
                continue
            new_name = f"{name}.{width}x{height}{ext}"
            new_path = os.path.join(renamed_dir, new_name)
            shutil.copy2(img_path, new_path)

# start='/Users/blauerbock/workspaces/react-photo-album-main/examples/react-lightbox-photo-album/photos/start/'
# renamed='/Users/blauerbock/workspaces/react-photo-album-main/examples/react-lightbox-photo-album/photos/renamed/'
# rename_images_add_dimensions(start, renamed)
