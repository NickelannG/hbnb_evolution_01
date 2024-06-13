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
        r = Review(feedback="Food sucks", commentor_user_id="0215a722-a3fc-4f08-9120-f8621147f2be", place_id="90c83333-35d4-4638-bdd8-1eceac56915e", rating=2)

        # Check if review instance is not none
        self.assertIsNotNone(r)

    def test_create_review_invalid_commentor_user_id(self):
        """ Tests error handling during creation of review instances """

        with self.assertRaises(ValueError):
            Review(commentor_user_id="93cc1b92-1927-4c21-bdc8-91fec1360564")


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
