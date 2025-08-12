import os
import shutil
from PIL import Image

def copy_and_rename_jpg_images(src_dir, dst_dir):
    # src_dir = 'renamed'
    # dst_dir = 'destination'
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
            print(f"Copied and renamed: {src_path} -> {dst_path}")


# renamed='/Users/blauerbock/workspaces/react-photo-album-main/examples/react-lightbox-photo-album/photos/renamed/'
# dest='/Users/blauerbock/workspaces/react-photo-album-main/examples/react-lightbox-photo-album/photos/dest/'
# copy_and_rename_jpg_images(renamed, dest)
