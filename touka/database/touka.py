"""This module provides the touka database functionality."""
# touka/database.py

import sys
from typing import Union
from tinydb import TinyDB, Query
from touka.utils.os_handler import check_file
from touka.database.client import Database


class ToukaDatabase:
    def __init__(self) -> None:
        self.touka = Database("touka")
        self.db = self.touka.connect()

    def save(self, data: set) -> None:
        self.db.insert(data)

    def get_address(self, id: str = None, name: str = None) -> Union[str, None]:
        Server = Query()
        
        if name:
            server = self.db.get(Server.name == name)
        if id:
            server = self.db.get(doc_id=id)
            
        if not server:
            return None
        return server.get("address")

    def get_name(self, address: str) -> Union[str, None]:
        Server = Query()
        server = self.db.search(Server.address == address)
        if len(server) == 0:
            return None
        return server[0].get("name")

    def get_all(self) -> []:
        return self.db.all()

    def purge(self, name: str) -> None:
        Server = Query()
        return self.db.remove(Server.name == name)

    def purge_all(self) -> None:
        return self.db.truncate()
