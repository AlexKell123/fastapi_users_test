from fastapi import APIRouter


def get_router(controller):

    router = APIRouter(prefix="/positions", tags=["positions"])

    @router.post("/")
    def create_position(title: str):
        return controller.create(title)

    @router.get("/{position_id}")
    def read_position(position_id: int):
        return controller.read(position_id)

    @router.put("/{position_id}")
    def update_position(position_id: int, title: str):
        return controller.update(position_id, title)

    @router.delete("/{position_id}")
    def delete_position(position_id: int):
        return controller.delete(position_id)

    return router
