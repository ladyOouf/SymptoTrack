# Prologue Comments
# • Name of code artifact: SymptoTrack_Database_Backend
# • Description: Establishes signal to MongoDb Cluster and Sample Collections. The code has sample lines to explain what
#  each section does. These sections are mainly being used as a reference and will not be used for the website's code.
# • Programmer’s name: Sarah Martinez
# • Data of Creation: 10.22.2023
# • Latest Revision: 10.22.2023
# • Brief description of each revision & author
# • Preconditions: Requires my password and username created on MongoDb in order to access the cluster
#   Username/Password are hidden and not shown. .ENV contains MongoDB URI. IP must be added to Database Cluster
#   Query setup: { field: 'value' }
# • Postconditions: Currently in this code, I used a sample set collection on MongoDB to test out the pymongo package
# • Return values: Depends on the query request
# • Errors: No current errors unless document doesn't exist
# • Side effects: None
# • Invariants: None
# • Any known faults: None

from flask import Flask, render_template, request, redirect
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)
app = Flask(__name__)

app.template_folder = "../templates"
app.static_folder = "../static"

# Sends a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# List all the databases in the cluster:
for db_info in client.list_database_names():
    print(db_info)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_email', methods=['POST'])
def add_email():
    email = request.form.get('email')
    if email:
        emails_collection = client.get_database().get_collection('emails')
        emails_collection.insert_one({'email': email})
    return redirect('/')  


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
