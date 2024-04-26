from fastapi import HTTPException
from src.models.barrio import BarrioResponse, BarrioCreate, BarrioUpdate
from src.services.barrios_services import BarriosService

class BarriosController:
    def __init__(self):
        self.barrios_service = BarriosService()

    def get_all_barrios(self):
        try:
            barrios_list = self.barrios_service.get_all_barrios()
            return [barrio.model_dump() for barrio in barrios_list]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_barrio_by_id(self, barrio_id: int):
        try:
            barrio = self.barrios_service.get_barrio_by_id(barrio_id)
            return barrio.model_dump()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_barrio(self, barrio_data: BarrioCreate):
        try:
            barrio_response = self.barrios_service.insert_barrio(barrio_data)
            return barrio_response.model_dump()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_barrio(self, barrio_id: int, barrio_data: BarrioUpdate):
        try:
            updated_barrio = self.barrios_service.update_barrio(barrio_id, barrio_data)
            return updated_barrio.model_dump()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_barrio(self, barrio_id: int):
        try:
            return self.barrios_service.delete_barrio(barrio_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
