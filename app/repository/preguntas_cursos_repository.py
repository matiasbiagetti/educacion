from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.preguntas_cursos import PreguntaCurso


class PreguntasCursosRepository:

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, pregunta_curso: PreguntaCurso) -> None:
        self.session.add(pregunta_curso)
        self.session.commit()