from repositories.repository import user_repository
from error_handlers import error_handler
from notifications import email_notification


class UserController:
    def __init__(self, repository, notification, er_handler):
        self.repository = repository
        self.notification = notification
        self.error_handler = er_handler

    def send_invite_notification(self, email, full_name):
        msg = f"Пользователь {full_name} добавлен в базу"
        self.notification.send(msg, email)

    def check_email_duplicate(self, email, current_key=None):
        return self.repository.check_duplicate("user", "email", email, current_key)

    def create(self, full_name: str, email: str):
        if self.check_email_duplicate(email):
            return self.error_handler.duplicate_found("email", email)

        data = {"full_name": full_name, "email": email}
        result = self.repository.create("user", data)

        self.send_invite_notification(email, full_name)
        return result

    def read(self, user_id: int):
        return self.repository.read("user", user_id)

    def update(self, user_id: int, full_name: str, email: str):
        if self.check_email_duplicate(email, current_key=user_id):
            return self.error_handler.duplicate_found("email", email)

        data = {"full_name": full_name, "email": email}
        return self.repository.update("user", user_id, data)

    def delete(self, user_id: int):
        return self.repository.delete("user", user_id)


user_controller = UserController(user_repository, email_notification, error_handler)
