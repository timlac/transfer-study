import glob
import os

# Specify the directory pattern
pattern = 'data/metahuman_items/**/*.mp4'

# Use glob to list all files matching the pattern
files = glob.glob(pattern, recursive=True)

print(files)

for file_path in files:
    print(file_path)
    # Get the base name of the file
    base_name = os.path.basename(file_path)

    # Remove the last occurrence of an underscore
    if '_' in base_name:
        new_base_name = base_name[::-1].replace('_', '', 1)[::-1]

        # Construct the new file path
        new_file_path = os.path.join(os.path.dirname(file_path), new_base_name)

        # Check if the new file path already exists to avoid overwriting
        if not os.path.exists(new_file_path):
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f'Renamed: {file_path} to {new_file_path}')
        else:
            print(f'Skipped renaming {file_path} to {new_file_path} as it already exists')