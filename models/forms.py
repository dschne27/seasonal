from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from datetime import datetime

class RegistrationForm(FlaskForm):
    name = StringField('Full Name: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    location = StringField('Current Location: ', validators=[DataRequired()], default=None)
    password_hash = PasswordField('Create a Password: ', validators=[DataRequired()])
    confirm_pwd = PasswordField('Confirm Password: ')
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')