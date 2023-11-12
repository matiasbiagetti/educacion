from sqlalchemy import Column, ForeignKey, Table

from app.models.base_model import EntityMeta

preguntas_cursos = Table('preguntas_cursos', EntityMeta.metadata,
                         Column('pregunta_id', ForeignKey('preguntas.id'), primary_key=True),
                         Column('curso_id', ForeignKey('cursos.id'), primary_key=True)
                         )
