from fastapi import FastAPI
from app.enhance.routes import router as enhance_router
from app.colorize.routes import router as colorize_router

app = FastAPI()

app.include_router(enhance_router, prefix="/enhance")
app.include_router(colorize_router, prefix="/colorize")