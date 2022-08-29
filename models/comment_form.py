from xml.etree.ElementTree import Comment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Email
from flask_ckeditor import CKEditorField

class CommentForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    comment = CKEditorField(label="Comment", validators=[DataRequired()])
    submit = SubmitField(label="Comment")

