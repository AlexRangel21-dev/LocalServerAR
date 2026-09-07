from sqlalchemy import Column, Integer, String, ForeignKey
from database.database import Base

class Usuario(Base): 
    __tablename__ = "Usuarios"

    id_usuario = Column(Integer, primary_key=True) 
    id_rol = Column(Integer, ForeignKey("Roles.id_rol"))

    nombre = Column(String, nullable=False)
    usuario = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)