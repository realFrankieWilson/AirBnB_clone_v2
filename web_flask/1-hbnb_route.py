#!/usr/bin/python3
"""
A module that contains functions that starts application
"""
from flask import Flask


# Create an instance of Flask class.
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hello():
    '''
    Starts a Flask web application:
        Web listens 0.0.0.0, port 5000
        Routs: -> display "Hello HBNB!"
        /hbnb: -> display "HBNB"
    '''
    return "HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
