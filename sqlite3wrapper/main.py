import os
import logging as log

from sqlite3wrapper import Sqlite3Wrapper


def main():
    log.basicConfig(level=log.DEBUG, format="[%(levelname)s] %(asctime)s - %(message)s")

    db_path = "test.db"

    if os.path.isfile(db_path):
        os.remove(db_path)

    with Sqlite3Wrapper(db_path) as con:
        cur = con.cursor()
        cur.execute("CREATE TABLE person (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT)")
        cur.execute("INSERT INTO person (firstname) VALUES ('Peter')")
        cur.execute("SELECT * FROM person")
        print(cur.fetchall())


if __name__ == "__main__":
    main()
