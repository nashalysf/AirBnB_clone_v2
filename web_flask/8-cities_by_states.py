#!/usr/bin/python3
"""
Starts a Flask web app
"""


from flask import Flask, render_template
from models import *
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """renders HTML page with the city list"""
    states = sorted.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    closes the storage on teardown
    """
    from models import storage
    storage.close()


if __name__ == '__main__':
    """
    run when invoked
    """
    app.run(host='0.0.0.0', port='5000')
