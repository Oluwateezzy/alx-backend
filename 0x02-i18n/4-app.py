#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ conig class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """ index page """
    return render_template('3-index.html')


@babel.localeselector
def get_locale() -> str:
    """ retrieve the locale """
    requested_locale = request.args.get('locale')
    if requested_locale in app.config['LANGUAGES']:
        return requested_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
