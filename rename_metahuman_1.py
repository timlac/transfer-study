import os

def rename_files_in_directory_tree(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):

        print(dirnames)

        for filename in filenames:
            if "face" in filename:
                new_filename = filename.replace("face", "")
                old_file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {old_file_path} -> {new_file_path}')

# Replace 'your_directory_path' with the path to your root directory
root_directory = 'data/metahuman_items'
rename_files_in_directory_tree(root_directory)