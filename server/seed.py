import sys
import os
from faker import Faker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.extensions import db
from server.models import Restaurant, Pizza, RestaurantPizza

faker = Faker()

def seed_data():
    with app.app_context():
        # Clean existing data safely (no drop_all)
        print("Cleaning existing data...")
        RestaurantPizza.query.delete()
        Pizza.query.delete()
        Restaurant.query.delete()
        db.session.commit()

        print("Seeding restaurants and pizzas...")

        # Create some random restaurants
        restaurants = [
            Restaurant(name=faker.company(), address=faker.address())
            for _ in range(5)
        ]
        db.session.add_all(restaurants)

        # Create some random pizzas
        pizzas = [
            Pizza(name=faker.word().capitalize() + " Pizza", ingredients=", ".join(faker.words(3)))
            for _ in range(8)
        ]
        db.session.add_all(pizzas)
        db.session.commit()  # Commit so IDs get assigned

        print(" Seeding RestaurantPizza prices...")

        # Create RestaurantPizza relationships with random prices
        restaurant_pizzas = []
        for _r in restaurants:
            # Each restaurant gets 2-4 pizzas with random prices
            sampled_pizzas = faker.random_choices(elements=pizzas, length=faker.random_int(min=2, max=4))
            for _p in sampled_pizzas:
                price = round(faker.random_number(digits=2, fix_len=False) / 10 + 5, 2)  # Price between 5 and ~15
                restaurant_pizzas.append(
                    RestaurantPizza(price=price, restaurant_id=_r.id, pizza_id=_p.id)
                )
        db.session.add_all(restaurant_pizzas)
        db.session.commit()

        print("Database seeded successfully with  data")

if __name__ == '__main__':
    from server.app import app
    with app.app_context():
        seed_data()
