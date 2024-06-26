#!/usr/bin/python3

from datetime import datetime
import uuid
import re
from data import review_data, user_data, place_data

class Review():
    """Representation of Reviews"""

    def __init__(self, *args, **kwargs):
        """The constructor"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at
        self.feedback = ""
        self.__commentor_user_id = ""
        self.__place_id = ""
        self.__rating = ""

        attr_list = [
            "feedback", "commentor_user_id", "place_id", "rating"
        ]

        if kwargs:
            for key, value in kwargs.items():
                if key in attr_list:
                    setattr(self, key, value)

    @property
    def commentor_user_id(self):
        """Getter for commentor_user_id"""
        return self.__commentor_user_id
    
    @commentor_user_id.setter
    def commentor_user_id(self, value):
        """Setter for commentor_user_id"""
        if user_data.get(value) is not None: 
            self.__commentor_user_id = value
        
        else:
            raise ValueError("Invalid commenter user ID specified: {}".format(value))
    
    @property
    def place_id(self):
        """Getter for place_id"""
        return self.__place_id
    
    @place_id.setter
    def place_id(self, value):
        """ Setter for place_id """
        if place_data.get(value) is not None:
            self.__place_id = value
        else:
            raise ValueError("Invalid place ID specified: {}".format(value))
    
    @property
    def rating(self):
        """Getter for rating"""
        return self.__rating
    
    @rating.setter
    def rating (self, value):
        """Setter for rating"""
        if isinstance(value, int) and 0 <= value <= 5:
            self.__rating = value
        else:
            raise ValueError("Rating must be an integer between 0 and 5")