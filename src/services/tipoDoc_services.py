from src.models.tipoDoc import TipoDocCreate, TipoDocResponse, TipoDocUpdate
from src.database.repositories.tipoDoc_repo import TipoDocRepository
from typing import List, Optional


class TipoDocService:
    def __init__(self):
        self.tipo_doc_repo = TipoDocRepository()  # Instancia del repositorio

    def insert_tipo_doc(self, tipo_doc_data: TipoDocCreate) -> TipoDocResponse:
        # Convertir el modelo a un diccionario
        data_dict = tipo_doc_data.model_dump()
        # Insertar en la base de datos
        response_dict = self.tipo_doc_repo.insert(data_dict)
        # Devolver la respuesta como modelo
        return TipoDocResponse(**response_dict)

    def get_tipo_doc_by_id(self, tipo_doc_id: int) -> Optional[TipoDocResponse]:
        response_dict = self.tipo_doc_repo.getById(tipo_doc_id)
        if not response_dict:
            raise ValueError("TipoDoc not found")
        # Convertir el diccionario en un modelo Pydantic
        return TipoDocResponse(**response_dict)

    def get_all_tipo_doc(self) -> List[TipoDocResponse]:
        response_dict = self.tipo_doc_repo.getAll()
        # Crear una lista de modelos Pydantic
        tipo_doc_list = [TipoDocResponse(**tipo_doc) for tipo_doc in response_dict]
        return tipo_doc_list

    def update_tipo_doc(self, tipo_doc_id: int, tipo_doc_data: TipoDocUpdate) -> TipoDocResponse:
        data_dict = tipo_doc_data.model_dump()
        updated_dict = self.tipo_doc_repo.update(tipo_doc_id, data_dict)
        if not updated_dict:
            raise ValueError("TipoDoc not found")
        return TipoDocResponse(**updated_dict)

    def delete_tipo_doc(self, tipo_doc_id: int):
        return self.tipo_doc_repo.delete(tipo_doc_id)
