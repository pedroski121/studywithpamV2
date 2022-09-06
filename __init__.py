from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
import os
from .extensions import db
from .routes.home import home_blueprint
from .routes.admin import admin_blueprint
from .routes.admin_dashboard import admin_dashboard_blueprint
from .routes.view_articles import view_articles_blueprint
from .routes.test_suite import test_blueprint
from .routes.error import error_blueprint
from .routes.security import security_blueprint
from .routes.upload_image import upload_image_blueprint
from .models.User import User


def create_app():
    app = Flask(__name__)
    # SQLALCHEMY INITIAL CONFIG
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///swp_database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # CKEDITOR INITIAL CONFIG
    app.config["CKEDITOR_HEIGHT"] = 300
    # FILE UPLOAD INITIAL CONFIG
    app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
    app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png", ".gif"]
    app.config["UPLOAD_PATH"] = os.path.join(
        os.getcwd(), "studywithpamV2", "static", "uploads"
    )

    app.secret_key = "swp"
    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(admin_dashboard_blueprint)
    app.register_blueprint(view_articles_blueprint)
    app.register_blueprint(error_blueprint)
    app.register_blueprint(test_blueprint)
    app.register_blueprint(security_blueprint)
    app.register_blueprint(upload_image_blueprint)
    Bootstrap(app)
    ckeditor = CKEditor(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    db.init_app(app)
    return app
