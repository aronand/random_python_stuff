import sqlite3
from typing import Iterable
import logging as log


class Sqlite3Wrapper:
    __slots__ = (
        "__db_path",
        "__connection"
    )

    def __init__(self, filepath: str):
        self.__db_path: str = filepath
    
    def __enter__(self) -> sqlite3.Connection:
        log.debug("Opening connection")
        self.__connection = sqlite3.connect(self.__db_path)
        return self.__connection

    def __exit__(self, type, value, traceback):
        log.debug("Closing connection")
        log.debug(f"__exit__ arguments: {type}, {value}, {traceback}")
        self.__connection.commit()
        self.__connection.close()
