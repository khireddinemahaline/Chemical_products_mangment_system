#!/usr/bin/python3
""" 
flask framwork
    create web server in Python
    make static HTML file dynamic by using objects stored in a file or database
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()

@app.route("/home")
def root(product):
    products = storage.all(Prodect).values()

    return render_template("home.html", product=products)

@app.route("/signup")
def signup():
    return

@app.root("/signin")
def signin():
    return

@app.route("dashbord")
def dashbord():
    return

@app.root("orders"):
def orders():
    return
