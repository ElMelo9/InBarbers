from fastapi import FastAPI
from src.routes.incial_route import inicial
from src.routes.usuarios_route import usuarios
from src.routes.roles_route import roles
from src.routes.tipoDoc_router import tipo_doc
from src.routes.barrios_router import barrios
from src.routes.login_router import login

app = FastAPI()

app.include_router(inicial)
app.include_router(usuarios)
app.include_router(roles)
app.include_router(tipo_doc)
app.include_router(barrios)
app.include_router(login)


#uvicorn main:app --reload