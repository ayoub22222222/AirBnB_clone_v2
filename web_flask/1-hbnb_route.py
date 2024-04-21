#!/usr/bin/python3
"""
description about this folder
start a flask application with ip 0.0.0.0
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """ display hello hbnb """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display hbnb """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
