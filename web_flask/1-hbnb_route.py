#!/usr/bin/python3
"""
Flask app with 2 routes
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def task0():
    """ Route 1:  /: display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def task1():
    """ Route 2:  /hbnb: display “HBNB”"""
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
