import glob
import os
import shutil

# Specify the directory pattern
pattern = 'data/metahuman_items/**/*.mp4'

# Use glob to list all files matching the pattern
files = glob.glob(pattern, recursive=True)

# Parent directory where files will be copied
parent_directory = 'data/metahuman_items/'

for file_path in files:
    # Get the base name of the file
    base_name = os.path.basename(file_path)

    # Construct the new file path in the parent directory
    new_file_path = os.path.join(parent_directory, base_name)

    # Check if the new file path already exists to avoid overwriting
    if os.path.exists(new_file_path):
        # If it exists, append a unique suffix
        base, ext = os.path.splitext(base_name)
        counter = 1
        while os.path.exists(new_file_path):
            new_file_path = os.path.join(parent_directory, f"{base}_{counter}{ext}")
            counter += 1

    # Copy the file to the new location
    shutil.copy2(file_path, new_file_path)
    print(f'Copied: {file_path} to {new_file_path}')