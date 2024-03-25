# Prologue Comments
# • Name of code artifact: app.py
# • Description: Establishes signal to MongoDb Cluster and Sample Collections and between the frontend html pages.
# • Programmer’s name: Sarah Martinez
# • Data of Creation: 01.25.2023
# • Latest Revision: 03.24.2024
# • Brief description of each revision & author
# • Preconditions: Requires my password and username created on MongoDb in order to access the cluster
#   Username/Password are hidden and not shown. .ENV contains MongoDB URI. IP must be added to Database Cluster
#   Query setup: { field: 'value' }
# • Postconditions: None
# • Errors: currently in process of data visual sprint
# • Side effects: None
# • Invariants: None
# • Any known faults: the entire folder doesn't seem to work in the actual repo, but it works separately.

from flask import Flask, render_template, session, flash, redirect, url_for
from functools import wraps
from database import db
from user.models import PainLog

from pymongo import MongoClient

from dotenv import load_dotenv
import os

# Database
# load_dotenv()
# MONGODB_URI = os.environ['MONGODB_URI']

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# # Connect to your MongoDB cluster:
# client = MongoClient(MONGODB_URI)
# db = client['symptotrack']
# users = db['user_creds']
# symptoms = db['pain']


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect('/')

    return wrap


# routes
from user import routes


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup/')
def register():
    return render_template('Sign up.html')


@app.route('/homepage/')
@login_required
def homepage():
    # Fetch pain log data
    pain_logs = PainLog().get_pain_logs(session['user']['_id'])

    # Prepare data for chart
    labels = []
    values = []
    descriptions = []  # Collect pain descriptions
    for log in pain_logs:
        labels.append(log['pain_date'])
        values.append(log['pain_input'])
        descriptions.append(log['pain_description'])  # Collect pain descriptions

    return render_template('homepage_new.html', labels=labels, values=values, descriptions=descriptions)


@app.route('/symptom_input/')
@login_required
def symptom_input():
    return render_template('symptom_input.html')


@app.route('/profile/')
@login_required
def profile():
    return render_template('profile.html')


