from fastapi.responses import FileResponse
from fastapi import FastAPI
from app.routes import router
import os

app = FastAPI()
app.include_router(router, prefix="/api")

@app.get("/favicon.ico")
def favicon():
    path = os.path.join(os.path.dirname(__file__), "favicon.ico")
    return FileResponse(path)
