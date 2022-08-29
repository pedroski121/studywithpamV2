from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class BuildArticleForm(FlaskForm):
    course = StringField(label="Course", validators=[DataRequired()])
    topic = StringField(label="Topic", validators=[DataRequired()])
    body = CKEditorField(label="Body", validators=[DataRequired()])
    submit = SubmitField(label="Submit")
