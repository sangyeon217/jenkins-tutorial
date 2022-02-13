import os


def mkdir_if_not_exist(directory):
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
