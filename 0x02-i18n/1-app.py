#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """ index page """
    return render_template('0-index.html')


class Config:
    """ conig class """
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
