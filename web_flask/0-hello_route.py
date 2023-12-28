#!/usr/bin/python3
"""
Flask app with 1 route
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def task1():
    """ Route 1 /: display “Hello HBNB!” """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
