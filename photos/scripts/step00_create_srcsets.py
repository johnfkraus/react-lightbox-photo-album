# script for creating srcset image copies

import step01_add_dimensions_to_original_image_names
import step02_create_resized_image_copies_for_srcset
import step03_copy_orig_image_rename_for_srcset

start='/Users/blauerbock/workspaces/react-photo-album-main/examples/react-lightbox-photo-album/photos/start/'
renamed='/Users/blauerbock/workspaces/react-photo-album-main/examples/react-lightbox-photo-album/photos/renamed/'
dest='/Users/blauerbock/workspaces/react-photo-album-main/examples/react-lightbox-photo-album/photos/dest/'

step01_add_dimensions_to_original_image_names.rename_images_add_dimensions(start, renamed)
step02_create_resized_image_copies_for_srcset.create_resized_copies(renamed, dest)

step03_copy_orig_image_rename_for_srcset.copy_and_rename_jpg_images(renamed, dest)

