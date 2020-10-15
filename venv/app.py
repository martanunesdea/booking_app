# File describing the web server side management
import sqlite3 as sql
from flask import Flask, g, render_template, request
from db_handler import *
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/bookings')
def view_bookings():
    my_db = DBHandler()
    #users = my_db.get_users()
    # #users_values = users.values()
    timeslots = my_db.get_timeslots()
    timeslots_values = timeslots.values()
    return render_template("bookings_page.html", bookings = timeslots_values)
