from fastapi import FastAPI
from .models.models import Base
from .api.routes import router as api_router
from .database import engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)