"""Top-level package for touka.ssh manager"""
# touka/__init__.py
from pathlib import Path

__app_name__ = "touka"
__about__ = "Awesome ssh manager, especially made for anii ☂️"
__source__ = "https://github.com/meanii/touka.ssh/"
__author__ = "Anil Chauhan <https://github.com/meanii>"
__version__ = "2.2.8"

DEFAULT_ROOT_DIR_PATH = Path(Path.home().joinpath(".meanii/touka.ssh/"))