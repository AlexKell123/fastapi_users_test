from fastapi import FastAPI
from controllers import user_controller, position_controller


app = FastAPI()


@app.post("/users/")
def create_user(full_name: str, email: str):
    return user_controller.create(full_name, email)


@app.get("/users/{user_id}")
def read_user(user_id: int):
    return user_controller.read(user_id)


@app.put("/users/{user_id}")
def update_user(user_id: int, full_name: str, email: str):
    return user_controller.update(user_id, full_name, email)


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return user_controller.delete(user_id)


@app.post("/positions/")
def create_position(title: str):
    return position_controller.create(title)


@app.get("/positions/{position_id}")
def read_position(position_id: int):
    return position_controller.read(position_id)


@app.put("/positions/{position_id}")
def update_position(position_id: int, title: str):
    return position_controller.update(position_id, title)


@app.delete("/positions/{position_id}")
def delete_position(position_id: int):
    return position_controller.delete(position_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
