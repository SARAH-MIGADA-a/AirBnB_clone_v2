#!/usr/bin/python3
"""web application must be listening on 0.0.0.0"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    display a HTML page: (inside the tag BODY)
    funtcion is executed url:port/states is requested
    Returns:
        [str]: HTML page
    """
    states = list(storage.all("State").values())
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Display HTML page with the list of cities of a state"""
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def tear_down(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
