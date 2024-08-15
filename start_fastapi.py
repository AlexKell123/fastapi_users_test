import uvicorn
from src.fastapi_app.init_app import init_app


app = init_app()

if __name__ == "__main__":
    uvicorn.run("start_fastapi:app", host="0.0.0.0", port=8000, reload=True)
