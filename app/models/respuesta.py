from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import EntityMeta
from app.models.opcion import Opcion
from app.models.pregunta import Pregunta
from app.models.curso import Curso



class Respuesta(EntityMeta):
    """
    Una respuesta es la respuesta de un alumno a una pregunta
    """

    __tablename__ = 'respuestas'
    id = Column(Integer, primary_key=True)
    opcion_id = Column(Integer, ForeignKey('opciones.id'), nullable=False)
    pregunta_id = Column(Integer, ForeignKey('preguntas.id'), nullable=False)
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'), nullable=False)
    curso_codigo = Column(Integer, ForeignKey('cursos.codigo'), nullable=False)

    # Define relationships
    opcion = relationship(Opcion, back_populates='respuestas')
    pregunta = relationship(Pregunta, back_populates='respuestas')
    curso = relationship(Curso, back_populates='respuestas')
    estudiante = relationship('Estudiante', back_populates='respuestas')

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "opcion": self.opcion.to_dict(),
            "pregunta": self.pregunta.to_dict(),
            "estudiante": self.alumno.to_dict(),
            "curso": self.curso.to_dict(),
        }


