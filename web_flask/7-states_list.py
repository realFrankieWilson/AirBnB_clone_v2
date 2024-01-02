#!/usr/bin/python3
"""
A module that contains functions that starts application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


# Create an instance of Flask class.
app = Flask(__name__)
# Allows route to match requests with or without trailing whitespace.
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_sess(error):
    '''
    Closes the session
    '''
    storage.close()


@app.route("/states_list")
def display_state():
    '''
    Starts a Flask web application:
        Web listens 0.0.0.0, port 5000
        /number: -> Displays states.
    '''
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
