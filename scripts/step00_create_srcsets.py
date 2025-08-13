# script for creating srcset image copies for upload to CDN

import step01_add_dimensions_to_original_image_names
import step02_create_resized_image_copies_for_srcset
import step03_copy_orig_image_rename_for_srcset
import step04_cleanup

start='photos/input/'  # this dir must exist before running this code; put the to-be-processed photos here
renamed='photos/work_in_process/'  # temporary location for renamed version of original photo
dest='photos/srcset/'  # final output of photo srcset for upload to CDN; there should be nine versions of each photo here
archives = 'photos/archives/'

if __name__ == "__main__":
    step01_add_dimensions_to_original_image_names.rename_images_add_dimensions(start, renamed)
    step02_create_resized_image_copies_for_srcset.create_resized_copies(renamed, dest)
    step03_copy_orig_image_rename_for_srcset.copy_and_rename_jpg_images(renamed, dest)
    step04_cleanup.cleanup_files(start, archives)
    step04_cleanup.cleanup_files(renamed, archives)
