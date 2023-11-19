from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.colegio import Colegio


class ColegiosRepository:
    """
    Colegios Repository
    """

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, colegio: Colegio) -> None:
        """
        Crea un colegio
        """
        self.session.add(colegio)
        self.session.commit()

    def get_by_curso(self, curso_codigo: int) -> Colegio:
        """
        Devuelve todos los colegios de un curso
        """
        return self.session.query(Colegio).filter(Colegio.curso_codigo == curso_codigo).all()