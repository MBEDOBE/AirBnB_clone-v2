#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """Displays a HTML page of states and cities"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
