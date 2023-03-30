import os


def walk_dir(root_dir):
    """
    Prints no of images in each subdirectory starting from root_dir
    :param root_dir:
    :return:
    """
    for dir_path, dir_name, file_name in os.walk(root_dir):
        print(f'there are {len(dir_name)} directories and {len(file_name)} images in path {dir_path}')
