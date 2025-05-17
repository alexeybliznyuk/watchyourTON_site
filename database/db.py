import sqlite3


db_name = "users.db"


class db_work:
    def __init__(self, db_file_name):
        self.db_file_name = db_file_name

    def get_password(self, login):
        conn = sqlite3.connect(self.db_file_name)

        curs = conn.cursor()

        query_str = f"""SELECT password FROM userss WHERE login = "{login}";"""

        quers = []
        query = curs.execute(query_str)

        for row in query:
            quers.append(list(row))

        conn.close()
        if quers:
            return quers[0][0]
        else:
            return None

    def registrate_user(self, login, password):

        conn = sqlite3.connect(self.db_file_name)

        curs = conn.cursor()

        query_str = (
            f"""INSERT INTO userss(login, password) VALUES("{login}", "{password}") ;"""
        )

        query = curs.execute(query_str)

        conn.commit()
        conn.close()

    def get_item(self, id):
        conn = sqlite3.connect(self.db_file_name)

        curs = conn.cursor()

        query_str = f"""SELECT * FROM items WHERE id = {str(id)};"""

        quers = []
        query = curs.execute(query_str)

        for row in query:
            quers.append(list(row))

        conn.close()
        return quers[0]

    def get_all_items(self):
        conn = sqlite3.connect(self.db_file_name)

        curs = conn.cursor()

        query_str = f"""SELECT * FROM items;"""

        quers = []
        query = curs.execute(query_str)

        for row in query:
            quers.append(list(row))

        conn.close()
        return quers

    def add_item(
        self,
        item_name,
        item_model,
        item_background,
        item_symbol,
        item_price,
        item_contact_info,
        item_description,
    ):

        conn = sqlite3.connect(self.db_file_name)

        curs = conn.cursor()

        query_str = f"""INSERT INTO items(name, model, background, symbol, price, contact_info, description) VALUES("{item_name}", "{item_model}", "{item_background}", "{item_symbol}", "{item_price}", "{item_contact_info}", "{item_description}") ;"""

        query = curs.execute(query_str)

        conn.commit()
        conn.close()


if __name__ == "__main__":

    testdb = db_work(db_name)
    print(testdb.get_password("fag"))
    print(testdb.get_item(1))
    print(testdb.get_all_items())
    # testdb.add_item("a","b","v", "c", "e", "123", "desc")
    # testdb.registrate_user("ultra", "faggot")


# CREATE TABLE userss (
#     id       INTEGER PRIMARY KEY AUTOINCREMENT,
#     login    TEXT    UNIQUE,
#     password TEXT
# );


# CREATE TABLE items (
#     id           INTEGER PRIMARY KEY AUTOINCREMENT,
#     name         TEXT,
#     model        TEXT,
#     background   TEXT,
#     symbol       TEXT,
#     price        TEXT,
#     contact_info TEXT,
#     description  TEXT
# );
