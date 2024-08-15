class Repository:
    def __init__(self, database, er_handler):
        self.db = database
        self.error_handler = er_handler

    def create(self, full_name: str, email: str):
        user_id = self.db.db.incr("user_counter")
        key = f"user:{user_id}"
        data = {"full_name": full_name, "email": email}
        self.db.db.hmset(key, data)
        return {f"{key} created": data}

    def read(self, user_id: int):
        key = f"user:{user_id}"
        data = self.db.db.hgetall(key)
        if not data:
            return self.error_handler.not_found(key)
        return {key: data}

    def update(self, user_id: int, full_name: str, email: str):
        key = f"user:{user_id}"
        user = self.db.db.hgetall(key)
        if not user:
            return self.error_handler.not_found(key)
        data = {"full_name": full_name, "email": email}
        self.db.db.hmset(key, data)
        return {f"{key} updated": data}

    def delete(self, user_id: int):
        key = f"user:{user_id}"
        user = self.db.db.hgetall(key)
        if not user:
            return self.error_handler.not_found(key)
        self.db.db.delete(key)
        return {"message": f"{key} deleted"}

    def read_by_email(self, email: str, current_key=None):
        current_key = f"b'user:{current_key}'"
        for key in self.db.db.scan_iter(match=f"user:*"):
            if str(key) != current_key and self.db.db.hget(key, "email").decode() == email:
                return self.db.db.hgetall(key)
