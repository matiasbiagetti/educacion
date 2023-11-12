from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta


class Opcion(EntityMeta):
    """
    Una opcion es una opcion de respuesta a una pregunta
    """

    __tablename__ = "opciones"

    id = Column(Integer, primary_key=True)
    texto = Column(String(100), nullable=False)
    pregunta_id = Column(Integer, ForeignKey("preguntas.id"), nullable=False)

    pregunta = relationship("Pregunta", back_populates="opciones")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "texto": self.texto,
            "pregunta": self.pregunta.to_dict(),
        }