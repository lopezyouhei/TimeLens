from fastapi import FastAPI
from app.enhance.routes import router as enhance_router

app = FastAPI()

app.include_router(enhance_router, prefix="/enhance")