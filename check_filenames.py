import os
from pathlib import Path

from nexa_sentimotion_filename_parser.metadata import Metadata


path1 = "data/actor_items"
path2 = "data/furhat_items"
path3 = "data/processed_metahuman"

for filepath in os.listdir(path3):
    filename = Path(filepath).stem
    print(filename)

    meta = Metadata(filename)

    print()
    print("filename: ", meta.filename)
    print("video id: ", meta.video_id)
    print("mode: ", meta.mode)
    print("emotion 1:", meta.emotion_1_abr)
    print("intensity_level: ", meta.intensity_level)

