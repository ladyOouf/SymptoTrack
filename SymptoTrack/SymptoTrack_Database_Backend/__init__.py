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

from flask import Flask, session, redirect
from functools import wraps
from dotenv import load_dotenv
import os

from pymongo import MongoClient

app = Flask(__name__)

load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)
db = client['symptotrack']
users = db['user_creds']

app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'


# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap

# Database

