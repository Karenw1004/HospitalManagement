# core/views.py

from flask import flash, request, Blueprint, render_template, redirect, session
# from flask_login import LoginManager, login_user, logout_user, login_required
# from collections import defaultdict
# import traceback
from HM.database import *

core = Blueprint('core',__name__)
db = database()

def is_logged_in(): 
    if 'username' in session:
        return True
    else:
        return False
@core.route('/')
def index():
    return render_template('index.html')

@core.route('/login', methods=['GET','POST'])
def login():
    error = None
    if (request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]

        result = db.login(username, password)
        if (result != False):
            session['username'] = result[0][1]
            session['password'] = result[0][2]
            session['name']= result[0][3]
            session['is_logged_in'] = True
            return redirect('/dashboard')
        else:
            error = "Invalid credentials"
            return render_template('login.html', error=error)

        
    else:
        return render_template('login.html', error=error)

@core.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if (is_logged_in()):
        count_dict = database().number_dict()
        return render_template('dashboard.html', count_dict=count_dict,username=session['username'])
    else:
        return redirect("/login")


@core.route('/patient')
def patients():
    if (is_logged_in()):
        return render_template('patient.html')
    else:
        return redirect("/login")