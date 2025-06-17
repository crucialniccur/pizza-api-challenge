from sqlalchemy import text
from server.extensions import db
from server.models import Restaurant, Pizza, RestaurantPizza
from server.app import app
from faker import Faker

faker = Faker()

def seed_data():
    with app.app_context():
        print("Truncating tables and resetting IDs...")
        db.session.execute(text('TRUNCATE restaurant_pizzas RESTART IDENTITY CASCADE;'))
        db.session.execute(text('TRUNCATE restaurants RESTART IDENTITY CASCADE;'))
        db.session.execute(text('TRUNCATE pizzas RESTART IDENTITY CASCADE;'))
        db.session.commit()

        print("Seeding restaurants and pizzas...")

        restaurants = [Restaurant(name=faker.company(), address=faker.address()) for _ in range(5)]
        pizzas = [Pizza(name=faker.word().capitalize() + " Pizza", ingredients=", ".join(faker.words(3))) for _ in range(8)]

        db.session.add_all(restaurants)
        db.session.add_all(pizzas)
        db.session.commit()  # Commit to assign IDs

        restaurant_pizzas = []
        for r in restaurants:
            sampled_pizzas = faker.random_choices(elements=pizzas, length=faker.random_int(min=2, max=4))
            for p in sampled_pizzas:
                price = round(faker.random_number(digits=2) / 10 + 5, 2)
                restaurant_pizzas.append(RestaurantPizza(price=price, restaurant_id=r.id, pizza_id=p.id))

        db.session.add_all(restaurant_pizzas)
        db.session.commit()
        print("Seeding done.")

if __name__ == '__main__':
    seed_data()
