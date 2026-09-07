from sqlalchemy import Column, Integer, String, foreignKey
from database.database import Base

class Usuario(Base): 
    __tablename__ = "Usuarios"

    id_usuario = Column(Integer, primary_key=True), id_rol = Column(Integer, foreignKey("Roles.id_rol"))

    nombre = Column(String)
    usuario = Column(String)
    password = Column(String)