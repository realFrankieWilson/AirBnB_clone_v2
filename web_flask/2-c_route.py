#!/usr/bin/python3
"""
A module that contains functions that starts application
"""
from flask import Flask, escape


# Create an instance of Flask class.
app = Flask(__name__)
# Allows route to match requests with or without trailing whitespace.
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    '''
    Starts a Flask web application:
        Web listens 0.0.0.0, port 5000
        Routs: -> display "Hello HBNB!"
    '''
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb():
    '''
    Starts a Flask web application:
        Web listens 0.0.0.0, port 5000
        /hbnb: -> display "HBNB"
    '''
    return "HBNB"


@app.route("/c/<text>")
def hello_c(text):
    '''
    Starts a Flask web application:
        Web listens 0.0.0.0, port 5000
        /hbnb: -> display "HBNB"
    '''
    return 'C %s' % escape(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
