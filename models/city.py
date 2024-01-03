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
        __table_args__ = ({'mysql_default_charset': 'latin1'})
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade='all, delete, delete-orphan',
                              backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initialised a constructor that inherits the 
            constructor from BaseModel super class.
        """
        super().__init__(*args, **kwargs)
