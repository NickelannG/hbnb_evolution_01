#!/usr/bin/python

from datetime import datetime
import uuid
import re
from data import place_data, user_data, city_data

class Place():
    """Defines a place"""
    def __init__(self, *args, **kwargs):
        """ constructor """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at
        self.description = ""
        self.address = ""
        self.latitude = 0.0
        self.longitude = 0.0
        self.num_rooms = 0
        self.num_bathrooms = 0
        self.price_per_night = 0.0
        self.max_guests = 0

        # private variables
        self.__name = ""
        self.__host_user_id = ""
        self.__city_id = ""

        attr_list = [
            "description", "address", "latitude", "longitude",
            "num_rooms", "num_bathrooms", "price_per_night", "max_guests",
            "name", "host_user_id", "city_id"
        ]

        if kwargs:
            for key, value in kwargs.items():
                if key in attr_list:
                    setattr(self, key, value)
    
    @property
    def name(self):
        """ Getter for place name """
        return self.__name
    
    @name.setter
    def name(self, value):
        """Setter for place name"""
        is_valid_name = len(value.strip()) > 0 and re.search("^[a-zA-Z ]+$", value)
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
    def city_id(self):
        """ Getter for private attr city_id"""
        return self.__city_id
    
    @city_id.setter
    def city_id(self, value):
        """Setter for city_id """
        if city_data.get(value) is not None:
            self.__city_id = value
        else:
            raise ValueError("Invalid city_id specified: {}".format(value))