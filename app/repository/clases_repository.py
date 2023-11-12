from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db_connection
from app.models.clase import Clase


class ClasesRespoitory:
    """
    Clase que maneja la persistencia de las clases
    """

    def __init__(self, session: Session = Depends(get_db_connection)) -> None:
        self.session = session

    def save(self, clase: Clase) -> None:
        """
        Crea una clase
        """
        self.session.add(clase)
        self.session.commit()

    def get_all(self) -> list:
        """
        Devuelve todas las clases
        """
        return self.session.query(Clase).all()

    def get_by_codigo(self, codigo: str) -> Clase:
        """
        Devuelve una clase por su codigo
        """
        return self.session.query(Clase).filter(Clase.codigo == codigo).first()

    def get_by_curso_id(self, curso_id: int) -> list:
        """
        Devuelve todas las clases de un curso
        """
        return self.session.query(Clase).filter(Clase.curso_id == curso_id).all()



