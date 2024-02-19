#!/usr/bin/python3
"""a script that starts a flask application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """returns a page"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities,
        places=places
    )


@app.teardown_appcontext
def close_database(arg):
    """closes the current database"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
