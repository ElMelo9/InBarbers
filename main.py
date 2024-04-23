from fastapi import FastAPI
from src.routes.incial_route import inicial
from src.routes.usuarios_route import usuarios

app = FastAPI()

app.include_router(inicial)
app.include_router(usuarios)