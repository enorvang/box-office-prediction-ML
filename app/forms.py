from flask_wtf import FlaskForm
from wtforms import BooleanField, FloatField, IntegerField, RadioField, SelectField, SelectMultipleField, StringField, SubmitField, widgets
from wtforms.validators import DataRequired, NumberRange

genre_choices = [("1", "Drama"), ("2", "Comedy"), ("3", "Thriller"), ("4", "Action"),
                 ("5", "Romance"), ("6", "Crime"), ("7", "Adventure"), ("8", "Horror"),
                 ("9", "Science Fiction"), ("10", "Family"), ("11", "Fantasy"), ("12", "Mystery"),
                 ("13", "Animation"), ("14", "History"), ("15", "Music"), ("16", "War"), ("17", "Documentary"),
                 ("18", "Western"), ("19", "Foreign")]


class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class DataForm(FlaskForm):

    """
    The form for entering values for a movie. 
    """

    budget = FloatField('Total budget', validators=[DataRequired()])
    runtime = FloatField('Runtime (minutes)', validators=[
                         DataRequired(), NumberRange(min=10, max=500)])

    has_collection = IntegerField(
        'Belongs to collection?. 0=No, 1=Yes', validators=[NumberRange(min=0, max=1)])
    has_homepage = IntegerField('Homepage?. 0=No, 1=Yes', validators=[
                                NumberRange(min=0, max=1)])
    original_language_is_english = IntegerField(
        'English original language?. 0=No, 1=Yes', validators=[NumberRange(min=0, max=1)])
    #no_of_genres = IntegerField('Number of genres?. 1 - 7', validators=[NumberRange(min=1, max=7)])
    no_of_production_companies = IntegerField(
        'Number of prod. companies. 1 - 12', validators=[NumberRange(min=1, max=12)])
    genres_checkbox = MultiCheckboxField("Genres", choices=genre_choices, render_kw={
                                         'style': 'height: fit-content; width: fit-content; list-style: none;'})

    submit = SubmitField('Submit')
