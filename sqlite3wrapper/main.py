import os
from sqlite3wrapper import Sqlite3Wrapper


def main():
    db_path = "test.db"
    con = Sqlite3Wrapper(db_path)
    con.query("CREATE TABLE person (id INTEGER PRIMARY KEY, firstname TEXT)")
    os.remove(db_path)


if __name__ == "__main__":
    main()
