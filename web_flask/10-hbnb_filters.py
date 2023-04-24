#!/usr/bin/env python3
"""
Starts a Flask web application
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def index_html_6():
    """Displays a html page like 6-index.html."""
    states_list = storage.all(State)
    amenities_list = storage.all(Amenity)
    return render_template(
            '10-hbnb_filters.html', states=states_list, amenities=amenities_list)


@app.teardown_appcontext
def close_session(exception=None):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
