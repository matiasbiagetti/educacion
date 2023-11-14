from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta
from app.models.pregunta import Pregunta


class Opcion(EntityMeta):
    """
    Una opcion es una opcion de respuesta a una pregunta
    """
    __tablename__ = 'opciones'
    id = Column(Integer, primary_key=True)
    texto = Column(String(length=100), nullable=False)
    pregunta_id = Column(Integer, ForeignKey('preguntas.id'), nullable=False)

    # Define the relationship with the 'preguntas' table
    pregunta = relationship('Pregunta', back_populates='opciones')
    respuestas = relationship('Respuesta', back_populates='opcion')


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "texto": self.texto,
            "pregunta": self.pregunta.to_dict(),
            "respuestas": [respuesta.to_dict() for respuesta in self.respuestas],
        }