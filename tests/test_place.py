#!/usr/bin/python3
""" Unittests for HBnB Evolution Part 1 """

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test that the review models work as expected
    """

    def test_create_place(self):
        """ Tests creation of Place instances """

        # don't forget to include the TESTING = 1 flag at the command line
        # type in the terminal: TESTING=1 python3 -m unittest discover
        r = Place(description="A fancy hotel",
                   address="Opposite Kebab Kingz", latitude="-37.814776",
                    longitude="145.230530", bathrooms="3", price_per_night="100.00", max_guests="4", name="Best hotel",
                    host_user_id="0215a722-a3fc-4f08-9120-f8621147f2be",
                    city_id="687da7c4-eaba-411f-b00d-65c954eb2b8c")

        # Check if review instance is not none
        self.assertIsNotNone(r)

    def test_create_place_invalid_name(self):
        """ Tests error handling during creation of place instances """

        error = 0
        try:
            # invalid characters
            Place(name="@#$%^&")
        except ValueError:
            error = 1

        # We're not able to use self.assertRaises here since it can't take kwargs
        self.assertEqual(error, 1)

    def test_invalid_host_user_id(self):
        """Test setting an invalid host_user_id"""
        error = 0
        try:
            Place(host_user_id="@#$%^&")
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
