from flask_wtf import Form
from wtforms import StringField, DateTimeField, TextAreaField, IntegerField
from wtforms.validators import DataRequired

class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    date = DateTimeField('Date', format='%m/%d/%Y', validators=[DataRequired()])
    time_spent = IntegerField('Time Spent', validators=[DataRequired()])
    things_learned = TextAreaField("What You Learned", validators=[DataRequired()])
    resources = TextAreaField("Resources to Remember", validators=[DataRequired()])
