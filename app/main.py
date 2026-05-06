from fastapi import FastAPI
from app.routers import crews
app = FastAPI()
app.include_router(crews.router)
@app.get("/")
def root():
    return {"message": "One Piece API funcionando"}