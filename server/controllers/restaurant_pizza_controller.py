from flask import Blueprint, jsonify, request
from server.config import db
from models.restaurant_pizza import RestaurantPizza
from models.restaurant import Restaurant
from models.pizza import Pizza
from sqlalchemy.exc import IntegrityError

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)


@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        restaurant_pizza = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(restaurant_pizza)
        db.session.commit()
        response = restaurant_pizza.to_dict()
        response['pizza'] = Pizza.query.get(data['pizza_id']).to_dict()
        response['restaurant'] = Restaurant.query.get(
            data['restaurant_id']).to_dict()
        return jsonify(response), 201
    except (ValueError, IntegrityError) as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]}), 400
