from fastapi import FastAPI

from config import settings


app = FastAPI()

# Чтение переменной settings из файла config.py
repository_type = settings['repository_type']
repository_settings = settings['repository_settings']

# Создание экземпляра класса репозитория, указанного в settings, с параметрами, также указанными в settings
repository = repository_type(*repository_settings.values())


# Создание пользователя
@app.post("/users/")
def create_user(full_name: str):
    return repository.create_user(full_name)


# Получение пользователя по id
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return repository.read_user(user_id)


# Изменение пользователя
@app.put("/users/{user_id}")
def update_user(user_id: int, full_name: str):
    return repository.update_user(user_id, full_name)


# Удаление пользователя
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return repository.delete_user(user_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
