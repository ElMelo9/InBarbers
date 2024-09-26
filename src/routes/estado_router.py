from fastapi import APIRouter, Depends
from src.models.estadoServicio import EstadoServicioCreate,EstadoServicioResponse,EstadoServicioUpdate
from src.controllers.estado_controllers import EstadoController
from src.utils.token import verificarToken

estado = APIRouter()
estado_controller = EstadoController()

@estado.get("/estado/getAll", response_model=list[EstadoServicioResponse])
def get_all(user=Depends(verificarToken)):
    return estado_controller.get_all_estado()

@estado.get("/estado/getById/{id}", response_model=EstadoServicioResponse)
def get_by_id(id: int, user=Depends(verificarToken)):
    return estado_controller.get_estado_by_id(id)

@estado.post("/estado/insert", response_model=EstadoServicioResponse)
def insert(estado_data: EstadoServicioCreate, user=Depends(verificarToken)):
    return estado_controller.insert_estado(estado_data)

@estado.put("/estado/update/{id}", response_model=EstadoServicioResponse)
def update(id: int, estado_data: EstadoServicioUpdate, user=Depends(verificarToken)):
    return estado_controller.update_estado(id, estado_data)

@estado.delete("/estado/delete/{id}")
def delete(id: int, user=Depends(verificarToken)):
    return estado_controller.delete_estado(id)