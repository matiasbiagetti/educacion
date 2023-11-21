from fastapi import Depends

from app.repository.opciones_repository import OpcionesRepository
from app.repository.preguntas_cursos_repository import PreguntasCursosRepository
from app.repository.preguntas_repository import PreguntasRepository
from app.repository.respuestas_repository import RespuestasRepository


class RespuestasService:
    def __init__(self, respuestas_repository: RespuestasRepository = Depends(RespuestasRepository),
                 opciones_repository: OpcionesRepository = Depends(OpcionesRepository),
                 preguntas_cursos_repository: PreguntasCursosRepository = Depends(PreguntasCursosRepository),
                 preguntas_repository: PreguntasRepository = Depends(PreguntasRepository)):
        self.respuestas_repository = respuestas_repository
        self.opciones_repository = opciones_repository
        self.preguntas_cursos_repository = preguntas_cursos_repository
        self.preguntas_repository = preguntas_repository

    def obtener_respuestas_a_pregunta(self, curso_codigo: int, pregunta_id: int):
        """
        Obtiene las respuestas a una pregunta de un curso
        """
        respuestas_repo = self.respuestas_repository.get_respuestas_a_pregunta_por_curso(pregunta_id, curso_codigo)
        respuestas_a_pregunta = []
        for respuesta in respuestas_repo:
            respuestas_a_pregunta.append(respuesta[0])
        return respuestas_a_pregunta






