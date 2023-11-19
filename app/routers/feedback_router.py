from http import HTTPStatus
from typing import List

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from app.services.feedback_service import FeedbackData, FeedbackService

feedback_router = APIRouter(prefix="/feedback", tags=["Feedback"])


class FeedbackPayload(BaseModel):
    estudiante_id: int
    curso_codigo: int
    clasificacion: str
    texto: str


class FeedbackResponse(FeedbackPayload):
    id: int
    estudiante: dict = None
    curso: dict = None


@feedback_router.post("/cursos/{curso_codigo}", status_code=HTTPStatus.CREATED, response_model=FeedbackResponse)
def crear_feedback(payload: FeedbackPayload, service: FeedbackService = Depends(FeedbackService)):
    """
    Crea un feedback
    """
    try:
        data = FeedbackData(
            estudiante_id=payload.estudiante_id,
            curso_codigo=payload.curso_codigo,
            clasificacion=payload.clasificacion,
            texto=payload.texto
        )
        feedback = service.crear_feedback(data)
        return FeedbackResponse(id=feedback.id,
                                estudiante_id=feedback.alumno_id,
                                curso_codigo=feedback.curso_id,
                                estudiante={
                                    "id": feedback.estudiante.id,
                                    "nombre": feedback.estudiante.nombre,
                                    "apellido": feedback.estudiante.apellido,
                                },
                                curso={
                                    "codigo": feedback.curso.codigo,
                                    "materia": feedback.curso.materia,
                                    "profesor_id": feedback.curso.profesor_id,
                                    "colegio_id": feedback.curso.colegio_id,
                                    "anio_cursado": feedback.curso.anio_cursado,
                                    "division": feedback.curso.division
                                }, clasificacion=feedback.clasificacion, texto=feedback.texto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@feedback_router.get("/cursos/{curso_codigo}", response_model=List[FeedbackResponse])
def obtener_feedback(curso_codigo: int, service: FeedbackService = Depends(FeedbackService)):
    """
    Obtiene todos los feedback de un curso
    """
    try:
        feedback = service.get_by_curso(curso_codigo)

        return [FeedbackResponse(estudiante_id=feedback.alumno_id,
                                 curso_codigo=feedback.curso_id,
                                 id=feedback.id,
                                 curso={
                                     "codigo": feedback.curso.codigo,
                                     "materia": feedback.curso.materia,
                                     "profesor_id": feedback.curso.profesor_id,
                                     "colegio_id": feedback.curso.colegio_id,
                                     "anio_cursado": feedback.curso.anio_cursado,
                                     "division": feedback.curso.division
                                 }, estudiante={
                "id": feedback.estudiante.id,
                "nombre": feedback.estudiante.nombre,
                "apellido": feedback.estudiante.apellido,
            },
                                 clasificacion=feedback.clasificacion,
                                 texto=feedback.texto, ) for feedback in feedback]

    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
