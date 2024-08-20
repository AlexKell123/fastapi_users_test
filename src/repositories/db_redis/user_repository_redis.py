class UserRepositoryRedis:
    def __init__(self, database, er_handler):
        self.__db = database
        self.__error_handler = er_handler

    def create(self, full_name: str, email: str):
        user_id = self.__db.db.incr("user_counter")
        key = f"user:{user_id}"
        data = {"full_name": full_name, "email": email}
        self.__db.db.hmset(key, data)
        return {f"{key} created": data}

    def read(self, user_id: int):
        key = f"user:{user_id}"
        data = self.__db.db.hgetall(key)
        if not data:
            return self.__error_handler.not_found(key)
        return {key: data}

    def update(self, user_id: int, full_name: str, email: str):
        key = f"user:{user_id}"
        user = self.__db.db.hgetall(key)
        if not user:
            return self.__error_handler.not_found(key)
        data = {"full_name": full_name, "email": email}
        self.__db.db.hmset(key, data)
        return {f"{key} updated": data}

    def delete(self, user_id: int):
        key = f"user:{user_id}"
        user = self.__db.db.hgetall(key)
        if not user:
            return self.__error_handler.not_found(key)
        self.__db.db.delete(key)
        return {"message": f"{key} deleted"}

    def read_by_email(self, email: str, current_key=None):
        current_key = f"b'user:{current_key}'"
        for key in self.__db.db.scan_iter(match=f"user:*"):
            if str(key) != current_key and self.__db.db.hget(key, "email").decode() == email:
                return self.__db.db.hgetall(key)
