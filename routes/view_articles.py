from flask import Blueprint, redirect, url_for, render_template, request, abort, flash
from datetime import date

from flask_login import current_user
from ..models.Article import Article, Comments
from ..models.comment_form import CommentForm
from ..extensions import db

view_articles_blueprint = Blueprint("view_articles_blueprint", __name__)


@view_articles_blueprint.route("/articles")
def view_articles():
    page = request.args.get("page", 1, type=int)
    articles = Article.query.order_by(Article.id.desc()).paginate(page=page, per_page=6)
    return render_template("view-articles.html", articles=articles)


@view_articles_blueprint.route(
    "/articles/<article_id>/<article_topic>", methods=["GET", "POST"]
)
def view_article_content(article_id, article_topic):
    article = Article.query.get(article_id)
    comments = Comments.query.filter_by(article_id=article.id).all()
    form = CommentForm()
    if current_user.is_authenticated:
        form =CommentForm(name=current_user.name, email=current_user.email)
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        if current_user.is_authenticated:
            if name != current_user.name or email != current_user.email:
                flash("Make sure your email address is the same as that registered with this account")
                return redirect(
                    url_for(
                        "view_articles_blueprint.view_article_content",
                        article_id=article_id,
                        article_topic=article_topic,
                    ),
                )

        comment = Comments(
                name=name,
                email=email,
                comment=form.comment.data,
                date=date.today().strftime("%b %d, %Y"),
                article=article,
            )
        db.session.add(comment)
        db.session.commit()
        return redirect(
            url_for(
                "view_articles_blueprint.view_article_content",
                article_id=article_id,
                article_topic=article_topic,
            )
        )
    return render_template(
        "view-article-content.html", article=article, form=form, comments=comments
    )
