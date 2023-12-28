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


@app.route("/c/<text>", strict_slashes=False)
def task2(text):
    """ Route 3: /c/<text>: display “C ” followed by the value of the
    text variable (replace underscore _
    symbols with a space )
    """
    formated_text = text.replace('_', ' ')
    return 'C {}'.format(formated_text)


@app.route("/python", strict_slashes=False, defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def task3(text):
    """ Route 4:  /python/<text>: display “Python ”,
    followed by the value of the text variable (replace underscore _
    symbols with a space )
    The default value of text is “is cool”
    """
    formated_text = text.replace('_', ' ')
    return 'Python {}'.format(formated_text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
