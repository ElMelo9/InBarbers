from fastapi import APIRouter
from src.models.login import Login
from src.controllers.usuarios_controllers import UserController

login = APIRouter()
user_controller = UserController()

@login.post("/login")
def insert(usuario_data: Login):
    # Llama al controlador para insertar el rol
    return user_controller.login_usuario(usuario_data)