#! /usr/bin/python

from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
