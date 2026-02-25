from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Creat DB Connection
db = SQLAlchemy()
DB_NAME = "database.db"

# Create App
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'semicircle_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #Import Blueprint
    from .views import views
    from .auth import auth

    #Apply Blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Create or Import Database
    from .models import User, Note # from .models import *
    create_database(app)

    return app

# Create or Check Database file
def create_database(app):
    # check db file
    if not path.exists(f'diary/{DB_NAME}'):
        with app.app_context():
            db.create_all()
        print('>>> Create DB')
