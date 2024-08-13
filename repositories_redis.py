import redis
from fastapi import HTTPException

from user_repository_abstract import UserRepository


class RepositoryRedis:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_db = redis.Redis(host=host, port=port, db=db)

    def create(self, model: str, data: dict):
        item_id = self.redis_db.incr(f"{model} + _counter")
        key = f"{model}:{item_id}"
        self.redis_db.hmset(key, data)
        return {key: data}

    def read(self, model: str, item_id: int):
        key = f"{model}:{item_id}"
        data = self.redis_db.hgetall(key)
        if not data:
            raise HTTPException(status_code=404, detail=f"{model} not found")
        return {key: data}

    def update(self, model: str, item_id: int, data: dict):
        key = f"{model}:{item_id}"
        if not self.redis_db.exists(key):
            raise HTTPException(status_code=404, detail=f"{model} not found")
        self.redis_db.hmset(key, data)
        return {key: data}

    def delete(self, model: str, item_id: int):
        key = f"{model}:{item_id}"
        if not self.redis_db.exists(key):
            raise HTTPException(status_code=404, detail=f"{model} not found")
        self.redis_db.delete(key)
        return {"message": f"{model} deleted"}

    def check_duplicate(self, model: str, field_name: str, value: str, current_key=None):
        for key in self.redis_db.scan_iter(match=f"{model}:*"):
            if key != current_key and self.redis_db.hget(key, field_name).decode() == value:
                return True
        return False
