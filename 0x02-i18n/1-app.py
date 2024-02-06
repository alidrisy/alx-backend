#!/usr/bin/env python3
""" A basic Flask app """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ an object to configure the application """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """main route for our app"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
