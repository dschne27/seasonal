from requests import Session
from models import *

from flask import Flask, render_template, request, jsonify, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Integer, Column, String, DateTime, text
from sqlalchemy.orm import declarative_base
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "p12W}!{Ohr"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Covington27!@localhost/seasonal_users'

    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)

    return app
