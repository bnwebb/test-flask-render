from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UserSubmitForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    submit = SubmitField('Submit')