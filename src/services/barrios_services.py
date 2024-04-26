from typing import List, Optional
from src.models.barrio import BarrioCreate, BarrioResponse, BarrioUpdate
from src.database.repositories.barrios_repo import BarriosRepository


class BarriosService:
    def __init__(self):
        self.barrio_repo = BarriosRepository()  # Instancia del repositorio

    def insert_barrio(self, barrio_data: BarrioCreate) -> BarrioResponse:
        # Convertir el modelo a un diccionario
        data_dict = barrio_data.model_dump()
        # Insertar en la base de datos
        response_dict = self.barrio_repo.insert(data_dict)
        # Devolver la respuesta como modelo Pydantic
        return BarrioResponse(**response_dict)

    def get_barrio_by_id(self, barrio_id: int) -> Optional[BarrioResponse]:
        response_dict = self.barrio_repo.getById(barrio_id)
        if not response_dict:
            raise ValueError("Barrio not found")
        # Convertir el diccionario a un modelo Pydantic
        return BarrioResponse(**response_dict)

    def get_all_barrios(self) -> List[BarrioResponse]:
        response_dict = self.barrio_repo.getAll()
        # Crear una lista de modelos Pydantic para la respuesta
        barrios_list = [BarrioResponse(**barrio) for barrio in response_dict]
        return barrios_list

    def update_barrio(self, barrio_id: int, barrio_data: BarrioUpdate) -> BarrioResponse:
        data_dict = barrio_data.model_dump()
        updated_dict = self.barrio_repo.update(barrio_id, data_dict)
        if not updated_dict:
            raise ValueError("Barrio not found")
        return BarrioResponse(**updated_dict)

    def delete_barrio(self, barrio_id: int):
        # Eliminar el barrio por ID
        return self.barrio_repo.delete(barrio_id)
