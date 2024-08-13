from fastapi import HTTPException


class ErrorHandler:
    def not_found(self, item):
        raise HTTPException(status_code=404, detail=f"{item} not found")

    def duplicate_found(self, field_name: str, value: str):
        raise HTTPException(status_code=400, detail=f"{field_name} : '{value}' already exists")


error_handler = ErrorHandler()
