import os
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from HM.users.views import users
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
  def __init__(self, doctor_id, password, address, is_at_work):
    self.doctor_id = doctor_id
    self.password = password
    self.address = address
    self.is_at_work = is_at_work

# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid)

from HM.core.views import core
app.register_blueprint(core)
# app.register_blueprint(users)
from HM.error_pages.handlers import error_pages
app.register_blueprint(error_pages)
