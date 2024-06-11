#!/usr/bin/python3

from datetime import datetime
import uuid
import re
from data import amenity_data

class Amenity():
    """ Representation of Amenities"""

    def __init__(self, *args, **kwargs):
        """The constructor"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at
        self.__name = ""
        # self.__amenity_id = ""


        if kwargs: # Keyword arguments passed in _init_ method
            for key, value in kwargs.items():
                if key == "name":
                    self.name = value
                # elif key == "amenity_id":
                    # self.amenity_id = value

    @property
    def name(self):
        """Getter for private prop name."""
        return self.__name
    
    @name.setter
    def name(self, value):
        """Setter for private prop name."""

        is_valid_name = len(value.strip()) > 0 and re.search("^[a-zA-Z]+$", value)
        if is_valid_name:
            self.__name = value
        else:
            raise ValueError("Invalid name of amenity: {}".format(value))
    
    # # @property
    # def amenity_id(self):
        # """Getter for private amenity ID"""
       #  return self.__amenity_id
    
    # @amenity_id.setter
    # def amenity_id(self, value):
       #  """Setter for private prop amenity ID"""

        # if amenity_data.get(value) is not None:
            # self.__amenity_id = value
        # else:
            # raise ValueError("Invalid amenity ID: {}".format(value))
