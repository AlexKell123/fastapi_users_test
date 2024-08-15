class Controller:
    def __init__(self, repository, notification, er_handler):
        self.repository = repository
        self.notification = notification
        self.error_handler = er_handler

    def send_invite_notification(self, email, full_name):
        msg = f"Пользователь {full_name} добавлен в базу"
        self.notification.send(msg, email)

    def check_email_duplicate(self, email, current_key=None):
        return self.repository.read_by_email(email, current_key)

    def create(self, full_name: str, email: str):
        if self.check_email_duplicate(email):
            return self.error_handler.duplicate_found("email", email)
        result = self.repository.create(full_name, email)
        self.send_invite_notification(email, full_name)
        return result

    def read(self, user_id: int):
        return self.repository.read(user_id)

    def update(self, user_id: int, full_name: str, email: str):
        if self.check_email_duplicate(email, current_key=user_id):
            return self.error_handler.duplicate_found("email", email)
        return self.repository.update(user_id, full_name, email)

    def delete(self, user_id: int):
        return self.repository.delete(user_id)
