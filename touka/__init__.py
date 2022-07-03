"""Top-level package for touka.ssh manager"""
# touka/__init__.py
from pathlib import Path

__app_name__ = "touka.ssh"
__version__ = "1.0.0"

DEFAULT_ROOT_DIR_PATH = Path(Path.home().joinpath(".meanii/touka.ssh/"))