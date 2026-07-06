import sqlite3
from pathlib import Path


DB_PATH = Path("data/market.db")


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(
            DB_PATH,
            check_same_thread=False,
        )
        self.conn.row_factory = sqlite3.Row

    def execute(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        self.conn.commit()
        return cur

    def query(self, sql, params=()):
        cur = self.conn.cursor()
        cur.execute(sql, params)
        return cur.fetchall()


db = Database()
