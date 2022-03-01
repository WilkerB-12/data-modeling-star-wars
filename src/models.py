import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class item(Base):
    __abstract__ = True
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url= Column(String(250), nullable=False)

class Character(item):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    starship = Column(String(250))
    vehicles = Column(String(250))
    children1=relationship("Favorite",back_populates="parent1")

class Planet(item):
    __tablename__= 'planet'
    diameter=Column(String(250))
    rotation_period=Column(String(250))
    orbital_period=Column(String(250))
    gravity=Column(String(250))
    population=Column(String(250))
    climate=Column(String(250))
    residents=Column(String(250))
    terrain=Column(String(250))
    children2=relationship("Favorite",back_populates="parent2")

class Vehicle(item):
    __tablename__='vehicle'
    vehicle_class=Column(String(250))
    manufacturer=Column(String(250))
    lenth=Column(String(250))
    cost_in_credits=Column(String(250))
    crew=Column(String(250))
    passengers=Column(String(250))
    cargo_capacity=Column(String(250))
    consumable=Column(String(250))
    children3=relationship("Favorite",back_populates="parent3")

class Favorite(Base):
    __tablename__='favorite'
    id=Column(Integer,primary_key=True)
    id_user=Column(Integer,ForeignKey('user.id_user'))
    character_fav=Column(Integer,ForeignKey('character.id'))
    planet_fav=Column(Integer,ForeignKey('planet.id'))
    vehicle_fav=Column(Integer,ForeignKey('vehicle.id'))
    parent1=relationship("Character",back_populates="children1")
    parent2=relationship("Character",back_populates="children2")
    parent3=relationship("Character",back_populates="children3")

class User(Base):
    __tablename__='user'
    id_user=Column(Integer, primary_key=True)
    password=Column(String(250))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')