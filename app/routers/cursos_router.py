from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from app.services.cursos_service import CursosService, CursoData
from app.models.curso import Curso

cursos_router = APIRouter(prefix="/cursos", tags=["Cursos"])


class CursoPayload(BaseModel):
    codigo: int
    materia: str
    profesor_id: int
    colegio_id: int
    anio_cursado: int
    division: str
    preguntas: list


class CursoResponse(CursoPayload):
    profesor: dict = None
    colegio: dict = None
    profesor_id: int = None
    colegio_id: int = None
    estudiantes: list = []


class AgregarAlumnoPayload(BaseModel):
    estudiante_id: int
    respuestas: dict


class AgregarAlumnoResponse(AgregarAlumnoPayload):
    curso_id: int


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
            division=payload.division,
            preguntas=payload.preguntas
        )
        curso = service.crear_curso(data)
        return CursoResponse(codigo=curso.codigo, materia=curso.materia, profesor=curso.profesor.to_dict(),
                             colegio=curso.colegio.to_dict(), anio_cursado=curso.anio_cursado, division=curso.division
                             , preguntas=[pregunta.to_dict() for pregunta in curso.preguntas])
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@cursos_router.get("/{id_curso}", response_model=List[CursoResponse])
def obtener_curso(id_curso: int, service: CursosService = Depends(CursosService)):
    """
    Obtiene un curso
    """
    try:
        curso = service.obtener_curso(id_curso)
        profesor_dict = {
            "id": curso.profesor.id,
            "nombre": curso.profesor.nombre,
            "apellido": curso.profesor.apellido,
        }
        colegio_dict = {
            "id": curso.colegio.id,
            "nombre": curso.colegio.nombre,
        }
        return [CursoResponse(codigo=curso.codigo, materia=curso.materia, profesor=profesor_dict,
                              colegio=colegio_dict, anio_cursado=curso.anio_cursado, division=curso.division,
                              preguntas=[pregunta.to_dict() for pregunta in curso.preguntas])]
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@cursos_router.get("/profesores/{profesor_id}", response_model=list[CursoResponse])
def obtener_cursos_por_profesor(profesor_id: int, service: CursosService = Depends(CursosService)):
    """
    Obtiene todos los cursos de un profesor
    """

    try:
        cursos = service.obtener_cursos_por_profesor(profesor_id)
        response = []
        for curso in cursos:
            profesor_dict = {
                "id": curso.profesor.id,
                "nombre": curso.profesor.nombre,
                "apellido": curso.profesor.apellido,
            }
            colegio_dict = {
                "id": curso.colegio.id,
                "nombre": curso.colegio.nombre,
            }
            response.append(CursoResponse(codigo=curso.codigo, materia=curso.materia, profesor=profesor_dict,
                                            colegio=colegio_dict, anio_cursado=curso.anio_cursado,
                                            division=curso.division,
                                            preguntas=[pregunta.to_dict() for pregunta in curso.preguntas]))
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@cursos_router.get("/estudiantes/{estudiante_id}", response_model=list[CursoResponse])
def obtener_cursos_por_estudiante(estudiante_id: int, service: CursosService = Depends(CursosService)):
    """
    Obtiene todos los cursos de un estudiante
    """

    try:
        cursos = service.obtener_cursos_por_estudiante(estudiante_id)
        response = []
        for curso in cursos:
            profesor_dict = {
                "id": curso.profesor.id,
                "nombre": curso.profesor.nombre,
                "apellido": curso.profesor.apellido,
            }
            colegio_dict = {
                "id": curso.colegio.id,
                "nombre": curso.colegio.nombre,
            }
            response.append(CursoResponse(codigo=curso.codigo, materia=curso.materia, profesor=profesor_dict,
                                            colegio=colegio_dict, anio_cursado=curso.anio_cursado,
                                            division=curso.division,
                                            preguntas=[pregunta.to_dict() for pregunta in curso.preguntas]))
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
