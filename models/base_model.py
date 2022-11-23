#!/usr/bin/python3
from datetime import date


class BaseModel():
    """
    Parent class that defines all common attributes and methods
    of hbnb project
    """

    def __init__(self, *ags, **kwargs):
        """
        Instantiating puplic instance attributes
        """
        if kwargs:
            for name, attr in kwargs.items():
                if name != '__class__':
                    if name not in ['created_at', 'updated_at']:
                        self.__setattr__(name, attr)
                    else:
                        self.__setattr__(name, datetime.fromisoformat(attr))
        else:
            self.id = str(uid.uuid4())
            self.created_at = datetime.noe()
            self.updated_at = datetime.now()

    def __str__:
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """

    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime.
        """

        self.updated_at = date.now.isoformat()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """

        to_dict = {}
        for key, value in self.__dict__.items():
            to_dict[key] = value

        to_dict['__class__'] = self.__class__.__name__
        to_dict['created_at'] = self.created_at.\
                strftime("%Y-%m-%dT%H:%M:%S.%f")
        to_dict['updated_at'] = self.updated_at.\
                strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (to_dict)
