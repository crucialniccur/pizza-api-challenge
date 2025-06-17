from config import db, app
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza

with app.app_context():
    print("Clearing database innit...")
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    print("Seeding restaurants...")
    restaurants = [
        Restaurant(name="Mati's Pizza", address="123 Saika Street"),
        Restaurant(name="Muindi's Pizzeria", address="456 Kayole Avenue"),
    ]
    db.session.bulk_save_objects(restaurants)

    print("Seeding pizzas...")
    pizzas = [
        Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese"),
        Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
    ]
    db.session.bulk_save_objects(pizzas)
    db.session.commit()

    print("Seeding restaurant_pizzas...")
    restaurant_pizzas = [
        RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
        RestaurantPizza(price=12, restaurant_id=1, pizza_id=2),
        RestaurantPizza(price=11, restaurant_id=2, pizza_id=1),
    ]
    db.session.bulk_save_objects(restaurant_pizzas)
    db.session.commit()

    print("Done seeding!")
