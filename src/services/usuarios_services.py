from src.models.login import Login, LoginResponse
from src.models.usuario import UsuarioResponse, UsuarioCreate, UsuarioUpdate
from src.database.repositories.usuarios_repo import UsuariosRepository


class UserService:

    def __init__(self):
        self.user_repo = UsuariosRepository()

    def insertUsuario(self, usuario: UsuarioCreate) -> UsuarioResponse:

        data_dict = usuario.model_dump()

        response_dict = self.user_repo.insert(data_dict)

        return UsuarioResponse(**response_dict)

    def getUsuarioById(self, user_id: int) -> UsuarioResponse:

        response_dict = self.user_repo.getById(user_id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("User not found")

        return UsuarioResponse(**response_dict)

    def getAllUsuarios(self) -> list[UsuarioResponse]:

        response_dict = self.user_repo.getAll()

        usuarios_list = [UsuarioResponse(**usuario)
                         for usuario in response_dict]

        return usuarios_list

    def getUsuarioByEmail(self, email_usuario: str) -> UsuarioResponse:
        # Obtener el usuario por email
        usuario_dict = self.user_repo.getByEmail(email_usuario)
        if not usuario_dict:
            raise ValueError("User not found")

        return UsuarioResponse(**usuario_dict)

    def updateUsuario(self, user_id: int, usuario: UsuarioUpdate) -> UsuarioResponse:

        data_dict = usuario.model_dump()

        usuario_dict = self.user_repo.update(user_id, data_dict)
        if not usuario_dict:
            raise ValueError("User not found")

        return UsuarioResponse(**usuario_dict)

    def deleteUsuario(self, user_id: int):

        return self.user_repo.delete(user_id)

    def usuarioLogin(self, email_usuario: str) -> dict:
        # Obtener el usuario por email
        usuario_dict = self.user_repo.getByEmail(email_usuario)
        if not usuario_dict:
            raise ValueError("Email incorrecto")
        return usuario_dict
