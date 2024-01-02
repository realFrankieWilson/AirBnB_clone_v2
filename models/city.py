#!/usr/bin/python
""" A module that creates city class """
import models
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv



class City(BaseModel, Base):
    """ A class that creates column records that of state_id, name and place
        in the cities table
    """
    if models.if_database == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initialised a constructor that inherits the 
            constructor from BaseModel super class.
        """
        super().__init__(*args, **kwargs)
