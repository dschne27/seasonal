
from flask import Flask, render_template, request, jsonify, url_for, flash
from datetime import timedelta
from .extensions import db, migrate
from .models.user import User
from .auth import auth
from .main import main
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "p12W}!{Ohr"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Covington27!@localhost/seasonal_users'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.permanent_session_lifetime = timedelta(minutes=30)

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(main)
    app.register_blueprint(auth)

    login_manager = LoginManager()
    # login_manager.session_protection = "strong"
    login_manager.login_view = "auth.login"
    # login_manager.refresh_view()
    login_manager.init_app(app)
    # login_manager.login_message_category = "info"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    return app
