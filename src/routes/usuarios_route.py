from fastapi import APIRouter,Depends
from src.models.login import Login
from src.models.usuario import UsuarioCreate,UsuarioResponse,UsuarioUpdate
from src.controllers.usuarios_controllers import UserController
from src.utils.token import get_current_user

usuarios = APIRouter()
user_controller = UserController()

@usuarios.get("/usuarios/getAll", response_model=list[UsuarioResponse])
def get_all(user=Depends(get_current_user)):
    return user_controller.get_all_usuarios()

@usuarios.post("/usuarios/insert")
def insert(usuario_data: UsuarioCreate):
    # Llama al controlador para insertar el rol
    return user_controller.insert_usuario(usuario_data)


@usuarios.post("/usuarios/login")
def insert(usuario_data: Login):
    # Llama al controlador para insertar el rol
    return user_controller.login_usuario(usuario_data)