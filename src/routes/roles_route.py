from fastapi import APIRouter
from src.models.rol import RolCreate
from src.controllers.roles_controllers import RolController

roles = APIRouter()
rol_controller = RolController()

@roles.get("/roles/getAll")
def get_all():
    return rol_controller.get_all_roles()


@roles.post("/roles/insert")
def insert_rol(rol_data: RolCreate):
    # Llama al controlador para insertar el rol
    return rol_controller.insert_rol(rol_data)