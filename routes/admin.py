from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user
from datetime import date
from sqlalchemy import exc
from ..extensions import db
from ..models.User import User


admin_blueprint = Blueprint("admin_blueprint", __name__)


@admin_blueprint.route("/admin", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pswd"]
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(pwhash=user.password, password=password):
                login_user(user)
                return redirect(url_for("admin_dashboard_blueprint.admin_dashboard"))
            else:
                flash("Incorrect username or password")
                return redirect(url_for("admin_blueprint.sign_in"))
    return render_template("admin-sign-in.html")


def create_user(route, redirect_link="admin_dashboard_blueprint.admin_dashboard"):
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        user = User.query.filter_by(email=email).first()
        if user:
            user.admin = True
            db.session.commit()
            return redirect(url_for("admin_dashboard_blueprint.admin_dashboard"))
        password = request.form["pswd"]
        password_hashed = generate_password_hash(
            password=password, method="pbkdf2:sha256", salt_length=8
        )
        today = date.today().strftime("%b %d, %Y")
        new_user = User(
            name=name,
            email=email,
            password=password_hashed,
            date_of_creation=today,
            admin=True,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for(redirect_link))
        except exc.IntegrityError:
            flash("Email address already registered")
    return render_template("admin-sign-up.html", route=route)


@admin_blueprint.route("/admin/create-new-admin", methods=["GET", "POST"])
@login_required
def sign_up():
    return create_user("/admin/create-new-admin")


@admin_blueprint.route("/admin/first-user", methods=["GET", "POST"])
def first_user():
    users = User.query.all()
    if len(users) == 0:
        return create_user("/admin/first-user")
    return "Sorry you are not the first user"
