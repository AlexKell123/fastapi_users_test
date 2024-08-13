from abc import ABC, abstractmethod


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
