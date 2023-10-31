from http import HTTPStatus

from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

colegios_router = APIRouter(prefix="/colegios", tags=["Colegios"])


class ColegioPayload(BaseModel):
    nombre: str


class ColegioResponse(ColegioPayload):
    id: int


@colegios_router.post("", status_code=HTTPStatus.CREATED, response_model=ColegioResponse)
def crear_colegio(payload: ColegioPayload, service: ColegioService = Depends(ColegioService)):
    """
    Crea un colegio
    """
    try:
        colegio = service.crear_colegio(payload)
        return ColegioResponse(**colegio)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
