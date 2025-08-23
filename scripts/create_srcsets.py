# script for creating srcset image copies for upload to CDN
import os
from PIL import Image
import shutil

# Step 1
# a function that will:
# 1. Iterate through all files in the 'start' directory.
# 2. For each file, check if it is a JPG or JPEG image (case-insensitive).
# 3. Open the image to get its dimensions.
# 4. Rename the file according to the rules (extension to .jpg, append .WIDTHxHEIGHT).
# 5. Save the renamed file in the 'renamed' directory.

def rename_images_add_dimensions(start_dir, renamed_dir, test=False):
    if test:
        print('cwd =', os.getcwd())
    if not os.path.exists(start_dir):
        os.makedirs(start_dir)
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

# test step 1
# if __name__ == "__main__":
#     test_dir1 = 'photos/test/test1'   # original photo named XXXX.YYY.jpg
#     test_dir2 = 'photos/test/test2'   # original photo with dimensions added to name
#     # i.e., XXXX.YYY.WIDTHxHEIGHT.jpg
#     rename_images_add_dimensions(test_dir1, test_dir2, test=True)

# step 2
# This function will create a srcset of resized copies of each JPG image
# in the 'start' directory, saving them in the destination
# directory with the specified filename format.

def create_resized_copies(start_dir, dest_dir, test=False):
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
                    if test:
                        print("dest_path:", dest_path)
                    resized_img.save(dest_path, "JPEG")


# if __name__ == "__main__":
#     test_dir2 = 'photos/test2'
#     test_dir3 = 'photos/test3'
#     create_resized_copies(test_dir2, test_dir3, test=True)


# step 3
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

# if __name__ == "__main__":
#     src_dir = "photos/test2"
#     dst_dir = "photos/test3"
#     copy_and_rename_jpg_images(src_dir, dst_dir, test=True)

# step 4
def cleanup_files(src_dir, dest_dir):
    # source_directory = "path/to/source_folder"  # Replace with your source directory path
    # destination_directory = "path/to/destination_folder"  # Replace with your destination directory path

    # Create the destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)

    # Get a list of all files in the source directory
    files_to_move = os.listdir(src_dir)

    # Iterate through each file and move it
    for filename in files_to_move:
      source_path = os.path.join(src_dir, filename)
      destination_path = os.path.join(dest_dir, filename)

      # Check if it's a file (and not a subdirectory) before moving
      if os.path.isfile(source_path):
        shutil.move(source_path, destination_path)
        print(f"Moved '{filename}' to '{dest_dir}'")
      else:
        print(f"Skipping '{filename}' as it is not a file.")


# if __name__ == "__main__":
#     src_dir = "photos/input/"  # Replace with the actual path to your file
#     dest_dir = "photos/archives/" # Replace with the actual path to your destination directory
#     cleanup_files(src_dir, dest_dir)


start='photos/input/'  # this dir must exist before running this code; put the to-be-processed photos here
renamed='photos/work_in_process/'  # temporary location for renamed version of original photo
dest='photos/srcset/'  # final output of photo srcset for upload to CDN; there should be nine versions of each photo here
archives = 'photos/archives/'

if __name__ == "__main__":
    rename_images_add_dimensions(start, renamed)
    # step01_add_dimensions_to_original_image_names.rename_images_add_dimensions(start, renamed)
    # (step02_create_resized_image_copies_for_srcset.
    create_resized_copies(renamed, dest)
    # (step03_copy_orig_image_rename_for_srcset.
    copy_and_rename_jpg_images(renamed, dest)
    # (step04_cleanup.
    cleanup_files(start, archives)
    #step04_cleanup.
    cleanup_files(renamed, archives)
