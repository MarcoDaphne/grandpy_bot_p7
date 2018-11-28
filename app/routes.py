#!/usr/bin/env python3
# Coding: utf-8


from flask import render_template
from flask import jsonify
from app import app
from app.forms import QueryForm
from grandpy.answer import Answer


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    if form.validate_on_submit():
        answer = Answer().answer_user_query(form.query.data)
        return jsonify(answer)
    return render_template(
        'index.html',
        form=form
    )