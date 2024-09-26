from fastapi import APIRouter, Depends
from src.models.asignacion import AsignacionCreate, AsignacionResponse, AsignacionUpdate
from src.controllers.asignacion_controllers import AsignController
from src.utils.token import verificarToken

asign = APIRouter()
asign_controller = AsignController()

@asign.get("/asign/getAll", response_model=list[AsignacionResponse])
def get_all(user=Depends(verificarToken)):
    return asign_controller.get_all_asignacion()

@asign.get("/asign/getById/{id}", response_model=AsignacionResponse)
def get_by_id(id: int, user=Depends(verificarToken)):
    return asign_controller.get_asignacion_by_id(id)

@asign.post("/asign/insert", response_model=AsignacionResponse)
def insert(asign_data: AsignacionCreate, user=Depends(verificarToken)):
    return asign_controller.insert_asignacion(asign_data)

@asign.put("/asign/update/{id}", response_model=AsignacionResponse)
def update(id: int, asign_data: AsignacionUpdate, user=Depends(verificarToken)):
    return asign_controller.update_asignacion(id, asign_data)

@asign.delete("/asign/delete/{id}")
def delete(id: int, user=Depends(verificarToken)):
    return asign_controller.delete_asignacion(id)