from flask import Blueprint, render_template, redirect, url_for

home_blueprint = Blueprint("home_blueprint", __name__)


@home_blueprint.route("/")
def home():
    # return render_template("index.html")
    return redirect(url_for("view_articles_blueprint.view_articles"))
