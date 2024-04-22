# Prologue Comments
# • Name of code artifact: app.py
# • Description: Establishes signal to MongoDb Cluster and Sample Collections and between the frontend html pages.
# • Programmer’s name: Sarah Martinez
# • Data of Creation: 01.25.2023
# • Latest Revision: 04.21.2024
# • Brief description of each revision & author
# • Preconditions: Requires my password and username created on MongoDb in order to access the cluster
#   Username/Password are hidden and not shown. .ENV contains MongoDB URI. IP must be added to Database Cluster
#   Query setup: { field: 'value' }
# • Postconditions: None
# • Errors: currently in process of data visual sprint
# • Side effects: None
# • Invariants: None
# • Any known faults: the entire folder doesn't seem to work in the actual repo, but it works separately.

from flask import Flask, render_template, session, flash, redirect, url_for, request
from functools import wraps
from user.models import PainLog, Journal, Medslist, Result
from bson import ObjectId
app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'


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
    pain_logs_bar = PainLog().get_pain_logs(session['user']['_id'])

    labels_bar = []
    values_bar = []
    descriptions_bar = []  
    for log in pain_logs_bar:
        labels_bar.append(log['pain_date'])
        values_bar.append(log['pain_input'])
        descriptions_bar.append(log['pain_description'])  

    result_logs = Result().get_results(session['user']['_id'])

    labels_line = []
    values_line = []
    for log in result_logs:
        labels_line.append(log['Date'])
        values_line.append(log['totalPoints'])

    return render_template('homepage_new.html', labels_bar=labels_bar, values_bar=values_bar, descriptions_bar=descriptions_bar, labels_line=labels_line, values_line=values_line)


@app.route('/symptom_input/')
@login_required
def symptom_input():
    return render_template('symptom_input.html')


@app.route('/profile/')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/journal_input/')
@login_required
def journal_input():
    return render_template('Journal_input _new.html')


@app.route('/journal_output/', methods=['GET', 'POST'])
@login_required
def journal_output():
    if request.method == 'POST':
        selected_date = request.form.get('selected_date') 
        user_id = session['user']['_id']
        journal_entries = Journal().get_journal_entries(user_id, selected_date)
        return render_template('Journal_output_new.html', journal_entries=journal_entries, selected_date=selected_date)
    return render_template('Journal_output_new.html')


@app.route('/meds_list/')
@login_required
def meds_list():
    user_id = session['user']['_id']
    meds = Medslist().get_meds(user_id)
    return render_template('MedsList.html', meds=meds)


@app.route('/meds_input/')
@login_required
def meds_input():
    return render_template('Meds_input.html')


@app.route('/meds_info/<string:med_id>')
@login_required
def meds_info(med_id):
    med = Medslist().find_one(med_id) 
    if med:
        return render_template('Med_info.html', med=med)
    else:
        return "Medication not found", 404


@app.route('/questionnaire/')
@login_required
def questionnaire():
    return render_template('questionnaire.html')
