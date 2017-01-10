from flask import render_template, flash, redirect, url_for

## import the blueprint from the init file
from app.main_app import mod


@mod.route('/', methods=['GET'])
def home():
    """
    Return a greeting on the main page.
    """

    greeting = 'Welcome to the coding test!'

    return render_template('main_app/home.html', greeting=greeting)