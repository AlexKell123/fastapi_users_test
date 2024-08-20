class PositionRepositoryRedis:
    def __init__(self, database, er_handler):
        self.__db = database
        self.__error_handler = er_handler

    def create(self, title: str):
        position_id = self.__db.db.incr("position_counter")
        key = f"position:{position_id}"
        data = {"title": title}
        self.__db.db.hmset(key, data)
        return {f"{key} created": data}

    def read(self, position_id: int):
        key = f"position:{position_id}"
        data = self.__db.db.hgetall(key)
        if not data:
            return self.__error_handler.not_found(key)
        return {key: data}

    def update(self, position_id: int, title: str):
        key = f"position:{position_id}"
        position = self.__db.db.hgetall(key)
        if not position:
            return self.__error_handler.not_found(key)
        data = {"title": title}
        self.__db.db.hmset(key, data)
        return {f"{key} updated": data}

    def delete(self, position_id: int):
        key = f"position:{position_id}"
        position = self.__db.db.hgetall(key)
        if not position:
            return self.__error_handler.not_found(key)
        self.__db.db.delete(key)
        return {"message": f"{key} deleted"}
