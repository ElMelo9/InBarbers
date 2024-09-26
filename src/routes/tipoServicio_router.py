from fastapi import APIRouter, Depends
from src.models.tipoServicio import TipoServicioCreate, TipoServicioResponse, TipoServicioUpdate
from src.controllers.tipo_servicio_controllers import TipoServicioController
from src.utils.token import verificarToken

tipoServicio = APIRouter()
tipoServicio_controller = TipoServicioController()

@tipoServicio.get("/TipoServicio/getAll", response_model=list[TipoServicioResponse])
def get_all(user=Depends(verificarToken)):
    return tipoServicio_controller.get_all_TipoServicio()

@tipoServicio.get("/TipoServicio/getById/{id}", response_model=TipoServicioResponse)
def get_by_id(id: int, user=Depends(verificarToken)):
    return tipoServicio_controller.get_servicio_by_id(id)

@tipoServicio.post("/TipoServicio/insert", response_model=TipoServicioResponse)
def insert(servicio_data: TipoServicioCreate, user=Depends(verificarToken)):
    return tipoServicio_controller.insert_TipoServicio(servicio_data)

@tipoServicio.put("/TipoServicio/update/{id}", response_model=TipoServicioResponse)
def update(id: int, servicio_data: TipoServicioUpdate, user=Depends(verificarToken)):
    return tipoServicio_controller.update_TipoServicio(id, servicio_data)

@tipoServicio.delete("/TipoServicio/delete/{id}")
def delete(id: int, user=Depends(verificarToken)):
    return tipoServicio_controller.delete_TipoServicio(id)