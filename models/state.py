#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    __table_args__ = ({'mysql_default_charst': 'latin1'})
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
