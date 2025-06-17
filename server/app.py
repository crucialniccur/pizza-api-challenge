from server.models import restaurant, pizza, restaurant_pizza
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config


app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

# importing models

if __name__ == '__main__':
    app.run(debug=True)
