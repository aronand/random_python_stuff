import sqlite3
from typing import Iterable


class Sqlite3Wrapper:
    __slots__ = "__db_path"

    def __init__(self, filepath: str):
        self.__db_path: str = filepath
    
    def query(self, query: str, values: Iterable = []):
        with sqlite3.connect(self.__db_path) as con:
            con.execute(query, values)
