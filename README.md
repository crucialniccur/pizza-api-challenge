Pizza Restaurant API
A RESTful API for managing a pizza restaurant's data, including restaurants, pizzas, and their associations, built with Python, Flask, SQLAlchemy, and SQLite.
Features

Manage restaurants, pizzas, and restaurant-pizza associations
CRUD operations for all resources
JSON API responses with proper error handling
Data validation for restaurant-pizza associations
Database seeding for quick setup

Getting Started
Prerequisites

Python 3.8+
pipenv (for virtual environment management)

Installation

Clone the repository:
git clone https://github.com/YOUR_GITHUB_USERNAME/pizza-api-challenge.git
cd pizza-api-challenge

Set up the virtual environment and install dependencies:
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

Set up the Flask app:
export FLASK_APP=server/app.py

Initialize and migrate the database:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Seed the database:
python server/seed.py

Run the application:
flask run --port 5555

The API will be available at http://localhost:5555.

API Endpoints
Restaurants

GET /restaurantsList all restaurants.Response: JSON array of restaurants with their details.

GET /restaurants/Get details of a specific restaurant, including associated pizzas.Response: JSON object with restaurant details or { "error": "Restaurant not found" } (404).

DELETE /restaurants/Delete a restaurant and its associated restaurant-pizzas.Response: 204 No Content or { "error": "Restaurant not found" } (404).

Pizzas

GET /pizzasList all pizzas.Response: JSON array of pizzas with their details.

Restaurant Pizzas

POST /restaurant_pizzasCreate a new restaurant-pizza association.Request Body:
{
"price": 5,
"pizza_id": 1,
"restaurant_id": 1
}

Response (201):
{
"id": 4,
"price": 5,
"pizza_id": 1,
"restaurant_id": 1,
"pizza": {
"id": 1,
"name": "Margherita",
"ingredients": "Dough, Tomato Sauce, Cheese"
},
"restaurant": {
"id": 1,
"name": "Kiki's Pizza",
"address": "123 Main St"
}
}

Error (400):
{ "errors": ["Price must be between 1 and 30"] }

Validation Rules

RestaurantPizza.price: Must be an integer between 1 and 30.
restaurant_id and pizza_id in RestaurantPizza: Must reference existing records in the database.

Testing with Postman

Open Postman and import challenge-1-pizzas.postman_collection.json.
Ensure the server is running at http://localhost:5555.
Run each request in the collection to test the API endpoints.

Project Structure
pizza-api-challenge/
├── server/
│ ├── **init**.py
│ ├── app.py
│ ├── config.py
│ ├── models/
│ │ ├── **init**.py
│ │ ├── restaurant.py
│ │ ├── pizza.py
│ │ ├── restaurant_pizza.py
│ ├── controllers/
│ │ ├── **init**.py
│ │ ├── restaurant_controller.py
│ │ ├── pizza_controller.py
│ │ ├── restaurant_pizza_controller.py
│ ├── seed.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
├── README.md
