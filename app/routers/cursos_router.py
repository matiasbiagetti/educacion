from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from app.services.cursos_service import CursosService, CursoData
from app.models.curso import Curso
from app.services.estudiantes_service import EstudiantesService

cursos_router = APIRouter(prefix="/cursos", tags=["Cursos"])


class CursoPayload(BaseModel):
    codigo: int = None
    materia: str
    profesor_id: int
    colegio_id: int
    anio_cursado: int
    division: str
    preguntas: List[int]


class CursoResponse(CursoPayload):
    profesor: dict = None
    colegio: dict = None
    profesor_id: int = None
    colegio_id: int = None
    estudiantes: list
    preguntas: List[dict] = []


@cursos_router.post("", status_code=HTTPStatus.CREATED, response_model=CursoResponse)
def crear_curso(payload: CursoPayload, service: CursosService = Depends(CursosService),
                estudiante_service: EstudiantesService = Depends(EstudiantesService)):
    """
    Crea un curso
    """
    try:
        if payload.codigo is None:
            data = CursoData(
                materia=payload.materia,
                profesor_id=payload.profesor_id,
                colegio_id=payload.colegio_id,
                anio_cursado=payload.anio_cursado,
                division=payload.division,
                preguntas=payload.preguntas
            )
        else:
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
        return CursoResponse(codigo=curso.codigo, materia=curso.materia, profesor={
            "id": curso.profesor.id,
            "nombre": curso.profesor.nombre,
            "apellido": curso.profesor.apellido,
        },
                             colegio={
                                 "id": curso.colegio.id,
                                 "nombre": curso.colegio.nombre,
                             }, anio_cursado=curso.anio_cursado, division=curso.division
                             , preguntas=[{
                "id": pregunta.id,
                "texto": pregunta.texto,
                "opciones": [{
                    "id": opcion.id,
                    "texto": opcion.texto,
                } for opcion in pregunta.opciones]
            } for pregunta in curso.preguntas],
                             estudiantes=[{
                                 "id": estudiante.id,
                                 "nombre": estudiante.nombre,
                                 "apellido": estudiante.apellido,
                             } for estudiante in estudiante_service.obtener_estudiantes_por_curso(curso.codigo)])


    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@cursos_router.get("/{curso_codigo}", response_model=List[CursoResponse])
def obtener_curso(curso_codigo: int, service: CursosService = Depends(CursosService),
                  estudiantes_service: EstudiantesService = Depends(EstudiantesService)):
    """
    Obtiene un curso
    """
    try:
        curso = service.obtener_curso(curso_codigo)
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
                              preguntas=[{
                                  "id": pregunta.id,
                                  "texto": pregunta.texto,
                                  "opciones": [{
                                      "id": opcion.id,
                                      "texto": opcion.texto,
                                  } for opcion in pregunta.opciones]
                              } for pregunta in curso.preguntas],
                              estudiantes=[{
                                  "id": estudiante.id,
                                  "nombre": estudiante.nombre,
                                  "apellido": estudiante.apellido,
                              } for estudiante in estudiantes_service.obtener_estudiantes_por_curso(curso.codigo)])]

    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@cursos_router.get("/profesores/{profesor_id}", response_model=list[CursoResponse])
def obtener_cursos_por_profesor(profesor_id: int, service: CursosService = Depends(CursosService),
                                estudiantes_service: EstudiantesService = Depends(EstudiantesService)):
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
                                          preguntas=[{
                                              "id": pregunta.id,
                                              "texto": pregunta.texto,
                                              "opciones": [{
                                                  "id": opcion.id,
                                                  "texto": opcion.texto,
                                              } for opcion in pregunta.opciones]
                                          } for pregunta in curso.preguntas],
                                          estudiantes=[{
                                              "id": estudiante.id,
                                              "nombre": estudiante.nombre,
                                              "apellido": estudiante.apellido,
                                          } for estudiante in estudiantes_service.obtener_estudiantes_por_curso(
                                              curso.codigo)]))

        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@cursos_router.get("/estudiantes/{estudiante_id}", response_model=list[CursoResponse])
def obtener_cursos_por_estudiante(estudiante_id: int, service: CursosService = Depends(CursosService),
                                  estudiantes_service: EstudiantesService = Depends(EstudiantesService)):
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
                                          preguntas=[{
                                              "id": pregunta.id,
                                              "texto": pregunta.texto,
                                              "opciones": [{
                                                  "id": opcion.id,
                                                  "texto": opcion.texto,
                                              } for opcion in pregunta.opciones]
                                          } for pregunta in curso.preguntas],
                                          estudiantes=[{
                                              "id": estudiante.id,
                                              "nombre": estudiante.nombre,
                                              "apellido": estudiante.apellido,
                                          } for estudiante in estudiantes_service.obtener_estudiantes_por_curso(
                                              curso.codigo)]))
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
