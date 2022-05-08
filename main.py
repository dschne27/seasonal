from flask import Blueprint, render_template, flash
from flask_login import current_user, login_required
from numpy import full
from pandas import concat
from .models.user import User
from .extensions import db
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/home')
@login_required
def home():
    # message = "welcome {}".format(current_user.name)
    # flash(message)

    def location():

        full_loc = None

        URL = "http://ip-api.com/json/"
        loc = requests.get(URL)
        data = loc.json()  
        city = data["city"]
        reg_name = data["regionName"]
        country = data["country"]

        full_loc = city + ", " + reg_name + ", " + country

        return full_loc

    full_loc = location()

    return render_template('home.html', name=current_user.name, location=full_loc)

# @login_required
# def set_loc():


