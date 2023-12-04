# Prologue Comments
# • Name of code artifact: SymptoTrack_Database_Backend
# • Description: Establishes signal to MongoDb Cluster and Sample Collections and between the frontend html pages.
# • Programmer’s name: Sarah Martinez
# • Data of Creation: 10.22.2023
# • Latest Revision: 12.03.2023
# • Brief description of each revision & author
# • Preconditions: Requires my password and username created on MongoDb in order to access the cluster
#   Username/Password are hidden and not shown. .ENV contains MongoDB URI. IP must be added to Database Cluster
#   Query setup: { field: 'value' }
# • Postconditions: None
# • Errors: login error occurs please check faults
# • Side effects: None
# • Invariants: None
# • Any known faults: revamping the entire set up the site, the script.js and jqueries are sending status codes 500 and
# 404, regardless of what I've done, I can't remove it and it's likely due to the set up the files and the script.js

from flask import Flask, session, render_template, request, jsonify
import os

from dotenv import load_dotenv
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

# # Load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']
# SECRET_KEY = os.environ['SECRET_KEY']

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)
app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'


db = client['symptotrack']
users = db['user_creds']

app.template_folder = "../templates"
app.static_folder = "../static"


# Sends a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
#
# # # List all the databases in the cluster:
# for db_info in client.list_database_names():
#     print(db_info)


# Establishes html links when flask project runs
@app.route('/', endpoint='login')
def index():
    return render_template('index.html')


@app.route('/homepage', endpoint='homepage')
def homepage():
    return render_template('Homepage.html')


@app.route('/signup/', endpoint='signup')
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


# # @app.route('/login', methods=['POST'])
# # def login_submit():
# #     if request.method == 'POST':
# #         data = request.get_json()
# #         print("Received data: ", data)
# #         email = data['email']
# #         password = data['password']
# #
# #         user = users.find_one({'email': email})
# #
# #         if user and check_password_hash(user['password'], password):
# #             session['user_id'] = user['_id']
# #             return jsonify({'message': 'Login successful'}), 200
# #         else:
# #             return jsonify({'message': 'Invalid email or password'}), 401
# #
#
# @app.route('/signup', methods=['GET', 'POST'])
# def signup_submit():
#     if request.method == 'POST':
#         data = request.get_json()
#         first_name = data['firstName']
#         last_name = data['lastName']
#         email = data['email']
#         password = data['password']
#
#         hashed_password = generate_password_hash(password)
#
#         user = {'first_name': first_name, 'last_name': last_name, 'email': email, 'password': hashed_password}
#         users.insert_one(user)
#
#         return jsonify({'message': 'User created successfully'}), 201
#     else:
#         return render_template('sign up.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
