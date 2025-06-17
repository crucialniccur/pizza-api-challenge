Pizza Restaurant API Challenge
Overview
This RESTful API for a Pizza Restaurant is built using Flask, SQLAlchemy, and Flask-Migrate. It manages restaurants, pizzas, and their associations, with price validations enforced at both the database and application levels.
Setup Instructions

Clone the repository:
git clone https://github.com/crucialniccur/pizza-api-challenge.git
cd pizza-api-challenge

Install dependencies using pipenv:
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

Set the Flask app environment variable:
export FLASK_APP=server/app.py

Initialize and apply database migrations:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Seed the database:
python -m server.seed

Run the app:
flask run

Route Summary
GET /restaurants

Description: List all restaurants with their associated pizzas.
Response: JSON array of restaurants with their details and pizzas.

GET /restaurants/

Description: Get details of a specific restaurant and its associated pizzas.
Response: JSON object with restaurant details and pizzas, or 404 if not found.

DELETE /restaurants/

Description: Delete a restaurant and its associated restaurant_pizzas.
Response: 204 on success, or 404 if not found.

GET /pizzas

Description: List all pizzas.
Response: JSON array of pizzas.

POST /restaurant_pizzas

Description: Create a restaurant-pizza association.

Request Body:
{
"price": float,
"restaurant_id": int,
"pizza_id": int
}

Response: JSON object of the created RestaurantPizza, or error if validation fails.

Validation Rules

RestaurantPizza.price: Must be between 1 and 30 (enforced at both database and application levels).
POST /restaurant_pizzas: Requires price, restaurant_id, and pizza_id.
Returns 400 for missing fields or invalid price.
Returns 404 if the specified restaurant or pizza does not exist.

Testing with Postman

Import the challenge-1-pizzas.postman_collection.json file into Postman.
Ensure the server is running (flask run).
Run the collection to test all routes.
Verify the following:
GET /restaurants: Returns a list of restaurants.
GET /restaurants/: Works with valid and invalid IDs.
DELETE /restaurants/: Deletes the restaurant and associated RestaurantPizza records.
GET /pizzas: Returns a list of pizzas.
POST /restaurant_pizzas: Works with valid data and returns errors for invalid data (e.g., price > 30).

This README provides all necessary steps to set up, run, and test the Pizza Restaurant API.
