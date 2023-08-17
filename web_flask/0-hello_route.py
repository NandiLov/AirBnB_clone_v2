#!/usr/bin/python3
"""A script that starts a flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask

#Create a Flask application instance
app = Flask("__name__")

#Define a route for /airbnb-onepage/
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_airbnb():
    return "Hello HBNB!\n"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=None)
