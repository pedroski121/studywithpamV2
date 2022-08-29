from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date
from ..models.User import User
from ..models.security_form import SignUpForm, SignInForm
from ..extensions import db
from flask_login import login_user,login_required,logout_user
from sqlalchemy import exc


security_blueprint = Blueprint("security_blueprint", __name__)


@security_blueprint.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        password_hashed = generate_password_hash(
            password=password, method="pbkdf2:sha256", salt_length=8
        )
        today = date.today().strftime("%b %d, %Y")
        new_user = User(
            name=name,
            email=email,
            password=password_hashed,
            date_of_creation=today,
            admin=False,
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for("view_articles_blueprint.view_articles"))
        except exc.IntegrityError:
            flash("Email address already registered")
    return render_template("sign-up.html", form=form)




@security_blueprint.route("/sign-in", methods=["GET","POST"])
def sign_in():
    form = SignInForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(pwhash=user.password, password=password):
                login_user(user)
                return redirect(url_for("view_articles_blueprint.view_articles"))
            else:
                flash("Incorrect email or password")
                return redirect(url_for("security_blueprint.sign_in"))
    return render_template("sign-in.html", form=form)



@security_blueprint.route("/sign-out", methods=["GET", "POST"])
@login_required
def sign_out():
    logout_user()
    return redirect(url_for("home_blueprint.home"))
