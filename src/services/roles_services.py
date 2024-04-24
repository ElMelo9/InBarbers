from src.models.rol import RolResponse,RolCreate,RolUpdate
from src.database.repositories.roles_repo import RolesRepository


class RolService:

    def __init__(self):
        self.rol_repo = RolesRepository()


    def insertRol(self, rol:RolCreate) -> RolResponse:

        data_dict = rol.model_dump()
        response_dict = self.rol_repo.insert(data_dict)
        return RolResponse(**response_dict)


    def getRol(self, rol_id: int) -> RolResponse:
        
        response_dict = self.rol_repo.getById(rol_id)

        # Verificar si se encontró el usuario
        if not response_dict:
            raise ValueError("Rol not found")

        return RolResponse(**response_dict)
    
    def getAllRoles(self) -> list[RolResponse] :

        response_dict = self.rol_repo.getAll()

        usuarios_list = [RolResponse(**usuario) for usuario in response_dict]

        return usuarios_list