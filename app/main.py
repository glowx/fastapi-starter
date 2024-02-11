from fastapi import FastAPI
from .main.models.models import Base
from .main.api.routes import router as api_router
from .database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}