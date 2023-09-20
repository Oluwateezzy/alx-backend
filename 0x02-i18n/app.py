#!/usr/bin/env python3
""" Basic flask app """
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime


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
    g.time = format_datetime()
    return render_template('index.html')


@babel.localeselector
def get_locale() -> str:
    '''Retrieves the locale for a web page.
    '''
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    locale = query_table.get('locale', '')
    # locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """ timezone """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
