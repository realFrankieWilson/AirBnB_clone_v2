#!/usr/bin/python
""" A module that defines the class Amenity and it
    funtionalities and data attribute to store
"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship



class Amenity(BaseModel, Base):
    """ A class that sets the coloumn record for the name 
        of the amenity in the database class attribute
        for json storage. 
    """
    if models.if_database == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """ Constructor for the amenity class """
        super().__init__(*args, **kwargs)
