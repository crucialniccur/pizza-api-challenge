import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.extensions import db
from server.models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    # Drop and recreate tables
    db.drop_all()
    db.create_all()

    # Seed Restaurants
    r1 = Restaurant(name="Pizza Palace", address="123 Main St")
    r2 = Restaurant(name="Slice Heaven", address="456 Oak Ave")
    db.session.add_all([r1, r2])

    # Seed Pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    db.session.add_all([p1, p2])

    # Commit to ensure IDs are assigned
    db.session.commit()

    # Seed RestaurantPizzas
    rp1 = RestaurantPizza(price=12.99, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=14.99, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=11.99, restaurant_id=r2.id, pizza_id=p1.id)
    db.session.add_all([rp1, rp2, rp3])

    # Final commit
    db.session.commit()
    print("Database seeded successfully!")

if __name__ == '__main__':
    # Initialize app context for db
    from server.app import app
    with app.app_context():
        seed_data()
