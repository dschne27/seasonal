from email.policy import default
from enum import unique
import os
from xmlrpc.client import DateTime
from attr import validate

from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Integer, Column, String, DateTime, text
from werkzeug.security import generate_password_hash, check_password_hash

from views import db

class SignUp(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    location = StringField('Current Location: ', validators=[DataRequired()])
    password_hash = PasswordField('Create a Password: ', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UserForm(FlaskForm):
    name = StringField('Enter your name.', validators=[DataRequired()])
    submit = SubmitField('Submit')

class User(db.Model, UserMixin):

    __tablename__ = 'usernames'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique = True)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    location  = db.Column(db.String(200))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute!")
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Name %r' % self.name
