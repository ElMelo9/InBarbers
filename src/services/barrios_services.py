from src.models.barrio import BarrioCreate,BarrioResponse,BarrioUpdate
from src.database.repositories.barrios_repo import BarriosRepository


class BarrioService:

    def __init__(self):
        self.barrio_repo = BarriosRepository()


    def insertBarrio(self, barrio:BarrioCreate) -> BarrioResponse:

        data_dict = barrio.model_dump()
        response_dict = self.barrio_repo.insert(data_dict)
        return BarrioResponse(**response_dict)


    def getBarrio(self, barrio_id: int) -> BarrioResponse:
        
        response_dict = self.barrio_repo.getById(barrio_id)

        # Verificar si se encontró
        if not response_dict:
            raise ValueError("Rol not found")

        return BarrioResponse(**response_dict)
    
    def getAllBarrios(self) -> list[BarrioResponse] :

        response_dict = self.barrio_repo.getAll()

        bario_list = [BarrioResponse(**barrio) for barrio in response_dict]

        return bario_list