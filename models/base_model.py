#!/usr/bin/python3
"""
Defines Basemodel class that defines:
all common attributes/methods for other classes.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Represents the BaseModel of the HBnB project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:

            *args (any): Unused parameter.

            **kwargs (dict): Key/value pairs of attributes.
        """

        # Date and time format string for parsing and formatting
        timeForm = "%Y-%m-%dT%H:%M:%S.%f"

        # Generate a unique identifier for the instance
        self.id = str(uuid.uuid4())

        # Set initial creation and update timestamps
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        # If keyword arguments are provided, populate instance attributes
        # else add the instance to the storage
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, timeForm)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates updated_at with the current datetime and save to storage.
        """

        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """

        # Create a copy of the instance dictionary
        iDictionary = self.__dict__.copy()

        # Format datetime fields as ISO 8601 strings
        iDictionary["created_at"] = self.created_at.isoformat()
        iDictionary["updated_at"] = self.updated_at.isoformat()

        # Add class name to the dictionary
        iDictionary["__class__"] = self.__class__.__name__
        return iDictionary

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance.
        """

        # Get the class name
        className = self.__class__.__name__

        # Format the string representation
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
