import uvicorn
from fastapi import FastAPI

from src.init_app import init_app
from src.gateways import get_user_router, get_position_router
from src.logger import log


log('starting fastapi init')
user_controller, position_controller = init_app('config.json', 'Fastapi')

log('create fastapi application')
app = FastAPI()

log('create routers')
user_router = get_user_router(user_controller)
position_router = get_position_router(position_controller)
app.include_router(user_router)
app.include_router(position_router)

log('start uvicorn')
if __name__ == "__main__":
    uvicorn.run("start_fastapi:app", host="0.0.0.0", port=8000, reload=True)
