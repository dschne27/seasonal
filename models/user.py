from email.policy import default
from enum import unique
import os
from xmlrpc.client import DateTime
from attr import validate

from flask_login import UserMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, create_engine, Integer, Column, String, DateTime, text
from werkzeug.security import generate_password_hash, check_password_hash

from ..extensions import db

# EqualTo('confirm_pwd', message="Passwords must match!")]

class User(db.Model, UserMixin):

    __tablename__ = 'usernames'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique = True)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)
    location  = db.Column(db.String(200))
    password_hash = db.Column(db.String(128))
    watching = db.relationship('Watch', backref='voi')
    

    # @property
    # def password(self):
    #     raise AttributeError("Password is not a readable attribute!")
    # @password.setter
    # def password(self, password):
    #     self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_name(self):
        return self.name

class Watch(db.Model):

    __tablename__ = 'watch'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable=False)
    location  = db.Column(db.String(200))
    veg_id = db.Column(db.Integer, db.ForeignKey('veg.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('usernames.id'))



class Veg(db.Model):

    __tablename__ = 'veg'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    status = db.Column(db.String(200))
    interest = db.relationship('Watch', backref='vegetable')
