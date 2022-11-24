#!/usr/bin/python3
"""Module for FileStoage class"""

import json

from models.base_model import BaseModel


class FileStorage:
    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        ''' deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        '''

        try:
            with open(self.__file_path, 'r') as f_obj:
                data = json.load(f_obj)

            for obj_dict in data.values():
                key = f"{obj_dict['__class__']}.{obj_dict['id']}"
                FileStorage.__objects.\
                    setdefault(key, eval(obj_dict['__class__'])(**obj_dict))

        except FileNotFoundError as e:
            pass

