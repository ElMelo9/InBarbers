from src.models.servicio import  ServicioCreate,ServicioResponse,ServicioUpdate
from src.services.servicio_services import ServicioService
from fastapi import HTTPException

class ServicioController:

    def __init__(self):
        self.service = ServicioService()


    def get_all_servicio(self):
        try:
            servicios: list[ServicioResponse] = self.service.getAllServicio()

            servicios_dicts = [servicio.model_dump() for servicio in servicios]

            return servicios_dicts  # Devolver la lista de diccionarios
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))
        


    def get_servicio_by_id(self,id: int):
        try:
            servicio: ServicioResponse= self.service.getServicioById(id)
            servicio= servicio.model_dump()

            return servicio
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))



    def insert_servicio(self, servicio:ServicioCreate):
        try:
            servicio_response = self.service.insertServicio(servicio)
            return (servicio_response.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))



    def update_servicio(self,id: int, servicio_data:ServicioUpdate):
        try:
            servicio: ServicioResponse = self.service.updateServicio(id,servicio)
            return (servicio.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))     
          

    def delete_servicio(self,id: int):
        try:
            return (self.service.deleteServicio(id))
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))       
        