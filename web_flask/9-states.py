#!/usr/bin/env python3
"""
Flask web application that displays States and Cities
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_states():
    """Displays a list of all State objects"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_state(id):
    """Displays a State object and its Cities"""
    state = storage.get(State, id)
    if state is None:
        return render_template('9-not_found.html')
    cities = sorted(state.cities, key=lambda c: c.name)
    return render_template('9-state.html', state=state, cities=cities)


@app.teardown_appcontext
def close_session(response_or_exc):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
