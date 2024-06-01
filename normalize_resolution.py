from glob import glob
import subprocess
import os

path1 = "data/actor_items/original/*"
path2 = "data/furhat_items/original/*"
path3 = "data/processed_metahuman/original/*"

output_folder = "data/furhat_items/modified_resolution"

paths = glob(path2)
print(paths)

for input_file in paths:
    # Construct the output file path with .mp4 extension
    output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + '.mp4')
    command = [
        'ffmpeg', '-i', input_file,
        '-vf', 'scale=1280:720',
        '-c:a', 'aac', '-b:a', '320k',
        '-c:v', 'libx264',
        output_file
    ]
    subprocess.run(command)

