Pizza Restaurant API Challenge
Overview
RESTful API for a Pizza Restaurant built with Flask, SQLAlchemy, and Flask-Migrate. Manages restaurants, pizzas, and their associations with price validations.
Setup Instructions

Clone the repository:git clone https://github.com/crucialniccur/pizza-api-challenge.git
cd pizza-api-challenge

Install dependencies using pipenv:pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

Set the Flask app:export FLASK_APP=server/app.py

Initialize and apply database migrations:flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Seed the database:python -m server.seed

Run the app:flask run

Route Summary

GET /restaurants: List all restaurants with their pizzas.
GET /restaurants/: Get a restaurant’s details and its pizzas.
DELETE /restaurants/: Delete a restaurant and its associated restaurant_pizzas.
GET /pizzas: List all pizzas.
POST /restaurant_pizzas: Create a restaurant-pizza association.
Request body: {"price": float, "restaurant_id": int, "pizza_id": int}
Response: Created RestaurantPizza or error if validation fails.

Validation Rules

RestaurantPizza.price: Must be between 1 and 30 (enforced at database and application levels).
POST /restaurant_pizzas: Requires price, restaurant_id, and pizza_id. Returns 400 for missing fields or invalid price, 404 if restaurant or pizza doesn’t exist.

Testing with Postman

Import challenge-1-pizzas.postman_collection.json into Postman.
Ensure the server is running (flask run).
Run the collection to test all routes.
Verify GET /restaurants returns a list of restaurants.
Test GET /restaurants/<id> with valid and invalid IDs.
Test DELETE /restaurants/<id> and confirm associated RestaurantPizza records are deleted.
Verify GET /pizzas returns a list of pizzas.
Test POST /restaurant_pizzas with valid and invalid data (e.g., price > 30).
