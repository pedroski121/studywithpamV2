from flask import Blueprint, render_template

error_blueprint = Blueprint("error_blueprint", __name__)


@error_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error="Page Not Found")


@error_blueprint.app_errorhandler(401)
def unauthorized(e):
    return render_template(
        "error.html", error="You are unauthorized to access this route"
    )


@error_blueprint.app_errorhandler(500)
def forbidden(e):
    return render_template(
        "error.html", error="The server encountered some errors"
    )

@error_blueprint.app_errorhandler(413)
def forbidden(e):
    return render_template(
        "error.html", error="File is too large"
    )

@error_blueprint.app_errorhandler(400)
def forbidden(e):
    return render_template(
        "error.html", error="Invalid Image"
    )