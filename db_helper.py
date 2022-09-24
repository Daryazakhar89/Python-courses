import sqlite3


class DBHelper:
    def __init__(self, db_name, table_name):
        self.table_name = table_name
        self.db_name = db_name
        with sqlite3.connect(db_name + ".db") as self.con:
            self.curs = self.con.cursor()
            self.curs.execute(f"""DROP TABLE IF EXISTS '{table_name}'""")
            self.curs.execute(f"""
            CREATE TABLE IF NOT EXISTS '{table_name}'(
                name  TEXT,
                price  TEXT
            )""")
            self.con.commit()

    def write_to_db(self, catalog):
        with sqlite3.connect(self.db_name + ".db") as self.con:
            self.curs = self.con.cursor()
            for element in catalog:
                self.curs.execute(f"INSERT INTO '{self.table_name}' VALUES ('{element['name']}','{element['price']}')")
            self.con.commit()

    def read_data(self):
        with sqlite3.connect(self.db_name + ".db") as self.con:
            self.curs = self.con.cursor()
            res = self.curs.execute(f"SELECT * FROM '{self.table_name}'")
            return res.fetchall()
