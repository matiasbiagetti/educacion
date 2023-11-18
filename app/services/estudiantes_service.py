from typing import List

from fastapi import Depends
from pydantic import BaseModel

from app.models.estudiante import Estudiante
from app.models.respuesta import Respuesta
from app.repository.estudiantes_repository import EstudiantesRepository
from app.repository.respuestas_repository import RespuestasRepository


class RespuestaData(BaseModel):
    pregunta_id: int
    opcion_id: int


class AgregarEstudianteACursoData(BaseModel):
    estudiante_id: int
    respuestas: List[RespuestaData]
    curso_codigo: int


class EstudiantesService:
    def __init__(self, estudiantes_repository: EstudiantesRepository = Depends(EstudiantesRepository),
                 respuestas_repository: RespuestasRepository = Depends(RespuestasRepository)) -> None:
        self.respuestas_repository = respuestas_repository
        self.estudiantes_repository = estudiantes_repository

    def agregar_estudiante_a_curso(self, data: AgregarEstudianteACursoData) -> Estudiante:
        for respuesta in data.respuestas:
            respuesta_a_guardar = Respuesta(
                alumno_id=data.estudiante_id,
                pregunta_id=respuesta.pregunta_id,
                opcion_id=respuesta.opcion_id,
                curso_codigo=data.curso_codigo
            )
            self.respuestas_repository.save(respuesta_a_guardar)
        estudiante = self.estudiantes_repository.get_by_id(data.estudiante_id)
        return estudiante
