from requests import Session
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


db = SQLAlchemy()
migrate = Migrate()

