from src.models.usuario import UsuarioResponse,UsuarioCreate,UsuarioUpdate
from src.database.repositories.usuarios import UsuariosRepository


class UserService:

    def __init__(self):
        self.user_repo = UsuariosRepository()


    def insertUsuario(self, usuario:UsuarioCreate) -> UsuarioResponse:

        data_dict = usuario.model_dump()

        response_dict = self.user_repo.insert(data_dict)

        return UsuarioResponse(**response_dict)


    def getUsuario(self, user_id: int) -> UsuarioResponse:
        
        response_dict = self.user_repo.getById(user_id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("User not found")

        return UsuarioResponse(**response_dict)
    
    def getAllUsuarios(self) -> list[UsuarioResponse] :

        response_dict = self.user_repo.getAll()

        usuarios_list = [UsuarioResponse(**usuario) for usuario in response_dict]

        return usuarios_list
