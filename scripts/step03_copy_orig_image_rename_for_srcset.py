import os
import shutil
from PIL import Image

# add width to the end of the original full-sized image name and copy the
# renamed image to the 'dst_dir' directory.
def copy_and_rename_jpg_images(src_dir, dst_dir, test=False):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for filename in os.listdir(src_dir):
        if filename.lower().endswith('.jpg'):
            src_path = os.path.join(src_dir, filename)
            try:
                with Image.open(src_path) as img:
                    width, _ = img.size
            except Exception as e:
                print(f"Error opening {filename}: {e}")
                continue
            name, ext = os.path.splitext(filename)
            new_filename = f"{name}.{width}w{ext}"
            dst_path = os.path.join(dst_dir, new_filename)
            shutil.copy2(src_path, dst_path)
            if test:
                print(f"Copied and renamed: {src_path} -> {dst_path}")

if __name__ == "__main__":
    src_dir = "photos/test2"
    dst_dir = "photos/test3"
    copy_and_rename_jpg_images(src_dir, dst_dir, test=True)

