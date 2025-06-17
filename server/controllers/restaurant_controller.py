from flask import Blueprint, jsonify, make_response
from config import db
from models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurant_bp', __name__)


@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()

    return jsonify([restaurant.to_dict() for restaurant in restaurants])


@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)

    if not restaurant:
        return jsonify({"error": 'an error occured, restaurant not found innit'}), 404
    return jsonify(restaurant.to_dict())
