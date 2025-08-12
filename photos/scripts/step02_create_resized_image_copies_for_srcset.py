# This function will create resized copies of each JPG image in the 'start' directory, saving
# them in the 'destination' directory with the specified filename format.

import os
from PIL import Image

def create_resized_copies(start_dir, dest_dir):
    widths = [1080, 640, 384, 256, 128, 96, 64, 48]
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for filename in os.listdir(start_dir):
        if filename.lower().endswith('.jpg'):
            filepath = os.path.join(start_dir, filename)
            with Image.open(filepath) as img:
                for w in widths:
                    # Calculate new height to maintain aspect ratio
                    aspect_ratio = img.height / img.width
                    new_height = int(w * aspect_ratio)
                    resized_img = img.resize((w, new_height), Image.LANCZOS)
                    # Build new filename
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}.{w}w{ext}"
                    dest_path = os.path.join(dest_dir, new_filename)
                    resized_img.save(dest_path, "JPEG")

# start='/Users/blauerbock/workspaces/react-photo-album-main/examples/react-lightbox-photo-album/photos/start/'
# renamed='/Users/blauerbock/workspaces/react-photo-album-main/examples/react-lightbox-photo-album/photos/renamed/'
# dest='/Users/blauerbock/workspaces/react-photo-album-main/examples/react-lightbox-photo-album/photos/dest/'
# create_resized_copies(start, dest)

