import os
from pathlib import Path
from touka import DEFAULT_ROOT_DIR_PATH


def check_file(file_name: str) -> Path:
    isExist = os.path.exists(DEFAULT_ROOT_DIR_PATH)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(DEFAULT_ROOT_DIR_PATH)

    # Create a new file if not exist
    DEFAULT_ROOT_DIR_PATH.joinpath(file_name).touch(exist_ok=True)
    return DEFAULT_ROOT_DIR_PATH.joinpath(file_name)


def check_dir(dir_name: str) -> None:
    DEFAULT_ROOT_DIR_PATH.joinpath(dir_name)
    isExist = os.path.exists(DEFAULT_ROOT_DIR_PATH)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(DEFAULT_ROOT_DIR_PATH)
