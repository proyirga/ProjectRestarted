#!/usr/bin/python3
from datetime import date

class BaseModel():
    """
    Parent class that defines all common attributes and methods
    of hbnb project
    """


    def __init__(self, created_at, updated_at):
        """
        Instantiating puplic instance attributes
        """

        self.id = uuid.uuid4()
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__:
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        """

    def save(self):
        """
        updates the public instance attribute updated_at with the 
        current datetime.
        """

        self.updated_at = date.now.isoformat();

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance.
        """

        return (class.self.__dict__)
