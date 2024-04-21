#!/usr/bin/python3
"""
description about this folder
start a flask application with ip 0.0.0.0
"""
from flask import Flask, render_template


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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """ display C with a given input """
    out_put = "Python {}".format(text)
    return out_put.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number_text(n):
    """ display C with a given input """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_text_html(n):
    """ display C with a given input """
    return render_template("5-number.html", var=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even_number(n):
    """ display C with a given input """
    return render_template("6-number_odd_or_even.html", var=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
