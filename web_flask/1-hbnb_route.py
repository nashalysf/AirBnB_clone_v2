#!/usr/bin/python3

"""
Starts a Flask web app
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns hello at index"""
    return ("Hello HBNB!")

@app.route("/hbnb", strict_slashes=False):
def hhbnb():
    """returns hbnb at hbnb"""
    return ('HBNB')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
