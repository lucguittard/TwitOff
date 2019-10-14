"""Main application for twitoff"""

#imports 
from flask import Flask
from.models import DB

# create app factory
def create_app():
    """Creates and configs an instance of a flask app"""
    app = Flask(__name__)

    # configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
    DB.init_app(app)

    @app.route("/")
    def root():
        return "Welcome"
    return app
