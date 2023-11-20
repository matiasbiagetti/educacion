from typing import List

from fastapi import Depends
from pydantic import BaseModel

from app.models.estudiante import Estudiante
from app.models.estudiantes_cursos import EstudianteCurso
from app.models.respuesta import Respuesta
from app.repository.estudiantes_cursos_repository import EstudiantesCursosRepository
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
                 respuestas_repository: RespuestasRepository = Depends(RespuestasRepository),
                 estudiantes_cursos_repository: EstudiantesCursosRepository = Depends(EstudiantesCursosRepository)) -> None:
        self.respuestas_repository = respuestas_repository
        self.estudiantes_repository = estudiantes_repository
        self.estudiantes_cursos_repository = estudiantes_cursos_repository

    def agregar_estudiante_a_curso(self, data: AgregarEstudianteACursoData) -> Estudiante:
        self.estudiantes_cursos_repository.save(EstudianteCurso(
            estudiante_id=data.estudiante_id,
            curso_codigo=data.curso_codigo
        ))

        for respuesta in data.respuestas:
            respuesta_a_guardar = Respuesta(
                estudiante_id=data.estudiante_id,
                pregunta_id=respuesta.pregunta_id,
                opcion_id=respuesta.opcion_id,
                curso_codigo=data.curso_codigo
            )
            self.respuestas_repository.save(respuesta_a_guardar)
        estudiante = self.estudiantes_repository.get_by_id(data.estudiante_id)
        return estudiante

    def obtener_estudiantes_por_curso(self, curso_codigo: int) -> List[Estudiante]:
        estudiantes_cursos = self.estudiantes_cursos_repository.get_by_curso_codigo(curso_codigo)
        estudiantes = []
        for estudiante_curso in estudiantes_cursos:
            estudiante = self.estudiantes_repository.get_by_id(estudiante_curso.estudiante_id)
            estudiantes.append(estudiante)
        return estudiantes

