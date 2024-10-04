from fastapi import APIRouter, Depends
from src.models.ubicacion import UbicacionCreate,UbicacionResponse,UbicacionUpdate
from src.controllers.ubicacion_controllers import UbicacionController
from src.utils.token import verificarToken

ubicacion = APIRouter()
ubicacion_controller = UbicacionController()

@ubicacion.get("/ubicacion/getAll", response_model=list[UbicacionResponse])
def get_all(user=Depends(verificarToken)):
    return ubicacion_controller.get_all_ubicacion()

@ubicacion.get("/ubicacion/getById/{id}", response_model=UbicacionResponse)
def get_by_id(id: int, user=Depends(verificarToken)):
    return ubicacion_controller.get_ultim_ubi_by_id(id)


@ubicacion.get("/ubicacion/getByUser/{id}", response_model=UbicacionResponse)
def get_by_user(id: int, user=Depends(verificarToken)):
    return ubicacion_controller.get_ultim_ubi_by_id(id)

@ubicacion.post("/ubicacion/insert", response_model=UbicacionResponse)
def insert(ubicacion_data: UbicacionCreate, user=Depends(verificarToken)):
    return ubicacion_controller.insert_ubicacion(ubicacion_data)

@ubicacion.put("/ubicacion/update/{id}", response_model=UbicacionResponse)
def update(id: int, ubicacion_data: UbicacionUpdate, user=Depends(verificarToken)):
    return ubicacion_controller.update_ubicacion(id, ubicacion_data)

@ubicacion.delete("/ubicacion/delete/{id}")
def delete(id: int, user=Depends(verificarToken)):
    return ubicacion_controller.delete_ubicacion(id)