#!/usr/bin/python3
"""
Flask app with 2 routes
"""

from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def task4(n):
    """Route 5: /number/<n>: display “n is a number”
    only if n is an integer"""
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def task5(n):
    """ route 6: /number_template/<n>: display a HTML page only
    if n is an integer:  """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def task6(n):
    """ route 7: /number_odd_or_even/<n>: display a HTML page only
    if n is an integer:   """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
