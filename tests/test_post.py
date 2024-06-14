#!/usr/bin/python3
""" Unittests for HBnB Evolution Part 1

Testing all POST methods 
"""

# from io import StringIO
# import sys
import os
import unittest
import data as data
from app import app

# --- USER POST ---
class TestUsersPost(unittest.TestCase):
    """Test the '/api/v1/users' POST endpoint"""

     # don't forget to include the TESTING = 1 flag at the command line
    # type in the terminal: TESTING=1 python3 -m unittest tests/test_post.py
    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_users_post_success(self):
        """Test POST request with valid JSON data"""
        # JSON data for a new user
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "password": "password123"
        }

        # Send a POST request to the '/api/v1/users' endpoint
        response = self.app.post('/api/v1/users', json=data)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "first_name", "last_name", "email", "created_at", "updated_at"}
        user_data = response.json
        self.assertEqual(set(user_data.keys()), expected_keys)
        self.assertEqual(user_data["first_name"], "John")
        self.assertEqual(user_data["last_name"], "Doe")
        self.assertEqual(user_data["email"], "john@example.com")

    def test_users_post_missing_email(self):
        """Test POST request with missing 'email' field"""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "password": "password123"
        }

        response = self.app.post('/api/v1/users', json=data)
        self.assertEqual(response.status_code, 400)

# --- COUNTRY POST ---
class TestCountriesPost(unittest.TestCase):
    """Test the '/api/v1/countries' endpoint"""

    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_countries_post_success(self):
        """Test POST request with valid JSON data"""
        # JSON data for a new country
        data = {
            "name": "France",
            "code": "FR"
        }

        # Send a POST request to the '/api/v1/countries' endpoint
        response = self.app.post('/api/v1/countries', json=data)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "name", "code", "created_at", "updated_at"}
        country_data = response.json
        self.assertEqual(set(country_data.keys()), expected_keys)
        self.assertEqual(country_data["name"], "France")
        self.assertEqual(country_data["code"], "FR")

    def test_countries_post_missing_name(self):
        """Test POST request with missing 'name' field"""
        data = {
            "code": "FR"
        }

        response = self.app.post('/api/v1/countries', json=data)
        self.assertEqual(response.status_code, 400)

    def test_countries_post_missing_code(self):
        """Test POST request with missing 'code' field"""
        data = {
            "name": "France"
        }

        response = self.app.post('/api/v1/countries', json=data)
        self.assertEqual(response.status_code, 400)

# --- CITIES POST ---
class TestCityPost(unittest.TestCase):
    """Test the '/api/v1/cities' POST endpoint"""

    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()



    def test_city_post_success(self):
        """Test POST request with valid JSON data"""
        # JSON data for a new city
        data = {
            "country_id": "d291a77f-fa95-4385-b70e-2691df246475",  # Assuming a valid country_id here
            "name": "Ontario"
        }

        # Send a POST request to the '/api/v1/cities' endpoint
        response = self.app.post('/api/v1/cities', json=data)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "name", "country_id", "created_at", "updated_at"}
        city_data = response.json
        self.assertEqual(set(city_data.keys()), expected_keys)
        self.assertEqual(city_data["name"], "Ontario")
        self.assertEqual(city_data["country_id"], "d291a77f-fa95-4385-b70e-2691df246475")

    def test_city_post_missing_name(self):
        """Test POST request with missing 'name' field"""
        data = {
            "country_id": "d291a77f-fa95-4385-b70e-2691df246475"  # Assuming a valid country_id here
        }

        response = self.app.post('/api/v1/cities', json=data)
        self.assertEqual(response.status_code, 400)

    def test_city_post_missing_country_id(self):
        """Test POST request with missing 'country_id' field"""
        data = {
            "name": "Ontario"
        }

        response = self.app.post('/api/v1/cities', json=data)
        self.assertEqual(response.status_code, 400)


# --- AMENITY POST ---
class TestAmenityPost(unittest.TestCase):
    """Test the '/api/v1/amenities' POST endpoint"""

    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_amenity_post_success(self):
        """Test POST request with valid JSON data"""
        # JSON data for a new amenity
        data = {
            "name": "Swimming Pool"
        }

        # Send a POST request to the '/api/v1/amenities' endpoint
        response = self.app.post('/api/v1/amenities', json=data, content_type='application/json')
        # print(response.__dict__)
        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "name", "created_at", "updated_at"}
        amenity_data = response.json
        # print(amenity_data)
        self.assertEqual(set(amenity_data.keys()), expected_keys)
        self.assertEqual(amenity_data["name"], "Swimming Pool")

    def test_amenity_post_missing_name(self):
        """Test POST request with missing 'name' field"""
        data = {}  # No name field provided

        response = self.app.post('/api/v1/amenities', json=data)
        self.assertEqual(response.status_code, 400)

# --- REVIEW POST ---
class TestReviewPost(unittest.TestCase):
    """Test the '/api/v1/reviews' POST endpoint"""

    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_review_post_success(self):
        """Test POST request with valid JSON data"""
        # JSON data for a new review
        data = {
            "feedback": "Great experience!",
            "commentor_user_id": "12345",  # Assuming a valid user id here
            "place_id": "54321",            # Assuming a valid place id here
            "rating": 5                     # Assuming a valid rating here
        }

        # Send a POST request to the '/api/v1/reviews' endpoint
        response = self.app.post('/api/v1/reviews', json=data)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "feedback", "commentor_user_id", "place_id", "rating", "created_at", "updated_at"}
        review_data = response.json
        self.assertEqual(set(review_data.keys()), expected_keys)
        self.assertEqual(review_data["feedback"], "Great experience!")
        self.assertEqual(review_data["commentor_user_id"], "12345")
        self.assertEqual(review_data["place_id"], "54321")
        self.assertEqual(review_data["rating"], 5)

    def test_review_post_missing_feedback(self):
        """Test POST request with missing 'feedback' field"""
        data = {
            "commentor_user_id": "12345",  # Assuming a valid user id here
            "place_id": "54321",            # Assuming a valid place id here
            "rating": 5                     # Assuming a valid rating here
        }

        response = self.app.post('/api/v1/reviews', json=data)
        self.assertEqual(response.status_code, 400)

    def test_review_post_missing_commentor_user_id(self):
        """Test POST request with missing 'commentor_user_id' field"""
        data = {
            "feedback": "Great experience!",
            "place_id": "54321",            # Assuming a valid place id here
            "rating": 5                     # Assuming a valid rating here
        }

        response = self.app.post('/api/v1/reviews', json=data)
        self.assertEqual(response.status_code, 400)

# --- PLACE POST ---
class TestPlacePost(unittest.TestCase):
    """Test the '/api/v1/places' POST endpoint"""

    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_place_post_success(self):
        """Test POST request with valid JSON data"""
        # JSON data for a new place
        data = {
            "description": "Beautiful villa near the beach",
            "address": "123 Ocean Avenue",
            "latitude": 40.7128,
            "longitude": -74.0060,
            "number_of_rooms": 3,
            "bathrooms": 2,
            "price_per_night": 200,
            "max_guests": 6,
            "name": "Ocean View Villa",
            "host_user_id": "0215a722-a3fc-4f08-9120-f8621147f2be",
            "city_id": "687da7c4-eaba-411f-b00d-65c954eb2b8c"
        }

        # Send a POST request to the '/api/v1/places' endpoint
        response = self.app.post('/api/v1/places', json=data)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "host_user_id", "city_id", "name", "description", "address", "latitude",
                         "longitude", "number_of_rooms", "bathrooms", "price_per_night", "max_guests",
                         "created_at", "updated_at"}
        place_data = response.json
        self.assertEqual(set(place_data.keys()), expected_keys)
        self.assertEqual(place_data["description"], "Beautiful villa near the beach")
        self.assertEqual(place_data["address"], "123 Ocean Avenue")

    def test_place_post_missing_fields(self):
        """Test POST request with missing fields"""
        data = {}  # No fields provided

        response = self.app.post('/api/v1/places', json=data)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
