from fastapi import APIRouter, Depends
from src.models.tipoDoc import TipoDocCreate, TipoDocResponse, TipoDocUpdate
from src.controllers.tipoDoc_controllers import TipoDocController
from src.utils.token import verificarToken  # Tu función para verificar tokens

tipo_doc = APIRouter()
tipo_doc_controller = TipoDocController()

@tipo_doc.get("/tipo-doc/getAll", response_model=list[TipoDocResponse])
def get_all(user=Depends(verificarToken)):
    return tipo_doc_controller.get_all_tipo_doc()

@tipo_doc.get("/tipo-doc/getById/{tipo_doc_id}", response_model=TipoDocResponse)
def get_by_id(tipo_doc_id: int, user=Depends(verificarToken)):
    return tipo_doc_controller.get_tipo_doc_by_id(tipo_doc_id)

@tipo_doc.post("/tipo-doc/insert", response_model=TipoDocResponse)
def insert(tipo_doc_data: TipoDocCreate, user=Depends(verificarToken)):
    return tipo_doc_controller.insert_tipo_doc(tipo_doc_data)

@tipo_doc.put("/tipo-doc/update/{tipo_doc_id}", response_model=TipoDocResponse)
def update(tipo_doc_id: int, tipo_doc_data: TipoDocUpdate, user=Depends(verificarToken)):
    return tipo_doc_controller.update_tipo_doc(tipo_doc_id, tipo_doc_data)

@tipo_doc.delete("/tipo-doc/delete/{tipo_doc_id}")
def delete(tipo_doc_id: int, user=Depends(verificarToken)):
    return tipo_doc_controller.delete_tipo_doc(tipo_doc_id)
