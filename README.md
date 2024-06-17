# Project Name
HBnB Evolution

## Description
Airbnb clone project as part of Holberton School Australia cohort 23 sprint 2 using Python and Flask.

## HBnB Evolution Project: Part 1 Guide
Welcome to the first leg of our exciting journey - creating our very own web application, HBnB Evolution, modeled after AirBnB using Python and Flask!

## Part 1 of HBnB Evolution Project
1. UML Diagram: The following diagram incorporates the "Unified Model Language" to develop the types of relationships between all classes and such components.
2. Logic Testing: Tests files were created for the API and business logic which can be found within the "tests" directory. These files were developed to ensure that all models worked coherently without having significant impact to other files or database structures.
3. implementation of API: Flask was used to create an API that plays well with our business logic and file-based persistence (for now).
4. File-Based Data Storage: JSON was used for a file-based system for storing our data.
5. Packaging with Docker: To finish off the project, everything is wrapped up into a Docker image.


## The Three Layers of the API Cake
<br>Services Layer: This is where our API greets the world. It handles all the requests and responses.
<br>Business Logic Layer: The brain of the operation. This is where all the processing and decision-making happens.
<br>Persistence Layer: For now, it's our humble file system, but we'll graduate to a database in the future.


The Data Model: Key Entities

1. Places: These are the heart of our app. Each place (like a house, apartment, or room) has characteristics like name, description, address, city, latitude, longitude, host, number of rooms, bathrooms, price per night, max guests, amenities, and reviews.
2. Users: Users are either owners (hosts) or reviewers (commenters) of places. They have attributes like email, password, first name, and last name. A user can be a host for multiple places and can also write reviews for places they don't own.
3. Reviews: Represent user feedback and ratings for a place. This is where users share their experiences.
4. Amenities: These are features of places, like Wi-Fi, pools, etc. Users can pick from a catalog or add new ones.
5. Country and City: Every place is tied to a city, and each city belongs to a country. This is important for categorizing and searching places.

Business Logic: Rules to Live By
1. Unique Users: Each user is unique and identified by their email.
2. One Host per Place: Every place must have exactly one host.
3. Flexible Hosting: A user can host multiple places or none at all.
4. Open Reviewing: Users can write reviews for places they don't own.
5. Amenity Options: Places can have multiple amenities from a catalog, and users can add new ones.
6. City-Country Structure: A place belongs to a city, cities belong to countries, and a country can have multiple cities.

As you design and implement these features, remember that our application will grow. The choices you make now should allow for easy additions and changes later, especially when we switch from file-based to database storage.

In our pursuit of creating a robust and efficient application, it's crucial that every entity in our data model, except for Country includes the following attributes.:

1. Unique ID (UUID4): Every object - whether it's a Place, User, Review, Amenity or City - must have a unique identifier. This ID should be generated using UUID4 to ensure global uniqueness. This is critical for identifying and managing entities across our application consistently.
2. Creation Date (created_at): This attribute will record the date and time when an object is created. It's vital for tracking the lifespan of our data and understanding the usage patterns.
3. Update Date (updated_at): Similarly, each object should have an attribute to record the last update made. This helps in maintaining the historical accuracy of our data and is essential for any modifications or audit trails.

Why These Attributes Matter?
- Uniqueness: The UUID4 ensures that each entity is distinct, eliminating any confusion or overlap, especially crucial when we scale up.
- Traceability: With created_at and updated_at, we can track the lifecycle of each entity, which is invaluable for debugging, auditing, and understanding user interactions over time.

### The Authors
- [Nicole Ann Gorospe](https://github.com/NickelannG)
- [Khang Nguyen](https://github.com/kdn95)