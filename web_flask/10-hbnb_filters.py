#!/usr/bin/env python3
"""
Starts a Flask web application
"""

from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_hbnb_filters():
    """Displays a HTML page like 6-index.html with updated files and data"""
    states = sorted(storage.all('State').values(), key=lambda s: s.name)
    amenities = sorted(storage.all('Amenity').values(), key=lambda a: a.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
