# Prologue Comments
# • Name of code artifact: SymptoTrack_Database_Backend
# • Description: Establishes signal to MongoDb Cluster and Sample Collections and between the frontend html pages.
# • Programmer’s name: Sarah Martinez
# • Data of Creation: 10.22.2023
# • Latest Revision: 11.05.2023
# • Brief description of each revision & author
# • Preconditions: Requires my password and username created on MongoDb in order to access the cluster
#   Username/Password are hidden and not shown. .ENV contains MongoDB URI. IP must be added to Database Cluster
#   Query setup: { field: 'value' }
# • Postconditions: None
# • Errors: None
# • Side effects: None
# • Invariants: None
# • Any known faults: None

from flask import Flask, render_template
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# # Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)
app = Flask(__name__)

app.template_folder = "../templates"
app.static_folder = "../static"

# # Sends a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# # List all the databases in the cluster:
for db_info in client.list_database_names():
    print(db_info)


# Establishes html links when flask project runs
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/homepage', endpoint='homepage')
def homepage():
    return render_template('Homepage.html')


@app.route('/signup', endpoint='signup')
def signup():
    return render_template('Sign up.html')


@app.route('/journal')
def journal():
    return render_template('Journal.html')


@app.route('/journal_input')
def journal_input():
    return render_template('Journal_input.html')


@app.route('/journal_output')
def journal_output():
    return render_template('Journal_output.html')


@app.route('/meds_input')
def meds_input():
    return render_template('Meds_input.html')


@app.route('/meds_list')
def meds_list():
    return render_template('Medslist.html')


@app.route('/more_info')
def more_info():
    return render_template('More info.html')


@app.route('/symptom_input')
def symptom_input():
    return render_template('symptom_input.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
