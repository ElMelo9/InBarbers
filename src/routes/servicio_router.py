from fastapi import APIRouter, Depends
from src.models.servicio import ServicioCreate,ServicioResponse,ServicioUpdate
from src.controllers.servicio_controllers import ServicioController
from src.utils.token import verificarToken

servicio = APIRouter()
servicio_controller = ServicioController()

@servicio.get("/servicio/getAll", response_model=list[ServicioResponse])
def get_all(user=Depends(verificarToken)):
    return servicio_controller.get_all_servicio()

@servicio.get("/servicio/getById/{id}", response_model=ServicioResponse)
def get_by_id(id: int, user=Depends(verificarToken)):
    return servicio_controller.get_servicio_by_id(id)

@servicio.post("/servicio/insert", response_model=ServicioResponse)
def insert(servicio_data: ServicioCreate, user=Depends(verificarToken)):
    return servicio_controller.insert_servicio(servicio_data)

@servicio.put("/servicio/update/{id}", response_model=ServicioResponse)
def update(id: int, servicio_data: ServicioUpdate, user=Depends(verificarToken)):
    return servicio_controller.update_servicio(id, servicio_data)

@servicio.delete("/servicio/delete/{id}")
def delete(id: int, user=Depends(verificarToken)):
    return servicio_controller.delete_servicio(id)