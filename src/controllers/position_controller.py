class PositionController:
    def __init__(self, repository):
        self.__repository = repository

    def create(self, title: str):
        return self.__repository.create(title)

    def read(self, position_id: int):
        return self.__repository.read(position_id)

    def update(self, position_id: int, title: str):
        return self.__repository.update(position_id, title)

    def delete(self, position_id: int):
        return self.__repository.delete(position_id)
