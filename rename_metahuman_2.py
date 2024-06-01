import os

# Define the patterns
patterns1 = ['A207', 'A437', 'A417', 'A435', 'A67', 'A200', 'A327', 'A303', 'A221', 'A220', 'A438']
patterns2 = ['A205', 'A102', 'A407', 'A323', 'A332', 'A227', 'A334', 'A425', 'A426', 'A91', 'A405', 'A424', 'A221', 'A337']

def process_files(directory):
    for dirname, _, filenames in os.walk(directory):
        dir_basename = os.path.basename(dirname)
        if dir_basename in patterns1 or dir_basename in patterns2:
            for filename in filenames:
                new_filename = f"{dir_basename}_{filename}"
                old_filepath = os.path.join(dirname, filename)
                new_filepath = os.path.join(dirname, new_filename)
                os.rename(old_filepath, new_filepath)
                print(f"Renamed {old_filepath} to {new_filepath}")

# Example usage
process_files('data/metahuman_items')