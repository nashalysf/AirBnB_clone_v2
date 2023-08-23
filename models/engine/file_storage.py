#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            dict = {}
            for key, value in self.__objects.items():
                if value.__class__ == cls or value.__class__.__name__ == cls:
                    dict[key] = value
            return dict
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        for key in self.__objects:
            temp[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    def delete(self, obj=None):
        """deletes obj from __objects"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.__objects:
                del self.__objects[key]
            self.save()

        if obj is None:
            return

    def get(self, cls, id):
        """get one object"""
        if cls is None or id is None:
            return None
        key = "{}.{}".format(cls.__name__, id)
        obj = self.__objects.get(key)
        return obj

    def reload(self):
        """Loads storage dictionary from file"""

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                val = json.load(f)
                for key in val:
                    self.__objects[key] = classes[val[key]
                                                  ["__class__"]](**val[key])
        except FileNotFoundError:
            pass

    def close(self):
        """ reloads for deserializations of JSON file"""
        self.reload()

    def count(self, cls=None):
        """count storage items"""
        if cls is None:
            return len(self.__objects)
        else:
            count = 0
            for obj in self.__objects.values():
                if type(obj) == cls:
                    count += 1
            return count
