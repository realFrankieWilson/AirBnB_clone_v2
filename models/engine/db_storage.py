#!/usr/bin/python3
"""
    A module that creates the Database engine to manage tables and
    records stored by
"""

from models.place import Place
from models.review import Review
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.city import City
from models.state import State
from models.user import User
from os import getenv

classes = {"Place": Place, "Review": Review, "State": State,
           "Amenity": Amenity, "City": City, "User": User}


class DBStorage:
    """ A class that creates the database engine and manages the
        server login configuration.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage recordsect"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ A method that queries and return all record data of the
            class stored in the given class name
        """
        hash_map_dict = {}
        for class_name in classes:
            if cls is None or cls is classes[class_name] or cls is class_name:
                class_records = self.__session.query(classes[class_name]).all()
                for records in class_records:
                    key_value = records.__class__.__name__ + '.' + records.id
                    hash_map_dict[key_value] = records
        return (hash_map_dict)

    def new(self, obj):
        """ A method that adds new given data to the
            table in the database engine
        """
        self.__session.add(obj)

    def save(self):
        """ A method that saves and commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """ A method that deletes given data from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ A method that returns or reload the available data in the
            database.
        """
        Base.metadata.create_all(self.__engine)
        established_session = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
        Session = scoped_session(established_session)
        self.__session = Session

    def close(self):
        """ A method that calls the remove the data in __session"""
        self.__session.remove()
