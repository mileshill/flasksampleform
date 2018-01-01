from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
class SearchForm(FlaskForm):
    stringfield = StringField('StringField', description="Top `N` coins", validators=[InputRequired()])
