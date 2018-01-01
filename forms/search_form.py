from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class SearchForm(FlaskForm):
    """SearchForm supports a single string field."""
    stringfield = StringField('StringField', description="Top `N` coins", validators=[InputRequired()])
