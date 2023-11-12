from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta


class Respuesta(EntityMeta):
    """
    Una respuesta es la respuesta de un alumno a una pregunta
    """

    __tablename__ = "respuestas"

    id = Column(Integer, primary_key=True)
    opcion_id = Column(Integer, ForeignKey("opciones.id"), nullable=False)
    pregunta_id = Column(Integer, ForeignKey("preguntas.id"), nullable=False)
    alumno_id = Column(Integer, ForeignKey("estudiantes.id"), nullable=False)

    pregunta = relationship("Pregunta", back_populates="respuestas")
    alumno = relationship("Alumno", back_populates="respuestas")
    opcion = relationship("Opcion", back_populates="respuestas")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "opcion": self.opcion.to_dict(),
            "pregunta": self.pregunta.to_dict(),
            "alumno": self.alumno.to_dict(),
        }


