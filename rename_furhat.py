import os

male_string = "transferstudy-male-mjpeg30.mov."
female_string = "transferstudy-female-mjpeg30.mov."

directory = "data/furhat_items"

for filename in os.listdir(directory):
    new_filename = filename.replace(male_string, "").replace(female_string, "").replace("-", "_")
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

