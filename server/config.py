import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(os.path.dirname(os.path.dirname(__file__)),
                     'pizza_restaurant.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
