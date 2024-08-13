import sqlite3
import threading

from .config import DB_CFG


class SqlDB:
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

    def create(self, model: str, data: dict):
        model += 's'
        keys = ''
        values = ''

        for key, value in data.items():
            keys += f'{key}, '
            values += f'"{value}", '

        keys = keys[:-2]
        values = values[:-2]

        cursor = self.execute_query(f'INSERT INTO {model} ({keys}) VALUES ({values})')
        item_id = cursor.lastrowid
        return item_id

    def read(self, model: str, item_id: int):
        model += 's'
        cursor = self.execute_query(f'SELECT * FROM {model} WHERE id = {item_id}')
        return cursor.fetchone()

    def update(self, model: str, item_id: int, data: dict):
        model += 's'
        result = ''

        for key, value in data.items():
            result += f'{key} = "{value}", '

        result = result[:-2]

        self.execute_query(f'UPDATE {model} SET {result} WHERE id = {item_id}')
        return item_id

    def delete(self, model: str, item_id: int):
        model += 's'
        self.execute_query(f'DELETE FROM {model} WHERE id = {item_id}')

    def is_exist_key(self, model: str, item_id: int):
        return self.read(model, item_id)

    def check_duplicate(self, model: str, field_name: str, value: str, current_key=None):
        model += 's'
        query = f'SELECT id FROM {model} WHERE {field_name} = "{value}"'
        if current_key:
            query += f'AND id != {current_key}'
        cursor = self.execute_query(query)
        return cursor.fetchone()


db = SqlDB(*DB_CFG.values())
