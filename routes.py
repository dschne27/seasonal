from atexit import register
from email import message
import os
from venv import create


from flask import Flask, render_template, request, jsonify, url_for, flash, redirect, Blueprint
from requests import session
from .models.user import User
from .extensions import db

# @app.route("/")
# def index():
    
#     return render_template('index.html')


# @app.route("/home", methods=["GET", "POST"])
# def home():
#     return render_template('home.html')

# @app.route("/login", methods=["GET", "POST"])
# def login():

#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user.verify_password(form.password.data):

#             login_user(user)

#             flash("Welcome {}!".format(user.name))

#             return render_template(url_for('home')) 
#         else:
#             flash("Invalid email or password")
            
#     return render_template('login.html')

# @app.route("/register", methods=["GET", "POST"])
# def signup():

#     form = RegistrationForm(request.form)

#     if request.method == 'POST' and form.validate():

#         user_pw = User.query.filter_by(email=form.email.data).first()

#         if user_pw is None:
#             hashed_pass = generate_password_hash(form.password_hash.data)
#             user = User(name = form.name.data, email=form.email.data, location=form.location.data, 
#                                                 password=hashed_pass)
#             db.session.add(user)
#             db.session.commit()

#             message = 'Thanks for signing up, {}'.format(user.name)

#             flash(message)

#             return redirect(url_for('home'))
#         else:
#             message = 'User {} already exists!'.format(user.name)
#             flash(message)
#             return redirect(url_for('index'))
#     # message = 'Oops'
#     # flash(message)
#     # return render_template('registration.html', form=form)


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404

# if __name__ == "__main__":
#     db.create_all(app=create_app())
#     app.run(debug=True)

