#!/usr/bin/python3
""" console """

import sys
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.review import Review
import shlex
from models.base_model import BaseModel
from models.city import City
import cmd
from datetime import datetime
import models
from models.place import Place  

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


def arg_key_value_convertor(arg):
        """
            A function that returns a parsed argument of given
            argument from the console in do_create method.
        """
        hash_map = {}
        for values in arg:
            if "=" in values:
                splitted_arg = values.split("=", 1)
                key_value = splitted_arg[0]
                value_data = splitted_arg[1]
                if value_data[0] == value_data[-1] == '"':
                    value_data = shlex.split(value_data)[0].replace('_', ' ')
                else:
                    try:
                        value_data = int(value_data)
                    except:
                        try:
                            value_data = float(value_data)
                        except:
                            continue
                hash_map[key_value] = value_data
        return hash_map

class HBNBCommand(cmd.Cmd):
    """ console class """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """End of file """
        return True

    def emptyline(self):
        """ manages empty lines in arguments """
        return False

    def do_quit(self, arg):
        """exit or quit"""
        return True

    def do_create(self, arg):
        """ A method that creates all object passed to it"""
        spiltted_args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif spiltted_args[0] in classes:
            hash_map = arg_key_value_convertor(spiltted_args[1:])
            class_object = classes[spiltted_args[0]](**hash_map)  
        else:
            print("** class doesn't exist **")
            return
        print(class_object.id)
        class_object.save()

    def do_show(self, arg):
        """
            A method that displays the object, it's created and
            updated time, id number and data for the given object
        """
        some_data = shlex.split(arg)
        if len(some_data) == 0:
            print("** class name missing **")
            return False
        if some_data[0] in classes:
            if len(some_data) > 1:
                data_k = some_data[0] + "." + some_data[1]
                if data_k in models.storage.all():
                    print(models.storage.all()[data_k])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ A method that deletes given object as argument
            and it's given data
        """
        some_data = shlex.split(arg)
        if len(some_data) == 0:
            print("** class name missing **")
        elif some_data[0] in classes:
            if len(some_data) > 1:
                data_k = some_data[0] + "." + some_data[1]
                if data_k in models.storage.all():
                    models.storage.all().pop(data_k)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """A method that displays given argument obj and it's data"""
        some_data = shlex.split(arg)
        stack_data = []
        if len(some_data) == 0:
            data_hash_map = models.storage.all()
        elif some_data[0] in classes:
            data_hash_map = models.storage.all(classes[some_data[0]])
        else:
            print("** class doesn't exist **")
            return False
        for data_k in data_hash_map:
            stack_data.append(str(data_hash_map[data_k]))
        print("[", end="")
        print(", ".join(stack_data), end="")
        print("]")

    def do_update(self, arg):
        """ A method that updates all object passed to it"""
        some_data = shlex.split(arg)
        kint_num = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        dec_num = ["latitude", "longitude"]
        if len(some_data) == 0:
            print("** class name missing **")
        elif some_data[0] in classes:
            if len(some_data) > 1:
                varr = some_data[0] + "." + some_data[1]
                if varr in models.storage.all():
                    if len(some_data) > 2:
                        if len(some_data) > 3:
                            if some_data[0] == "Place":
                                if some_data[2] in kint_num:
                                    try:
                                        some_data[3] = int(some_data[3])
                                    except:
                                        some_data[3] = 0
                                elif some_data[2] in dec_num:
                                    try:
                                        some_data[3] = float(some_data[3])
                                    except:
                                        some_data[3] = 0.0
                            setattr(models.storage.all()[varr], some_data[2], some_data[3])
                            models.storage.all()[varr].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
