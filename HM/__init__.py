import os
from flask import Flask, render_template

app = Flask(__name__)
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key= "KEYISRANDOM"

from HM.core.views import core
app.register_blueprint(core)
# app.register_blueprint(users)
from HM.error_pages.handlers import error_pages
app.register_blueprint(error_pages)
