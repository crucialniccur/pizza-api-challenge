from flask import Flask
from server.config import Config
from server.extensions import db, migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

# Import models after db initialization to avoid circular import
from server.models import restaurant, pizza, restaurant_pizza  # isort: skip

if __name__ == '__main__':
    app.run(debug=True)
