import sqlite3
import threading


class DBSqlite:
    def __init__(self, db_name):
        self.type = 'DB_SQLITE'
        self.db_name = db_name
        self.thread_local = threading.local()

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
