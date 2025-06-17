# Pizza Restaurant API Challenge

## Overview

This is a RESTful API for a Pizza Restaurant built with Flask, SQLAlchemy, and Flask-Migrate. It manages restaurants, pizzas, and their associations, including price validations.

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/crucialniccur/pizza-api-challenge.git
   cd pizza-api-challenge
   Install dependencies using pipenv:
   ```

bash
Copy
Edit
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
Set the Flask app environment variable:

bash
Copy
Edit
export FLASK_APP=server/app.py
Initialize and apply database migrations:

bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed the database:

bash
Copy
Edit
python -m server.seed
Run the app:

bash
Copy
Edit
flask run
Route Summary
GET /restaurants
List all restaurants with their pizzas.

GET /restaurants/<id>
Get a specific restaurant’s details and its pizzas.

DELETE /restaurants/<id>
Delete a restaurant and its associated restaurant_pizzas.

GET /pizzas
List all pizzas.

POST /restaurant_pizzas
Create a restaurant-pizza association.
Request body:

json
Copy
Edit
{
"price": float,
"restaurant_id": int,
"pizza_id": int
}
Response: Created RestaurantPizza or error if validation fails.

Validation Rules
RestaurantPizza.price must be between 1 and 30 (enforced both at the database and application levels).

POST /restaurant_pizzas requires price, restaurant_id, and pizza_id.

Returns 400 for missing fields or invalid price.

Returns 404 if the specified restaurant or pizza does not exist.

Testing with Postman
Import the challenge-1-pizzas.postman_collection.json into Postman.

Ensure the server is running (flask run).

Run the collection to test all routes.

Verify:

GET /restaurants returns a list of restaurants.

GET /restaurants/<id> works with valid and invalid IDs.

DELETE /restaurants/<id> deletes the restaurant and associated RestaurantPizza records.

GET /pizzas returns a list of pizzas.

POST /restaurant_pizzas works with valid data and returns errors for invalid data (e.g., price > 30).

This README provides all necessary steps to set up, run, and test the Pizza Restaurant API.

Copy
Edit

Tools
