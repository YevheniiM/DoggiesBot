import os
import sys
import uuid


def sort_in_dir(directory_path: str):
    files = os.listdir(directory_path)
    dog_breed = directory_path.split('/')[-1]
    print(f"Renaming files in {directory_path}, detected dog breed: {dog_breed}")
    for index, file in enumerate(files):
        os.rename(os.path.join(directory_path, file), os.path.join(directory_path, str(uuid.uuid4()) + '.jpeg'))
    files = os.listdir(directory_path)
    print(f"Renaming files in {directory_path} with indexes, detected dog breed: {dog_breed}")
    for index, file in enumerate(files):
        os.rename(os.path.join(directory_path, file), os.path.join(directory_path, f"{dog_breed}-{index}.jpeg"))


def main():
    dir_path = sys.argv[1]
    sort_in_dir(dir_path)


if __name__ == '__main__':
    main()
