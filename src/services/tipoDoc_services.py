from src.models.tipoDoc import TipoDocCreate,TipoDocResponse,TipoDocUpdate
from src.database.repositories.tipoDoc_repo import TipoDocRepository


class TipoDocService:

    def __init__(self):
        self.tipoDoc_repo = TipoDocRepository()


    def insertTipoDoc(self, tipoDoc:TipoDocCreate) -> TipoDocResponse:

        data_dict = tipoDoc.model_dump()
        response_dict = self.tipoDoc_repo.insert(data_dict)
        return TipoDocResponse(**response_dict)


    def getTipoDoc(self, tipoDoc_id: int) -> TipoDocResponse:
        
        response_dict = self.tipoDoc_repo.getById(tipoDoc_id)

        # Verificar si se encontró
        if not response_dict:
            raise ValueError("Rol not found")

        return TipoDocResponse(**response_dict)
    
    def getAllTipoDocs(self) -> list[TipoDocResponse] :

        response_dict = self.tipoDoc_repo.getAll()

        tipoDoc_list = [TipoDocResponse(**tipoDoc) for tipoDoc in response_dict]

        return tipoDoc_list