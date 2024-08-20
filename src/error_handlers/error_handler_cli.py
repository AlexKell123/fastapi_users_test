class ErrorHandlerCli:
    @staticmethod
    def not_found(item):
        return f'error 404 - {item} not found'

    @staticmethod
    def duplicate_found(field_name: str, value: str):
        return f"error 400 - {field_name} : '{value}' already exists"
