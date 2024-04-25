from src.models.tipoDoc import TipoDocCreate,TipoDocResponse,TipoDocUpdate
from src.services.tipoDoc_services import TipoDocService
from fastapi import HTTPException

class TipoDocController:

    def __init__(self):
        self.tipoDoc_service = TipoDocService()


    def get_all_tipoDocs(self):
        try:
            # Llama al servicio para obtener una lista de usuarios
            tipoDocs: list[TipoDocResponse] = self.tipoDoc_service.getAllTipoDocs()

            # Convierte cada usuario a un diccionario usando model_dump()
            tipoDocs_dicts = [tipoDoc.model_dump() for tipoDoc in tipoDocs]

            return tipoDocs_dicts  # Devolver la lista de diccionarios
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))
        

    def insert_tipoDoc(self, tipoDoc_dict:TipoDocCreate):
        try:
            tipoDoc_response= self.tipoDoc_service.insertTipoDoc(tipoDoc_dict)
            return (tipoDoc_response.model_dump())
        
        except Exception as e:
            # Manejo de errores
            raise HTTPException(status_code=500, detail=str(e))