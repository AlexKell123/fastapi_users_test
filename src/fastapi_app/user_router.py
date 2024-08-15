from fastapi import APIRouter


def get_router(controller):

    router = APIRouter(prefix="/users", tags=["users"])

    @router.post("/")
    def create_user(full_name: str, email: str):
        return controller.create(full_name, email)

    @router.get("/{user_id}")
    def read_user(user_id: int):
        return controller.read(user_id)

    @router.put("/{user_id}")
    def update_user(user_id: int, full_name: str, email: str):
        return controller.update(user_id, full_name, email)

    @router.delete("/{user_id}")
    def delete_user(user_id: int):
        return controller.delete(user_id)

    return router
