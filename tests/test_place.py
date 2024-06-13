#!/usr/bin/python3
""" Unittests for HBnB Evolution Part 1 """

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test that the review models work as expected
    """

    def test_create_place(self):
        """ Tests creation of Review instances """

        # don't forget to include the TESTING = 1 flag at the command line
        # type in the terminal: TESTING=1 python3 -m unittest discover
        r = Place(description="A fancy hotel",
                   address="Opposite Kebab Kingz", latitude="-37.814776",
                    longitude="145.230530", bathrooms="3", price_per_night="100.00", max_guests="4", name="Best hotel",
                    host_user_id="0a3ce021-4b30-4860-bddb-414cc3913ca6",
                    city_id="93cc1b92-1927-4c21-bdc8-91fec1360564")

        # Check if review instance is not none
        self.assertIsNotNone(r)

    def test_create_place_invalid_name(self):
        """ Tests error handling during creation of place instances """

        error = 0
        try:
            # invalid characters
            Place(commenter_user_id="@#$%^&")
        except ValueError:
            error = 1

        # We're not able to use self.assertRaises here since it can't take kwargs
        self.assertEqual(error, 1)

    def test_invalid_commenter_user_id(self):
        """Test setting an invalid host_user_id"""
        error = 0
        try:
            Place(host_user_id="@#$%^&")
        except ValueError:
            error = 1
        self.assertEqual(error, 1)

    def test_invalid_latitude(self):
        """Test setting an invalid latitude"""
        error = 0
        try:
            Place(latitude="hehe")
        except ValueError:
            error = 1
        self.assertEqual(error, 1)

    def test_invalid_longitude(self):
        """Test setting an invalid longitude"""
        error = 0
        try:
            Place(longitude="haha")
        except ValueError:
            error = 1
        self.assertEqual(error, 1)

    def test_invalid_bathrooms(self):
        """Test setting invalid bathrooms"""
        error = 0
        try:
            Place(bathrooms="hoho")
        except ValueError:
            error = 1
        self.assertEqual(error, 1)

    def test_invalid_price_per_night(self):
        """Test setting invalid price_per_night"""
        error = 0
        try:
            Place(price_per_night="something")
        except ValueError:
            error = 1
        self.assertEqual(error, 1)

    def test_invalid_max_guests(self):
        """Test setting invalid max_guests"""
        error = 0
        try:
            Place(max_guests="-4")
        except ValueError:
            error = 1
        self.assertEqual(error, 1)

    def test_invalid_city_id(self):
        """Test setting invalid city_id"""
        error = 0
        try:
            Place(city_id="123456")
        except ValueError:
            error = 1
        self.assertEqual(error, 1)

    # TODO: add more tests

if __name__ == '__main__':
    unittest.main()
