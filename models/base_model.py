#!/usr/bin/python3
"""
    A module that creates the basemodel to serves as a superclass
    other subclass that inherits from it.
"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
import sqlalchemy
import models
from os import getenv


time_utc_format = "%Y-%m-%dT%H:%M:%S.%f"

if models.if_database == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """
        A module that determines the id and time of which all objects are
        created and modified.
    """
    if models.if_database == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
            initialised the constructor for the base model.
        """
        if kwargs:
            for key_value, obj_data in kwargs.items():
                if key_value != "__class__":
                    setattr(self, key_value, obj_data)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time_utc_format)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time_utc_format)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """ A method that displays given content in the specified format"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """A method that saves the outlined object created"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
            A method that creates a dictionary of given data it is been
            passed to.
        """
        hash_map = self.__dict__.copy()
        if "created_at" in hash_map:
            hash_map["created_at"] = hash_map["created_at"].strftime(time_utc_format)
        if "updated_at" in hash_map:
            hash_map["updated_at"] = hash_map["updated_at"].strftime(time_utc_format)
        hash_map["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in hash_map:
            del hash_map["_sa_instance_state"]
        return hash_map

    def delete(self):
        """ A method that deletes given object and it data it contains"""
        models.storage.delete(self)
