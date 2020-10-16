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
    timeslots = my_db.get_timeslots()
    return render_template("bookings_page.html", rows = timeslots)

@app.route('/users')
def view_users():
    my_db = DBHandler()
    users = my_db.get_users()
    return render_template("users_page.html", rows = users)

