#!/usr/bin/python3
""" Unittests for HBnB Evolution Part 1

Testing all DELETE methods 
"""

import unittest
from app import app
import data as data


# --- USER DELETE --- #
class TestUsersDelete(unittest.TestCase):
    """Test the '/api/v1/users/<user_id>' DELETE endpoint"""

    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_users_delete_success(self):
        """Test DELETE request with valid user ID"""
        user_id = "0215a722-a3fc-4f08-9120-f8621147f2be"
        response = self.app.delete(f'/api/v1/users/{user_id}')

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

    def test_users_delete_invalid_id(self):
        """Test DELETE request with invalid user ID"""
        user_id = "100"  # Assuming this user_id doesn't exist
        response = self.app.delete(f'/api/v1/users/{user_id}')

        # Assert the response status code is 404 Not Found
        self.assertEqual(response.status_code, 404)


# --- CITY DELETE --- #
class TestCitiesDelete(unittest.TestCase):
    """Test the '/api/v1/cities/<city_id>' DELETE endpoint"""

    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_cities_delete_success(self):
        """Test DELETE request with valid city ID"""
        city_id = "687da7c4-eaba-411f-b00d-65c954eb2b8c"
        response = self.app.delete(f'/api/v1/cities/{city_id}')

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

    def test_cities_delete_invalid_id(self):
        """Test DELETE request with invalid city ID"""
        city_id = "d291a77f-fa95-4385-b70e-2691df246475"
        response = self.app.delete(f'/api/v1/cities/{city_id}')

        # Assert the response status code is 404 Not Found
        self.assertEqual(response.status_code, 404)


# --- REVIEW DELETE --- #
class TestReviewsDelete(unittest.TestCase):
    """Test the '/api/v1/reviews/<review_id>' DELETE endpoint"""
    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_reviews_delete_success(self):
        """Test DELETE request with valid review ID"""
        review_id = "92c2e4eb-a446-463d-b8e3-8810b0150276"
        response = self.app.delete(f'/api/v1/reviews/{review_id}')

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

    def test_reviews_delete_invalid_id(self):
        """Test DELETE request with invalid review ID"""
        review_id = "1234"
        response = self.app.delete(f'/api/v1/reviews/{review_id}')

        # Assert the response status code is 404 Not Found
        self.assertEqual(response.status_code, 404)


# --- AMENITY DELETE --- #
class TestAmenitiesDelete(unittest.TestCase):
    """Test the '/api/v1/amenities/<amenity_id>' DELETE endpoint"""
    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_amenities_delete_success(self):
        """Test DELETE request with valid amenity ID"""
        amenity_id = "a34bb185-d6e7-4d78-a519-995c51ada64d"
        response = self.app.delete(f'/api/v1/amenities/{amenity_id}')

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

    def test_amenities_delete_invalid_id(self):
        """Test DELETE request with invalid amenity ID"""
        amenity_id = "1234"
        response = self.app.delete(f'/api/v1/amenities/{amenity_id}')

        # Assert the response status code is 404 Not Found
        self.assertEqual(response.status_code, 404)


# --- PLACE DELETE --- #
class TestPlacesDelete(unittest.TestCase):
    """Test the '/api/v1/places/<place_id>' DELETE endpoint"""
    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_places_delete_success(self):
        """Test DELETE request with valid place ID"""
        place_id = "90c83333-35d4-4638-bdd8-1eceac56915e"
        response = self.app.delete(f'/api/v1/places/{place_id}')

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

    def test_places_delete_invalid_id(self):
        """Test DELETE request with invalid place ID"""
        place_id = "1234"
        response = self.app.delete(f'/api/v1/places/{place_id}')

        # Assert the response status code is 404 Not Found
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()