from src.models.barrio import BarrioCreate, BarrioResponse, BarrioUpdate
from src.services.barrios_services import BarrioService
from fastapi import HTTPException

class BarrioController:

    def __init__(self):
        self.barrio_service = BarrioService()


    def get_all_barrios(self):
        try:
            # Llama al servicio para obtener una lista de usuarios
            barrios: list[BarrioResponse] = self.barrio_service.getAllBarrios()

            # Convierte cada usuario a un diccionario usando model_dump()
            barrios_dicts = [barrio.model_dump() for barrio in barrios]

            return barrios_dicts  # Devolver la lista de diccionarios
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))
        

    def insert_barrio(self, barrio_dict:BarrioCreate):
        try:
            barrio_response= self.barrio_service.insertBarrio(barrio_dict)
            return (barrio_response.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))