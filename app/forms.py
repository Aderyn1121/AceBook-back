from flask_wtf import FlaskForm
from wtforms.fields import (
    DateField, StringField, IntegerField, SelectField,
    BooleanField, SubmitField
)
from wtforms.validators import DataRequired

choices = [('Other', "Other"), ("String", "String"), ("Woodwind", "Woodwind"), ("Brass", "Brass"), ("Percussion", "Percussion")]


class NewInstrument(FlaskForm):
    date_bought = DateField("Date Bought", [DataRequired()])
    nickname = StringField("Nickname", [DataRequired()])
    year = IntegerField("Year")
    maker = StringField("Maker")
    type = SelectField("Type", choices=choices)
    used = BooleanField("Used")
    submit = SubmitField("Submit")
