#!/usr/bin/python3

from datetime import datetime
import uuid
import re
from data import review_data

class Review():
    """Representation of Reviews"""

    def __init__(self, *args, **kwargs):
        """The constructor"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at
        self.__name = ""
        self.__review_id = ""
        self.__rating = ""

        if kwargs:
            for key, value in kwargs.items():
                if key == "name":
                    setattr(self, key, value)

    @property
    def name(self):
        """Getter for private prop Review"""
        return self.__name
    
    @name.setter
    def name(self, value):
        """Setter for private prop Review"""