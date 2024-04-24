from fastapi import FastAPI
from src.routes.incial_route import inicial
from src.routes.usuarios_route import usuarios
from src.routes.roles_route import roles

app = FastAPI()

app.include_router(inicial)
app.include_router(usuarios)
app.include_router(roles)


#uvicorn main:app --reload