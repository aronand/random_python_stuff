from sqlite3wrapper import Sqlite3Wrapper


def main():
    con = Sqlite3Wrapper("test.db")
    con.query("CREATE TABLE person (id INTEGER PRIMARY KEY, firstname TEXT)")


if __name__ == "__main__":
    main()
