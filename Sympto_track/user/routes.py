# Prologue Comments
# • Name of code artifact: routes.py
# • Description: Establishes signal to MongoDb Cluster and Sample Collections and between the frontend html pages.
# • Programmer’s name: Sarah Martinez
# • Data of Creation: 01.25.2023
# • Latest Revision: 01.28.2024
# • Brief description of each revision & author
# • Preconditions: Requires my password and username created on MongoDb in order to access the cluster
#   Username/Password are hidden and not shown. .ENV contains MongoDB URI. IP must be added to Database Cluster.
#   Must be logged in for certain pages to be accessed
#   Query setup: { field: 'value' }
# • Postconditions: None
# • Errors:
# • Side effects: None
# • Invariants: None
# • Any known faults: the entire folder doesn't seem to work in the actual repo, but it works separately.

from flask import render_template, redirect, url_for, request, jsonify, Flask, session
from app import app, db
from user.models import User
from app import login_required


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login', methods=['POST'])
def login():
    return User().login()


@app.route('/log/')
@login_required
def log():
    return render_template('log_options.html')


@app.route('/questionnaire/')
@login_required
def questionnaire():
    return render_template('questionnaire.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/meds_info/')
@login_required
def meds_info():
    return render_template('Med_info.html')


@app.route('/meds_input/')
@login_required
def meds_input():
    return render_template('Meds_input.html')


@app.route('/meds_list/')
@login_required
def meds_list():
    return render_template('MedsList.html')


@app.route('/more_info/')
@login_required
def more_info():
    return render_template('More info.html')


@app.route('/services/')
def services():
    return render_template('Services.html')


@app.route('/journal/')
@login_required
def journal():
    return render_template('Journal.html')


@app.route('/journal_input/')
@login_required
def journal_input():
    return render_template('Journal_input.html')


@app.route('/journal_output/')
@login_required
def journal_output():
    return render_template('Journal_output.html')


@app.route('/contact/')
def contact():
    return render_template('Contact.html')


@app.route('/symptom_input/')
@login_required
def symptom_input():
    return render_template('symptom_input.html')