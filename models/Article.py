from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from ..extensions import db


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String)
    topic = db.Column(db.String)
    body = db.Column(db.String)
    date = db.Column(db.String)

class Comments(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    comment = db.Column(db.String, nullable=False)
    date = db.Column(db.String)
    article_id = db.Column(db.Integer,ForeignKey("article.id"))
    article = relationship("Article", foreign_keys=[article_id])