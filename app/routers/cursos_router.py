from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from app.services.cursos_service import CursosService, CursoData

cursos_router = APIRouter(prefix="/cursos", tags=["Cursos"])


class CursoPayload(BaseModel):
    codigo: int
    materia: str
    profesor_id: int
    colegio_id: int
    anio_cursado: int
    division: str


class CursoResponse(CursoPayload):
    profesor_id: int = None
    colegio_id: int = None
    colegio: dict = None
    profesor: dict = None
    colegio: str
    estudiantes: list = []


@cursos_router.post("", status_code=HTTPStatus.CREATED, response_model=CursoResponse)
def crear_curso(payload: CursoPayload, service: CursosService = Depends(CursosService)):
    """
    Crea un curso
    """
    try:
        data = CursoData(
            codigo=payload.codigo,
            materia=payload.materia,
            profesor_id=payload.profesor_id,
            colegio_id=payload.colegio_id,
            anio_cursado=payload.anio_cursado,
            division=payload.division
        )
        curso = service.crear_curso(data)
        return CursoResponse(codigo=curso.codigo, materia=curso.materia, profesor_id=curso.profesor_id,
                             colegio_id=curso.colegio_id, anio_cursado=curso.anio_cursado, division=curso.division)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


#ENDPOINT PARA AGREGAR ALUMNO A UN CURSO
@cursos_router.post("/{id_curso}/estudiantes/{id_estudiante}", status_code=HTTPStatus.CREATED, response_model=CursoResponse)
def agregar_alumno_a_curso(id_curso: int, id_estudiante: int, service: CursosService = Depends(CursosService)):
    """
    Agrega un alumno a un curso
    """
    try:
        curso = service.agregar_alumno_a_curso(id_curso, id_estudiante)
        return CursoResponse(codigo=curso.codigo, materia=curso.materia, profesor_id=curso.profesor_id,
                             colegio_id=curso.colegio_id, anio_cursado=curso.anio_cursado, division=curso.division, estudiantes=curso.estudiantes)

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
