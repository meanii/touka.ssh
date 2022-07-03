import os
from touka import DEFAULT_ROOT_DIR_PATH

def _connect_callback(address: str) -> None:
    os.system(f"ssh root@{address}")