#!/usr/bin/python3
"""
A module that contains functions that starts application
"""
from flask import Flask, render_template, escape


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


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>")
def hello_python(text):
    '''
    Starts a Flask web application:
        Web listens 0.0.0.0, port 5000
        /python: -> default "text is cool"
    '''
    return 'Python %s' % escape(text.replace('_', ' '))


@app.route("/number/<int:n>")
def num_int(n):
    '''
    Starts a Flask web application:
        Web listens 0.0.0.0, port 5000
        /number: -> Displays an integer.
    '''
    return "%i is a number" % (n)


@app.route("/number_template/<int:n>")
def num_int_template(n):
    '''
    Starts a Flask web application:
        Web listens 0.0.0.0, port 5000
        /number: -> Displays an integer from template.
    '''
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def num_int_template_odd_or_even(n):
    '''
    Starts a Flask web application:
        Web listens 0.0.0.0, port 5000
        /number: -> Displays an integer from template.
                -> Displays if number or even.
    '''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
