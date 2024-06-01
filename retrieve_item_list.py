import pandas as pd
import shutil
import os
from pathlib import Path


def get_item_list():
    df = pd.read_excel('data/Transfer study_final item list .xlsx')
    return df["item"].values


def process_path(path):
    for filepath in os.listdir(path):
        filename = Path(filepath).stem

        if filename not in item_list:
            print(f"{filename} not in item_list")


def check_if_item_exists(path):
    filenames = []
    for filepath in os.listdir(path):
        filename = Path(filepath).stem
        filenames.append(filename)

    for item in item_list:
        if item not in filenames:
            print(f"{item} not in filenames in path {path}")


item_list = get_item_list()

path1 = "data/actor_items"
path2 = "data/furhat_items"
path3 = "data/processed_metahuman"

check_if_item_exists(path1)
check_if_item_exists(path2)
check_if_item_exists(path3)


def copy_files_if_exist(path, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for filepath in os.listdir(path):
        filename = Path(filepath).stem

        if filename in item_list:
            source_file = os.path.join(path, filepath)
            destination_file = os.path.join(destination, filepath)
            shutil.copy(source_file, destination_file)
            print(f"Copied {filename} to {destination}")


path2 = "data/processed_metahuman/modified_resolution"
destination_path = "data/processed_metahuman/filtered"

# copy_files_if_exist(path1, destination_path)
copy_files_if_exist(path2, destination_path)
# copy_files_if_exist(path3, destination_path)