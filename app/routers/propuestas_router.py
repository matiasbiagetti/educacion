from http import HTTPStatus

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.propuestas_service import PropuestasService

propuestas_router = APIRouter(prefix="/propuestas", tags=["Propuestas"])


class PropuestaPayload(BaseModel):
    tipo: str
    tema: str


class PropuestaResponse(PropuestaPayload):
    texto: str


@propuestas_router.post("/cursos/{curso_codigo}", status_code=HTTPStatus.CREATED, response_model=PropuestaResponse)
def crear_propuesta(curso_codigo: int, payload: PropuestaPayload,
                    service: PropuestasService = Depends(PropuestasService)):
    """
    Crea una propuesta
    """
    propuesta = service.crear_propuesta(curso_codigo, payload.tema, payload.tipo)
    print(propuesta)

    return PropuestaResponse(
        tipo=payload.tipo,
        tema=payload.tema,
        texto=propuesta
    )



