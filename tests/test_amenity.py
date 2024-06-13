#!/usr/bin/python3
""" Unittests for HBnB Evolution Part 1 """

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test that the amenity models work as expected
    """

    def test_create_amenity(self):
        """ Tests creation of Review instances """

        # don't forget to include the TESTING = 1 flag at the command line
        # type in the terminal: TESTING=1 python3 -m unittest discover
        a = Amenity(name="fridge")

        # Check if review instance is not none
        self.assertIsNotNone(a)

    def test_create_amenity_invalid_name(self):
        """ Tests error handling during creation of amenity instances """

        error = 0
        try:
            # invalid characters
            Amenity(name="@#$%^&")
        except ValueError:
            error = 1

        # We're not able to use self.assertRaises here since it can't take kwargs
        self.assertEqual(error, 1)

    # TODO: add more tests

if __name__ == '__main__':
    unittest.main()
