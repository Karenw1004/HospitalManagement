# core/views.py

from flask import render_template,request,Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():
    # MORE TO COME!
    return render_template('index.html')

@core.route('/login')
def login():
    return render_template('login.html')
