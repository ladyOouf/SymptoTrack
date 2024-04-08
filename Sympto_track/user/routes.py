# Prologue Comments
# • Name of code artifact: routes.py
# • Description: Establishes signal to MongoDb Cluster and Sample Collections and between the frontend html pages.
# • Programmer’s name: Sarah Martinez
# • Data of Creation: 01.25.2023
# • Latest Revision: 04.07.2024
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
from app import app
from database import db
from user.models import User, PainLog, Journal
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


@app.route('/user/log_pain', methods=['POST'])
def log_pain():
    print("Received POST request to log pain")  # Add this line to check
    return PainLog().log_pain()


@app.route('/user/pain_chart')
def pain_chart():
    pain_logs = PainLog().get_pain_logs(session['user']['_id'])

    labels = []
    values = []
    for log in pain_logs:
        labels.append(log['pain_date'])
        values.append(log['pain_input'])

    return render_template('pain_chart.html', labels=labels, values=values)

@app.route('/user/journal_log', methods=['POST'])
def journal_insert():
    print("Received POST request to log journal")  
    return Journal().journal_input()


@app.route('/log/')
@login_required
def log():
    return render_template('log_options_update.html')


@app.route('/questionnaire/')
@login_required
def questionnaire():
    return render_template('questionnaire_update.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/meds_list/')
@login_required
def meds_list():
    return render_template('MedsList.html')


@app.route('/meds_input/')
@login_required
def meds_input():
    return render_template('Meds_input.html')


@app.route('/meds_info/')
@login_required
def meds_info():
    return render_template('Med_info.html')


@app.route('/journal/')
@login_required
def journal():
    return render_template('Journal_new.html')


@app.route('/journal_input/')
@login_required
def journal_input():
    return render_template('Journal_input _new.html')


@app.route('/journal_output/')
@login_required
def journal_output():
    return render_template('Journal_output_new.html')


@app.route('/contact/')
def contact():
    return render_template('Contact.html')


@app.route('/services/')
def services():
    return render_template('Services.html')


@app.route('/stressresources/')
def stressresources():
    return render_template('stressresources.html')
