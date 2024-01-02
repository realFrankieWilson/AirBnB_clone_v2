#!/usr/bin/python3
"""
    A module that create the FileStorage class to manage the data
    storage in json file.
"""

from models.place import Place
from models.review import Review
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User


classes = {"City": City, "Amenity": Amenity, "BaseModel": BaseModel,
           "Place": Place, "State": State, "User": User, "Review": Review}


class FileStorage:
    """A class that manages and stores serialised objects and data"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """ A custom method that returns the data stored in __object"""
        if cls is not None:
            hash_map = {}
            for key_data, data_value in self.__objects.items():
                if cls == data_value.__class__ or
                cls == data_value.__class__.__name__:
                    hash_map[key_data] = data_value
            return hash_map
        return self.__objects

    def new(self, obj):
        """ A custom method that sets new data of the class name and id in the
            json file
        """
        if obj is not None:
            key_data = obj.__class__.__name__ + "." + obj.id
            self.__objects[key_data] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        hash_map = {}
        for key_data in self.__objects:
            hash_map[key_data] = self.__objects[key_data].to_dict()
        with open(self.__file_path, 'w') as json_file:
            json.dump(hash_map, json_file)

    def reload(self):
        """ A module that reloads the data stored in the json file"""
        try:
            with open(self.__file_path, 'r') as file:
                cnt = json.load(file)
            for key_data in cnt:
                self.__objects[key_data] =
                classes[cnt[key_data]["__class__"]](**cnt[key_data])
        except:
            pass

    def delete(self, obj=None):
        """ A custom Method that deletes data in the json file with the given
            class name.
        """
        if obj is not None:
            key_data = obj.__class__.__name__ + '.' + obj.id
            if key_data in self.__objects:
                del self.__objects[key_data]

    def close(self):
        """ A method that returns reload method when called to reload available
            data
        """
        self.reload()
