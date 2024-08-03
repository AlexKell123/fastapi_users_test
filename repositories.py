from abc import ABC, abstractmethod
from fastapi import HTTPException
import redis
import sqlite3
import threading


# Абстрактный класс репозитория, от которого наследуются классы другие репозиториев
class UserRepository(ABC):
    @abstractmethod
    def create_user(self, full_name: str):
        pass

    @abstractmethod
    def read_user(self, user_id: int):
        pass

    @abstractmethod
    def update_user(self, user_id: int, full_name: str):
        pass

    @abstractmethod
    def delete_user(self, user_id: int):
        pass


# Класс репозитория Redis
class RedisUserRepository(UserRepository):
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_db = redis.Redis(host=host, port=port, db=db)

    # Создание пользователя
    def create_user(self, full_name: str):
        user_id = self.redis_db.incr("user_counter")
        self.redis_db.set(f"user:{user_id}", full_name)
        return {"id": user_id, "full_name": full_name}

    # Получение пользователя по id
    def read_user(self, user_id: int):
        full_name = self.redis_db.get(f"user:{user_id}")
        if full_name is None:
            raise HTTPException(status_code=404, detail="User not found")
        return {"id": user_id, "full_name": full_name}

    # Изменение пользователя
    def update_user(self, user_id: int, full_name: str):
        if not self.redis_db.exists(f"user:{user_id}"):
            raise HTTPException(status_code=404, detail="User not found")
        self.redis_db.set(f"user:{user_id}", full_name)
        return {"id": user_id, "full_name": full_name}

    # Удаление пользователя
    def delete_user(self, user_id: int):
        if not self.redis_db.exists(f"user:{user_id}"):
            raise HTTPException(status_code=404, detail="User not found")
        self.redis_db.delete(f"user:{user_id}")
        return {"message": "User deleted"}


# Класс репозитория Sqlite
class SqliteUserRepository(UserRepository):
    def __init__(self, database):
        self.database = database
        self.thread_local = threading.local()
        self.init_db()

    # Создание таблицы users, если её не существует
    def init_db(self):
        self.execute_query('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, full_name TEXT)''')

    # Функция выполняющая запрос к базе данных
    def execute_query(self, query, params=()):
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor

    # Подключение к базе данных
    def get_db_connection(self):
        if not hasattr(self.thread_local, "connection"):
            self.thread_local.connection = sqlite3.connect(self.database)
            self.thread_local.connection.row_factory = sqlite3.Row
        return self.thread_local.connection

    # Создание пользователя
    def create_user(self, full_name: str):
        cursor = self.execute_query('INSERT INTO users (full_name) VALUES (?)', (full_name,))
        user_id = cursor.lastrowid
        return {"id": user_id, "full_name": full_name}

    # Получение пользователя по id
    def read_user(self, user_id: int):
        cursor = self.execute_query('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return dict(user)

    # Изменение пользователя
    def update_user(self, user_id: int, full_name: str):
        self.execute_query('UPDATE users SET full_name = ? WHERE id = ?', (full_name, user_id))
        return {"id": user_id, "full_name": full_name}

    # Удаление пользователя
    def delete_user(self, user_id: int):
        self.execute_query('DELETE FROM users WHERE id = ?', (user_id,))
        return {"message": "User deleted"}



