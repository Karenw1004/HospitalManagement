import os
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
from HM.core.views import core
# from HM.users.views import users
from HM.error_pages.handlers import error_pages
from HM.database import *

# Initialisation
database().__init__
app = Flask(__name__)
app.config['TESTING'] = True


app.register_blueprint(core)
# app.register_blueprint(users)
app.register_blueprint(error_pages)




# @app.route('/')
# def login():

# from database import *
# from flask import Flask, render_template




# # Initialisation
# database().__init__
# app = Flask(__name__)


# @app.route('/')
# def login():
    
    