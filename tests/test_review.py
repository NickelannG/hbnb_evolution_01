#!/usr/bin/python3
""" Unittests for HBnB Evolution Part 1 """

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test that the review models work as expected
    """

    def test_create_review(self):
        """ Tests creation of Review instances """

        # don't forget to include the TESTING = 1 flag at the command line
        # type in the terminal: TESTING=1 python3 -m unittest discover
        r = Review(feedback="Food sucks", commenter_user_id="d32cbeb4-a526-4500-b865-4398cc6a6976", place_id="4466e456-f2bf-47aa-8755-ed39374b9a89", rating="0.25")

        # Check if review instance is not none
        self.assertIsNotNone(r)

    def test_create_review_invalid_commenter_user_id(self):
        """ Tests error handling during creation of review instances """

        error = 0
        try:
            # invalid characters
            Review(commenter_user_id="Kelly")
        except ValueError:
            error = 1

        # We're not able to use self.assertRaises here since it can't take kwargs
        self.assertEqual(error, 1)

    def test_create_review_invalid_rating(self):
        """ Tests error handling during creation of City instances """

        error = 0
        try:
            # Not an int
            Review(rating="poor")
        except ValueError:
            error = 1

        # We're not able to use self.assertRaises here since it can't take kwargs
        self.assertEqual(error, 1)


    # TODO: add more tests

if __name__ == '__main__':
    unittest.main()
