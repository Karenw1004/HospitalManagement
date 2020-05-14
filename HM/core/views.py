# core/views.py

from flask import flash, request, Blueprint, Response, abort, render_template, redirect, jsonify
# from flask_login import LoginManager, login_user, logout_user, login_required
# from collections import defaultdict
# import traceback
from HM.database import *

core = Blueprint('core',__name__)


@core.route('/')
def index():
    return render_template('index.html')

@core.route('/login', methods=['GET','POST'])
def login():
    error = None
    if (request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]

        is_logged_in = database().login(username, password)
        if (is_logged_in):
            count_dict = database().number_dict()
            return render_template('dashboard.html', count_dict=count_dict,username=username)
        else:
            error = "Invalid credentials"
            return render_template('login.html', error=error)

        
    else:
        return render_template('login.html', error=error)
