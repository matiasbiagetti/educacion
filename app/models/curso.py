from sqlalchemy import Column, String, Integer, ForeignKey, CHAR
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta
from app.models.profesor import Profesor
from app.models.estudiante import Estudiante
from app.models.feedback import Feedback
from app.models.pregunta import Pregunta


class Curso(EntityMeta):
    __tablename__ = 'cursos'
    codigo = Column(Integer, primary_key=True)
    materia = Column(String(length=100), nullable=False)
    profesor_id = Column(Integer, ForeignKey('profesores.id'), nullable=False)
    colegio_id = Column(Integer, ForeignKey('colegios.id'), nullable=False)
    anio_cursado = Column(Integer, nullable=False)
    division = Column(CHAR(1), nullable=False)

    # Define relationships
    profesor = relationship('Profesor', back_populates='cursos')
    colegio = relationship('Colegio', back_populates='cursos')
    estudiantes = relationship('Estudiante', secondary='estudiantes_cursos', back_populates='cursos')
    feedback = relationship('Feedback', back_populates='curso')
    preguntas = relationship('Pregunta', secondary='preguntas_cursos', back_populates='cursos')


    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "materia": self.materia,
            "profesor": self.profesor.to_dict(),
            "colegio": self.colegio.to_dict(),
            "anio_cursado": self.anio_cursado,
            "division": self.division,
            "estudiantes": [estudiante.to_dict() for estudiante in self.estudiantes],
            "feedback": [feedback.to_dict() for feedback in self.feedback],
            "preguntas": [pregunta.to_dict() for pregunta in self.preguntas],
        }


