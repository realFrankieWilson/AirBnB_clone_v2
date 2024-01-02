#!/usr/bin/python3
""" A module that creates class named User"""

from sqlalchemy.orm import relationship
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
import models
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """ A class inheriting from base model """
    if models.if_database == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for the class User"""
        super().__init__(*args, **kwargs)
