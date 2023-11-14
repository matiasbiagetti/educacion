from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta
from app.models.clase import Clase


class Propuesta(EntityMeta):
    """
    Una propuesta es una propuesta de clase que genera la IA para una clase
    """

    __tablename__ = 'propuestas'
    id = Column(Integer, primary_key=True)
    clase_id = Column(Integer, ForeignKey('clases.id'), nullable=False)
    tipo = Column(String(length=255), nullable=False)

    # Define the relationship with the 'clases' table
    clase = relationship('Clase', back_populates='propuestas')

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "clase": self.clase.to_dict(),
            "tipo": self.tipo,
        }