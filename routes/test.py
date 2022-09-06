from flask import Blueprint, render_template, redirect, url_for

test_blueprint = Blueprint("test_blueprint", __name__)


@test_blueprint.route("/test-suite")
def test():
    return render_template('test-suite.html')
