import sqlite3



db_name = "users.db"


class db_work:
    def __init__(self, db_file_name):
        self.db_file_name = db_file_name

    def get_password(self, login):
        conn = sqlite3.connect(self.db_file_name)

        curs = conn.cursor()

        query_str = f"""SELECT login FROM userss;"""


        query = curs.execute(query_str)
    
        conn.close()

        return query


if __name__ == "__main__":

    testdb = db_work(db_name)
    print(testdb.get_password("alex"))



# CREATE TABLE userss (
#     id       INTEGER PRIMARY KEY AUTOINCREMENT,
#     login    TEXT    UNIQUE,
#     password TEXT
# );
