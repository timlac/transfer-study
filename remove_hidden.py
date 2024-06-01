import os
import glob

# Define the directory
directory = 'data/metahuman_items'

# Get a list of all hidden files
hidden_files = glob.glob(os.path.join(directory, '.[^.]*')) + glob.glob(os.path.join(directory, '.??*'))

# Remove each hidden file
for file in hidden_files:
    try:
        os.remove(file)
        print(f"Removed: {file}")
    except Exception as e:
        print(f"Error removing {file}: {e}")