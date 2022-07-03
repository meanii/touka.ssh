import os
from touka import DEFAULT_ROOT_DIR_PATH


def _connect_callback(address: str, force: bool) -> None:
    if force:
        os.system(f"ssh-keygen -R {address} -q")
        os.system(f"ssh-copy-id -f root@{address}")
    os.system(f"ssh root@{address}")