#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """ conig class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.url_map.strict_slashes = False


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """ get user """
    return users.get(user_id)


@app.before_request
def before_request():
    """ before request """
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id) if user_id else None


@app.route('/')
def index():
    """ index page """
    return render_template('5-index.html')


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
