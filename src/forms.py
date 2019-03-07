from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from .models import Category

class CompanyForm(FlaskForm):
    """
    """
    symbol = StringField('symbol', validators=[DataRequired()])


class CompanyAddForm(FlaskForm):
    """
    """
    symbol = StringField('symbol', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    categories = SelectField('categories')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.categories.choices = [(str(c.id), c.name) for c in Category.query.all()]


class CategoryCreateForm(FlaskForm):
    """
    """
    name = StringField('name', validators=[DataRequired()])
