from fastapi import APIRouter, Depends
from src.models.barrio import BarrioCreate, BarrioResponse, BarrioUpdate
from src.controllers.barrios_controllers import BarriosController
from src.utils.token import verificarToken

barrios = APIRouter()
barrios_controller = BarriosController()

@barrios.get("/barrios/getAll", response_model=list[BarrioResponse])
def get_all(user=Depends(verificarToken)):
    return barrios_controller.get_all_barrios()

@barrios.get("/barrios/getById/{barrio_id}", response_model=BarrioResponse)
def get_by_id(barrio_id: int, user=Depends(verificarToken)):
    return barrios_controller.get_barrio_by_id(barrio_id)

@barrios.post("/barrios/insert", response_model=BarrioResponse)
def insert(barrio_data: BarrioCreate, user=Depends(verificarToken)):
    return barrios_controller.insert_barrio(barrio_data)

@barrios.put("/barrios/update/{barrio_id}", response_model=BarrioResponse)
def update(barrio_id: int, barrio_data: BarrioUpdate, user=Depends(verificarToken)):
    return barrios_controller.update_barrio(barrio_id, barrio_data)

@barrios.delete("/barrios/delete/{barrio_id}")
def delete(barrio_id: int, user=Depends(verificarToken)):
    return barrios_controller.delete_barrio(barrio_id)
