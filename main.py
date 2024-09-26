from fastapi import FastAPI
from src.routes.incial_route import inicial
from src.routes.usuarios_route import usuarios
from src.routes.roles_route import roles
from src.routes.tipoDoc_router import tipo_doc
from src.routes.barrios_router import barrios
from src.routes.login_router import login
from src.routes.asignacion_router import asign
from src.routes.estado_router import estado
from src.routes.servicio_router import servicio
from src.routes.tipoServicio_router import tipoServicio
from src.routes.ubicacion_router import ubicacion
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
app.include_router(asign)
app.include_router(estado)
app.include_router(servicio)
app.include_router(tipoServicio)
app.include_router(ubicacion)



#uvicorn main:app --reload