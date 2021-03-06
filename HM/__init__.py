import os
from flask import Flask, render_template

app = Flask(__name__)
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key= "KEYISRANDOM"

from HM.blueprints.auth import auth
app.register_blueprint(auth)
from HM.blueprints.doctor import doctor
app.register_blueprint(doctor)
from HM.blueprints.patient import patient
app.register_blueprint(patient)
from HM.error_pages.handlers import error_pages
app.register_blueprint(error_pages)
