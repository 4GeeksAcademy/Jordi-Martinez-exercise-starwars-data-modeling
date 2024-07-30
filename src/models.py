import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)    
    first_name = Column(String(50), nullable=False)  
    last_name = Column(String(50), nullable=False) 
    password = Column(String(50), nullable=False)   
    email = Column(String(50), nullable=False) 
    birthday = Column(String(50), nullable=False)   
    # favorites = relationship(Favorites)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=True)
    species_id = Column(Integer, ForeignKey('species.id'), nullable=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    starships_id = Column(Integer, ForeignKey('starships.id'), nullable=True)
    user = relationship(User)
    # people = relationship(People)
    # species = relationship(Species)
    # planets = relationship(Planets)
    # starships = relationship(Starships)


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)    
    birthyear = Column(String(50), nullable=False)  
    gender = Column(String(50), nullable=False) 
    height = Column(String(50), nullable=False)   
    skin_color = Column(String(50), nullable=False) 
    eye_color = Column(String(50), nullable=False)   
    favorites = relationship(Favorites)
    

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)    
    classification = Column(String(50), nullable=False)  
    designation = Column(String(50), nullable=False) 
    average_lifespan = Column(String(50), nullable=False)   
    skin_colors = Column(String(50), nullable=False) 
    Average_height = Column(String(50), nullable=False)   
    favorites = relationship(Favorites) 
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)    
    climate = Column(String(50), nullable=False)  
    terrain = Column(String(50), nullable=False) 
    population = Column(String(50), nullable=False)   
    diameter = Column(String(50), nullable=False) 
    gravity = Column(String(50), nullable=False)    
    favorites = relationship(Favorites)
    

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)    
    lenght = Column(String(50), nullable=False)  
    crew = Column(String(50), nullable=False) 
    passengers = Column(String(50), nullable=False)   
    manufacturer = Column(String(50), nullable=False) 
    cargo_capacity = Column(String(50), nullable=False)   
    favorites = relationship(Favorites) 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
