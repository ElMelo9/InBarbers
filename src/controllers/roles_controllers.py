from fastapi import HTTPException
from src.models.rol import RolResponse, RolCreate, RolUpdate
from src.services.roles_services import RolesService

class RolesController:

    def __init__(self):
        self.roles_service = RolesService()

    def get_all_roles(self):
        try:
            roles_list = self.roles_service.get_all_roles()
            return [rol.model_dump() for rol in roles_list]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_rol_by_id(self, rol_id: int):
        try:
            rol = self.roles_service.get_rol_by_id(rol_id)
            return rol.model_dump()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_rol(self, rol_data: RolCreate):
        try:
            rol_response = self.roles_service.insert_rol(rol_data)
            return rol_response.model_dump()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_rol(self, rol_id: int, rol_data: RolUpdate):
        try:
            updated_rol = self.roles_service.update_rol(rol_id, rol_data)
            return updated_rol.model_dump()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_rol(self, rol_id: int):
        try:
            return self.roles_service.delete_rol(rol_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
