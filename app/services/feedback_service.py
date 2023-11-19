from typing import List

from fastapi import Depends
from pydantic import BaseModel

from app.models.feedback import Feedback
from app.repository.feedback_repository import FeedbackRepository


class FeedbackData(BaseModel):
    estudiante_id: int
    curso_codigo: int
    clasificacion: str
    texto: str


class FeedbackService:
    def __init__(self, feedback_repository: FeedbackRepository = Depends(FeedbackRepository)) -> None:
        self.feedback_repository = feedback_repository

    def get_by_curso(self, curso_codigo: int) -> List[Feedback]:
        return self.feedback_repository.get_by_curso(curso_codigo)

    def crear_feedback(self, data: FeedbackData) -> Feedback:
        feedback = Feedback(
            estudiante_id=data.estudiante_id,
            curso_codigo=data.curso_codigo,
            clasificacion=data.clasificacion,
            texto=data.texto
        )
        self.feedback_repository.save(feedback)
        return feedback
