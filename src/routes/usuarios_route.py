from fastapi import APIRouter
from src.controllers.usuarios_controllers import UserController

usuarios = APIRouter()
user_controller = UserController()

@usuarios.get("/usuarios/getAll")
def get_all():
    return user_controller.get_all_usuarios()