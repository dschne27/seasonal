from flask import Blueprint, render_template
from flask_login import login_required
from .models.user import User
from .extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def index():

    # user = User(name='Daniel', email='email@email.com', password_hash='pass')
    # db.session.add(user)
    # db.session.commit()

    return render_template('index.html')

@login_required
@main.route('/home')
def home():
    return render_template('home.html')