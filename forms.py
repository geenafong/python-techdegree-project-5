from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    date = DateTimeField('Date, ex: 03/05/2020', format='%m/%d/%Y', validators=[DataRequired()])
    time_spent = IntegerField('Time Spent(in hours)', validators=[DataRequired()])
    things_learned = TextAreaField("What You Learned", validators=[DataRequired()])
    resources = TextAreaField("Resources to Remember", validators=[DataRequired()])
