
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import g, url_for
import sqlite3 as sql
from db_handler import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/delete_booking", methods=["POST"])
def delete_booking():
    a = request.form.get("timeslot")
    b = request.form.get("author")
    # my_db.delete_timeslot(a)
    return render_template("plain.html")

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


@app.route('/edit')
def edit_booking():
    return render_template("delete.html")

