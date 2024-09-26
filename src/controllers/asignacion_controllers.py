from src.models.asignacion import AsignacionCreate,AsignacionResponse,AsignacionUpdate
from src.services.asignacion_services import AsignacionService
from fastapi import HTTPException

class AsignController:

    def __init__(self):
        self.asign_service = AsignacionService()


    def get_all_asignacion(self):
        try:
            asings: list[AsignacionResponse] = self.asign_service.getAllAsignacion()

            asings_dicts = [asign.model_dump() for asign in asings]

            return asings_dicts  # Devolver la lista de diccionarios
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))
        


    def get_asignacion_by_id(self,id: int):
        try:
            asing: AsignacionResponse= self.asign_service.getAsingnacionById(id)
            asing= asing.model_dump()

            return asing
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))



    def insert_asignacion(self, asignacion:AsignacionCreate):
        try:
            #mandamos el usuario con al contraseña hash
            asignacion_response = self.asign_service.insertAsignacion(asignacion)
            return (asignacion_response.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))



    def update_asignacion(self,id: int, asignacion_data:AsignacionUpdate):
        try:
            asing: AsignacionResponse = self.asign_service.updateAsignacion(id,asing)
            return (asing.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))     
          

    def delete_asignacion(self,id: int):
        try:
            return (self.asign_service.deleteAsignacion(id))
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))       
        