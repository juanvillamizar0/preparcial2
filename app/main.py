from fastapi import FastAPI
from app.database import engine, Base
import app.models
Base.metadata.create_all(bind=engine)
app = FastAPI()
@app.get("/")
def root():
    return {"message": "One Piece API funcionando"}
