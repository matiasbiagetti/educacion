from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

cursos_router = APIRouter(prefix="/cursos", tags=["Cursos"])


class CursoPayload(BaseModel):
    materia: str
    profesor_id: int
    colegio_id: int
    anio_cursado: int
    division: str


class CursoResponse(CursoPayload):
    id: int
    profesor_id: int = None
    colegio_id: int = None
    colegio: str
    profesor: str
    colegio: str


@cursos_router.post("/", status_code=HTTPStatus.CREATED, response_model=CursoResponse)
def crear_curso(payload: CursoPayload, service: CursosService = Depends(CursosService)):
    """
    Crea un curso
    """
    try:
        curso = service.crear_curso(payload)
        return CursoResponse(**curso)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@cursos_router.get("/{id_curso}", response_model=CursoResponse)
def obtener_curso(id_curso: int, service: CursosService = Depends(CursosService)):
    """
    Obtiene un curso
    """
    try:
        curso = service.obtener_curso(id_curso)
        return CursoResponse(**curso)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

