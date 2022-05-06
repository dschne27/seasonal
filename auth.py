from unicodedata import name
from argon2 import verify_password
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)
from werkzeug.security import generate_password_hash, check_password_hash

from .models.forms import RegistrationForm, LoginForm
from .models.user import User
from .extensions import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():

    form = LoginForm()
    return render_template('login.html', form=form)
            
@auth.route('/login', methods=['POST'])
def login_post():

    form = LoginForm()
    email = form.email.data
    pwd = form.password.data

    user = User.query.filter_by(email=email).first()
    if user and form.validate_on_submit():
        if user.verify_password(pwd):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Wrong password')
            return redirect(url_for('auth.login'))
    else:
        flash('No account associated with {}'.format(email))
        return redirect(url_for('auth.login'))


@auth.route('/register', methods=['POST'])
def signup_post():
    form = request.form

    email = form['email']

    user = User.query.filter_by(email=email).first()

    if user:
        flash("You already have an account with this email!")
        return redirect(url_for('auth.login'))
    else:
        reg_user = User(name = form['name'], email=form['email'], password_hash=generate_password_hash(form["password_hash"]))
        db.session.add(reg_user)
        db.session.commit()
        flash('Thanks for signing up!')
        return redirect(url_for('auth.login'))


@auth.route('/register',methods=['GET'])
def sign_up():
    form = RegistrationForm()
    return render_template('registration.html', form=form)

@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))