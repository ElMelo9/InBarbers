from fastapi import FastAPI
from src.routes.incial_route import inicial
from src.routes.usuarios_route import usuarios
from src.routes.roles_route import roles
from src.routes.tipoDoc_router import tipo_doc
from src.routes.barrios_router import barrios
from src.routes.login_router import login
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# Agregar middleware para permitir CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes especificar una lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Puedes especificar una lista de métodos permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Puedes especificar una lista de encabezados permitidos
)

app.include_router(inicial)
app.include_router(usuarios)
app.include_router(roles)
app.include_router(tipo_doc)
app.include_router(barrios)
app.include_router(login)


#uvicorn main:app --reload