from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.models.base_model import EntityMeta
from app.models.curso import Curso


class Pregunta(EntityMeta):
    """
    Una pregunta es parte de un formulario que deben completar los alumnos que estan inscritos a un curso,
    cada curso tiene sus propias preguntas
    """

    __tablename__ = "preguntas"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    texto = Column(String(100), nullable=False)

    cursos : Mapped[list[Curso]] = relationship(secondary="preguntas_cursos", back_populates="preguntas")
    respuestas = relationship("Respuesta", back_populates="pregunta")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "texto": self.texto,
            "cursos": [curso.to_dict() for curso in self.cursos],
            "respuestas": [respuesta.to_dict() for respuesta in self.respuestas],
        }