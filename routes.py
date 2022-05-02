from atexit import register
import os
from venv import create

from flask import Flask, render_template, request, jsonify, url_for, flash
from requests import session
from models import *
from views import *


app = create_app()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/user/<name>")
def user(name):
    return render_template('user.html', name=name)

@app.route("/name", methods=['GET','POST'])
def name():
    name = None
    form = UserForm()
    # validate
    if form.validate_on_submit():
       name = form.name.data
       form.name.data = ''
       flash("Form Submitted Successfully")
    return render_template('name.html', name=name, form=form)

@app.route("/delete/<int:id>")
def delete(id):
    user_del = User.query.get_or_404(id)
    name = None
    form = SignUp()
    try:
        db.session.delete(user_del)
        db.session.commit()
        message = "User {} deleted successfully".format(user_del.name)
        flash(message)
        curr_users = User.query.order_by(User.date_added)
        return render_template('deleted.html', form=form, name=name, curr_users=curr_users)
    except:
        flash("There was an issue deleting this user.")
        return render_template('register.html', form=form, name=name, curr_users=curr_users)


@app.route("/user/add", methods=['GET','POST'])
def add_user():
    name = None
    form = SignUp()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        user_pw = User.query.filter_by(email=form.email.data).first()

        form.name.data = ''
        form.email.data = ''
        form.location.data = ''
        form.password_hash.data = ''


        if user_pw is None:
            user = User(name = form.name.data, email=form.email.data, location=form.location.data)
            db.session.add(user)
            db.session.commit()
    
        flash("Sign up was successful")
    curr_users = User.query.order_by(User.date_added)
    return render_template('register.html', form=form, name=name, curr_users=curr_users)

@app.route("/update/<int:id>", methods=['GET','POST'])
def update(id):
    form = SignUp()
    name_change = User.query.get_or_404(id)
    if request.method == "POST":
        name_change.name = request.form['name']
        name_change.email = request.form['email']
        name_change.location = request.form['location']
        try:
            db.session.commit()
            flash("Update Successful")
            return render_template('update.html', form=form, name_change=name_change, id=id)
        except:
            flash("There was a problem updating the user.")
            return render_template('update.html', form=form, name_change=name_change, id=id)
    else:
        return render_template('update.html', form=form, name_change=name_change, id=id)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)

