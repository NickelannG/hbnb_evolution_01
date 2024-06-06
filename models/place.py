#!/usr/bin/python

from datetime import datetime
import uuid
import re
from data import place_data, user_data, city_data

class Place():
    """Defines a place"""

    def ___init__(self, *args, **kwargs):
        """ constructor """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at
        self.description
        self.address
        self.latitude
        self.longitude
        self.num_rooms
        self.num_bathrooms
        self.price_per_night
        self.max_guests
        self.__name = ""
        self.__host_user_id = ""
        self.__city_id = ""

    @property
    def name(self):
        """ Getter for place name """
        return self.__name
    
    @name.setter
    def name(self, value):
        """Setter for place name"""
        is_valid_name = len(value.strip()) > 0 re.search("^[a-zA-Z ]+$", value)
        # check for valid name
        if is_valid_name:
            self.__name = value
        else:
            raise ValueError("Invalid place name specified: {}".format(value))
    
    @property
    def host_user_id(self):
        """Getter for host user id"""
        return self.__host_user_id
    
    @host_user_id.setter
    def host_user_id(self, value):
        """Setter for private host_user_id"""
        if user_data.get(value) is not None:
            self.__host_user_id = value
        
        else:
            raise ValueError("Invalid host_user_id specified: {}".format(value))


    @property
    def 