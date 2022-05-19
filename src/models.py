import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Personaje(Base):
    __tablename__="personaje"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    planeta = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)

class Personaje_favorito(Base):
    __tablename__="personaje_favorito"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    id_personaje = Column(Integer,ForeignKey('personaje.id'))
    personaje = relationship(Personaje)

class Planeta(Base):
    __tablename__= "planeta"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    poblacion = Column(Integer, nullable=False)
    tamaño = Column(Integer, nullable=False)
    clima = Column(String(250), nullable=False)


class Planeta_favorito(Base):
    __tablename__="planeta_favorito"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    id_planeta = Column(Integer,ForeignKey('planeta.id'))
    planeta = relationship(Planeta)


class Nave(Base):
    __tablename__:"nave"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    tamaño = Column(Integer, nullable=False)
    tipo = Column(String(250), nullable=False)

class Nave_favorito(Base):
    __tablename__="nave_favorito"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    id_planeta = Column(Integer,ForeignKey('nave.id'))
    nave = relationship(Nave)






    

    




"""
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
"""
## Draw from SQLAlchemy Base
render_er(Base, 'diagram.png')