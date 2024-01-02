#!/usr/bin/python3
""" A module that creates the class named State"""

from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ Initialised class name State """
    if models.if_database == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Constructor that inherits from super class"""
        super().__init__(*args, **kwargs)

    if models.if_database != "db":
        @property
        def cities(self):
            """A custom getter method for cities"""
            stack = []
            return_city_obj = models.storage.all(City)
            for obj_rt in return_city_obj.values():
                if obj_rt.state_id == self.id:
                    stack.append(obj_rt)
            return stack
