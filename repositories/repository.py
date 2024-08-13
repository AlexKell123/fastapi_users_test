from abc import ABC, abstractmethod
from . import db
from error_handlers import error_handler


class AbstractRepository(ABC):
    @abstractmethod
    def create(self, model: str, data: dict):
        pass

    @abstractmethod
    def read(self, model: str, item_id: int):
        pass

    @abstractmethod
    def update(self, model: str, item_id: int, data: dict):
        pass

    @abstractmethod
    def delete(self, model: str, item_id: int):
        pass


class Repository(AbstractRepository):
    def __init__(self, database, er_handler):
        self.db = database
        self.error_handler = er_handler

    def create(self, model: str, data: dict):
        item_id = self.db.create(model, data)
        return {f"{model}:{item_id} created": data}

    def read(self, model: str, item_id: int):
        data = self.db.read(model, item_id)
        key = f"{model}:{item_id}"
        if not data:
            return self.error_handler.not_found(key)
        return {key: data}

    def update(self, model: str, item_id: int, data: dict):
        key = f"{model}:{item_id}"
        if not self.db.is_exist_key(model, item_id):
            return self.error_handler.not_found(key)
        self.db.update(model, item_id, data)
        return {f"{key} updated": data}

    def delete(self, model: str, item_id: int):
        key = f"{model}:{item_id}"
        if not self.db.is_exist_key(model, item_id):
            return self.error_handler.not_found(key)
        self.db.delete(model, item_id)
        return {"message": f"{key} deleted"}

    def check_duplicate(self, model: str, field_name: str, value: str, current_key=None):
        return self.db.check_duplicate(model, field_name, value, current_key)


user_repository = Repository(db, error_handler)
position_repository = Repository(db, error_handler)
