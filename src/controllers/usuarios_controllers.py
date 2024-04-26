from src.models.login import Login, LoginResponse
from src.models.usuario import UsuarioResponse,UsuarioCreate,UsuarioUpdate
from src.services.usuarios_services import UserService
from fastapi import HTTPException
from src.utils.security import Security
from src.utils.token import Token

class UserController:

    def __init__(self):
        self.user_service = UserService()
        self.user_security = Security()
        self.user_token = Token()


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
        


    def get_usuarios_by_id(self,id_usuario: int):
        try:
            usuario: UsuarioResponse= self.user_service.getUsuarioById(id_usuario)
            usuario= usuario.model_dump()

            return usuario 
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))


    def insert_usuario(self, usuario:UsuarioCreate):
        try:
            # Aplica el hash a la contraseña antes de llamar al servicio
            usuario.password_usuario = self.user_security.hash_password(usuario.password_usuario)
            #mandamos el usuario con al contraseña hash
            usuario_response= self.user_service.insertUsuario(usuario)
            return (usuario_response.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))


    def update_usuario(self,id_usuario: int, usuario_data:UsuarioUpdate):
        try:
            #mandamos el usuario con al contraseña hash
            usuario: UsuarioResponse = self.user_service.updateUsuario(id_usuario,usuario_data)
            return (usuario.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))     
          

    def delete_usuario(self,id_usuario: int):
        try:
            return (self.user_service.deleteUsuario(id_usuario))
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))       
        

    def login_usuario(self,login: Login)-> LoginResponse:
        try:
            usuario = self.user_service.usuarioLogin(login.email_usuario)

            # Verificar la contraseña
            if not self.user_security.verify_password(login.password_usuario, usuario['password_usuario']):
             raise HTTPException(status_code=401, detail="Contraseña incorrecta")

            return LoginResponse(**self.user_token.generarToken(usuario['nombre_usuario']))
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))        