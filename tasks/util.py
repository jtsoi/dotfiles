from os import path


def full_path(file_path):
    return path.abspath(path.expanduser(file_path))
