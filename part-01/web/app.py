#!/usr/bin/python3

from flask import Flask, jsonify
from models.city import City
from data.file_storage import FileStorage
import json

# We should load the data for all the Models early
storage = FileStorage()
country_data = storage.load_from_json_file('data/country.json')
city_data = storage.load_from_json_file('data/city.json')

app = Flask(__name__)


@app.route('/')
def hello_world():
    """ Hello world """
    return 'Hello World'

@app.route('/storage_example')
def storage_example():
    """ Example to show that we can view data loaded above """
    return jsonify(country_data)

@app.route('/cities_example')
def cities_example():
    """ Example route to show what to put in the City model """

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

    return cities_list


# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)