from flask import Blueprint, render_template, url_for, redirect, request, abort
from flask_login import login_required, current_user
from ..models.build_form import BuildArticleForm
from ..models.Article import Article
from ..models.User import User
from ..extensions import db
from datetime import date

admin_dashboard_blueprint = Blueprint("admin_dashboard_blueprint", __name__)


@admin_dashboard_blueprint.route("/admin/admin-dashboard")
@login_required
def admin_dashboard():
    if current_user.admin:
        page = request.args.get("page", 1, type=int)
        articles = Article.query.order_by(Article.id.desc()).paginate(
            page=page, per_page=6
        )
        return render_template("admin-dashboard.html", articles=articles)
    abort(401)


@admin_dashboard_blueprint.route(
    "/admin/admin-dashboard/create-article", methods=["GET", "POST"]
)
@login_required
def create_article():
    if current_user.admin:
        form = BuildArticleForm()
        if form.validate_on_submit():
            article = Article(
                course=form.course.data,
                topic=form.topic.data,
                body=form.body.data,
                date=date.today().strftime("%b %d, %Y"),
            )
            db.session.add(article)
            db.session.commit()
            return redirect(url_for("admin_dashboard_blueprint.admin_dashboard"))
        return render_template(
            "build-article.html",
            form=form,
            article_page_type="Create a Medical Article",
        )
    abort(401)


@admin_dashboard_blueprint.route(
    "/admin/admin-dashboard/edit-article/<article_id>/<article_topic>",
    methods=["GET", "POST"],
)
@login_required
def edit_article(article_id, article_topic):
    if current_user.admin:
        article = Article.query.get(article_id)
        form = BuildArticleForm(
            course=article.course, topic=article_topic, body=article.body
        )
        if form.validate_on_submit():
            article.course = form.course.data
            article.topic = form.topic.data
            article.body = form.body.data
            db.session.commit()
            return redirect(url_for("admin_dashboard_blueprint.admin_dashboard"))
        return render_template(
            "build-article.html", form=form, article_page_type="Edit Article"
        )
    abort(401)


@admin_dashboard_blueprint.route(
    "/admin/admin-dashboard/delete-article/<article_id>/<article_topic>"
)
@login_required
def delete_article(article_id,article_topic):
    if current_user.admin:
        article = Article.query.get(article_id)
        db.session.delete(article)
        db.session.commit()
        return redirect(url_for("admin_dashboard_blueprint.admin_dashboard"))
    abort(401)
