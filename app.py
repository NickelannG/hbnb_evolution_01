#!/usr/bin/python3

from datetime import datetime
from flask import Flask, jsonify, request, abort
from models.city import City
from models.country import Country
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from data import country_data, place_data, amenity_data, place_to_amenity_data, review_data, user_data, city_data

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Hello world """
    return 'Hello World'

@app.route('/', methods=["POST"])
def hello_world_post():
    """ Hello world endpoint for POST requests """
    # curl -X POST localhost:5000/
    return "hello world\n"


# Examples
@app.route('/example/country_data')
def example_country_data():
    """ Example to show that we can view data loaded in the data module's init """
    return jsonify(country_data)

@app.route('/example/cities')
def example_cities():
    """ Example route to showing usage of the City model class """

    # We will be appending dictionaries to the list instead of City objects
    # This is so we can print them out on the webpage
    # If there is no need to display the data, we can consider storing the City objects themselves
    cities_list = []

    # the 'hello' and 'world' params below will be filtered off in City constructor
    cities_list.append(City(name="Gotham", hello="hello").__dict__)
    cities_list.append(City(name="Metropolis", world="world").__dict__)

    # Validation: The city with the invalid name is not appended to the list
    try:
        cities_list.append(City(name="#$%^&**", country_id=2).__dict__)
    except ValueError as exc:
        # This is printed internally in the server output. Not shown on website.
        print("City creation Error - ", exc)

    # Validation: The city with the invalid country_id is not appended to the list
    try:
        cities_list.append(City(name="Duckburg", country_id=1234).__dict__)
    except ValueError as exc:
        print("City creation Error - ", exc)

    # Note that private attributes have a weird key format. e.g. "_City__country_id"
    # This shows that the output of the City object's built-in __dict__ is not usable as-is

    return cities_list

@app.route('/example/places_amenties_raw')
def example_places_amenities_raw():
    """ Prints out the raw data for relationships between places and their amenities """
    return jsonify(place_to_amenity_data)

@app.route('/example/places_amenties_prettified_example')
def example_places_amenties_prettified():
    """ Prints out the relationships between places and their amenities using names """

    output = {}

    for place_key in place_to_amenity_data:
        place_name = place_data[place_key]['name']
        if place_name not in output:
            output[place_name] = []

        amenities_ids = place_to_amenity_data[place_key]
        for amenity_key in amenities_ids:
            amenity_name = amenity_data[amenity_key]['name']
            output[place_name].append(amenity_name)

    return jsonify(output)

@app.route('/example/places_reviews')
def example_places_reviews():
    """ prints out reviews of places """

    output = {}

    for key in review_data:
        row = review_data[key]
        place_id = row['place_id']
        place_name = place_data[place_id]['name']
        if place_name not in output:
            output[place_name] = []
        
        reviewer = user_data[row['commentor_user_id']]

        output[place_name].append({
            "review": row['feedback'],
            "rating": str(row['rating'] * 5) + " / 5",
            "reviewer": reviewer['first_name'] + " " + reviewer['last_name']
        })

    return jsonify(output)

# Consider adding other test routes to display data for:
# - the places within the countries
# - which places are owned by which users
# - names of the owners of places with toilets


# --- API endpoints ---
# --- USER ---
@app.route('/api/v1/users', methods=["GET"])
def users_get():
    """returns Users"""
    data = []

    for k, v in user_data.items():
        data.append({
            "id": v['id'],
            "first_name": v['first_name'],
            "last_name": v['last_name'],
            "email": v['email'],
            "password": v['password'],
            "created_at": datetime.fromtimestamp(v['created_at']),
            "updated_at": datetime.fromtimestamp(v['updated_at'])
        })

    return jsonify(data)

@app.route('/api/v1/users/<user_id>', methods=["GET"])
def users_specific_get(user_id):
    """returns specified user"""
    data = []

    if user_id not in user_data:
        # raise IndexError("User not found!")
        return "User not found!"

    v = user_data[user_id]
    data.append({
        "id": v['id'],
        "first_name": v['first_name'],
        "last_name": v['last_name'],
        "email": v['email'],
        "password": v['password'],
        "created_at": datetime.fromtimestamp(v['created_at']),
        "updated_at": datetime.fromtimestamp(v['updated_at'])
    })
    return jsonify(data)

@app.route('/api/v1/users', methods=["POST"])
def users_post():
    """ posts data for new user then returns the user data"""
    # -- Usage example --
    # curl -X POST [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    # print(request.content_type)

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()
    if 'email' not in data:
        abort(400, "Missing email")
    if 'password' not in data:
        abort(400, "Missing password")

    try:
        u = User(first_name=data["first_name"],last_name=data["last_name"], email=data["email"], password=data["password"])
    except ValueError as exc:
        return repr(exc) + "\n"

    # add new user data to user_data
    # note that the created_at and updated_at are using timestamps
    user_data[u.id] = {
        "id": u.id,
        "first_name": u.first_name,
        "last_name": u.last_name,
        "email": u.email,
        "created_at": u.created_at,
        "updated_at": u.updated_at
    }

    # note that the created_at and updated_at are using readable datetimes
    attribs = {
        "id": u.id,
        "first_name": u.first_name,
        "last_name": u.last_name,
        "email": u.email,
        "created_at": datetime.fromtimestamp(u.created_at),
        "updated_at": datetime.fromtimestamp(u.updated_at)
    }

    return jsonify(attribs)

@app.route('/api/v1/users/<user_id>', methods=["PUT"])
def users_put(user_id):
    """ updates existing user data using specified id """
    # -- Usage example --
    # curl -X PUT [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()

    if user_id not in user_data:
        abort(400, "User not found for id {}".format(user_id))

    u = user_data[user_id]

    # modify the values
    for k, v in data.items():
        # only first_name and last_name are allowed to be modified
        if k in ["first_name", "last_name"]:
            u[k] = v

    # update user_data with the new name - print user_data out to confirm it if you want
    user_data[user_id] = u

    attribs = {
        "id": u["id"],
        "first_name": u["first_name"],
        "last_name": u["last_name"],
        "email": u["email"],
        "created_at": datetime.fromtimestamp(u["created_at"]),
        "updated_at": datetime.fromtimestamp(u["updated_at"])
    }

    # print out the updated user details
    return jsonify(attribs)

# --- COUNTRY ---
@app.route('/api/v1/countries', methods=["POST"])
def countries_post():
    """ posts data for new country then returns the country data"""
    # -- Usage example --
    # curl -X POST [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()
    if 'name' not in data:
        abort(400, "Missing name")
    if 'code' not in data:
        abort(400, "Missing country code")

    try:
        c = Country(name=data["name"],code=data["code"])
    except ValueError as exc:
        return repr(exc) + "\n"

    # add new user data to user_data
    # note that the created_at and updated_at are using timestamps
    country_data[c.id] = {
        "id": c.id,
        "name": c.name,
        "code": c.code,
        "created_at": c.created_at,
        "updated_at": c.updated_at
    }

    # note that the created_at and updated_at are using readable datetimes
    attribs = {
        "id": c.id,
        "name": c.name,
        "code": c.code,
        "created_at": datetime.fromtimestamp(c.created_at),
        "updated_at": datetime.fromtimestamp(c.updated_at)
    }

    return jsonify(attribs)

@app.route('/api/v1/countries', methods=["GET"])
def countries_get():
    """ returns countires data """
    data = []

    for k, v in country_data.items():
        data.append({
            "id": v['id'],
            "name": v['name'],
            "code": v['code'],
            "created_at": datetime.fromtimestamp(v['created_at']),
            "updated_at": datetime.fromtimestamp(v['updated_at'])
        })

    return jsonify(data)

@app.route('/api/v1/countries/<country_code>', methods=["GET"])
def countries_specific_get(country_code):
    """ returns specific country data """
    for k, v in country_data.items():
        if v['code'] == country_code:
            data = v

    c = {
        "id": data['id'],
        "name": data['name'],
        "code": data['code'],
        "created_at": datetime.fromtimestamp(data['created_at']),
        "updated_at": datetime.fromtimestamp(data['updated_at'])
    }

    return jsonify(c)

@app.route('/api/v1/countries/<country_code>', methods=["PUT"])
def countries_put(country_code):
    """ updates existing country data using specified id """
    # -- Usage example --
    # curl -X PUT [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    c = {}

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()
    for k, v in country_data.items():
        if v['code'] == country_code:
            c = v

    if not c:
        abort(400, "Country not found for code {}".format(country_code))

    # modify the values
    # only name is allowed to be modified
    for k, v in data.items():
        if k in ["name"]:
            c[k] = v

    # update country_data with the new name - print country_data out to confirm it if you want
    country_data[c['id']] = c

    attribs = {
        "id": c["id"],
        "name": c["name"],
        "code": c["code"],
        "created_at": datetime.fromtimestamp(c["created_at"]),
        "updated_at": datetime.fromtimestamp(c["updated_at"])
    }

    # print out the updated user details
    return jsonify(attribs)

@app.route('/api/v1/countries/<country_code>/cities', methods=["GET"])
def countries_specific_cities_get(country_code):
    """ returns cities data of specified country """

    # Initialize empty list to store cities data
    data = []
    
    # Initialize a variable to store the country ID we are looking for
    wanted_country_id = ""

    # Iterate through the country_data dictionary to find the country with the provided country code
    for k, v in country_data.items():
        if v['code'] == country_code:
            # Once the country with the specified code is found, store its ID
            wanted_country_id = v['id']

    # Iterate through the city_data dictionary to find cities belonging to the country with the wanted_country_id
    for k, v in city_data.items():
        if v['country_id'] == wanted_country_id:
            # If the city belongs to the country, construct a dictionary containing city details and append it to the data list
            data.append({
                "id": v['id'],
                "name": v['name'],
                "country_id": v['country_id'],
                "created_at": datetime.fromtimestamp(v['created_at']),
                "updated_at": datetime.fromtimestamp(v['updated_at'])
            })

    return jsonify(data)

# Create the rest of the endpoints for:
#  - City
#  - Amenity
#  - Place
#  - Review

# --- CITY ---
# note the capital C for city and lowercase for country

@app.route('/api/v1/cities', methods=["GET"])
def cities_get():
    """returns Cities"""
    data = []

    for k, v in city_data.items():
        data.append({
            "id": v['id'],
            "name": v['name'],
            "country_id": v['country_id'],
            "created_at": datetime.fromtimestamp(v['created_at']),
            "updated_at": datetime.fromtimestamp(v['updated_at'])
        })

    return jsonify(data)

@app.route('/api/v1/city/<city_id>', methods=["GET"])
def city_specific_get(city_id):
    """returns specific city"""
    data = []

    if city_id not in city_data:
        # raise IndexError("City not found!")
        return "City not found!"

    v = city_data[city_id]
    data.append({
        "id": v['id'],
            "name": v['name'],
            "country_id": v['country_id'],
            "created_at": datetime.fromtimestamp(v['created_at']),
            "updated_at": datetime.fromtimestamp(v['updated_at'])
    })
    return jsonify(data)

@app.route('/api/v1/cities', methods=["POST"])
def city_post():
    """Posts data for new city then returns the city data"""

    if request.get_json() is None:
        abort(400, "Not a JSON")
    
    data = request.get_json()
    if 'name' not in data:
        abort(400, "Missing name")
    # need to check country id as well
    if 'country_id' not in data:
        abort(400, "Missing country_id") 

    try:
        C = City(name=data["name"], country_id=data["country_id"])
    except ValueError as exc:
        return repr(exc) + "\n"

    # add new user data to user_data
    # note that the created_at and updated_at are using timestamps
    
    city_data[C.id] = {
        "id": C.id,
        "name": C.name,
        "country_id": C.country_id,
        "created_at": C.created_at,
        "updated_at": C.updated_at
    }

    # note that the created_at and updated_at are using readable datetimes
    attribs = {
        "id": C.id,
        "name": C.name,
        "country_id": C.country_id,
        "created_at": datetime.fromtimestamp(C.created_at),
        "updated_at": datetime.fromtimestamp(C.updated_at)
    }

    return jsonify(attribs)

@app.route('/api/v1/cities/<city_id>', methods=["PUT"])
def cities_put(city_id):
    """ updates existing city data using specified id """

    # initialize empty dictionary to hold the city data if found
    C = {}

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()
    for k, v in city_data.items():
        if v['id'] == city_id:
            C = v

    if not C:
        abort(400, "City not found for id {}".format(city_id))

    # modify the values
    # only name is allowed to be modified
    for k, v in data.items():
        if k in ["name", "country_id"]:
            C[k] = v
    
    # update 'updated_at' timestamp
    C["updated_at"] = datetime.now().timestamp()

    # update city_data - print city_data out to confirm it if you want
    city_data[C['id']] = C

    attribs = {
        "id": C["id"],
        "name": C["name"],
        "country_id": C["country_id"],
        "created_at": datetime.fromtimestamp(C["created_at"]),
        "updated_at": datetime.fromtimestamp(C["updated_at"])
    }

    # print out the updated user details
    return jsonify(attribs)

@app.route('/api/v1/cities/<city_id>/countries', methods=["GET"])
def cities_specific_country_get(city_id):
    """returns contries data of specified city"""
    
    # Check if the provided city ID exists in the city_data dictionary
    if city_id not in city_data:
        # If city not found, return a message indicating so
        return "City not found!"
    
    # Retrieve the city's details from city_data
    city = city_data[city_id]
    
    # Retrieve the country ID associated with the city
    country_id = city['country_id']

    # Check if the country ID exists in country_data dictionary
    if country_id not in country_data:
        # If country not found for the city, return a message indicating so
        return "Country not found for city with ID: {}".format(city_id)
    
    # Retrieve the country's details from country_data
    c = country_data[country_id]
    
    # Construct country details dictionary with required information
    country_details = {
        "id": c['id'],
        "name": c['name'],
        "code": c['code'],
        "created_at": datetime.fromtimestamp(c['created_at']),
        "updated_at": datetime.fromtimestamp(c['updated_at'])
    }

    # Return the country details as JSON response
    return jsonify(country_details)


# --- REVIEW ---
@app.route('/api/v1/reviews', methods=["GET"])
def reviews_get():
    """Return Reviews"""
    data = []

    for k, v in review_data.items():
        data.append({
            "id": v['id'],
            "feedback": v['feedback'],
            "commentor_user_id": v["commentor_user_id"],
            "place_id": v["place_id"],
            "rating": v["rating"],
            "created_at": datetime.fromtimestamp(v['created_at']),
            "updated_at": datetime.fromtimestamp(v['updated_at'])
        })
    return jsonify(data)

@app.route('/api/v1/reviews/<review_id>', methods=["GET"])
def reviews_specific_get(review_id):
    """returns specified review"""
    data = []

    if review_id not in review_data:
        # raise IndexError("Review not found!")
        return "Review not found!"
    
    v = review_data[review_id]
    data.append({
            "id": v['id'],
            "feedback": v['feedback'],
            "commentor_user_id": v["commentor_user_id"],
            "place_id": v["place_id"],
            "rating": v["rating"],
            "created_at": datetime.fromtimestamp(v['created_at']),
            "updated_at": datetime.fromtimestamp(v['updated_at'])
    })
    return jsonify(data)

@app.route('/api/v1/reviews', methods=["POST"])
def review_post():
    """Posts data for new reviews then return review data"""
    # -- Usage example --
    # curl -X POST [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()
    if 'feedback' not in data:
        abort(400, "Missing feedback")
    if 'commentor_user_id' not in data:
        abort(400, "Missing commentor user id")
    if 'place_id' not in data:
        abort(400, "Missing place id")
    if 'rating' not in data:
        abort(400, "Missing rating")

    try:
        r = Review(feedback=data["feedback"], commentor_user_id=data["commentor_user_id"],
                   place_id=data["place_id"], rating=data["rating"])
    except ValueError as exc:
        return repr(exc) + "\n"

    # add new review data to review_data
    # note that the created_at and updated_at are using timestamps

    review_data[r.id] = {
        "id": r.id,
        "feedback": r.feedback,
        "commentor_user_id": r.commentor_user_id,
        "place_id": r.place_id,
        "rating": r.rating,
        "created_at": r.created_at,
        "updated_at": r.updated_at
    }

    attribs = {
        "id": r.id,
        "feedback": r.feedback,
        "commentor_user_id": r.commentor_user_id,
        "place_id": r.place_id,
        "rating": r.rating,
        "created_at": datetime.fromtimestamp(r.created_at),
        "updated_at": datetime.fromtimestamp(r.updated_at)
    }

    return jsonify(attribs)

@app.route('/api/v1/reviews/<review_id>', methods=["PUT"])
def review_put(review_id):
    """ updates existing review data using specified id """
    # -- Usage example --
    # curl -X PUT [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    r = {}

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()
    for k, v in review_data.items():
        if v['id'] == review_id:
            r = v

    if not r:
        abort(400, "Review not found for id {}".format(review_id))

    # modify the values
    # only name is allowed to be modified
    for k, v in data.items():
        if k in ["feedback", "commentor_user_id", "place_id", "rating"]:
            r[k]: v

     # update 'updated_at' timestamp
    r["updated_at"] = datetime.now().timestamp()

    # update review_data - print review data out to confirm if needed
    review_data[r['id']] = r

    attribs = {
        "id": r["id"],
        "feedback": r["feedback"],
        "commentor_user_id": r["commentor_user_id"],
        "place_id": r["place_id"],
        "rating": r["rating"],
        "created_at": datetime.fromtimestamp(r["created_at"]),
        "updated_at": datetime.fromtimestamp(r["updated_at"])
    }
    # print out the updated review details
    return jsonify(attribs)

@app.route('/api/v1/reviews/<review_id>/place', methods=["GET"])
def review_specific_place_get(review_id):
    """Returns place data of specific review"""
    # Check if the provided review ID exists in the review_data dictionary
    if review_id not in review_data:
        # If review not found, return message
        return "Review not found"

    # Retrieve the review's details from review_data
    review = review_data[review_id]

    # Retrieve place ID associated with the review
    place_id = review['place_id']

    # Check if the place ID exists in place_data dictionary
    if place_id not in place_data:
        # If place not found for the review, return a message indicating
        return "Place not found for review with ID: {}".format(review_id)
    
    # Retrieve the place's details from place_data
    p = place_data[place_id]

    # Counstruct place details dictionary with required information
    place_details = {
        "id": p['id'],
        "host_user_id": p["host_user_id"],
        "city_id": p["city_id"],
        "name": p["name"],
        "description": p["description"],
        "address": p["address"],
        "longitude": p["longitude"],
        "latitude": p["latitude"],
        "number_of_rooms": p["number_of_rooms"],
        "bathrooms": p["bathrooms"],
        "price_per_night": p["price_per_night"],
        "max_guests": p["max_guests"],
        "created_at": datetime.fromtimestamp(p["created_at"]),
        "updated_at": datetime.fromtimestamp(p["updated_at"])
    }

    # Return the place details as JSON response
    return jsonify(place_details)

@app.route('/api/v1/review/<review_id>/user', methods=["GET"])
def review_specific_user_get(review_id):
    """Returns commentor user data of specific review"""

    # Check if the provided review ID exists in the review_data dictionary
    if review_id not in review_data:
        # If review not found, return message
        return "Review not found"

    # Retrieve the review's details from review_data
    review = review_data[review_id]

    # Retrieve user ID associated with the review
    user_id = review['commentor_user_id']

    # Check if the user ID exists in user_data dictionary
    if user_id not in user_data:
        # If user not found for the review, return a message indicating
        return "User not found for review with ID: {}".format(review_id)
    
    # Retrieve the user's details from user_data
    u = user_data[user_id]

    # Counstruct user details dictionary with required information
    user_details = {
        "id": u['id'],
        "first_name": u["first_name"],
        "last_name": u["last_name"],
        "email": u["email"],
        "password": u["password"],
        "created_at": datetime.fromtimestamp(u["created_at"]),
        "updated_at": datetime.fromtimestamp(u["updated_at"])
    }

    # Return the user details as JSON response
    return jsonify(user_details)



# --- AMENITY ---
@app.route('/api/v1/amenities', methods=["GET"])
def amenity_get():
    """Return Amenities"""
    data = []

    for k, v in amenity_data.items():
        data.append({
            "id": v['id'],
            "name": v['name'],
            "created_at": datetime.fromtimestamp(v['created_at']),
            "updated_at": datetime.fromtimestamp(v['updated_at'])
        })
    return jsonify(data)


@app.route('/api/v1/amenities/<amenity_id>', methods=["GET"])
def amenity_specific_get(amenity_id):
    """returns specified amenity"""
    data = []

    if amenity_id not in amenity_data:
        # raise IndexError("Review not found!")
        return "Amenity not found!"
    
    v = amenity_data[amenity_id]
    data.append({
            "id": v['id'],
            "name": v['name'],
            "created_at": datetime.fromtimestamp(v['created_at']),
            "updated_at": datetime.fromtimestamp(v['updated_at'])
    })
    return jsonify(data)

@app.route('/api/v1/amenities', methods=["POST"])
def amenity_post():
    """Posts data for new amenities then return amenity data"""
    # -- Usage example --
    # curl -X POST [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()
    if 'name' not in data:
        abort(400, "Missing name")

    try:
        a = Amenity(name=data["name"])
    except ValueError as exc:
        return repr(exc) + "\n"

    # add new amenity data to amenity_data
    # note that the created_at and updated_at are using timestamps

    amenity_data[a.id] = {
        "id": a.id,
        "name": a.name,
        "created_at": a.created_at,
        "updated_at": a.updated_at
    }

    attribs = {
        "id": a.id,
        "name": a.name,
        "created_at": datetime.fromtimestamp(a.created_at),
        "updated_at": datetime.fromtimestamp(a.updated_at)
    }

    return jsonify(attribs)


@app.route('/api/v1/amenities/<amenity_id>', methods=["PUT"])
def amenity_put(amenity_id):
    """ updates existing amenity data using specified id """
    # -- Usage example --
    # curl -X PUT [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    a = {}

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()
    for k, v in amenity_data.items():
        if v['id'] == amenity_id:
            a = v

    if not a:
        abort(400, "Amenity not found for id {}".format(amenity_id))

    # modify the values
    # only name is allowed to be modified
    for k, v in data.items():
        if k in ["name"]:
            a[k]: v

     # update 'updated_at' timestamp
    a["updated_at"] = datetime.now().timestamp()

    # update amenity_data - print amenity data out to confirm if needed
    amenity_data[a['id']] = a

    attribs = {
        "id": a["id"],
        "name": a["name"],
        "created_at": datetime.fromtimestamp(a["created_at"]),
        "updated_at": datetime.fromtimestamp(a["updated_at"])
    }
    # print out the updated review details
    return jsonify(attribs)


@app.route('/api/v1/amenities/<amenity_id>/place', methods=["GET"])
def amenity_specific_places_get(amenity_id):
    """Returns places data of specific amenity"""
     # Initialize empty list to store cities data
    data = []
    

    if amenity_id not in amenity_data:
        # raise IndexError("Review not found!")
        return "Amenity not found!"

    # Iterate through the city_data dictionary to find cities belonging to the country with the wanted_country_id
    for k, v in place_to_amenity_data.items():
        if 'amenity_id' in v and v['amenity_id'] == amenity_id:
            # If the city belongs to the country, construct a dictionary containing city details and append it to the data list
            data.append({
                "place_id": v['place_id'],
            })

    return jsonify(data)


# --- PLACE ---
@app.route('/api/v1/places', methods=["GET"])
def place_get():
    """Returns Place"""
    data = []

    for k, v in place_data.items():
        data.append({
            "id": v['id'],
            "host_user_id": v['host_user_id'],
            "city_id": v['city_id'],
            "name": v['name'],
            "description": v['description'],
            "address": v['address'],
            "latitude": v['latitude'],
            "longitude": v['longitude'],
            "number_of_rooms": v['number_of_rooms'],
            "bathrooms": v['bathrooms'],
            "price_per_night": v['price_per_night'],
            "max_guests": v['max_guests'],
            "created_at": datetime.fromtimestamp(v['created_at']),
            "updated_at": datetime.fromtimestamp(v['updated_at'])
        })
    return jsonify(data)

@app.route('/api/v1/places/<place_id>', methods=["GET"])
def places_specific_get(place_id):
    """Returns specific place"""
    data = []

    if place_id not in place_data:
        #Raise IndexError("Place not found!")
        return "Place not found!"

    v = place_data[place_id]
    data.append({
            "id": v['id'],
            "host_user_id": v['host_user_id'],
            "city_id": v['city_id'],
            "name": v['name'],
            "description": v['description'],
            "address": v['address'],
            "latitude": v['latitude'],
            "longitude": v['longitude'],
            "number_of_rooms": v['number_of_rooms'],
            "bathrooms": v['bathrooms'],
            "price_per_night": v['price_per_night'],
            "max_guests": v['max_guests'],
            "created_at": datetime.fromtimestamp(v['created_at']),
            "updated_at": datetime.fromtimestamp(v['updated_at'])
            })
    return jsonify(data)

@app.route('/api/v1/places', methods=["POST"])
def place_post():
    """Posts data for new places then return place data"""
     # -- Usage example --
    # curl -X POST [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()
    if 'description' not in data:
        abort(400, "Missing description")
    if 'address' not in data:
        abort(400, "Missing address")
    if 'latitude' not in data:
        abort(400, "Missing latitude")
    if 'longitude' not in data:
        abort(400, "Missing longitude")
    if 'number_of_rooms' not in data:
        abort(400, "Missing number of rooms")
    if 'bathrooms' not in data:
        abort(400, "Missing number of bathrooms")
    if 'price_per_night' not in data:
        abort(400, "Missing pricing per night")
    if 'max_guests' not in data:
        abort(400, "Missing max number of guests")
    if 'name' not in data:
        abort(400, "Missing name of place")
    if 'host_user_id' not in data:
        abort(400, "Missing host ID")
    if 'city_id' not in data:
        abort(400, "Missing city ID")

    try:
        p = Place(description=data["description"],
                  address=data["address"],
                  latitude=data["latitude"],
                  longitude=data["longitude"],
                  number_of_rooms=data["number_of_rooms"],
                  bathrooms=data["bathrooms"],
                  price_per_night=data["price_per_night"],
                  max_guests=data["max_guests"],
                  name=data["name"],
                  host_user_id=data["host_user_id"],
                  city_id=data["city_id"],
                  )
    except ValueError as exc:
        return repr(exc) + "\n"

    # add new place data to place_data
    # note that the created_at and updated_at are using timestamps

    place_data[p.id] = {
        "id": p.id,
        "host_user_id": p.host_user_id,
        "city_id": p.city_id,
        "name": p.name,
        "description": p.description,
        "address": p.address,
        "latitude": p.latitude,
        "longitude": p.longitude,
        "number_of_rooms": p.number_of_rooms,
        "bathrooms": p.bathrooms,
        "price_per_night": p.price_per_night,
        "max_guests": p.max_guests,
        "created_at": p.created_at,
        "updated_at": p.updated_at
    }

    attribs = {
        "id": p.id,
        "host_user_id": p.host_user_id,
        "city_id": p.city_id,
        "name": p.name,
        "description": p.description,
        "address": p.address,
        "latitude": p.latitude,
        "longitude": p.longitude,
        "number_of_rooms": p.number_of_rooms,
        "bathrooms": p.bathrooms,
        "price_per_night": p.price_per_night,
        "max_guests": p.max_guests,
        "created_at": datetime.fromtimestamp(p.created_at),
        "updated_at": datetime.fromtimestamp(p.updated_at)
    }

    return jsonify(attribs)

@app.route('/api/v1/places/<place_id>', methods=["PUT"])
def place_put(place_id):
    """Updates existing place data using specific id"""
    # -- Usage example --
    # curl -X PUT [URL] /
    #    -H "Content-Type: application/json" /
    #    -d '{"key1":"value1","key2":"value2"}'

    p = {}

    if request.get_json() is None:
        
        data = request.get_json()

    for k, v in place_data.items():
        if v['id'] == place_id:
            r = v

    if not p:
        abort(400, "Place not found for id {}".format(place_id))

    # modify the values
    # only name is allowed to be modified
    for k, v in data.items():
        if k in ["description","address", "latitude", "longitude",
                 "number_of_rooms", "bathrooms", "price_per_night",
                 "max_guests", "name", "host_user_id", "city_id"]:
            p[k]: v

    # update 'updated_at' timestamp
    p["updated_at"] = datetime.now().timestamp()

    # update palce_data - print place data out to confirm if needed
    place_data[p['id']] = p

    attribs = {
        "id": p["id"],
        "host_user_id": p["host_user_id"],
        "city_id": p["city_id"],
        "name": p["name"],
        "description": p["description"],
        "address": p["address"],
        "latitude": p["latitude"],
        "longitude": p["longitude"],
        "number_of_rooms": p["number_of_rooms"],
        "bathrooms": p["bathrooms"],
        "price_per_night": p["price_per_night"],
        "max_guests": p["max_guests"],
        "created_at": datetime.fromtimestamp(p["created_at"]),
        "updated_at": datetime.fromtimestamp(p["updated_at"])
    }
    # print out the updated place details
    return jsonify(attribs)

@app.route('/api/v1/places/<place_id>/user', methods=["GET"])
def place_specific_user_get(place_id):
    """Returns host user data of specified place"""

    # Check if the provided place ID exists in the place_data dictionary
    if place_id not in place_data:
        # If place not found, return message
        return "Place not found"
    
    # Retrieve the place's details from place_data
    place = place_data[place_id]

    # Retrieve user ID associated with the place
    user_id = place['host_user_id']

    # Check if the user ID exists in user_data dictionary
    if user_id not in user_data:
        # If user not found for the place, return message
        return "Host user not found for place with ID: {}".format(place_id)
    
    # Retrieve the user's details from user_data
    u = user_data[user_id]

    # Construct user details dictionary with required information
    user_details = {
        "id": u["id"],
        "first_name": u["first_name"],
        "last_name": u["last_name"],
        "email": u["email"],
        "created_at": datetime.fromtimestamp(u["created_at"]),
        "updated_at": datetime.fromtimestamp(u["updated_at"])
    }

    # Return the user details as JSON response
    return jsonify(user_details)


@app.route('/api/v1/places/<place_id>/city', methods=["GET"])
def place_specific_city_get(place_id):
    """Returns city data of specified place"""

    # Check if the provided place ID exists in the place_data dictionary
    if place_id not in place_data:
        # If place not found, return message
        return "Place not found"
    
    # Retrieve the place's details from place_data
    place = place_data[place_id]

    # Retrieve the city ID associated with the place
    city_id = place['city_id']

    if city_id not in city_data:
        # If city not found for the place, return a message
        return "City not found for place with ID: {}".format(place_id)

    # Retrieve the city's details from country_data
    C = city_data[city_id]

    # Construct city details dictionary with required information
    city_details = {
        "id": C['id'],
        "name": C['name'],
        "country_id": C['country_id'],
        "created_at": datetime.fromtimestamp(C['created_at']),
        "updated_at": datetime.fromtimestamp(C['updated_at'])
    }

    # Return the city details as JSON response
    return jsonify(city_details)


@app.route('/api/v1/places/<place_id>/review', methods=["GET"])
def place_specific_reviews_get(place_id):
    """Returns review data of specified place"""

    # Initialize empty list to store reviews data
    data = []
    
    # Initialize a variable to store the place ID we are looking for
    wanted_place_id = ""

    # Iterate through the place_data dictionary to find the place with the provided place ID
    for k, v in place_data.items():
        if v['id'] == place_id:
            # Once the place with the specified code is found, store its ID
            wanted_place_id = v['id']

    # Iterate through the city_data dictionary to find cities belonging to the country with the wanted_country_id
    for k, v in review_data.items():
        if v['place_id'] == wanted_place_id:
            # If the review belongs to the place, construct a dictionary containing review details and append it to the data list
            data.append({
                "id": v['id'],
                "feedback": v['feedback'],
                "commentor_user_id": v["commentor_user_id"],
                "place_id": v["place_id"],
                "rating": v["rating"],
                "created_at": datetime.fromtimestamp(v['created_at']),
                "updated_at": datetime.fromtimestamp(v['updated_at'])
            })

    return jsonify(data)


@app.route('/api/v1/places/<place_id>/amenity', methods=["GET"])
def place_specific_amenities_get(place_id):
    
    output = {}
    
    # Check if the place_id exists in place_data
    if place_id not in place_data:
        return jsonify({"error": "Place ID not found"}), 404
    
    place_name = place_data[place_id]['name']
    
    if place_name not in output:
        output[place_name] = []

    # Iterate through the list in place_to_amenity_data["Place_to_Amenity"]
    for item in place_to_amenity_data.items():
        if item['place_id'] == place_id:
            amenity_id = item['amenity_id']
            amenity_name = amenity_data[amenity_id]['name']
            output[place_name].append(amenity_name)

    return jsonify(output)

# WIP..
# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
