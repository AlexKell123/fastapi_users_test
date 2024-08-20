class UserController:
    def __init__(self, repository, notification, er_handler):
        self.__repository = repository
        self.__notification = notification
        self.__error_handler = er_handler

    def send_invite_notification(self, email, full_name):
        msg = f"Пользователь {full_name} добавлен в базу"
        self.__notification.send(msg, email)

    def check_email_duplicate(self, email, current_key=None):
        return self.__repository.read_by_email(email, current_key)

    def create(self, full_name: str, email: str):
        if self.check_email_duplicate(email):
            return self.__error_handler.duplicate_found("email", email)
        result = self.__repository.create(full_name, email)
        self.send_invite_notification(email, full_name)
        return result

    def read(self, user_id: int):
        return self.__repository.read(user_id)

    def update(self, user_id: int, full_name: str, email: str):
        if self.check_email_duplicate(email, current_key=user_id):
            return self.__error_handler.duplicate_found("email", email)
        return self.__repository.update(user_id, full_name, email)

    def delete(self, user_id: int):
        return self.__repository.delete(user_id)
