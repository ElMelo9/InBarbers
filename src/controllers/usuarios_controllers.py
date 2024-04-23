from src.models.usuario import UsuarioResponse
from src.services.usuarios_services import UserService
from fastapi import HTTPException

class UserController:

    def __init__(self):
        self.user_service = UserService()


    def get_all_usuarios(self):
        try:
            # Llama al servicio para obtener una lista de usuarios
            usuarios: list[UsuarioResponse] = self.user_service.getAllUsuarios()

            # Convierte cada usuario a un diccionario usando model_dump()
            usuarios_dicts = [usuario.model_dump() for usuario in usuarios]

            return usuarios_dicts  # Devolver la lista de diccionarios
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))