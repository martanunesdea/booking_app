# File describing the web server side management
import sqlite3 as sql
from flask import Flask, g, render_template, request
from db_handler import *
app = Flask(__name__)


@app.route('/')
def index():
    my_db = DBHandler()
    users_list = my_db.get_users()
    users_names = users_list.values()


    return render_template("list.html",rows = users_list.values())
