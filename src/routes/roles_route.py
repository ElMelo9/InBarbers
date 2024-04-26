from fastapi import APIRouter, Depends
from src.models.rol import RolCreate, RolResponse, RolUpdate
from src.controllers.roles_controllers import RolesController
from src.utils.token import verificarToken

roles = APIRouter()
roles_controller = RolesController()

@roles.get("/roles/getAll", response_model=list[RolResponse])
def get_all(user=Depends(verificarToken)):
    return roles_controller.get_all_roles()

@roles.get("/roles/getById/{rol_id}", response_model=RolResponse)
def get_by_id(rol_id: int, user=Depends(verificarToken)):
    return roles_controller.get_rol_by_id(rol_id)

@roles.post("/roles/insert", response_model=RolResponse)
def insert(rol_data: RolCreate, user=Depends(verificarToken)):
    return roles_controller.insert_rol(rol_data)

@roles.put("/roles/update/{rol_id}", response_model=RolResponse)
def update(rol_id: int, rol_data: RolUpdate, user=Depends(verificarToken)):
    return roles_controller.update_rol(rol_id, rol_data)

@roles.delete("/roles/delete/{rol_id}")
def delete(rol_id: int, user=Depends(verificarToken)):
    return roles_controller.delete_rol(rol_id)
