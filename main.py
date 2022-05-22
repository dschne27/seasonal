from crypt import methods
from datetime import datetime
from flask import Blueprint, render_template, flash, request
from flask_login import current_user, login_required
from numpy import full
from pandas import concat
from .models.user import User, Watch
from .extensions import db
import requests
from bs4 import BeautifulSoup

main = Blueprint('main', __name__)

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():

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

    veglist = None

    def get_watching():
        veglist = Watch.query.filter_by(user_id=current_user.id).first()
        return veglist

    veglist = get_watching()

    if request.method == "POST":
        user = User.query.filter_by(id=current_user.id).first()
        if request.form:
            loc = request.form['geocomplete']
            user.location = loc
            db.session.commit()
            return render_template('home.html', location=full_loc)
        user.location = full_loc
        db.session.commit()
    
    

    return render_template('home.html', location=full_loc, user_watches=veglist)

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

    veglist = None

    def get_watching():
        veglist = Watch.query.filter_by(user_id=current_user.id).first()
        return veglist

    veglist = get_watching()

    def get_season():

        current_month = datetime.now().month
        if current_month >= 1 and current_month <= 3:
            return "winter"
        elif current_month >= 4 and current_month < 6:
            return "spring" 
        elif current_month >= 6 and current_month < 9:
            return "summer"
        else:
            return "fall"

    month = get_season()

    def load_products():
        seasonal_data = requests.get("https://snaped.fns.usda.gov/seasonal-produce-guide")
        soup = BeautifulSoup(seasonal_data.content, "html.parser")
        veg_list = []
        content = soup.find("div", class_=month)
        ul = content.find("ul")
        li = ul.find_all("li")

        for veg in li:
            veg_list.append(veg.text)

        return veg_list


    products = load_products()

    return render_template('profile.html', user_watches=veglist, seasonal_list=products, len=len(products))

# @main.route('/profile')
# @login_required



    # state = current_user.location.str.split()[1]

    # KEY = "FDB8665F-92A7-3198-B404-1DD0D963B70E"
    # URL = "http://quickstats.nass.usda.gov/api/api_GET/?key={}&state_name={}".format(KEY, state)

    # data = requests.get(URL)
    # json = data.json()

