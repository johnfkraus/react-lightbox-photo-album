
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

def rename_images_add_dimensions(start_dir, renamed_dir, test=False):
    if test:
        print('cwd =', os.getcwd())
    if not os.path.exists(renamed_dir):
        os.makedirs(renamed_dir)
    for filename in os.listdir(start_dir):
        file_lower = filename.lower()
        if file_lower.endswith('.jpg') or file_lower.endswith('.jpeg'):
            name, ext = os.path.splitext(filename)
            if test:
                print("name:", name, ", ext:", ext)
            ext = '.jpg'  # always use .jpg, not .jpeg
            img_path = os.path.join(start_dir, filename)
            try:
                with Image.open(img_path) as img:
                    width, height = img.size
            except Exception as e:
                print(f"Could not open {filename}: {e}")
                continue
            new_name = f"{name}.{width}x{height}{ext}"
            if test:
                print("new_name: ", new_name)
                print(f'{{ src: "{new_name}", alt: "A photo" }},')
            new_path = os.path.join(renamed_dir, new_name)
            shutil.copy2(img_path, new_path)

            # append a Typescript snippet to a file for pasting into 'src/photos.tx'
            code = f'{{ src: "{new_name}", alt: "A photo" }},'
            with open('filenames-list.txt', 'a') as file:
                file.write(code + '\n')


if __name__ == "__main__":
    test_dir1 = 'photos/test/test1'   # original photo named XXXX.YYY.jpg
    test_dir2 = 'photos/test/test2'   # original photo with dimensions added to name
    # i.e., XXXX.YYY.WIDTHxHEIGHT.jpg
    rename_images_add_dimensions(test_dir1, test_dir2, test=True)
