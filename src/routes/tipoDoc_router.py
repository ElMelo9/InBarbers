from fastapi import APIRouter
from src.models.tipoDoc import TipoDocCreate
from src.controllers.tipoDoc_controllers import TipoDocController

tipoDoc = APIRouter()
tipoDoc_controller = TipoDocController()

@tipoDoc.get("/tipoDoc/getAll")
def get_all():
    return tipoDoc_controller.get_all_tipoDocs()


@tipoDoc.post("/tipoDoc/insert")
def insert(tipoDoc_data: TipoDocCreate):
    # Llama al controlador para insertar el rol
    return tipoDoc_controller.insert_tipoDoc(tipoDoc_data)