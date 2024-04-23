from src.models.rol import RolResponse,RolCreate,RolUpdate
from src.services.roles_services import RolService
from fastapi import HTTPException

class RolController:

    def __init__(self):
        self.rol_service = RolService()


    def get_all_roles(self):
        try:
            # Llama al servicio para obtener una lista de usuarios
            roles: list[RolResponse] = self.rol_service.getAllRoles()

            # Convierte cada usuario a un diccionario usando model_dump()
            roles_dicts = [rol.model_dump() for rol in roles]

            return roles_dicts  # Devolver la lista de diccionarios
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))
        

    def insert_rol(self, rol_dict: dict):
        try:
            rol_create= RolCreate(**rol_dict)   
            rol_response= self.rol_service.insertRol(rol_create)
            return rol_dict(rol_response.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))