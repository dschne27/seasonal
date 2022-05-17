from crypt import methods
from flask import Blueprint, render_template, flash, request
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

@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    # message = "welcome {}".format(current_user.name)
    # flash(message)
    full_loc = None

    def location():

        URL = "http://ip-api.com/json/"
        loc = requests.get(URL)
        data = loc.json()  
        city = data["city"]
        reg_name = data["regionName"]
        # country = data["country"]

        full_loc = city + ", " + reg_name

        return full_loc

    full_loc = location()

    if request.method == "POST":
        user = User.query.filter_by(id=current_user.id).first()
        if request.form:
            loc = request.form['geocomplete']
            user.location = loc
            db.session.commit()
            return render_template('home.html', location=full_loc)
        user.location = full_loc
        db.session.commit()
        return render_template('home.html', location=full_loc)
    else:
        return render_template('home.html', location=full_loc)

# @main.route('/home', methods=['POST'])
# @login_required
# def edit_loc():
#     user = User.query.filter_by(id=current_user.id).first()
#     loc = request.form['geocomplete']
#     user.location = loc
#     db.session.commit()

#     return render_template('home.html', location_in=loc)

@main.route('/profile')
@login_required
def load_profile():


    return render_template('dashboard.html')



