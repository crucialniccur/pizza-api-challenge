from config import db
from sqlalchemy_serializer import SerializerMixin


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship(
        'RestaurantPizza', backref='restaurant', cascade='all, delete-orphan')

    serialize_rules = ('-restaurant_pizzas.restaurant',)

    def __repr__(self):
        return f'<Restaurant {self.name}>'
