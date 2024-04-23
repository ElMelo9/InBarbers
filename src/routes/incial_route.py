from fastapi import APIRouter

inicial = APIRouter()

@inicial.get("/")
def read_root():
    return {"Hello": "World"}