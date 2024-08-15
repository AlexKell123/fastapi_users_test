from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, msg: str, address: str):
        pass


class EmailNotification(Notification):
    def send(self, msg: str, address: str):
        print(f'Уведомление "{msg}" отправлено на адрес {address}')
