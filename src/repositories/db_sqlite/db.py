import sqlite3
import threading


class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.thread_local = threading.local()
        self.execute_query('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, full_name TEXT, email TEXT)''')
        self.execute_query('''CREATE TABLE IF NOT EXISTS positions (id INTEGER PRIMARY KEY, title TEXT)''')

    def get_db_connection(self):
        if not hasattr(self.thread_local, "connection"):
            self.thread_local.connection = sqlite3.connect(self.db_name)
            self.thread_local.connection.row_factory = sqlite3.Row
        return self.thread_local.connection

    def execute_query(self, query, params=()):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor
