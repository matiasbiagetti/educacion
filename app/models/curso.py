from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta


class Curso(EntityMeta):
    """
    Un curso es un grupo de estudiantes + profesor que asisten a las mismas clases
    """

    __tablename__ = "cursos"

    codigo = Column(String(6), primary_key=True)
    materia = Column(String(100), nullable=False)
    profesor_id = Column(Integer, ForeignKey("profesores.id"), nullable=False)
    colegio_id = Column(String(6), ForeignKey("colegios.id"), nullable=False)
    anio_cursado = Column(Integer, nullable=False)
    division = Column(String(1), nullable=False)

    profesor = relationship("Profesor", back_populates="cursos")
    colegio = relationship("Colegio", back_populates="cursos")
    estudiantes = relationship("Estudiante", back_populates="curso")

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "materia": self.materia,
            "profesor": self.profesor.nombre,
            "colegio": self.colegio.nombre,
            "anio_cursado": self.anio_cursado,
            "division": self.division,
            "estudiantes": [estudiante.to_dict() for estudiante in self.estudiantes],
        }


