import redis
from .config import DB_CFG


class RedisDB:
    def __init__(self, host='localhost', port=6379, db=0):
        self.db = redis.Redis(host=host, port=port, db=db)

    def create(self, model: str, data: dict):
        item_id = self.db.incr(f"{model} + _counter")
        key = f"{model}:{item_id}"
        self.db.hmset(key, data)
        return item_id

    def read(self, model: str, item_id: int):
        key = f"{model}:{item_id}"
        return self.db.hgetall(key)

    def update(self, model: str, item_id: int, data: dict):
        key = f"{model}:{item_id}"
        self.db.hmset(key, data)
        return item_id

    def delete(self, model: str, item_id: int):
        key = f"{model}:{item_id}"
        self.db.delete(key)

    def is_exist_key(self, model: str, item_id: int):
        key = f"{model}:{item_id}"
        return self.db.exists(key)

    def check_duplicate(self, model: str, field_name: str, value: str, current_key=None):
        current_key = f"b'user:{current_key}'"
        for key in self.db.scan_iter(match=f"{model}:*"):
            if str(key) != current_key and self.db.hget(key, field_name).decode() == value:
                return True
        return False


db = RedisDB(*DB_CFG.values())
