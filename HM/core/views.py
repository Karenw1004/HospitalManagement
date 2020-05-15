# core/views.py

from flask import flash, request, Blueprint, render_template, redirect, session, flash, url_for
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
    if (request.method == "POST"):
        username = request.form["username"]
        password = request.form["password"]

        result = db.login(username, password)
        if (result != False):
            session['username'] = result[0][1]
            session['password'] = result[0][2]
            session['name']= result[0][3]
            flash('You were successfully logged in','success')
            return redirect(url_for('core.dashboard'))
        else:
            flash('Invalid credentials','error')
            return render_template('login.html') 
    else:
        return render_template('login.html')

@core.route('/register',methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")

        username = request.form.get("username").lower()
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if (password1 != password2):
            flash('Password do not match','error')
            return render_template('register.html')
        else:
            flash(f'User {username} has been successfully created','success')
            return redirect(url_for('core.login'))

    else:
        print("lol")
        return render_template('register.html')


@core.route('/logout')
def logout():
    session.clear()
    return render_template("login.html", data={"success": "You have logged out"})


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
        data = db.get_all_patient_info_list()
        return render_template('patient.html', data=data)
    else:
        return redirect("/login")