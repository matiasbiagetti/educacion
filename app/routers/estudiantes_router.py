from http import HTTPStatus
from typing import List, Dict

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.services.cursos_service import CursosService
from app.services.estudiantes_service import AgregarEstudianteACursoData, EstudiantesService

estudiantes_router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])


class AgregarEstudianteACursoPayload(BaseModel):
    respuestas: List[Dict[str,int]]


class AgregarEstudianteACursoResponse(AgregarEstudianteACursoPayload):
    cursos: List[dict]
    estudiante_id: int
    estudiante_nombre: str


@estudiantes_router.post("/{estudiante_id}/cursos/{curso_codigo}", status_code=HTTPStatus.CREATED,
                         response_model=AgregarEstudianteACursoResponse)
def agregar_estudiante_a_curso(estudiante_id: int,
                               curso_codigo: int,
                               payload: AgregarEstudianteACursoPayload,
                               service: EstudiantesService = Depends(EstudiantesService)):
    """
    Agrega un estudiante a un curso
    """
    try:
        data = AgregarEstudianteACursoData(
            estudiante_id=estudiante_id,
            respuestas=payload.respuestas,
            curso_codigo=curso_codigo
        )
        estudiante_respuesta = service.agregar_estudiante_a_curso(data)
        cursos = [curso.to_dict() for curso in estudiante_respuesta.cursos if curso.codigo == curso_codigo]
        respuestas_response = [{
            "id": respuesta.id,
            "opcion": {
                "id": respuesta.opcion.id,
                "opcion": respuesta.opcion.texto,
            },
            "pregunta": {
                "id": respuesta.pregunta.id,
                "pregunta": respuesta.pregunta.texto,
            },
            "estudiante": {
                "id": respuesta.estudiante.id,
                "nombre": respuesta.estudiante.nombre,
            },
            "curso": {
                "codigo": respuesta.curso.codigo,
                "materia": respuesta.curso.materia,
                "anio_cursado": respuesta.curso.anio_cursado,
                "division": respuesta.curso.division,
            },
        } for respuesta in estudiante_respuesta.respuestas if respuesta.curso.codigo == curso_codigo]

        return AgregarEstudianteACursoResponse(
            cursos=cursos,
            estudiante_id=estudiante_respuesta.id,
            estudiante_nombre=estudiante_respuesta.nombre,
            respuestas=respuestas_response
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
