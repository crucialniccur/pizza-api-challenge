from config import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(
        'restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey(
        'pizzas.id'), nullable=False)

    serialize_rules = ('-restaurant.restaurant_pizzas',
                       '-pizza.restaurant_pizzas')

    @validates('price')
    def validate_price(self, key, price):
        if not 1 <= price <= 30:
            raise ValueError('Price must be between 1 and 30')
        return price

    def __repr__(self):
        return f'<RestaurantPizza ${self.price}>'
