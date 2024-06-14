#!/usr/bin/python3
""" Unittests for HBnB Evolution Part 1

Testing all PUT methods 
"""

import unittest
from app import app


# --- USER PUT --- #
class TestUsersPut(unittest.TestCase):
    """Test the '/api/v1/users/<user_id>' PUT endpoint"""

    # don't forget to include the TESTING = 1 flag at the command line
    # type in the terminal: TESTING=1 python3 -m unittest tests/test_put.py
    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_users_put_success(self):
        """Test PUT request with valid JSON data"""
        # JSON data for updating an existing user
        user_id = "0215a722-a3fc-4f08-9120-f8621147f2be"
        data = {
            "first_name": "Clark",
            "last_name": "Kent",
            #"email": "iluvsuperman@email.com",
            #"password": "1234"
        }

        # Send a PUT request to the '/api/v1/users/<user_id>' endpoint
        response = self.app.put(f'/api/v1/users/{user_id}', json=data)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "first_name", "last_name", "email", "created_at", "updated_at"}
        user_data = response.json
        self.assertEqual(set(user_data.keys()), expected_keys)
        self.assertEqual(user_data["first_name"], "Clark")

    def test_users_put_invalid_id(self):
        """Test PUT request with invalid user ID"""
        user_id = "100"  # Assuming this user_id doesn't exist
        data = {
            "first_name": "Clark",
            "last_name": "Kent",
            #"email": "iluvsuperman@email.com",
            #"password": "1234"
        }

        response = self.app.put(f'/api/v1/users/{user_id}', json=data)
        self.assertEqual(response.status_code, 400)

    def test_users_put_missing_json(self):
        """Test PUT request with missing JSON data"""
        user_id = "0215a722-a3fc-4f08-9120-f8621147f2be"

        response = self.app.put(f'/api/v1/users/{user_id}')
        self.assertEqual(response.status_code, 415)

    def test_users_put_invalid_fields(self):
        """Test PUT request with invalid fields"""
        user_id = "0215a722-a3fc-4f08-9120-f8621147f2be"
        data = {
            "invalid_field": "value"
        }

        response = self.app.put(f'/api/v1/users/{user_id}', json=data)
        self.assertEqual(response.status_code, 400)


# --- COUNTRY PUT --- #
class TestCountriesPut(unittest.TestCase):
     """Test the '/api/v1/countries/<country_code>' PUT endpoint"""
     @classmethod
     def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

     def test_countries_put_success(self):
        """Test PUT request with valid JSON data"""
        # JSON data for updating an existing user
        country_code = "CA"
        data = {
            "name": "Canada",
            "code": "CA",
            }

        # Send a PUT request to the '/api/v1/countries/<country_code>' endpoint
        response = self.app.put(f'/api/v1/countries/{country_code}', json=data)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "name", "code", "created_at", "updated_at"}
        country_data = response.json
        self.assertEqual(set(country_data.keys()), expected_keys)
        self.assertEqual(country_data["name"], "Canada")
        self.assertEqual(country_data["code"], "CA")

     def test_countries_put_invalid_id(self):
        """Test PUT request with invalid country code"""
        country_code = "PH"
        data = {
            "name": "Canada",
            "code": "CA",
        }

        response = self.app.put(f'/api/v1/countries/{country_code}', json=data)
        self.assertEqual(response.status_code, 400)

     def test_countries_put_missing_json(self):
        """Test PUT request with missing JSON data"""
        country_code = "CA"

        response = self.app.put(f'/api/v1/countries/{country_code}')
        self.assertEqual(response.status_code, 415)

     def test_countries_put_invalid_fields(self):
        """Test PUT request with invalid fields"""
        country_code = "CA"
        data = {
            "invalid_field": "value"
        }

        response = self.app.put(f'/api/v1/countries/{country_code}', json=data)
        self.assertEqual(response.status_code, 400)

# --- CITY PUT --- #
class TestCitiesPut(unittest.TestCase):
    """Test the '/api/v1/cities/<city_id>' PUT endpoint"""

    # don't forget to include the TESTING = 1 flag at the command line
    # type in the terminal: TESTING=1 python3 -m unittest tests/test_put.py
    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_cities_put_success(self):
        """Test PUT request with valid JSON data"""
        # JSON data for updating an existing user
        city_id = "687da7c4-eaba-411f-b00d-65c954eb2b8c"
        data = {
            "name": "Melbourne",
            "country_id": "04051500-051f-4e0f-97ba-e452cbb14d19",
        }

        # Send a PUT request to the '/api/v1/cities/<city_id>' endpoint
        response = self.app.put(f'/api/v1/cities/{city_id}', json=data)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "name", "country_id", "created_at", "updated_at"}
        city_data = response.json
        self.assertEqual(set(city_data.keys()), expected_keys)
        self.assertEqual(city_data["name"], "Melbourne")
        self.assertEqual(city_data["country_id"], "04051500-051f-4e0f-97ba-e452cbb14d19")

    def test_cities_put_invalid_id(self):
        """Test PUT request with invalid user ID"""
        city_id = "d291a77f-fa95-4385-b70e-2691df246475"
        data = {
            "name": "Melbourne"
        }

        response = self.app.put(f'/api/v1/cities/{city_id}', json=data)
        self.assertEqual(response.status_code, 400)

    def test_cities_put_missing_json(self):
        """Test PUT request with missing JSON data"""
        city_id = "687da7c4-eaba-411f-b00d-65c954eb2b8c"

        response = self.app.put(f'/api/v1/cities/{city_id}')
        self.assertEqual(response.status_code, 415)

    def test_cities_put_invalid_fields(self):
        """Test PUT request with invalid fields"""
        city_id = "687da7c4-eaba-411f-b00d-65c954eb2b8c"
        data = {
            "invalid_field": "value"
        }

        response = self.app.put(f'/api/v1/cities/{city_id}', json=data)
        self.assertEqual(response.status_code, 400)

# --- REVIEW PUT --- #
class TestReviewsPut(unittest.TestCase):
    """Test the '/api/v1/reviews/<review_id>' PUT endpoint"""
    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_reviews_put_success(self):
        """Test PUT request with valid JSON data"""
        # JSON data for updating an existing user
        review_id = "92c2e4eb-a446-463d-b8e3-8810b0150276"
        data = {
            "feedback": "The place stinks and the floor is dirty",
            "commentor_user_id": "0215a722-a3fc-4f08-9120-f8621147f2be",
            "place_id": "cee845de-c341-4f5a-a0c5-2ca1f4c327b2",
            "rating": 0.35,                    
        }

        # Send a PUT request to the '/api/v1/reviews/<review_id>' endpoint
        response = self.app.put(f'/api/v1/reviews/{review_id}', json=data)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "feedback", "commentor_user_id", "place_id", "rating", "created_at", "updated_at"}
        review_data = response.json
        self.assertEqual(set(review_data.keys()), expected_keys)
        self.assertEqual(review_data["feedback"], "The place stinks and the floor is dirty")
        self.assertEqual(review_data["commentor_user_id"], "0215a722-a3fc-4f08-9120-f8621147f2be")
        self.assertEqual(review_data["place_id"], "cee845de-c341-4f5a-a0c5-2ca1f4c327b2")
        self.assertEqual(review_data["rating"], 0.35)

    def test_reviews_put_invalid_id(self):
        """Test PUT request with invalid review id"""
        review_id = "1234"
        data = {
            "feedback": "The place stinks and the floor is dirty",
            "commentor_user_id": "0215a722-a3fc-4f08-9120-f8621147f2be",
            "place_id": "cee845de-c341-4f5a-a0c5-2ca1f4c327b2",
            "rating": 0.35,                    
        }

        response = self.app.put(f'/api/v1/reviews/{review_id}', json=data)
        self.assertEqual(response.status_code, 400)

    def test_reviews_put_missing_json(self):
        """Test PUT request with missing JSON data"""
        review_id = "92c2e4eb-a446-463d-b8e3-8810b0150276"

        response = self.app.put(f'/api/v1/reviews/{review_id}')
        self.assertEqual(response.status_code, 415)

    def test_reviews_put_invalid_fields(self):
        """Test PUT request with invalid fields"""
        review_id = "92c2e4eb-a446-463d-b8e3-8810b0150276"
        data = {
            "invalid_field": "value"
        }

        response = self.app.put(f'/api/v1/reviews/{review_id}', json=data)
        self.assertEqual(response.status_code, 400)


# --- AMENITY PUT --- #
class TestAmenitiesPut(unittest.TestCase):
    """Test the '/api/v1/amenities/<amenity_id>' PUT endpoint"""
    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_amenities_put_success(self):
        """Test PUT request with valid JSON data"""
        # JSON data for updating an existing review
        amenity_id = "a34bb185-d6e7-4d78-a519-995c51ada64d"
        data = {
            "name": "toilet"
        }

        # Send a PUT request to the '/api/v1/amenities/<amenity_id>' endpoint
        response = self.app.put(f'/api/v1/amenities/{amenity_id}', json=data)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "name", "created_at", "updated_at"}
        amenity_data = response.json
        self.assertEqual(set(amenity_data.keys()), expected_keys)
        self.assertEqual(amenity_data["name"], "toilet")

    def test_amenities_put_invalid_id(self):
        """Test PUT request with invalid amenity id"""
        amenity_id = "1234"
        data = {
            "name": "toilet"
        }

        response = self.app.put(f'/api/v1/amenities/{amenity_id}', json=data)
        self.assertEqual(response.status_code, 400)

    def test_amenities_put_missing_json(self):
        """Test PUT request with missing JSON data"""
        amenity_id = "a34bb185-d6e7-4d78-a519-995c51ada64d"

        response = self.app.put(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 415)

    def test_amenities_put_invalid_fields(self):
        """Test PUT request with invalid fields"""
        amenity_id = "a34bb185-d6e7-4d78-a519-995c51ada64d"
        data = {
            "invalid_field": "value"
        }

        response = self.app.put(f'/api/v1/amenities/{amenity_id}', json=data)
        self.assertEqual(response.status_code, 400)

# --- PLACE PUT --- #
class TestPlacesPut(unittest.TestCase):
    """Test the '/api/v1/places/<place_id>' PUT endpoint"""
    @classmethod
    def setUpClass(cls):
        """Set up the Flask test client"""
        cls.app = app.test_client()

    def test_places_put_success(self):
        """Test PUT request with valid JSON data"""
        # JSON data for updating an existing review
        place_id = "90c83333-35d4-4638-bdd8-1eceac56915e"
        data = {
            "description": "A decent hotel",
            "address": "Next to Eastland Mall",
            "latitude": -37.814666,
            "longitude": 145.230620,
            "number_of_rooms": 5,
            "bathrooms": 1,
            "price_per_night": 150.00,
            "max_guests": 2,
            "name": "Ringwood Hotel",
            "host_user_id": "0215a722-a3fc-4f08-9120-f8621147f2be",
            "city_id": "687da7c4-eaba-411f-b00d-65c954eb2b8c",
        }

        # Send a PUT request to the '/api/v1/places/<place_id>' endpoint
        response = self.app.put(f'/api/v1/places/{place_id}', json=data)

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert the response data
        expected_keys = {"id", "host_user_id",
                         "city_id", "name", "description",
                         "address", "latitude",
                         "longitude", "number_of_rooms",
                         "bathrooms", "price_per_night",
                         "max_guests",
                         "created_at", "updated_at"}
        place_data = response.json
        self.assertEqual(set(place_data.keys()), expected_keys)
        self.assertEqual(place_data["description"], "A decent hotel")
        self.assertEqual(place_data["address"], "Next to Eastland Mall")
        self.assertEqual(place_data["latitude"], -37.814666)
        self.assertEqual(place_data["longitude"], 145.230620)
        self.assertEqual(place_data["number_of_rooms"], 5)
        self.assertEqual(place_data["bathrooms"], 1)
        self.assertEqual(place_data["price_per_night"], 150.00)
        self.assertEqual(place_data["max_guests"], 2)
        self.assertEqual(place_data["name"], "Ringwood Hotel")
        self.assertEqual(place_data["host_user_id"], "0215a722-a3fc-4f08-9120-f8621147f2be")
        self.assertEqual(place_data["city_id"], "687da7c4-eaba-411f-b00d-65c954eb2b8c")


    def test_places_put_invalid_id(self):
        """Test PUT request with invalid place id"""
        place_id = "1234"
        data = {
            "description": "A decent hotel",
            "address": "Next to Eastland Mall",
            "latitude": -37.814666,
            "longitude": 145.230620,
            "number_of_rooms": 5,
            "bathrooms": 1,
            "price_per_night": 150.00,
            "max_guests": 2,
            "name": "Ringwood Hotel",
            "host_user_id": "0215a722-a3fc-4f08-9120-f8621147f2be",
            "city_id": "687da7c4-eaba-411f-b00d-65c954eb2b8c"
        }

        response = self.app.put(f'/api/v1/places/{place_id}', json=data)
        self.assertEqual(response.status_code, 400)

    def test_places_put_missing_json(self):
        """Test PUT request with missing JSON data"""
        place_id = "90c83333-35d4-4638-bdd8-1eceac56915e"

        response = self.app.put(f'/api/v1/places/{place_id}')
        self.assertEqual(response.status_code, 415)

    def test_places_put_invalid_fields(self):
        """Test PUT request with invalid fields"""
        place_id = "90c83333-35d4-4638-bdd8-1eceac56915e"
        data = {
            "invalid_field": "value"
        }

        response = self.app.put(f'/api/v1/places/{place_id}', json=data)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()