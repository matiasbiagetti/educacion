from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.feedback import Feedback


class FeedbackRepository:
    """
    Clase para interactuar con la base de datos de feedback
    """

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, feedback: Feedback) -> None:
        """
        Crea un feedback
        """
        self.session.add(feedback)
        self.session.commit()

    def get_by_curso(self, curso_id: int) -> List[Feedback]:
        """
        Devuelve todos los feedback de un curso
        """
        return self.session.query(Feedback).filter(Feedback.curso_id == curso_id).all()

    def get_all(self) -> list:
        """
        Devuelve todos los feedback
        """
        return self.session.query(Feedback).all()

    def get_by_id(self, id: int) -> Feedback:
        """
        Devuelve un feedback por su id
        """
        return self.session.query(Feedback).filter(Feedback.id == id).first()

    def get_by_curso_id(self, curso_id: int) -> list:
        """
        Devuelve todos los feedback de un curso
        """
        return self.session.query(Feedback).filter(Feedback.curso_id == curso_id).all()
