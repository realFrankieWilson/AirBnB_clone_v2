#!/usr/bin/python
""" A module that create review class"""

from sqlalchemy import Column, String, ForeignKey
from os import getenv
from models.base_model import BaseModel, Base
import sqlalchemy
import models


class Review(BaseModel, Base):
    """ Initialised class named Review """
    if models.if_database == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """ Constructor for the class inheriting from the
            super class constructor
        """
        super().__init__(*args, **kwargs)
