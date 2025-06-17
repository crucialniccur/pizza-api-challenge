from flask import Blueprint, jsonify, make_response
from config import db
from models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurant_bp', __name__)


@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()

    return jsonify([restaurant.to_dict() for restaurant in restaurants])
