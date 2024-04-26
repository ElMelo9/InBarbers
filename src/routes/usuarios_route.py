from fastapi import APIRouter,Depends
from src.models.login import Login
from src.models.usuario import UsuarioCreate,UsuarioResponse,UsuarioUpdate
from src.controllers.usuarios_controllers import UserController
from src.utils.token import verificarToken

usuarios = APIRouter()
user_controller = UserController()

@usuarios.get("/usuarios/getAll", response_model=list[UsuarioResponse])
def get_all(user=Depends(verificarToken)):
    return user_controller.get_all_usuarios()


@usuarios.get("/usuarios/getById/{id_usuario}", response_model=UsuarioResponse)
def get_by_id(id_usuario,user=Depends(verificarToken)):
    return user_controller.get_usuarios_by_id(id_usuario)


@usuarios.post("/usuarios/insert", response_model=UsuarioResponse)
def insert(usuario_data: UsuarioCreate,user=Depends(verificarToken)):
    # Llama al controlador para insertar el rol
    return user_controller.insert_usuario(usuario_data)



@usuarios.put("/usuarios/update/{id_usuario}", response_model=UsuarioResponse)
def update(id_usuario,usuario_data: UsuarioUpdate,user=Depends(verificarToken)):
    # Llama al controlador para insertar el rol
    return user_controller.update_usuario(id_usuario,usuario_data)


@usuarios.delete("/usuarios/delete/{id_usuario}")
def update(id_usuario,user=Depends(verificarToken)):
    # Llama al controlador para insertar el rol
    return user_controller.delete_usuario(id_usuario)
