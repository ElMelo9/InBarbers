from fastapi import HTTPException
from src.models.tipoDoc import TipoDocResponse, TipoDocCreate, TipoDocUpdate
from src.services.tipoDoc_services import TipoDocService

class TipoDocController:
    def __init__(self):
        self.tipo_doc_service = TipoDocService()

    def get_all_tipo_doc(self):
        try:
            tipo_doc_list = self.tipo_doc_service.get_all_tipo_doc()
            return [tipo_doc.model_dump() for tipo_doc in tipo_doc_list]  # Lista de diccionarios
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_tipo_doc_by_id(self, tipo_doc_id: int):
        try:
            tipo_doc = self.tipo_doc_service.get_tipo_doc_by_id(tipo_doc_id)
            return tipo_doc.model_dump()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def insert_tipo_doc(self, tipo_doc_data: TipoDocCreate):
        try:
            tipo_doc_response = self.tipo_doc_service.insert_tipo_doc(tipo_doc_data)
            return tipo_doc_response.model_dump()  # Devolver diccionario
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_tipo_doc(self, tipo_doc_id: int, tipo_doc_data: TipoDocUpdate):
        try:
            updated_tipo_doc = self.tipo_doc_service.update_tipo_doc(tipo_doc_id, tipo_doc_data)
            return updated_tipo_doc.model_dump()  # Devolver diccionario
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_tipo_doc(self, tipo_doc_id: int):
        try:
            return self.tipo_doc_service.delete_tipo_doc(tipo_doc_id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
