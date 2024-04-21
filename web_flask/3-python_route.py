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


@app.route("/c/<text>", strict_slashes=False)
def hbnb_text(text):
    """ display C with a given input """
    out_put = "C {}".format(text)
    return out_put.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """ display C with a given input """
    if text == "is cool":
       return "Pyhton {}".format(text)
    else:
        out_put = "Python {}".format(text)
        return out_put.replace("_", " ")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
