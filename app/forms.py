#!/usr/bin/env python3
# Coding: utf-8


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    query = StringField('Bonjour mon enfant, que cherches tu ?', validators=[DataRequired()])
    submit = SubmitField('Soumettre')