#!/usr/bin/python3
"""
displays list of states
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """displays cities by a state on an HTML template"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown(self):
    """remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

