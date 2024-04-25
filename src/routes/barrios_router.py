from fastapi import APIRouter
from src.models.barrio import BarrioCreate,BarrioResponse,BarrioUpdate
from src.controllers.barrios_controllers import BarrioController

barrios = APIRouter()
barrio_controller = BarrioController()

@barrios.get("/barrios/getAll")
def get_all():
    return barrio_controller.get_all_barrios()


@barrios.post("/barrios/insert")
def insert(barrio_data: BarrioCreate):
    # Llama al controlador para insertar el rol
    return barrio_controller.insert_barrio(barrio_data)