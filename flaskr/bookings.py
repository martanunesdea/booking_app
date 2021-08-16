from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

from datetime import date

bp = Blueprint('bookings', __name__, url_prefix='/bookings')

@bp.route('/')
def index():
    db = get_db()
    db_adverts = db.execute(
        'SELECT b.id, date_booking, title, author_id, username'
        ' FROM bookings b JOIN user u ON b.author_id = u.id'
        ' ORDER BY b.id DESC'
    ).fetchall()
    return render_template('bookings/index.html', adverts=db_adverts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        date_booking = request.form['date_booking']
        attendees_count = request.form['attendees_count']
        max_capacity = request.form['max_capacity']
        description = request.form['description']

        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO bookings (title, author_id, date_booking, attendees_count, max_capacity, description)'
                ' VALUES (?, ?, ?, ?, ?, ?)',
                (title, g.user['id'], date_booking, attendees_count, max_capacity, description)
            )
            db.commit()
            return redirect(url_for('bookings.index'))

    return render_template('bookings/create.html')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT b.id, title, date_booking, author_id, username, attendees_count, max_capacity'
        ' FROM bookings b JOIN user u ON b.author_id = u.id'
        ' WHERE b.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Booking id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    db_advert = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        date_booking = request.form['date_booking']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE bookings SET title = ?, date_booking = ?'
                ' WHERE id = ?',
                (title, date_booking, id)
            )
            db.commit()
            return redirect(url_for('bookings.index'))

    return render_template('bookings/update.html', advert=db_advert)


@bp.route('/<int:id>/view_full_details')
@login_required
def view_full_details(id):
    db_advert = get_db().execute(
        'SELECT b.id, title, date_booking, author_id, username, attendees_count, max_capacity, description'
        ' FROM bookings b JOIN user u ON b.author_id = u.id'
        ' WHERE b.id = ?',
        (id,)
    ).fetchone()

    if db_advert is None:
        abort(404, "Booking id {0} doesn't exist.".format(id))
    
    return render_template('bookings/view_full_details.html', advert=db_advert)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM bookings WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('bookings.index'))

@bp.route('/<int:id>/add_to_cart', methods=('POST',))
@login_required
def add_to_cart(id):
    date_booked = date.today().strftime("%d/%m/%y")
    print(date_booked)
    post = get_post(id, False)
    db = get_db()
    capacityAvailable = post['attendees_count'] < post['max_capacity']
    post = get_db().execute(
        'SELECT id, username, booking_id, date_booked'
        ' FROM attendees'
        ' WHERE id = ? and booking_id = ?',
        (g.user['id'],id)
        ).fetchone()
    if post is None and capacityAvailable:
        db.execute('INSERT INTO attendees (username, booking_id, date_booked) VALUES (?, ?,?)', (g.user['username'], id, date_booked))
        db.commit()
        print("Added ", g.user['username'], "to attendees db")
    elif post is not None:
        abort(404, "User {} is already signed up for this booking.".format(g.user['username']))
    return redirect(url_for('bookings.index'))

@bp.route('/show_all', methods=('GET',))
@login_required
def show_bookings():
    print("user id is ", g.user['id'])
    db = get_db()
    bookings = db.execute(
        'SELECT a.id, username, booking_id, date_booked, title, date_booking'
        ' FROM attendees a'
        ' INNER JOIN bookings b ON b.id = a.booking_id'
    ).fetchall()
    
    bookings_by_user = list()

    for booking in bookings:
        if booking['username'] == g.user['username']:
            bookings_by_user.append(booking)

        
    return render_template('bookings/show_all.html', bookings=bookings_by_user)
