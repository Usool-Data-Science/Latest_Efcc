#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from flask import Flask
from dotenv import load_dotenv

# Extension importation
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

# Custom modules
from api.v1.views import app_views

# Import Environment Variables
load_dotenv()

# App Creation
app = Flask(__name__)
app.register_blueprint(app_views)
app.config["SECRET_KEY"] = getenv('APP_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_efcc.db'
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.app_context().push()


# Extension Instantiation
admin = Admin()
bcrypt = Bcrypt()
db = SQLAlchemy(app)
login_manager = LoginManager()

# Extension Initializaiton
admin.init_app(app)
bcrypt.init_app(app)
# db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'app_views.login'
login_manager.login_message_category = 'info'

# with app.app_context():
#     db.create_all()

# Add a new view to the admin page
from models.staff import Staff
admin.add_view(ModelView(Staff, db.session))

# Handle user retrieval with login manager
@login_manager.user_loader
def load_user(user_id):
    """
        Retrieves user with a particular ID, It however expect our user model
        to have the following 4 attributes at least:
        1. is_authenticated: returns true if the user provided valid credentials
        2. is_active 3. is_anonymous 4.get_id()
            All these are available in flask_login and its called UserMixin.
            So ensure the Staff model is inheriting from UserMixin to get these
            four attributes
    """
    return Staff.query.get(int(user_id))
