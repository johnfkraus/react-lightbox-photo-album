import shutil
import os


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


if __name__ == "__main__":
    src_dir = "photos/input/"  # Replace with the actual path to your file
    dest_dir = "photos/archives/" # Replace with the actual path to your destination directory
    cleanup_files(src_dir, dest_dir)
