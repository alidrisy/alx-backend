#!/usr/bin/env python3
""" A basic Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union

app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ an object to configure the new application """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_user(id: Union[str, None]) -> Union[Dict, None]:
    """find a user if any"""
    return users.get(int(id))


@app.before_request
def before_request():
    """a user login system"""
    login_as = request.args.get('login_as')
    if login_as in users:
        setattr(g, "user", get_user(login_as))


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel = Babel(app, locale_selector=get_locale)

@app.route('/', strict_slashes=False)
def index() -> str:
    """main route for our app"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
