from typing import List, Optional
from src.models.rol import RolCreate, RolResponse, RolUpdate
from src.database.repositories.roles_repo import RolesRepository


class RolesService:
    def __init__(self):
        self.rol_repo = RolesRepository()  # Instancia del repositorio

    def insert_rol(self, rol_data: RolCreate) -> RolResponse:
        # Convertir el modelo a un diccionario
        data_dict = rol_data.model_dump()
        # Insertar en la base de datos
        response_dict = self.rol_repo.insert(data_dict)
        # Devolver la respuesta como modelo Pydantic
        return RolResponse(**response_dict)

    def get_rol_by_id(self, rol_id: int) -> Optional[RolResponse]:
        response_dict = self.rol_repo.getById(rol_id)
        if not response_dict:
            raise ValueError("Rol not found")
        # Convertir el diccionario a un modelo Pydantic
        return RolResponse(**response_dict)

    def get_all_roles(self) -> List[RolResponse]:
        response_dict = self.rol_repo.getAll()
        # Crear una lista de modelos Pydantic para la respuesta
        roles_list = [RolResponse(**rol) for rol in response_dict]
        return roles_list

    def update_rol(self, rol_id: int, rol_data: RolUpdate) -> RolResponse:
        data_dict = rol_data.model_dump()
        updated_dict = self.rol_repo.update(rol_id, data_dict)
        if not updated_dict:
            raise ValueError("Rol not found")
        return RolResponse(**updated_dict)

    def delete_rol(self, rol_id: int):
        # Eliminar el rol por ID
        return self.rol_repo.delete(rol_id)
