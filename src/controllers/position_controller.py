class Controller:
    def __init__(self, repository, notification, er_handler):
        self.repository = repository

    def create(self, title: str):
        data = {"title": title}
        return self.repository.create("position", data)

    def read(self, position_id: int):
        return self.repository.read("position", position_id)

    def update(self, position_id: int, title: str):
        data = {"title": title}
        return self.repository.update("position", position_id, data)

    def delete(self, position_id: int):
        return self.repository.delete("position", position_id)
