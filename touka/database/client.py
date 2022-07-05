from dataclasses import dataclass

from tinydb import TinyDB
from touka.utils.os_handler import check_file


@dataclass
class DatabaseRegister:
    """this stores createred database instances and names"""

    name: str
    instance: TinyDB


class Database:
    """Database handling, for handling diffrent databases of intances"""

    def __init__(self, database: str) -> None:
        try:
            self.database = database
            self.db = TinyDB(check_file(f".{database}.json"))
        except OSError as e:
            sys.exit(e)

    def connect(self) -> TinyDB:
        """returns specified database's intances"""
        return self.db

    def get_database(self) -> DatabaseRegister:
        """returns specified database's name and intances"""
        return DatabaseRegister(self.database, self.db)
